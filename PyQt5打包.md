# 使用PyInstaller打包项目生成EXE文件  
PyInstaller可以将.py文件编译成.exe文件  
## 安装PyInstaller  
使用pip命令安装：pip install PyInstaller  
## 使用PyInstaller  
在命令行窗口进入需要打包的代码所在目录，运行: pyinstaller [opts] yourprogram.py  
opts: -F, -onefile, 打包成一个EXE文件  
      -D, -onedir,  创建一个目录，包含EXE文件  
      -c, -console, -nowindowed, 使用控制台，无窗口  
      -w, -windowed, -noconsole, 使用窗口  
通常 opts = -F -w  
