import pymel.core as pm
import re

def attachObj(axis):
    #選択オジェクトの名前を文字列で取得
    selectObj = pm.selected()
    #AにBをコンストレイント！
    fromSelectObj = selectObj[len(pm.selected())-1]
    toSelectObj = selectObj[0]
    if axis == 0: #ワールド
        pm.parentConstraint(toSelectObj,fromSelectObj, weight=1,skipRotate=['x','y','z'])
    elif axis == 1: #ローカル    
        pm.parentConstraint(toSelectObj,fromSelectObj, weight=1)
    #必要のないコンストレイントノードの削除
    delNode = fromSelectObj.listRelatives(c=True,ad=True,type='constraint')
    pm.delete(delNode)

def createLocate(axis):
    toSelectObj = pm.selected()[len(pm.selected())-1]
    newLocator = pm.spaceLocator()
    if axis == 0: #ワールド
        pm.parentConstraint(toSelectObj,newLocator, weight=1,skipRotate=['x','y','z'])
    elif axis == 1: #ローカル
        pm.parentConstraint(toSelectObj,newLocator, weight=1)
    pm.delete(newLocator,constraints=True)

def createJointOffset(Offset):
    if Offset == "":
        Offset = "Offset"
    selectJoints = pm.selected()

    for joint in selectJoints: 
        offsetObjName = ""
        if prefix.getSelect() == 1: #置き換え
            offsetObjName = re.sub(r"^[a-zA-Z]*?_",Offset+"_",str(joint))
        elif prefix.getSelect() == 2: #追加
            offsetObjName = str(Offset) + "_" + str(joint)  
        offsetObj = pm.group(em = True,name = offsetObjName)
        #AにBをコンストレイント！
        pm.parentConstraint(joint,offsetObj, weight=1)
        #必要のないコンストレイントノードの削除
        delNode = offsetObj.listRelatives(c=True,ad=True,type='constraint')
        pm.delete(delNode)
    

with pm.window( title = 'アタッチ！', width=300) as testWin:
    with pm.columnLayout( adjustableColumn=True):
        with pm.frameLayout( label='アタッチ'):
            with pm.horizontalLayout( ):
                attach = pm.button( label='アタッチ！' , command='print attachObj(0)  ')
                locate = pm.button( label='アタッチ！(ローカル軸)' , command='print attachObj(1)  ')
        with pm.frameLayout( label='ロケーター作成'):
            with pm.horizontalLayout( ):
                attach = pm.button( label='ロケーター作成' , command='print createLocate(0)  ')
                locate = pm.button( label='ロケーター作成(ローカル軸)' , command='print createLocate(1)  ')
        with pm.frameLayout( label='オフセットオブジェクトの作成'):
            prefix = pm.radioButtonGrp( numberOfRadioButtons=2, #radioButtonGrp: 最大4個１グループのラジオボタンを作成　numberOfRadioButtons:[nrb]の短縮系でも可。ラジオボタンの個数を指定。
            label='接頭辞の設定:', #グループの名前
            labelArray2=['置き換え','追加'],
            select=1)
            pm.separator()
            offsetname = pm.textFieldGrp( label='オフセットの接頭辞',pht='デフォルトはOffsetです')
            pm.button( label='オフセット実行' , command='print createJointOffset(offsetname.getText())')
         
