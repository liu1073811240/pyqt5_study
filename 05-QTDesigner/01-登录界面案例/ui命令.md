# QTDesigner软件路径： %Python_path%\Lib\site-packages\qt5_applications\Qt\bin\designer.exe

## 配置external tool
program: $python\$Qt\bin\designer.exe
working directory: $ProjectFileDir$

# <1> ui转py文件
cd %Python_path%\Scripts
pyuic5.exe ui文件路径 -o py文件路径

# <2> ui转py可执行文件
pyuic5.exe ui文件路径 -o py文件路径2 -x

## 配置external tool
program: $python$\Scripts\pyuic5.exe
Arguments: $FileName$ -o $FileNameWithoutExtension$.py -x
working directory: $FileDir$

# <3> qrc资源转换。(包含图片，转成我们能调用的资源)
pyrcc5.exe 资源路径.qrc -o 路径\test_source_rc.py

## 3.1 配置external tool
program: $python$\Scripts\pyrcc5.exe
Argements: $FileName$ -o $FileNameWithoutExtension$_rc.py
working directory: $FileDir$



