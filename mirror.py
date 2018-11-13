import pymel.core as pm

with pm.window(title='インスタンスミラー') as objMirror:
    with pm.columnLayout(adjustableColumn =True): #columnLayout:縦方向に要素を配置する　adjustableColumn: trueでUI横幅一杯に伸縮する
        
        with pm.frameLayout(label='ミラー設定'):
            # #ミラー軸の設定
            mirrorCoordinate = pm.optionMenu(label='ミラーの位置: ',width=150)
            pm.menuItem(label='ワールド')
            pm.menuItem(label='オブジェクト')
            # floatFieldGrp( label='オフセット: ', bgc=[0.3,0.3,0.3])
            mirrorAxis = pm.radioButtonGrp( numberOfRadioButtons=3, #radioButtonGrp: 最大4個１グループのラジオボタンを作成　numberOfRadioButtons:[nrb]の短縮系でも可。ラジオボタンの個数を指定。
            label='ミラー軸: ', #グループの名前
            labelArray3=['x','y','z'],
            select=1)
        with pm.horizontalLayout():
              pm.button( label='ミラー' , command='print createMirror(), "ミラー" ',bgc=[0.35,0.35,0.35])
              pm.button( label='閉じる' , command='print objMirror.delete(), "閉じる" ',bgc=[0.35,0.35,0.35])
        with pm.horizontalLayout():
              pm.button( label='オブジェクト化' , command='print toObj(), "オブジェクト化" ',bgc=[0.35,0.35,0.35])

def toObj():
    selectObj = pm.selected()
    #選択オジェクトの名前を文字列で取得
    prevSelectObjN = str(selectObj[len(pm.selected())-1])
    #選択オブジェクトのピボット(スケール、回転)の取得
    prevSelectObjSP = selectObj[len(pm.selected())-1].scalePivot.get()
    prevSelectObjRP = selectObj[len(pm.selected())-1].rotatePivot.get()
    
    #結合して一つにしたオブジェクト([transfrom,polyunite]の配列オブジェクト) chでヒストリを削除しておく
    newSelectObj = pm.polyUnite(selectObj,n=prevSelectObjN,ch=False)
    #結合したオブジェクトのピボットを設定
    newSelectObj[0].scalePivot.set(prevSelectObjSP)
    newSelectObj[0].rotatePivot.set(prevSelectObjRP)
    print 'ピボット', newSelectObj[0].scalePivot.get()
    #結合した選択オブジェクトの中心点を取る処理
    sBbox = pm.exactWorldBoundingBox(newSelectObj)
    sBboxP =  [(sBbox[0] + sBbox[3])/2, (sBbox[1] + sBbox[4])/2, (sBbox[2] + sBbox[5])/2]
    #結合した選択オブジェクトのピボットを取る処理    
    pivot = newSelectObj[0].scalePivot.get()
    print 'ピボット',pivot
    #ミラーに関する情報の取得
    mirrorInfo = getScaleAxis(sBboxP,pivot)
    #複製してリネームする処理
    duplicateObj = pm.duplicate(newSelectObj[0],n=prevSelectObjN+mirrorInfo['nNameTail'])
    pm.rename(newSelectObj[0],prevSelectObjN+mirrorInfo['sNameTail'])
    #ミラー配置する処理
    pm.scale(mirrorInfo['mirrorScale'],p=pivot)
    #ヒストリとグループノードの残骸の削除
    pm.delete(prevSelectObjN)
def createMirror():
    # 選択オブジェクト
    selectObj = pm.selected()[len(pm.selected())-1]
    prevObj = str(selectObj) #ミラー処理前の選択オブジェクト名
    sBbox = pm.exactWorldBoundingBox(selectObj)
    sBboxP =  [(sBbox[0] + sBbox[3])/2, (sBbox[1] + sBbox[4])/2, (sBbox[2] + sBbox[5])/2]
    # 軸の対象となるオブジェクト
    centerObj = pm.selected()[0]
    cBbox = pm.exactWorldBoundingBox(centerObj)
    # オブジェクトの中心点の取得
    cBboxP =  [(cBbox[0] + cBbox[3])/2, (cBbox[1] + cBbox[4])/2, (cBbox[2] + cBbox[5])/2]
    # ピボット位置の設定(ワールド、オブジェクト)
    if mirrorCoordinate.getSelect() == 1 : #ワールド中心
        pivot = [0,0,0]
        mirrorInfo = getScaleAxis(sBboxP,pivot)
        print 'これはワールドですか？いいえ、違います。'
    else : #オブジェクト中心
        pivot = cBboxP
        mirrorInfo = getScaleAxis(sBboxP,pivot)
        print 'オブジェクトでーーーーーーす',cBboxP
    print 'これ絶対取れないやつ',mirrorCoordinate.getSelect()
    # 選択オブジェクトのグループ化
    grpObj = pm.group(selectObj,n=selectObj+mirrorInfo['sNameTail'])
    # 選択オブジェクトグループのインスタンスの作成
    instanceGrpObj = pm.instance(grpObj,n=selectObj+mirrorInfo['nNameTail'])
    print 'ワールド取れててくれー！頼む！',mirrorCoordinate.getValue()
    pm.scale(mirrorInfo['mirrorScale'],p=pivot)
    #親グループの作成
    pm.group(grpObj,instanceGrpObj,n=prevObj+'_Mirror')
    
    print mirrorCoordinate.getValue(), mirrorAxis.getSelect()

    #リネーム処理の正規表現を実装する
    #選択オブジェクトの中心点を取って対象オブジェクトの中心点と比較し、右ならR,左ならLを振る処理の追加
    # オブジェクトの複数選択に対応する

def getScaleAxis(sBboxP,pivot):
    if mirrorAxis.getSelect() == 1: #X軸対象
        mirrorScale = [-1,1,1]
        if sBboxP[0] < pivot[0]:
            sNameTail = '_L'
            nNameTail = '_R'
        else :
            sNameTail = '_R'
            nNameTail = '_L'
    elif mirrorAxis.getSelect() == 2: #y軸対象
        mirrorScale = [1,-1,1]
        if sBboxP[1] < pivot[1]:
            sNameTail = '_Bottom'
            nNameTail = '_Top'
        else :
            sNameTail = '_Top'
            nNameTail = '_Bottom'
    elif mirrorAxis.getSelect() == 3: #z軸対象
        mirrorScale = [1,1,-1]
        if sBboxP[2] < pivot[2]:
            sNameTail = '_L'
            nNameTail = '_R'
        else :
            sNameTail = '_R'
            nNameTail = '_L'
    return {'sNameTail':sNameTail,'nNameTail':nNameTail,'mirrorScale':mirrorScale}