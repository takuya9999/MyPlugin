import pymel.core as pm
import maya.cmds as cmds

chankflag=False
#シェイプを持ってるかチェック。シェイプがある場合nurbsCurveかチェック　(Bool)
def rigCheck(obj):
    print 'チェック開始'
    if pm.objectType(obj) == 'nurbsCurve': #obj.getChildren()の場合、transformじゃなくてshapeが取れるっぽい？よくわからない。getparentの場合、この処理は必要ない。なぜ？
        return True
    if pm.objectType(obj) == 'transform' and obj.getShape(): #オブジェクトタイプがtransform かつシェイプを持っている場合。'transform'の条件式付け足すと上手くいくっぽい理由がわからない。
        shape = obj.getShape()
        if pm.objectType(shape) == 'nurbsCurve':
            return True
        else :
            return False 
    else :
        return False

with pm.window( title = 'リグセレクターユーティリティ', width=300) as testWin:
    with pm.columnLayout( adjustableColumn=True):
        with pm.horizontalLayout( ):
            pm.toolCollection()
            rotateButton = pm.toolButton(tool='RotateSuperContext',toolImage1=('RotateSuperContext', 'rotate_M.xpm'),style='iconAndTextHorizontal')
            moveButton = pm.toolButton(tool='moveSuperContext',toolImage1=('moveSuperContext', 'move_M.xpm'),style='iconAndTextHorizontal')
        with pm.frameLayout( label='リセット'):
        # pm.text(label='リセット')
            with pm.horizontalLayout() as reset_Rotate:
                # pm.iconTextButton( label='リセット' , command='print resetRotate("")  ',image1='rotate_M.xpm',style='iconAndTextHorizontal',bgc=[0.35,0.35,0.35])
                pm.button( label='リセット' , command='print resetRotate("")  ', bgc=[0.35,0.35,0.35])
                reset_RotateX = pm.button( label='X' , command='print resetRotate("x")  ', bgc=[0.4, 0.0, 0.0] )
                reset_RotateY = pm.button( label='Y' , command='print resetRotate("y")  ', bgc=[0.0, 0.4, 0.0])
                reset_RotateZ = pm.button( label='Z' , command='print resetRotate("z")  ', bgc=[0.0, 0.0, 0.4])
            with pm.horizontalLayout( ) as reset_Move:
                # pm.iconTextButton( label='リセット' , command='print resetTranslate()  ',image1='move_M.xpm',style='iconAndTextHorizontal',bgc=[0.35,0.35,0.35])
                pm.button( label='リセット' , command='print resetTranslate()  ',bgc=[0.35,0.35,0.35])
                reset_translateX = pm.button( label='X' , command='print resetTranslate("x")  ',bgc=[0.4, 0.0, 0.0])
                reset_translateY = pm.button( label='Y' , command='print resetTranslate("y")  ',bgc=[0.0, 0.4, 0.0])
                reset_translateZ = pm.button( label='Z' , command='print resetTranslate("z")  ',bgc=[0.0, 0.0, 0.4])
        
        pm.separator() #UIの間に分割線を入れる。
        with pm.frameLayout( label='ロック'):
        # pm.text(label='ロック')
            with pm.horizontalLayout( ) as lock_Rotate:
                # pm.iconTextButton( label='ロック' , command='print lockRotate()  ',image1='rotate_M.xpm',style='iconAndTextHorizontal',bgc=[0.35,0.35,0.35])
                pm.button( label='回転ロック' , command='print lockRotate()  ',bgc=[0.35,0.35,0.35])
                pm.button( label='X' , command='print lockRotate("x")  ', bgc=[0.4, 0.0, 0.0])
                pm.button( label='Y' , command='print lockRotate("y")  ', bgc=[0.0, 0.4, 0.0])
                pm.button( label='Z' , command='print lockRotate("z")  ', bgc=[0.0, 0.0, 0.4])
            with pm.horizontalLayout( ) as lock_Move:
                # pm.iconTextButton( label='ロック' , command='print lockTransform()  ',image1='move_M.xpm',style='iconAndTextHorizontal',bgc=[0.35,0.35,0.35])
                pm.button( label='移動ロック' , command='print lockTransform()  ',bgc=[0.35,0.35,0.35])
                pm.button( label='X' , command='print lockTransform("x")  ', bgc=[0.4, 0.0, 0.0])
                pm.button( label='Y' , command='print lockTransform("y")  ', bgc=[0.0, 0.4, 0.0])
                pm.button( label='Z' , command='print lockTransform("z")  ', bgc=[0.0, 0.0, 0.4])
            with pm.horizontalLayout( ) as unlock_Rotate:
                # pm.iconTextButton( label='解除' , command='print unlockRotate()  ',image1='rotate_M.xpm',style='iconAndTextHorizontal',bgc=[0.35,0.35,0.35])
                pm.button( label='解除' , command='print unlockRotate()  ',bgc=[0.35,0.35,0.35])
                pm.button( label='X' , command='print unlockRotate("x")  ', bgc=[0.4, 0.0, 0.0])
                pm.button( label='Y' , command='print unlockRotate("y")  ', bgc=[0.0, 0.4, 0.0])
                pm.button( label='Z' , command='print unlockRotate("z")  ', bgc=[0.0, 0.0, 0.4])
            with pm.horizontalLayout( ) as unlock_Move:
                # pm.iconTextButton( label='解除' , command='print unlockTransform()  ',image1='move_M.xpm',style='iconAndTextHorizontal',bgc=[0.35,0.35,0.35])
                pm.button( label='解除' , command='print unlockTransform()  ',bgc=[0.35,0.35,0.35])
                pm.button( label='X' , command='print unlockTransform("x")  ', bgc=[0.4, 0.0, 0.0])
                pm.button( label='Y' , command='print unlockTransform("y")  ', bgc=[0.0, 0.4, 0.0])
                pm.button( label='Z' , command='print unlockTransform("z")  ', bgc=[0.0, 0.0, 0.4])

        
        pm.separator() #UIの間に分割線を入れる。
        with pm.frameLayout( label='親子リグ選択'):
            with pm.horizontalLayout():
                pm.button( label='子を選択' , command='print getChildren()  ')
                pm.button( label='親を選択' , command='print getParent()  ')
        with pm.frameLayout( label='全てのリグを選択'):
            with pm.horizontalLayout():
                pm.button( label='(ワールド)' , command='print getAllRig(root=True)  ')
                pm.button( label='(ローカル)' , command='print getAllRig(root=False)  ')
        
        pm.separator() #UIの間に分割線を入れる。
        with pm.frameLayout( label='ポーズリセット'): 
            with pm.horizontalLayout( ):
                pm.button( label='(ワールド)' , command='print poseReset(root=True)  ')
                pm.button( label='(ローカル)' , command='print poseReset(root=False)  ')
                
        # 回転スライダー
        with pm.frameLayout( label='回転アトリビュート'):
            rotate_sld_x = pm.floatSliderGrp( label='X', field=True, ss=1.0, minValue= -180.0, maxValue=360.0, fieldMinValue= -180.0, fieldMaxValue=360.0, value=0, cc='print changeRotate_x()',dc='print drag_changeRotate_x()',bgc=[0.3,0.0,0.0])
            rotate_sld_y = pm.floatSliderGrp( label='Y', field=True, ss=1.0, minValue= -180.0, maxValue=360.0, fieldMinValue= -180.0, fieldMaxValue=360.0, value=0, cc='print changeRotate_y()',dc='print drag_changeRotate_y()',bgc=[0.0,0.3,0.0])
            rotate_sld_z = pm.floatSliderGrp( label='Z', field=True, ss=1.0, minValue= -180.0, maxValue=360.0, fieldMinValue= -180.0, fieldMaxValue=360.0, value=0, cc='print changeRotate_z()',dc='print drag_changeRotate_z()',bgc=[0.0,0.0,0.3])
        
        # with pm.frameLayout( label='ロックアトリビュート(工事中)'):        
        #         with pm.horizontalLayout() as lockCheck_Translate:
        #             #チェックボックス
        #             translateBoxGrp = pm.checkBoxGrp( numberOfCheckBoxes=4, #チェックボックスグループ作成する。
        #             label='移動',
        #             labelArray4=['xyz','x','y','z',],
        #             cc='print lockCheckTranslate()'
        #             )
        #         with pm.horizontalLayout() as lockCheck_Rotate:
        #             #チェックボックス
        #             rotateBoxGrp = pm.checkBoxGrp( numberOfCheckBoxes=4, #チェックボックスグループ作成する。
        #             label='回転',
        #             labelArray4=['xyz','x','y','z',],
        #             cc='print lockCheckRotate()'
        #             )
        # 移動のロック
        # def lockCheckTranslate():
        #     select = pm.selected()[len(pm.selected())-1]
        #     checklist = translateBoxGrp.getValueArray4()
        #     for axis,item in enumerate(checklist):
        #         if axis == 1:
        #             if item:
        #                 pm.setAttr(select.translateX,l=True)
        #             else:
        #                 pm.setAttr(select.translateX,l=False)
        #         elif axis == 2:
        #             if item:
        #                 pm.setAttr(select.translateY,l=True)
        #             else:
        #                 pm.setAttr(select.translateY,l=False)
        #         elif axis == 3:
        #             if item:
        #                 pm.setAttr(select.translateZ,l=True)
        #             else:
        #                 pm.setAttr(select.translateZ,l=False)  
        #         else:
        #             if item:
        #                 pm.setAttr(select.translate,l=True)
        #             else:
        #                 pm.setAttr(select.translate,l=False)  
        # # 回転のロック
        # def lockCheckRotate():
        #     select = pm.selected()[len(pm.selected())-1]
        #     checklist = rotateBoxGrp.getValueArray4()
        #     xyz = rotateBoxGrp.getValueArray4()[0]
        #     x = rotateBoxGrp.getValueArray4()[1]
        #     y = rotateBoxGrp.getValueArray4()[2]
        #     z = rotateBoxGrp.getValueArray4()[3]
        #     #forを使わない方法でテストしたけど結果変わらず。このバグはもしかしたら仕様かもしれない。
        #     pm.setAttr(select.rotateX,l=x)
        #     pm.setAttr(select.rotateY,l=y)
        #     pm.setAttr(select.rotateZ,l=z)
        #     pm.setAttr(select.rotate,l=xyz)
        #     print 'チェックしまーす！'
        #     # for axis,item in enumerate(checklist):
        #     #     if axis == 1:
        #     #         if item:
        #     #             pm.setAttr(select.rotateX,l=True)
        #     #             print 'とぅるー'
        #     #         else:
        #     #             pm.setAttr(select.rotateX,l=False)
        #     #             print 'ふぉるす'
        #     #     elif axis == 2:
        #     #         if item:
        #     #             pm.setAttr(select.rotateY,l=True)
        #     #         else:
        #     #             pm.setAttr(select.rotateY,l=False)
        #     #     elif axis == 3:
        #     #         if item:
        #     #             pm.setAttr(select.rotateZ,l=True)
        #     #         else:
        #     #             pm.setAttr(select.rotateZ,l=False)  
        #     #     elif axis == 0:
        #     #         if item:
        #     #             pm.setAttr(select.rotate,l=True)
        #     #         else:
        #     #             pm.setAttr(select.rotate,l=False)  
        #     #         print axis,'あくしす！'

        # def checkRotate():
        #     select = pm.selected()[len(pm.selected())-1]
        #     x = pm.getAttr(select.rotateX,lock=True)
        #     y = pm.getAttr(select.rotateY,lock=True)
        #     z = pm.getAttr(select.rotateZ,lock=True)
        #     xyz = pm.getAttr(select.rotate,lock=True)

        #     #試しにpythonで書いてみたけど、はいダメー
        #     # select = cmds.ls(sl=True)[0]
        #     # print cmds.ls(select)
        #     # x = cmds.getAttr(select+'.rotateX',lock=True)
        #     # y = cmds.getAttr(select+'.rotateY',lock=True)
        #     # z = cmds.getAttr(select+'.rotateZ',lock=True)
        #     # xyz = cmds.getAttr(select+'.rotate',lock=True)

        #     #xyzのみにチェックをいれて、再選択するとxyzだけでなくx,y,zにもチェック入った状態になるバグあり。なんとか治したい。
        #     #getAttryでの取得段階で、すでにすべての値がTrueになってしまっている。
        #     #どうやら、内部的にはちゃんとした値を保持できているが、pm.getAttr(select.rotateX,lock=True)で取得する場合、UI表示上のロック情報が取得されるぽい。そのため、xyzのロックがかかっていると、x,y,zもロックがかかっているという間違った情報が取得される。
        #     locklist = [xyz,x,y,z]
        #     print '回転チェック',x,y,z,xyz
        #     rotateBoxGrp.setValueArray4(locklist)

        # def checkTransform():
        #     select = pm.selected()[len(pm.selected())-1]
        #     x = pm.getAttr(select.translateX,lock=True)
        #     y = pm.getAttr(select.translateY,lock=True)
        #     z = pm.getAttr(select.translateZ,lock=True)
        #     xyz = pm.getAttr(select.translate,lock=True)
        #     locklist = [xyz,x,y,z]
        #     print '移動チェック',x,y,z,xyz
        #     translateBoxGrp.setValueArray4(locklist)

        def changeSelected():
            if pm.selected():
                e = pm.selected()[len(pm.selected())-1]
                # checkRotate()
                # checkTransform()
                if rigCheck(e):
                    print 'チェンジセレクトエラー確認!'
                    if (not pm.objectType(e) == 'transform') and pm.objectType(pm.listRelatives(e, p=True)[0] ) == 'transform':
                        e_transform = pm.listRelatives(e, p=True)[0]
                        rotate_sld_x.setValue(pm.getAttr(e_transform.rotateX))
                        rotate_sld_y.setValue(pm.getAttr(e_transform.rotateY))
                        rotate_sld_z.setValue(pm.getAttr(e_transform.rotateZ))
                        reset_RotateX.setLabel(pm.getAttr(e.rotateX))
                        reset_RotateY.setLabel(pm.getAttr(e.rotateY))
                        reset_RotateZ.setLabel(pm.getAttr(e.rotateZ))
                        reset_translateX.setLabel(round(pm.getAttr(e.translateX),2))
                        reset_translateY.setLabel(pm.getAttr(e.translateY))
                        reset_translateZ.setLabel(pm.getAttr(e.translateZ))
                        pm.scriptJob(attributeChange= (e_transform.rotate,'changeSliderValue()'),parent=testWin ) 
                        # pm.scriptJob(attributeChange= (e_transform.rotate.lock,'checkRotate()'),parent=testWin,replacePrevious=True ) 



                        print 'オブジェクト選択時のイベント取得'
                    else:
                        rotate_sld_x.setValue(pm.getAttr(e.rotateX))
                        rotate_sld_y.setValue(pm.getAttr(e.rotateY))
                        rotate_sld_z.setValue(pm.getAttr(e.rotateZ))
                        reset_RotateX.setLabel(round(pm.getAttr(e.rotateX),2))
                        reset_RotateY.setLabel(round(pm.getAttr(e.rotateY),2))
                        reset_RotateZ.setLabel(round(pm.getAttr(e.rotateZ),2))
                        reset_translateX.setLabel(round(pm.getAttr(e.translateX),2))
                        reset_translateY.setLabel(round(pm.getAttr(e.translateY),2))
                        reset_translateZ.setLabel(round(pm.getAttr(e.translateZ),2))
                        pm.scriptJob(attributeChange= (e.rotate,'changeSliderValue()'),parent=testWin )  
                        pm.scriptJob(attributeChange= (e.translate,'changeSliderValue()'),parent=testWin )  #移動値が変ったときに値の再設定を行う処理。slider用の関数に依存してしまっているので、モジュール化する。
                        # pm.scriptJob(ac= (e.r,'checkRotate()'),parent=testWin,alc=True,dri=True )  #アトリビュートエディタの方でロック情報を変更した場合、プラグインと紐づけたい。上手くいかない。
                        # pm.scriptJob(attributeChange= (e.rotate,'checkRotate()') ) 

                        print 'オブジェクト選択時のイベント取得'
                else:
                    return
            else:
                rotate_sld_x.setValue(0)
                rotate_sld_y.setValue(0)
                rotate_sld_z.setValue(0)
                reset_RotateX.setLabel('X')
                reset_RotateY.setLabel('Y')
                reset_RotateZ.setLabel('Z')
                reset_translateX.setLabel('X') 
                reset_translateY.setLabel('Y')
                reset_translateZ.setLabel('Z')
                # rotateBoxGrp.setValueArray4([False,False,False,False])
                # translateBoxGrp.setValueArray4([False,False,False,False])
        
        def changeSliderValue():
            if pm.selected():
                e = pm.selected()[len(pm.selected())-1]
                if rigCheck(e):
                    print 'エラー確認!'
                    if (not pm.objectType(e) == 'transform') and pm.objectType(pm.listRelatives(e, p=True)[0] ) == 'transform':
                        e_transform = pm.listRelatives(e, p=True)[0]
                        x = pm.getAttr(e_transform.rotateX)
                        y = pm.getAttr(e_transform.rotateY)
                        z = pm.getAttr(e_transform.rotateZ)
                        rotate_sld_x.setValue(x)
                        rotate_sld_y.setValue(y)
                        rotate_sld_z.setValue(z)
                        reset_RotateX.setLabel(round(pm.getAttr(e.rotateX),2))
                        reset_RotateY.setLabel(round(pm.getAttr(e.rotateY),2))
                        reset_RotateZ.setLabel(round(pm.getAttr(e.rotateZ),2))
                        reset_translateX.setLabel(round(pm.getAttr(e.translateX),2))
                        reset_translateY.setLabel(round(pm.getAttr(e.translateY),2))
                        reset_translateZ.setLabel(round(pm.getAttr(e.translateZ),2))
                        print 'はわわー'
                    else:
                        x = pm.getAttr(e.rotateX)
                        y = pm.getAttr(e.rotateY)
                        z = pm.getAttr(e.rotateZ)
                        rotate_sld_x.setValue(x)
                        rotate_sld_y.setValue(y)
                        rotate_sld_z.setValue(z)
                        reset_RotateX.setLabel(round(pm.getAttr(e.rotateX),2))
                        reset_RotateY.setLabel(round(pm.getAttr(e.rotateY),2))
                        reset_RotateZ.setLabel(round(pm.getAttr(e.rotateZ),2))
                        reset_translateX.setLabel(round(pm.getAttr(e.translateX),2))
                        reset_translateY.setLabel(round(pm.getAttr(e.translateY),2))
                        reset_translateZ.setLabel(round(pm.getAttr(e.translateZ),2))

        def changeRotate_x():

            global chankflag 

            if chankflag:
                chankflag = False
                pm.undoInfo(cck=True)
            
            e = pm.selected()[len(pm.selected())-1]
            value = rotate_sld_x.getValue()
            print 'リリース！',value
            pm.setAttr(e.rotateX,value) 

        def changeRotate_y():

            global chankflag 

            if chankflag:
                chankflag = False
                pm.undoInfo(cck=True)

            e = pm.selected()[len(pm.selected())-1]
            value = rotate_sld_y.getValue()
            print 'リリース！',chankflag
            pm.setAttr(e.rotateY,value) 

        def changeRotate_z():

            global chankflag 
            
            if chankflag:
                chankflag = False
                pm.undoInfo(cck=True)

            e = pm.selected()[len(pm.selected())-1]
            value = rotate_sld_z.getValue()
            print 'リリース！',value
            pm.setAttr(e.rotateZ,value) 

        def drag_changeRotate_x():

            global chankflag 
            
            e = pm.selected()[len(pm.selected())-1]
            value = rotate_sld_x.getValue()
            pm.setAttr(e.rotateX,value) 

            if not chankflag:
                chankflag = True
                pm.undoInfo(ock=True)
            
            print 'チャンク！',chankflag

        def drag_changeRotate_y():

            global chankflag 
            
            e = pm.selected()[len(pm.selected())-1]
            value = rotate_sld_y.getValue()
            pm.setAttr(e.rotateY,value) 

            if not chankflag:
                chankflag = True
                pm.undoInfo(ock=True)
                
            print 'チャンク！',chankflag

        def drag_changeRotate_z():
            
            global chankflag 
            
            e = pm.selected()[len(pm.selected())-1]
            value = rotate_sld_z.getValue()
            pm.setAttr(e.rotateZ,value) 

            if not chankflag:
                chankflag = True
                pm.undoInfo(ock=True)
           
            print 'チャンク！',chankflag

        
        # pm.scriptJob(ct= ['SomethingSelected','cttest()'],runOnce=True ) #何かしら選択されている場合はtrueが返ってきてcttest()が実行されるはずなんだけど上手く動かないのであとで調べる。
        def cttest():
            print 'ヤッホー'

        # pm.separator() #UIの間に分割線を入れる。
        # pm.button( label='選択オブジェクトの情報を表示(デバッグ用)' , command='print objTypePrint()  ')

        def changeContext():
            currentTool =  pm.currentCtx()
            if currentTool == 'RotateSuperContext':
                # lockCheck_Rotate.setVisible(True)

                reset_Move.setVisible(False)
                lock_Move.setVisible(False)
                unlock_Move.setVisible(False)
                
                reset_Rotate.setVisible(True)
                lock_Rotate.setVisible(True)
                unlock_Rotate.setVisible(True)
                # lockCheck_Translate.setVisible(False)



                # rotateButton.setTool('RotateSuperContext')
                rotateButton.select()
                print 'カレントツール',currentTool
            elif currentTool == 'moveSuperContext':
                reset_Rotate.setVisible(False)
                lock_Rotate.setVisible(False)
                unlock_Rotate.setVisible(False)
                # lockCheck_Rotate.setVisible(False)
                
                reset_Move.setVisible(True)
                lock_Move.setVisible(True)
                unlock_Move.setVisible(True)
                # lockCheck_Translate.setVisible(True)


                # moveButton.setTool('moveSuperContext')
                moveButton.select()
                print 'カレントツール',currentTool
            else:
                reset_Rotate.setVisible(False)
                lock_Rotate.setVisible(False)
                unlock_Rotate.setVisible(False)
                # lockCheck_Rotate.setVisible(False)
                
                reset_Move.setVisible(False)
                lock_Move.setVisible(False)
                unlock_Move.setVisible(False)        
                # lockCheck_Translate.setVisible(False)

        changeContext() #初期化処理
        changeSelected() #初期化処理
        selectCg = pm.scriptJob(e= ('SelectionChanged','changeSelected()'),p=testWin) #選択オブジェクト変えるたびにめっちゃ呼ばれるんで、原因わかるまで封印。記述する場所が違うと処理が変わる。かなりの罠。
        toolCg = pm.scriptJob(e= ('ToolChanged','changeContext()'),p=testWin) #ツールが切り替わるたびに呼ばれる処理    うっかり消してしまった！THE失態!!   



    def poseReset(root=False):
        getAllRig(root)
        resetTranslate()
        resetRotate()


    def objTypePrint():
        obj = pm.selected()[0]
        # obj = pm.selected()
        shape = obj.getShape()
        objtype = pm.objectType(shape)
        # nodetype = pm.nodeType(obj, api=True)
        nodetype = pm.nodeType(obj)
        print 'オブジェクトタイプを返却します', objtype, 'ノードタイプを返却します'
        # print pm.getAttr(obj)


    def getParent():
        prevRig = None
        obj = pm.selected()[len(pm.selected())-1]
        print '現在選択されているオブジェクト', obj
        parent = obj.getParent()
        while (parent):
            if rigCheck(parent):
                prevRig = parent
                break
            parent = parent.getParent()
    
        parent = parent.getParent()
        while (parent): #次に選択するリグが一番親かどうかを確認する処理
            if rigCheck(parent):
                break
            parent = parent.getParent()
        if parent:
            pm.select(prevRig, add=True)
            print 'こいつの親はメインでないです', prevRig
        else: 
            print 'こいつの親はメインだす' 
        return

    def getAllRig(root):
        obj = pm.selected()[len(pm.selected())-1]
        parent = obj.getParent()
        latestRig = obj
        while (parent):
            if rigCheck(parent):
                latestRig = parent
            parent = parent.getParent()
        print 'ここにメインが入ってないとおかしいよなぁ！？', latestRig 
        children = latestRig.getChildren()
        if not root and len(children):
            children.pop(0)   
        loopAllChildren(children)
        
        return

    def getAllParents():
        obj = pm.selected()[0]
        #最上階層までの全ての親を取得
        print '最上階層までの全ての親を取得' , obj.getAllParents()


    def getRoot():
        obj = pm.selected()[0]
        #ルートノードを取得
        root = obj.root()
        print 'ルートノードを取得' , root
        return root


    def getSiblings():
        obj = pm.selected()[0]
        #同じ階層を取得
        print '同じ階層を取得' , obj.getSiblings()

    def getChildren():
        #子階層を取得
        obj = pm.selected()[len(pm.selected())-1]
        print '現在選択されているオブジェクト', obj
        children = obj.getChildren()
        # children=pm.listRelatives(obj)
        if len(children):
            children.pop(0)
        # for child in children:
        #     if child.nodeType() == "transform":
        #         mask.append(child)
        #     print 'チルドレン', child.nodeType()    
        print 'チルドレン', children

        loopChildren(children)

    def loopChildren(childList): #子要素の再帰処理用関数
        for child in childList:
            if rigCheck(child):
                # child = pm.listRelatives(child, p=True)[0]
                print 'childの中身はなんじゃらほい', child
                pm.select(child, add=True)
            else:
                loopChildren(child.getChildren())
        return

    def loopAllChildren(childList): #子要素の再帰処理用関数全部選択バージョン
        for child in childList:
            if rigCheck(child):
                # child = pm.listRelatives(child, p=True)[0]
                print 'childの中身はなんじゃらほい', child    
                pm.select(child, add=True)
                loopAllChildren(child.getChildren())
            else:
                loopAllChildren(child.getChildren())
        return


    def createParentCubeSphere():
        # | による親子付け

        #トランスフォームノードとシェイプノードのリストが返ってくるため、[0]で一つ目の要素のみ受け取っています
        myCube = pm.polyCube()[0]
        #同じく
        mySphere = pm.polySphere()[0]
        #親子付け
        myCube | mySphere

        #階層化されているか確認
        print '階層化の確認', mySphere.name( long=True)


    #新機能のテスト
    # 原点へ移動
    def zeroTransform():
        obj = pm.selected()[0]
        pm.move(obj,0,0,0,a=False)

    #　ポジションリセット
    def resetTranslate(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item) : #選択されているのがリグの場合
                # itemに別の値を代入すると.translateプロパティが取得できなくのるので、allitemという別の変数を作る必要がある。
                if (not pm.objectType(item) == 'transform') and pm.objectType(pm.listRelatives(item, p=True)[0] ) == 'transform':
                    allitem = pm.listRelatives(item, p=True)[0]
                    # print 'ここに何がはいっているのか', pm.objectType(item)
                    if axis == 'x':
                        pm.setAttr(allitem.translateX,l=False)
                        pm.setAttr(allitem.translateX,0)
                    elif axis == 'y':
                        pm.setAttr(allitem.translateY,l=False)
                        pm.setAttr(allitem.translateY,0)
                    elif axis == 'z':
                        pm.setAttr(allitem.translateZ,l=False)
                        pm.setAttr(allitem.translateZ,0)
                    else:
                        pm.setAttr(allitem.translateX,l=False)
                        pm.setAttr(allitem.translateY,l=False)
                        pm.setAttr(allitem.translateZ,l=False)
                        pm.setAttr(allitem.translate,l=False)
                        pm.setAttr(allitem.translate,0,0,0)
                elif axis == 'x':
                    pm.setAttr(item.translateX,l=False)
                    pm.setAttr(item.translateX,0)
                elif axis == 'y':
                    pm.setAttr(item.translateY,l=False)
                    pm.setAttr(item.translateY,0)
                elif axis == 'z':
                    pm.setAttr(item.translateZ,l=False)
                    pm.setAttr(item.translateZ,0)
                else:
                    # pm.setAttr(item.translate,0,0,0,l=False)
                    # translateXとtranslateは重複して持つことができるぽい？
                    # 解除するときは両方解除する必要がある
                    pm.setAttr(item.translateX,l=False)
                    pm.setAttr(item.translateY,l=False)
                    pm.setAttr(item.translateZ,l=False)
                    pm.setAttr(item.translate,l=False)
                    pm.setAttr(item.translate,0,0,0)
                    print 'リセットして', pm.objectType(item)
        changeSelected()
        return

    #　回転リセット
    def resetRotate(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item) :
                #全選択処理した場合、selectedでshapeが選択された状態になってしまうので、transformを選択した状態にリセットする処理
                #原因がまだわかっていないので解明する。
                if (not pm.objectType(item) == 'transform') and pm.objectType(pm.listRelatives(item, p=True)[0] ) == 'transform':
                    allitem = pm.listRelatives(item, p=True)[0]
                    # print 'ここに何がはいっているのか', pm.objectType(item)
                    if axis == 'x':
                        pm.setAttr(allitem.rotateX,l=False)
                        pm.setAttr(allitem.rotateX,0)
                    elif axis == 'y':
                        pm.setAttr(allitem.rotateY,l=False)
                        pm.setAttr(allitem.rotateY,0)
                    elif axis == 'z':
                        pm.setAttr(allitem.rotateZ,l=False)
                        pm.setAttr(allitem.rotateZ,0)
                    else:
                        pm.setAttr(allitem.rotateX,l=False)
                        pm.setAttr(allitem.rotateY,l=False)
                        pm.setAttr(allitem.rotateZ,l=False)
                        pm.setAttr(allitem.rotate,l=False)
                        pm.setAttr(allitem.rotate,0,0,0)
                elif axis == 'x':
                    pm.setAttr(item.rotateX,l=False)
                    pm.setAttr(item.rotateX,0)
                elif axis == 'y':
                    pm.setAttr(item.rotateY,l=False)
                    pm.setAttr(item.rotateY,0)
                elif axis == 'z':
                    pm.setAttr(item.rotateZ,l=False)
                    pm.setAttr(item.rotateZ,0)
                else:
                    # pm.setAttr(item.rotate,0,0,0,l=False)
                    # rotateXとrotateは重複して持つことができるぽい？
                    # 解除するときは両方解除する必要がある
                    pm.setAttr(item.rotateX,l=False)
                    pm.setAttr(item.rotateY,l=False)
                    pm.setAttr(item.rotateZ,l=False)
                    pm.setAttr(item.rotate,l=False)
                    pm.setAttr(item.rotate,0,0,0)
                    print 'リセットして', pm.objectType(item)
        changeSelected()    
        return
                    


    #　スケールリセット
    def resetScale(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item) :
                if axis == 'x':
                    pm.setAttr(item.scaleX,1)
                elif axis == 'y':
                    pm.setAttr(item.scaleY,1)
                elif axis == 'z':
                    pm.setAttr(item.scaleZ,1)
                else:
                    pm.setAttr(item.scale,1,1,1)


    # 移動のロック
    def lockTransform(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item):
                if axis == 'x':
                    pm.setAttr(item.translateX,l=True)
                elif axis == 'y':
                    pm.setAttr(item.translateY,l=True)
                elif axis == 'z':
                    pm.setAttr(item.translateZ,l=True)
                else:
                    pm.setAttr(item.translate,l=True)
        #  item.t or item.translateどちらでも可
            
    # 回転のロック
    def lockRotate(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item):
                if axis == 'x':
                    pm.setAttr(item.rotateX,l=True)
                elif axis == 'y':
                    pm.setAttr(item.rotateY,l=True)
                elif axis == 'z':
                    pm.setAttr(item.rotateZ,l=True)
                else:
                    pm.setAttr(item.rotate,l=True)

    # スケールのロック
    def lockScale(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item):
                if axis == 'x':
                    pm.setAttr(item.scaleX,l=True)
                elif axis == 'y':
                    pm.setAttr(item.scaleY,l=True)
                elif axis == 'z':
                    pm.setAttr(item.scaleZ,l=True)
                else:
                    pm.setAttr(item.scale,l=True)


    # 移動のアンロック
    def unlockTransform(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item):
                if axis == 'x':
                    pm.setAttr(item.translateX,l=False)
                elif axis == 'y':
                    pm.setAttr(item.translateY,l=False)
                elif axis == 'z':
                    pm.setAttr(item.translateZ,l=False)
                else:
                    pm.setAttr(item.translate,l=False)
        #  item.t or item.translateどちらでも可
            
    # 回転のアンロック
    def unlockRotate(axis=None):
        selectList = pm.selected()
        for item in selectList:
            if rigCheck(item):
                if axis == 'x':
                    pm.setAttr(item.rotateX,l=False)
                elif axis == 'y':
                    pm.setAttr(item.rotateY,l=False)
                elif axis == 'z':
                    pm.setAttr(item.rotateZ,l=False)
                else:
                    pm.setAttr(item.rotate,l=False)



#機能改善案
# ロック機能：選択しているマニュピレータの種類によってロックをかける項目を切り替える。もう一度押すと解除
# リセット機能も同様の仕様にする　-クリア-
#nurbsurb以外のリグにも対応する
#ロックされている部分の背景色を暗くする。ロックは各軸と全体の二重ロックがかかる場合、さらに暗くする -mayaの仕様上実装が困難なため保留-
#英単語のスペルミス修正。　chunkとか。
#決められた命名規則によるピッカーセレクトツールの実装
#スライダーとリセット機能の統合 -ユーザビリティが低下しそうなので見送り-
#スクリプトウィンドウを閉じてもスクリプトの処理が残り続ける問題の対処方法を考える。　-クリア-
#checkrig関数のglobal checkrig() not defind エラーを出ないようにする。ネームスペースの問題？他のプラグインを実行した後に使うと競合するぽいかも。
#ロックボタンをいっそのことチェックボックス式にする。 -実装したが、仕様上回避できない問題があるので保留-
#リセットツールの値の変化をリアルタイムにする
#選択したコンポーネントにキーが打ってある場合は赤色でマークをつける機能。
