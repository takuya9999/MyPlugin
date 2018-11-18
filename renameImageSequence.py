import subprocess
import os
import datetime
import shutil
import mimetypes
import re
import pymel.core as pm

#現在開いているシーンの置き場所をエクスプローラで開く
def openCurrentScene():
    currentPath = pm.sceneName()

    if currentPath:
        #currentPathを開く処理
        arg =['Explorer', currentPath.dirname().replace('/','\\')]
    else:
        #currentPathが空の時の処理
        projPath = pm.workspace.getPath()
        currentPath = projPath / pm.workspace.fileRules['mayaAscii']
        arg=['Explorer', currentPath.replace('/','\\')]
    subprocess.call(arg)

#現在指定しているイメージファイルの置き場所をエクスプローラで開く
def openCurrentImage():
    myNode = pm.selected()
    if len(myNode) == 1: #選択したオブジェクトのアトリビュートがshapしかない場合
        imagePlaneName = myNode[0] 
    else:
        imagePlaneName = myNode[0].getShape() #選択したオブジェクトのアトリビュートが複数ある場合
    myName = pm.getAttr( "%s.imageName" % imagePlaneName) #imagePlaneName.imageNameでもとれないか試す
    currentDir = os.path.dirname(myName) #イメージデータフォルダのパス
    currentPathReplace = currentDir.replace('/','\\')
    arg=['Explorer', currentPathReplace.encode('cp932')]
    print arg
    subprocess.call(arg)

def getSelectedImagePlaneName(dirName='', sameDirFlag='True', fileName = '', startNum = 1):
    
    if dirName == '': #ディレクトリ名がない場合は実行できないようにする
        return

    myNode = pm.selected()
    if len(myNode) == 1: #選択したオブジェクトのアトリビュートがshapしかない場合
        imagePlaneName = myNode[0] 
    else:
        imagePlaneName = myNode[0].getShape() #選択したオブジェクトのアトリビュートが複数ある場合
    myName = pm.getAttr( "%s.imageName" % imagePlaneName)
    currentDir = os.path.dirname(myName) #イメージデータフォルダのパス
    arg =['Explorer', currentDir.replace('/','\\')]
    
    # ユーザー入力情報
    start_num = startNum
    new_dir_name = dirName
    new_file_name = fileName + '.'

    if not sameDirFlag:
        new_file_name = dirName + '.'

    new_dir_path = currentDir + '/'+ new_dir_name

    #カレントディレクトリの下に新しいディレクトリを作って画像データをコピーする処理
    if __name__ == '__main__':
        file_type = 'image/jpeg'
        if os.path.isdir(new_dir_path) is False: #指定したディレクトリパスが存在しない場合
            os.mkdir(new_dir_path) #新しくディレクトリを作成する
        arr = []
        for files in os.listdir(currentDir):
            if mimetypes.guess_type(files)[0] == file_type:
                arr.append(files)
                # ファイルのコピー
                shutil.copy(currentDir+'/'+files, new_dir_path)

    # 更新日時順に画像ファイルを連番でリネームする処理
    if __name__ == '__main__':
        # print 'test'
        arr = []
        child_dir = new_dir_path+'/'
        for file_name in os.listdir(new_dir_path):
            # print 'fortest'
            if file_name.endswith('.jpg') or file_name.endswith('.JPG') : #JPGとjpgだと違う文字列扱いなので拡張子を指定するときは注意！
                path = child_dir + file_name
                arr.append((os.path.getmtime(path), file_name) )
        ind = start_num
        print arr
        for mtime,file_name in sorted(arr):
            new_name = new_file_name + str(ind).zfill(5) + '.jpg' #JPGとjpgだと違う文字列扱いなので拡張子を指定するときは注意！
            t = datetime.datetime.fromtimestamp(mtime)
            print(t, new_name)
            shutil.move(child_dir + file_name, child_dir + new_name)
            ind += 1
            print ind
    #イメージプレーンのイメージパスの更新
    pm.setAttr( "%s.imageName" % imagePlaneName, new_dir_path + '/' + new_file_name + str(start_num).zfill(5) + '.jpg')

with pm.window( title = 'RE:ネームイメージシーケンス', width=300) as testWin:
    with pm.columnLayout( adjustableColumn=True):
        
        
        #ディレクトリ名
        # pm.text( label='text field')
        newDir = pm.textFieldGrp( label='新しいディレクトリ名',
        pht='ディレクトリ名を半角英数字で指定してください...')
        pm.separator()

        #ファイル名
        # pm.text( label='text field')
        pm.checkBox( label='ディレクトリ名を使用する',cc='newFile.setEnable( False if newFile.getEnable() else True)')
        newFile = pm.textFieldGrp( label='新しいファイル名',
        pht='新しいファイル名を半角英数字で指定してください...')
        pm.separator()

        #連番指定
        # pm.text( label= '連番スタート')
        iField = pm.intFieldGrp( numberOfFields=1, #int数値入力のフィールドを作成する
        label='連番スタート', value=[1,0,0,0] )
        pm.separator()
        pm.button( label='フォルダを開く' , command='openCurrentImage()')
        # pm.button( label='printselectItem' , command='print pm.selected()')
        pm.button( label='デバッグ用' , command='print newDir.getText(), newFile.getEnable(), newFile.getText(), iField.getValue()[0] ')
        pm.button( label='リネーム実行' , command='print getSelectedImagePlaneName(newDir.getText(), newFile.getEnable(), newFile.getText(), iField.getValue()[0])')