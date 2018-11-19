import pymel.core as pm
import maya.cmds as mc
from decimal import *

def generateCurve(currentSel):
    curvelist = []
    d_outline_char = mc.curve(p=[[-1.244, 1.613, 0.0], [-1.195, 1.613, 0.0], [-1.195, 2.011, 0.0], [-1.244, 2.011, 0.0], [-1.244, 1.856, 0.0], [-1.261, 1.872, 0.0], [-1.271, 1.878, 0.0], [-1.281, 1.884, 0.0], [-1.291, 1.888, 0.0], [-1.302, 1.891, 0.0], [-1.313, 1.892, 0.0], [-1.325, 1.893, 0.0], [-1.338, 1.892, 0.0], [-1.35, 1.89, 0.0], [-1.362, 1.887, 0.0], [-1.373, 1.883, 0.0], [-1.383, 1.877, 0.0], [-1.393, 1.87, 0.0], [-1.402, 1.861, 0.0], [-1.41, 1.851, 0.0], [-1.418, 1.84, 0.0], [-1.424, 1.829, 0.0], [-1.43, 1.816, 0.0], [-1.434, 1.803, 0.0], [-1.438, 1.789, 0.0], [-1.44, 1.774, 0.0], [-1.442, 1.758, 0.0], [-1.442, 1.741, 0.0], [-1.441, 1.712, 0.0], [-1.435, 1.685, 0.0], [-1.426, 1.662, 0.0], [-1.414, 1.642, 0.0], [-1.398, 1.627, 0.0], [-1.39, 1.62, 0.0], [-1.38, 1.615, 0.0], [-1.37, 1.611, 0.0], [-1.359, 1.609, 0.0], [-1.348, 1.607, 0.0], [-1.336, 1.606, 0.0], [-1.321, 1.607, 0.0], [-1.307, 1.61, 0.0], [-1.294, 1.614, 0.0], [-1.282, 1.621, 0.0], [-1.271, 1.629, 0.0], [-1.261, 1.639, 0.0], [-1.252, 1.651, 0.0], [-1.244, 1.664, 0.0], [-1.244, 1.613, 0.0]],d=1)
    d_inline_char = mc.curve(p=[[-1.244, 1.821, 0.0], [-1.244, 1.695, 0.0], [-1.264, 1.675, 0.0], [-1.285, 1.661, 0.0], [-1.295, 1.656, 0.0], [-1.305, 1.653, 0.0], [-1.315, 1.651, 0.0], [-1.326, 1.65, 0.0], [-1.341, 1.651, 0.0], [-1.353, 1.656, 0.0], [-1.364, 1.664, 0.0], [-1.373, 1.674, 0.0], [-1.38, 1.688, 0.0], [-1.385, 1.704, 0.0], [-1.388, 1.724, 0.0], [-1.389, 1.746, 0.0], [-1.388, 1.771, 0.0], [-1.385, 1.793, 0.0], [-1.379, 1.811, 0.0], [-1.371, 1.827, 0.0], [-1.36, 1.84, 0.0], [-1.348, 1.848, 0.0], [-1.334, 1.854, 0.0], [-1.318, 1.856, 0.0], [-1.309, 1.855, 0.0], [-1.3, 1.853, 0.0], [-1.282, 1.847, 0.0], [-1.263, 1.836, 0.0], [-1.244, 1.821, 0.0]],d=1)
    i_top_char = mc.curve(p=[[-1.095, 1.937, 0.0], [-1.045, 1.937, 0.0], [-1.045, 1.986, 0.0], [-1.095, 1.986, 0.0], [-1.095, 1.937, 0.0]],d=1)
    i_bottom_char = mc.curve(p=[[-1.095, 1.613, 0.0], [-1.045, 1.613, 0.0], [-1.045, 1.887, 0.0], [-1.095, 1.887, 0.0], [-1.095, 1.613, 0.0]],d=1)
    v_char = mc.curve(p=[[-0.888, 1.613, 0.0], [-0.838, 1.613, 0.0], [-0.73, 1.887, 0.0], [-0.776, 1.887, 0.0], [-0.86, 1.674, 0.0], [-0.94, 1.887, 0.0], [-0.99, 1.887, 0.0], [-0.888, 1.613, 0.0]],d=1)
    sliderFIeld = mc.curve(p=[[-1.428, 1.546, 0.047], [-1.428, 0.998, 0.047], [0.133, 0.998, 0.047], [0.133, 1.546, 0.047], [-1.428, 1.546, 0.047]],d=1)
    slider = mc.curve(p=[[-1.39, 1.5, 0.047], [-1.39, 1.043, 0.047], [-1.133, 1.043, 0.047], [-1.133, 1.5, 0.047], [-1.39, 1.5, 0.047]],d=1)
    line = mc.curve(p=[[0.0, 0.998, 0.0], [0.0, -0.0, 0.0]],d=1)
    

    curvelist.append(d_outline_char)
    curvelist.append(d_inline_char)
    curvelist.append(i_top_char)
    curvelist.append(i_bottom_char)
    curvelist.append(v_char)
    curvelist.append(sliderFIeld)
    curvelist.append(slider)
    curvelist.append(line)


    sBbox = pm.exactWorldBoundingBox(currentSel)
    sBboxP =  [(sBbox[0] + sBbox[3])/2, sBbox[4], (sBbox[2] + sBbox[5])/2]
    pm.xform(slider,cp=True)	
    smoothParentGroup = pm.group(curvelist,n=currentSel+'_smooth_Ctrl')
    smoothParentGroup.scalePivot.set([0,0,0])
    smoothParentGroup.rotatePivot.set([0,0,0])
    pm.xform(smoothParentGroup,t=sBboxP)
    pm.pointConstraint(currentSel,smoothParentGroup,mo=True)
    return [slider,sliderFIeld,smoothParentGroup]

def generateChildCurve(currentSel):
    curvelist = []
    d_outline_char = mc.curve(p=[[-0.384, 1.094, 0.0], [-0.335, 1.094, 0.0], [-0.335, 1.492, 0.0], [-0.384, 1.492, 0.0], [-0.384, 1.337, 0.0], [-0.401, 1.353, 0.0], [-0.411, 1.359, 0.0], [-0.421, 1.365, 0.0], [-0.431, 1.369, 0.0], [-0.442, 1.372, 0.0], [-0.453, 1.373, 0.0], [-0.465, 1.374, 0.0], [-0.478, 1.373, 0.0], [-0.49, 1.371, 0.0], [-0.502, 1.368, 0.0], [-0.513, 1.364, 0.0], [-0.523, 1.358, 0.0], [-0.533, 1.351, 0.0], [-0.542, 1.342, 0.0], [-0.55, 1.332, 0.0], [-0.558, 1.321, 0.0], [-0.564, 1.31, 0.0], [-0.57, 1.297, 0.0], [-0.574, 1.284, 0.0], [-0.578, 1.27, 0.0], [-0.58, 1.255, 0.0], [-0.582, 1.239, 0.0], [-0.582, 1.222, 0.0], [-0.581, 1.193, 0.0], [-0.575, 1.166, 0.0], [-0.566, 1.143, 0.0], [-0.554, 1.123, 0.0], [-0.538, 1.108, 0.0], [-0.53, 1.101, 0.0], [-0.52, 1.096, 0.0], [-0.51, 1.092, 0.0], [-0.499, 1.09, 0.0], [-0.488, 1.088, 0.0], [-0.476, 1.087, 0.0], [-0.461, 1.088, 0.0], [-0.447, 1.091, 0.0], [-0.434, 1.095, 0.0], [-0.422, 1.102, 0.0], [-0.411, 1.11, 0.0], [-0.401, 1.12, 0.0], [-0.392, 1.132, 0.0], [-0.384, 1.145, 0.0], [-0.384, 1.094, 0.0]],d=1)
    d_inline_char = mc.curve(p=[[-0.384, 1.302, 0.0], [-0.384, 1.176, 0.0], [-0.404, 1.156, 0.0], [-0.425, 1.142, 0.0], [-0.435, 1.137, 0.0], [-0.445, 1.134, 0.0], [-0.455, 1.132, 0.0], [-0.466, 1.131, 0.0], [-0.481, 1.132, 0.0], [-0.493, 1.137, 0.0], [-0.504, 1.145, 0.0], [-0.513, 1.155, 0.0], [-0.52, 1.169, 0.0], [-0.525, 1.185, 0.0], [-0.528, 1.205, 0.0], [-0.529, 1.227, 0.0], [-0.528, 1.252, 0.0], [-0.525, 1.274, 0.0], [-0.519, 1.292, 0.0], [-0.511, 1.308, 0.0], [-0.5, 1.321, 0.0], [-0.488, 1.329, 0.0], [-0.474, 1.335, 0.0], [-0.458, 1.337, 0.0], [-0.449, 1.336, 0.0], [-0.44, 1.334, 0.0], [-0.422, 1.328, 0.0], [-0.403, 1.317, 0.0], [-0.384, 1.302, 0.0]],d=1)
    i_top_char = mc.curve(p=[[-0.235, 1.418, 0.0], [-0.185, 1.418, 0.0], [-0.185, 1.467, 0.0], [-0.235, 1.467, 0.0], [-0.235, 1.418, 0.0]],d=1)
    i_bottom_char = mc.curve(p=[[-0.235, 1.094, 0.0], [-0.185, 1.094, 0.0], [-0.185, 1.368, 0.0], [-0.235, 1.368, 0.0], [-0.235, 1.094, 0.0]],d=1)
    v_char = mc.curve(p=[[-0.028, 1.094, 0.0], [0.022, 1.094, 0.0], [0.13, 1.368, 0.0], [0.084, 1.368, 0.0], [0.0, 1.155, 0.0], [-0.08, 1.368, 0.0], [-0.13, 1.368, 0.0], [-0.028, 1.094, 0.0]],d=1)
    line = mc.curve(p=[[0.0, 0.998, 0.0], [0.0, -0.0, 0.0]],d=1)

    curvelist.append(d_outline_char)
    curvelist.append(d_inline_char)
    curvelist.append(i_top_char)
    curvelist.append(i_bottom_char)
    curvelist.append(v_char)
    curvelist.append(line)

    sBbox = pm.exactWorldBoundingBox(currentSel)
    sBboxP =  [(sBbox[0] + sBbox[3])/2, sBbox[4], (sBbox[2] + sBbox[5])/2]
    smoothParentGroup = pm.group(curvelist,n=currentSel+'_smooth')
    smoothParentGroup.scalePivot.set([0,0,0])
    smoothParentGroup.rotatePivot.set([0,0,0])
    pm.xform(smoothParentGroup,t=sBboxP)
    pm.pointConstraint(currentSel,smoothParentGroup,mo=True)
    return smoothParentGroup
#複数オブジェクトにスムースをかけ、分割数をコントローラで一括制御できるようにする。
def createEasySmooth():
    sel = pm.selected()
    objs = sel[0:]
    cruveGen = generateCurve(sel[-1])
    slider = cruveGen[0]
    sliderField = cruveGen[1]
    smoothCtls = [cruveGen[2]]
    ctl = sliderField
    for currentSel in (sel[:-1]):
        smoothCtls.append(generateChildCurve(currentSel))
    pm.group(smoothCtls,n=smoothCtls[0]+'_Group' )
    # ctl = sel[-1] #[-1]で要素の末尾を取得
    #新しいアトリビュートを作成する
    pm.addAttr( ctl, ln='divisions',nn='div',at='long',min=0,max=4,dv=0)
    #作成したアトリビュートの編集を有効可する
    ctlDiv = pm.Attribute( ctl+'.divisions') 
    pm.setAttr( ctlDiv,e=True,keyable=True,)
    for obj in objs:
        smthChk=False
        for cnct in set( obj.getShape().inputs()):
            if isinstance(cnct, pm.nt.PolySmoothFace): #セットでinputsノードの重複を無くし、cnctの方がpolysmoothfaceだった場合（すでにスムースノードがある場合）はsmthckをtrueにする
                smthChk = True
                break
        if smthChk:
            ctlDiv >> cnct.divisions #すでにスムースノードがある場合は、それをctlDivアトリビュートと接続
            continue #すでにスムースノードがある場合、以降の処理をスキップ
        smthNode = pm.polySmooth(obj) #objに新しくスムースを追加し
        ctlDiv >> smthNode[0].divisions #スムースノードのdivisionsアトリビュートとctlのdivisionアトリビュート(ctlDiv)をつなぐ
    
    pm.transformLimits(slider,tx=(0,1.23),etx=(True,True))
    pm.setDrivenKeyframe("%s.divisions" % ctl,cd = "%s.tx" % slider,dv=0,v=0)
    pm.setDrivenKeyframe("%s.divisions" % ctl,cd = "%s.tx" % slider,dv=1.23,v=4)

with pm.window(title='イージースムーズ',width=250) as EasySmooth:
    with pm.columnLayout(adjustableColumn =True): #columnLayout:縦方向に要素を配置する　adjustableColumn: trueでUI横幅一杯に伸縮する
        with pm.horizontalLayout():
              pm.button( label='スムーズ' , command='print createEasySmooth()',bgc=[0.35,0.35,0.35])
        with pm.horizontalLayout():
              pm.button( label='閉じる' , command='print EasySmooth.delete(), "閉じる" ',bgc=[0.35,0.35,0.35])