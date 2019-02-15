import pymel.core as pm
import re
import maya.cmds as cmds
# from maya.OpenMaya import MGlobal

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

#空のオフセット用オブジェクトを作成する
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
    
#ジョイントとリグの回転を接続する。
def connectRotate():
    selectObj = pm.selected()
    #AにBをコンストレイント！
    lastSelectObj = selectObj[len(pm.selected())-1]
    firstSelectObj = selectObj[0]
    # print 'fromSelectObj',firstSelectObj
    pm.connectAttr(lastSelectObj.rotate,firstSelectObj.rotate)
def connectScale():
    selectObj = pm.selected()
    #AにBをコンストレイント！
    lastSelectObj = selectObj[len(pm.selected())-1]
    firstSelectObj = selectObj[0]
    # print 'fromSelectObj',firstSelectObj
    pm.connectAttr(lastSelectObj.scale,firstSelectObj.scale)

def printConnectionInfo(node, direction):
    u'''
    :param node: ノード名
    :param direction: インプット側の情報かアウトプット側の情報かを in/out で指定
    :return:
    '''
    dest = False
    src = False
    if direction == 'in': src = True
    elif direction == 'out': dest = True
    else: return

    l_connections = cmds.listConnections(node, connections=True, plugs=True, destination=dest, source=src)
    if not l_connections:
        MGlobal.displayWarning('No connections!')
        return

    counter = 0
    for i in range(len(l_connections) / 2):
        src_node = l_connections[counter]
        dest_node = l_connections[counter+1]
        if direction == 'in':
            src_node = l_connections[counter+1]
            dest_node = l_connections[counter]
        print('%s -> %s' % (src_node, dest_node))
        counter += 2

def displayConnections():
    # selectObj = cmds.ls(sl=True)
    selectObj = pm.selected()[0]
    sList = []
    dList = []
    dest = True
    src = False
    # もっときれいに取り出せる方法を考える。
    destConnectList = list(pm.listConnections(selectObj, connections=True, plugs=True, destination=dest, source=src))
    if len(destConnectList) >= 1 :
       dList = [x[1] for x in destConnectList] 
    print 'dest=True',dList
    dest = False
    src = True
    sourceConnectList = list(pm.listConnections(selectObj, connections=True, plugs=True, destination=dest, source=src))
    if len(sourceConnectList) >= 1 :
       sList = [x[1] for x in sourceConnectList]         
    print 'source=True',sList
    

    # plugsObj = cmds.listConnections(selectObj,plugs=True)
    # destinationObj = cmds.listConnections(selectObj,destination=True)
    # sourceObj = cmds.listConnections(selectObj,source=True,destination=True)
    # skipConversionNodesObj = cmds.listConnections(selectObj,skipConversionNodes = True)
    # printConnectionInfo(selectObj,'in')
    # print '接続リスト', connectList,'plugs',plugsObj,'destination',destinationObj,'source',sourceObj,'skipConversionNodes',skipConversionNodesObj




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
            offsetname = pm.textFieldGrp( label='オフセットの接頭辞',pht='Offset')
            pm.button( label='オフセット実行' , command='print createJointOffset(offsetname.getText())')
        with pm.frameLayout( label='ノードの接続'):
            with pm.horizontalLayout( ):
                attach = pm.button( label='回転の接続' , command='print connectRotate()  ')
            with pm.horizontalLayout( ):
                attach = pm.button( label='スケールの接続' , command='print connectScale()  ')
        with pm.frameLayout( label='接続リスト表示'):
            with pm.horizontalLayout( ):
                attach = pm.button( label='リスト表示' , command='print displayConnections()  ')
                attach = pm.button( label='リスト表示' , command='print displayConnections()  ')
#リグとジョイントのノードを接続する機能の実装。複数まとめての実行にも対応させる。
