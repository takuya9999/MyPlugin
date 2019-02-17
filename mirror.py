import pymel.core as pm
import re

def toObjLegacy():
    selectObj = pm.selected()
    
    #選択オジェクトの名前を文字列で取得
    prevSelectObjN = str(selectObj[len(pm.selected())-1])
    
    #選択オブジェクト(ミラーオブジェクトの軸となる親階層)のピボット(スケール、回転)の取得
    prevSelectObjSP = selectObj[len(pm.selected())-1].scalePivot.get()
    prevSelectObjRP = selectObj[len(pm.selected())-1].rotatePivot.get()

    #結合して一つにしたオブジェクト([transfrom,polyunite]の配列オブジェクト) chでヒストリを削除しておく
    newSelectObj = pm.polyUnite(selectObj,n=prevSelectObjN,ch=False)
    
    #結合したオブジェクトのピボットを設定
    newSelectObj[0].scalePivot.set(prevSelectObjSP)
    newSelectObj[0].rotatePivot.set(prevSelectObjRP)
    
    #結合した選択オブジェクトの中心点を取る処理
    sBbox = pm.exactWorldBoundingBox(newSelectObj)
    sBboxP =  [(sBbox[0] + sBbox[3])/2, (sBbox[1] + sBbox[4])/2, (sBbox[2] + sBbox[5])/2]
    
    #結合した選択オブジェクトのピボットを取る処理    
    pivot = newSelectObj[0].scalePivot.get()
    
    #ミラーに関する情報の取得
    mirrorInfo = getScaleAxis(sBboxP,pivot)
    
    #複製してリネームする処理
    duplicateObj = pm.duplicate(newSelectObj[0],n=prevSelectObjN+mirrorInfo['nNameTail'])
    pm.rename(newSelectObj[0],prevSelectObjN+mirrorInfo['sNameTail'])
    
    #ミラー配置する処理
    pm.scale(mirrorInfo['mirrorScale'],p=pivot)
    
    #ヒストリとグループノードの残骸の削除
    pm.delete(prevSelectObjN)


def toObj():
    selectObj = pm.selected()
    #選択オジェクトの名前を文字列で取得
    prevSelectObjN = str(selectObj[len(pm.selected())-1])
    prevSelectObjN = re.sub(r".*\|","",str(prevSelectObjN))
    #選択オブジェクトのピボット(スケール、回転)の取得
    parentObj = selectObj[len(pm.selected())-1].getParent()
    parentObjSuffix = re.search(r"[^_]*_*$",str(parentObj))
    pParentObj = parentObj.getParent()
    pPParentObj = pParentObj.getParent()
    prevSelectObjSP = pParentObj.scalePivot.get()
    prevSelectObjRP = pParentObj.rotatePivot.get()

    #親の親要素のバウンディングボックスの取得
    pPbox = pm.exactWorldBoundingBox(pParentObj)
    #親の親要素のバウンディングボックスの中心点の取得
    pPboxP =  [(pPbox[0] + pPbox[3])/2, (pPbox[1] + pPbox[4])/2, (pPbox[2] + pPbox[5])/2]
    #選択オブジェクトの複製
    newSelectObj = pm.duplicate(selectObj[len(pm.selected())-1],n=prevSelectObjN)
    
    #親グループの作成。ミラーグループに親がいない場合はワールドにオブジェクトを作成する。
    if pPParentObj != None:
        pm.parent(newSelectObj,pPParentObj)
    else :
        pm.parent(newSelectObj,w=True)
    pm.parent(pParentObj, rm=True)
    
    #結合した選択オブジェクトの中心点を取る処理
    sBbox = pm.exactWorldBoundingBox(newSelectObj[0])
    sBboxP =  [(sBbox[0] + sBbox[3])/2, (sBbox[1] + sBbox[4])/2, (sBbox[2] + sBbox[5])/2]
    #ミラーの軸となるピボットの指定（親の親要素の中心点）    
    pivot = pPboxP
   
    #ミラーに関する情報の取得
    print "sBboxP,pivotの値の確認",sBboxP, pivot
    mirrorInfo = getScaleAxisObj(sBboxP,pivot,parentObjSuffix.group())
   
    #複製してリネームする処理
    #sName=オリジナル,nName=複製オブジェクトのこと
    print "newSelectObj[0]の中身の確認",newSelectObj[0]
    #フリーズ処理
    # pm.makeIdentity(newSelectObj[0],apply=True,t=1,r=1,s=1,n=0,pn=1)
    pm.makeIdentity(newSelectObj,apply=True,t=1,r=1,s=1,n=0,pn=1)
    
    duplicateObj = pm.duplicate(newSelectObj[0],n=prevSelectObjN+mirrorInfo['nNameTail'])
    pm.rename(newSelectObj[0],prevSelectObjN+mirrorInfo['sNameTail'])
    #ミラー配置する処理
    print "pivotの値の確認", pivot
    pm.select(duplicateObj)
    pm.xform(scale = mirrorInfo['mirrorScale'],scalePivot=pivot,ws=True)
    #複製オブジェクトのフリーズ
    pm.makeIdentity(duplicateObj,apply=True,t=1,r=1,s=1,n=0,pn=1)
    pm.xform(cp=True)
    pm.select(newSelectObj[0])
    pm.xform(cp=True)

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
    else : #オブジェクト中心
        pivot = cBboxP
        mirrorInfo = getScaleAxis(sBboxP,pivot)
    
    # 選択オブジェクトのフリーズ処理 フリーズしたほうが良いのか悪いのか判断難しい。しない方がいい場合もありそう。
    pm.makeIdentity(selectObj,apply=True,t=1,r=1,s=1,n=0,pn=1)
    
    # 選択オブジェクトのグループ化
    grpObj = pm.group(selectObj,n=selectObj+mirrorInfo['sNameTail'])

    # 選択オブジェクトグループのインスタンスの作成
    instanceGrpObj = pm.instance(grpObj,n=selectObj+mirrorInfo['nNameTail'])
    
    #　反転（ミラー）処理xormのwsだとオブジェクトのローカル軸基準で変換してるっぽい？何故かわからない。
    pm.select(instanceGrpObj)
    pm.xform(scale = mirrorInfo['mirrorScale'],scalePivot=pivot,ws=True)
    pm.xform(cp=True)
    
    #scaleのドキュメントにwsないけどつけるとワールド軸でスケールがかかってるっぽい。でも思ったような結果にならない。
    # pm.scale(mirrorInfo['mirrorScale'],p=pivot,ws=True) 
    # pm.scale(mirrorInfo['mirrorScale'],p=pivot) 
    
    #親グループの作成 あり、なしで選択できるようにした方がいいかも。
    pm.group(grpObj,instanceGrpObj,n=prevObj+'_Mirror')
    
    #リネーム処理の正規表現を実装する
    # オブジェクトの複数選択に対応する

def getScaleAxis(sBboxP,pivot):
    if mirrorAxis.getSelect() == 1: #X軸対象
        mirrorScale = [-1,1,1]
        if sBboxP[0] < pivot[0]:
            sNameTail = '_R'
            nNameTail = '_L'
        else :
            sNameTail = '_L'
            nNameTail = '_R'
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
            sNameTail = '_B'
            nNameTail = '_F'
        else :
            sNameTail = '_F'
            nNameTail = '_B'
    return {'sNameTail':sNameTail,'nNameTail':nNameTail,'mirrorScale':mirrorScale}

def getScaleAxisObj(sBboxP,pivot,parentObjSuffix):
    if parentObjSuffix == 'L' or parentObjSuffix == 'R': #X軸対象
        mirrorScale = [-1,1,1]
        if sBboxP[0] < pivot[0]:
            sNameTail = '_R'
            nNameTail = '_L'
        else :
            sNameTail = '_L'
            nNameTail = '_R'
    elif parentObjSuffix == 'Bottom' or parentObjSuffix == 'Top': #y軸対象
        mirrorScale = [1,-1,1]
        if sBboxP[1] < pivot[1]:
            sNameTail = '_Bottom'
            nNameTail = '_Top'
        else :
            sNameTail = '_Top'
            nNameTail = '_Bottom'
    elif parentObjSuffix == 'B' or parentObjSuffix == 'F': #z軸対象
        mirrorScale = [1,1,-1]
        if sBboxP[2] < pivot[2]:
            sNameTail = '_B'
            nNameTail = '_F'
        else :
            sNameTail = '_F'
            nNameTail = '_B'
    return {'sNameTail':sNameTail,'nNameTail':nNameTail,'mirrorScale':mirrorScale}


with pm.window(title='インスタントミラー') as objMirror:
    with pm.columnLayout(adjustableColumn =True): #columnLayout:縦方向に要素を配置する　adjustableColumn: trueでUI横幅一杯に伸縮する
        
        with pm.frameLayout(label='ミラー設定'):
            # ミラー軸の設定
            mirrorCoordinate = pm.optionMenu(label='ミラーの位置: ',width=150)
            pm.menuItem(label='ワールド')
            pm.menuItem(label='オブジェクト')
            mirrorAxis = pm.radioButtonGrp( numberOfRadioButtons=3, #radioButtonGrp: 最大4個１グループのラジオボタンを作成　numberOfRadioButtons:[nrb]の短縮系でも可。ラジオボタンの個数を指定。
            label='ミラー軸: ', #グループの名前
            labelArray3=['x','y','z'],
            select=1)
        with pm.horizontalLayout():
              pm.button( label='ミラー' , command='print createMirror(), "ミラー" ',bgc=[0.35,0.35,0.35])
              pm.button( label='閉じる' , command='print objMirror.delete(), "閉じる" ',bgc=[0.35,0.35,0.35])
        # with pm.horizontalLayout():
            #   pm.button( label='オブジェクト化(レガシー)' , command='print toObjLegacy(), "オブジェクト化(レガシー)" ',bgc=[0.35,0.35,0.35])
        with pm.horizontalLayout():
              pm.button( label='オブジェクト化' , command='print toObj(), "オブジェクト化" ',bgc=[0.35,0.35,0.35])
    
    
    #ミラーしたオブジェクトを更にミラーした場合のオブジェクト化対応
    #複数選択したオブジェクトをミラーした場合、一つ一つのオブジェクトに個別でミラー処理を適用する機能の追加。
    #現状、応急処置的にオブジェクト化の際の軸を親要素のサフィックスで判別しているが、将来的にはインスタンスの情報をもとにオブジェクト化する軸を決定するようにする。