# 认识PyQt5
  PyQt5 是Qt框架的Python语言实现，可以进行GUI编程。此外Python这类的包还有，Tkinter， wxPython， PyGTK等。
  
  PyQt5环境的搭建(PyCharm)主要包括两步，一是PyQt5工具包；二是含有Qtdesigner的tools，均可以用pip安装：  
  详细介绍先贴两个连接
  [1](https://blog.csdn.net/HuangZhang_123/article/details/78046706)
  [2](https://www.cnblogs.com/dalanjing/p/6978373.html)
  
  这样的话，使用Qt就比较简单，先用Qtdesigner画一个图形界面，然后转成.py文件，最后进行调用即可

# 基本控件
## 窗口类
### QMainWindow
主窗口，包含菜单栏，工具栏，状态栏，标题栏等。
### QWigdet
基础窗口控件，用于建立界面。  

## 文本框类
### QLabel  
用来显示不可编辑的文本或者图片。  
### QLineEdit  
单行文本框，可以输入单行字符串，多行输入需要用到`QTextEdit`  
用法包括1. setText     2. setPlaceholderText(默认内容)     3. setInputMask(掩码)等  
### QTextEdit 
多行显示内容  

## 按钮类
按钮的基类为QAbstractButton,下面的各种按钮均继承该类。  
### QPushButton
单击执行命令的按钮。常用方法：1. setCheckable   2. toggle   3. setIcon   4. setEnabled    5. isChecked   6. setText  
### QRadioButton  
单选按钮：1. setCheckable  2. isChecked  3. setText  
### QCheckBox 
复选框： 1.setChecked   2. setText  
其中可以设置三态复选框，即选中有两种形式，半选中与选中  
### QComboBox
下拉列表框，1. addItem()    2. currentText()    3. currentIndex  
当选中一个选项时触发反应用Activate()  
### QSpinBox
计数器，通过单击增加或者减少当前的值， 1. setMinimum()   2. setMaximum()   3. Value()  
### QSlider
滑动条，滑动选择数值  

## 对话类控件  
QDialog, showDialog  
### QMessageBox  
用于显示消息的弹出式对话框，包括问答式(question), 警告(warning)等  
### QInputDialog  
获取交互的输入值  
### QFontDialog  
字体选择对话框  
### QFileDialog  
文件交互对话框, 1. get()openFilename   2. setFileMode  

## 窗口绘图类
### QPainter  
在QWidget上执行绘图操作, 绘制方法放在QtGui.QPainter对象的begin()与end()之间  
### QPen  
用于绘制直线、曲线、多边形等其它形状  
###  QBrush  
用于填充矩形等多边形的纹理  
### QPixmap  
由于显示图像，通常是标签(Label)  

## 日历与时间  
### QCalendar  
日历显示 1. setMinimumDate()   2. setMaximumDate()   3. setGridvisible()  
### QDateTimeEdit  
允许用户进行修改日期，可以设置日期的显示格式  

### 菜单栏、工具栏与状态栏  
## QMenuBar  
并行的菜单为级联的menubar对象，二级菜单则为QAction对象  
eg.  
bar = self.menuBar()  
file = bar.addMenu(“File”)  
file.addAction("New")  
file.triggered["New"].connect(self.function)  
### QToolBar  
工具栏，位于菜单栏下方，用法类似主菜单  
### QStatusBar  
状态栏  

### QPrinter  
嵌入到菜单栏或者状态栏中，将图片打印  





