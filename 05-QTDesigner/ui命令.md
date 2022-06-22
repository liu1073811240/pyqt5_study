# QTDesigner软件路径： %Python_path%\Lib\site-packages\qt5_applications\Qt\bin\designer.exe

# <1> ui转py文件
cd %Python_path%\Scripts
pyuic5.exe ui文件路径 -o py文件路径

# <2> ui转py可执行文件
pyuic5.exe ui文件路径 -o py文件路径2 -x

# qrc资源转换
pyrcc5.exe 资源路径.qrc -o 路径\test_source_rc.py
