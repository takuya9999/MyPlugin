import pymel.core as pm

def attachObj(axis):
    selectObj = pm.selected()
    #選択オジェクトの名前を文字列で取得
    #AにBをコンストレイント！
    fromSelectObj = selectObj[len(pm.selected())-1]
    toSelectObj = selectObj[0]
    if axis == 0: #ワールド
        pm.parentConstraint(toSelectObj,fromSelectObj, weight=1,skipRotate=['x','y','z'])
    elif axis == 1: #ローカル    
        pm.parentConstraint(toSelectObj,fromSelectObj, weight=1)
    pm.delete(fromSelectObj,constraints=True)

def createLocate(axis):
    toSelectObj = pm.selected()[len(pm.selected())-1]
    newLocator = pm.spaceLocator()
    if axis == 0: #ワールド
        pm.parentConstraint(toSelectObj,newLocator, weight=1,skipRotate=['x','y','z'])
    elif axis == 1: #ローカル
        pm.parentConstraint(toSelectObj,newLocator, weight=1)
    pm.delete(newLocator,constraints=True)

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
