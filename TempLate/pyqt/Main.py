import sys,keyboard
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal,QObject
from ui_untitled_ui import Ui_Form  # 需要更换ui_file_py以及Ui_Form
from PySide6.QtCore import QThreadPool,QThread

#全局变量区
GLOBAL_INT_VAR = 0
GLOBAL_DOUBLE_VAR = 0.0
GLOBAL_STR_VAR = ""
GLOBAL_LIST_VAR = list()
GLOBAL_TUPLE_VAR = tuple()
GLOBAL_DICT_VAR = dict()
GLOBAL_SET_VAR = set()

class MyThreadObject(QObject):
    # 自定义信号
    Signal_1 = Signal()
    Signal_2 = Signal()

    def __init__(self):
        super().__init__()
        self.Signal_1.connect(self.TaskFunction_1)
        self.Signal_2.connect(self.TaskFunction_2)

    def TaskFunction_1(self):
        pass

    def TaskFunction_2(self):
        pass

class MyWidget(QWidget):
    # 设置自定义信号
    MySignal_1 = Signal()
    MySignal_2 = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.SetUi()
        self.SetVar()
        self.SetBind()
        self.SetHook()
        self.SetThread()

    def SetUi(self):
        # 设置Ui
        pass

    def SetVar(self):
        # 设置变量
        pass

    def SetBind(self):
        # 设置绑定函数
        pass

    def SetHook(self):
        # 设置热键
        pass

    def SetThread(self):
        # 设置多线程
        self.MythreadObejct = MyThreadObject()
        self.thread = QThread()
        self.MythreadObejct.moveToThread(self.thread)
        self.thread.start()
        # # 在线程开启之后可以通过调用信号的方式来启动多线程任务
        # self.MythreadObejct.Signal_1.emit()
        # self.MythreadObejct.Signal_2.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
