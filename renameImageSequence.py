import subprocess
import os
import datetime
import shutil
import mimetypes
import re
import pymel.core as pm
import pymel.mayautils as mutl

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

def runImgcvt(dirName='', sameDirFlag='True', fileName = '', startNum = 1,):

    if dirName == '': #ディレクトリ名がない場合は実行できないようにする
        return

    myNode = pm.selected()
    if len(myNode) == 1: #選択したオブジェクトのアトリビュートがshapしかない場合
        imagePlaneName = myNode[0] 
    else:
        imagePlaneName = myNode[0].getShape() #選択したオブジェクトのアトリビュートが複数ある場合
    myName = pm.getAttr( "%s.imageName" % imagePlaneName) #イメージデータフォルダのパス(絶対パスで取得できてるぽい)
    currentDir = os.path.dirname(myName)
    file_type = os.path.splitext(myName)[1]
    print 'myNameで何が取得できているか確認。',file_type
    mayaLocation = mutl.getMayaLocation() + '\\bin'
    print 'test',mayaLocation
    rejectPadName = re.search(r"[^.]*(?=\.)",str(os.path.basename(myName)))
    currentImgPath = currentDir + '/' + rejectPadName.group() + '.#' + file_type
    print 'rejectPadName',os.path.basename(myName),rejectPadName.group()
    #現在使用している画像のファイルフォーマットを取得
    currentImgName = currentDir + '/' + myName
    
    # ユーザー入力情報
    start_num = startNum
    new_dir_name = dirName
    new_file_name = fileName
    if not sameDirFlag:
        new_file_name = dirName

    new_dir_path = currentDir + '/'+ new_dir_name
    imgFormatList = {
    'JPEG':'.jpg',
    'PNG':'.png',
    'TIFF 6.0': '.tif',
    'Targa':'.tga',
    'GIF':'.gif',
    'Abekas NTSC':'.yuv',
    'Alias':'.als',
    'Kodak Cineon':'.cin',
    'Lucas Film':'.lff',
    'Pixibox PXB':'.pxb',
    'SCN':'.scn',
    'PPM raw/ascii': '.ppm',
    'Prisms':'.pri',
    'Quantel':'.qtl',
    'SGI':'.sgi',
    'Avid® Softimage®':'.pic',
    'Vista':'.vst',
    'Wavefront RLA':'.rla'
    }


    #カレントディレクトリの下に新しいディレクトリを作って画像データをコピーする処理
    if __name__ == '__main__':
        if os.path.isdir(new_dir_path) is False: #指定したディレクトリパスが存在しない場合
            os.mkdir(new_dir_path) #新しくディレクトリを作成する
        arr = []
        for files in os.listdir(currentDir):
            if files.endswith(file_type):           
                arr.append(files)
                # ファイルのコピー
                print 'でバッグ1'
                shutil.copy(currentDir+'/'+files, new_dir_path)
                print 'でバッグ2'
    # 更新日時順に画像ファイルを連番でリネームする処理
    if __name__ == '__main__':
        print 'test'
        arr = []
        child_dir = new_dir_path+'/'
        # arrに更新日時:ファイル名の連想配列を追加していく処理
        for file_name in os.listdir(new_dir_path):
            path = child_dir + file_name
            arr.append((os.path.getmtime(path), file_name) )
        ind = start_num
        print arr
        #画像をソートしてファイル名に連番をつける処理
        for mtime,file_name in sorted(arr):
            new_name = new_file_name + '.' + str(ind).zfill(5) + file_type 
            t = datetime.datetime.fromtimestamp(mtime)
            print 'mtimeにはパスが入っているはず',t, new_name,mtime
            shutil.move(child_dir + file_name, child_dir + new_name)
            ind += 1
            print ind

    #カレントディレクトリの下に新しいディレクトリを作って画像データをコピーする処理
    selectFormat = imgFormatList[imgFormat.getValue()] 
    if file_type != selectFormat:
        renameList = os.listdir(new_dir_path)
        listLen = len(renameList)
        print 'フォーマット確認', selectFormat
        cmd = ['imgcvt','-r',str(startNum) + '-' + str(listLen+startNum-1).encode('cp932'),new_dir_path.encode('cp932') + '/' + new_file_name.encode('cp932') + '.@@@@@' + file_type.encode('cp932'),new_dir_path.encode('cp932') + '/'+ new_file_name.encode('cp932') + '.@@@@@' + selectFormat.encode('cp932')]
        print 'test',cmd
        returncode = subprocess.call(cmd,cwd=mayaLocation)
        for removeFile in renameList:
            if removeFile.endswith(file_type):
                os.remove(new_dir_path + '/' + removeFile)
    pm.setAttr( "%s.imageName" % imagePlaneName, new_dir_path + '/' + new_file_name + '.' + str(start_num).zfill(5) + selectFormat)




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
    print 'myNameで何が取得できているか確認。',myName
    #現在使用している画像のファイルフォーマットを取得
    currentImgName = currentDir + '/' + myName
    img = Image.open(currentImgName)
    imageFileFormat = img.format  
    print 'イメージフォーマットの確認' , imageFileFormat

    # ユーザー入力情報
    start_num = startNum
    new_dir_name = dirName
    new_file_name = fileName + '.'
    newImageFileFormat = 'bmp'
    if not sameDirFlag:
        new_file_name = dirName + '.'

    new_dir_path = currentDir + '/'+ new_dir_name

    #カレントディレクトリの下に新しいディレクトリを作って画像データをコピーする処理
    if __name__ == '__main__':
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
        # arrにファイルパス:ファイル名の連想配列を追加していく処理
        for file_name in os.listdir(new_dir_path):
            # print 'fortest'
            # if file_name.endswith('.jpg') or file_name.endswith('.JPG') : #JPGとjpgだと違う文字列扱いなので拡張子を指定するときは注意！
            path = child_dir + file_name
            arr.append((os.path.getmtime(path), file_name) )
        ind = start_num
        print arr
        #画像をソートしてファイル名に連番をつける処理
        for mtime,file_name in sorted(arr):
            new_name = new_file_name + str(ind).zfill(5) + '.' + newImageFileFormat #JPGとjpgだと違う文字列扱いなので拡張子を指定するときは注意！
            
            img = Image.open(mtime)
            img.save(child_dir + new_name,newImageFileFormat)
            new_name 
            t = datetime.datetime.fromtimestamp(mtime)
            print 'mtimeにはパスが入っているはず',t, new_name,mtime
            shutil.move(child_dir + file_name, child_dir + new_name)
            ind += 1
            print ind
    #イメージプレーンのイメージパスの更新
    pm.setAttr( "%s.imageName" % imagePlaneName, new_dir_path + '/' + new_file_name + str(start_num).zfill(5) + newImageFileFormat)

with pm.window( title = 'RE:ネームイメージシーケンス', width=300) as testWin:
    with pm.columnLayout( adjustableColumn=True):
        
        
        #ディレクトリ名
        # pm.text( label='text field')
        newDir = pm.textFieldGrp( label='※必須:新しいディレクトリ名',
        pht='ディレクトリ名を半角英数字で指定してください...')
        pm.separator()

        #ファイル名
        # pm.text( label='text field')
        pm.checkBox( label='ディレクトリ名を使用する',cc='newFile.setEnable( False if newFile.getEnable() else True)')
        newFile = pm.textFieldGrp( label='新しいファイル名',
        pht='新しいファイル名を半角英数字で指定してください...')
        # ファイルフォーマットの指定
        imgFormat = pm.optionMenu(label='フォーマット: ',width=150)
        pm.menuItem(label='JPEG')
        pm.menuItem(label='PNG')
        pm.menuItem(label='TIFF 6.0')
        pm.menuItem(label='Targa')
        pm.menuItem(label='GIF')
        pm.menuItem(label='Abekas NTSC')
        pm.menuItem(label='Alias')
        pm.menuItem(label='Kodak Cineon')
        pm.menuItem(label='Lucas Film')
        pm.menuItem(label='Pixibox PXB')
        pm.menuItem(label='SCN')
        pm.menuItem(label='PPM raw/ascii')
        pm.menuItem(label='Prisms')
        pm.menuItem(label='Quantel')
        pm.menuItem(label='SGI')
        pm.menuItem(label='Avid® Softimage®')
        pm.menuItem(label='Vista')
        pm.menuItem(label='Wavefront RLA')
        pm.separator()

        #連番指定
        # pm.text( label= '連番スタート')
        iField = pm.intFieldGrp( numberOfFields=1, #int数値入力のフィールドを作成する
        label='連番スタート', value=[1,0,0,0] )
        pm.separator()
        pm.button( label='フォルダを開く' , command='openCurrentImage()')
        # pm.button( label='printselectItem' , command='print pm.selected()')
        pm.button( label='リネーム実行' , command='print getSelectedImagePlaneName(newDir.getText(), newFile.getEnable(), newFile.getText(), iField.getValue()[0])')
        pm.button( label='リネーム実行runImgcvt' , command='print runImgcvt(newDir.getText(), newFile.getEnable(), newFile.getText(), iField.getValue()[0])')