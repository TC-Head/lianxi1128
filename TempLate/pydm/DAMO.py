import win32com.client
import os

class DMLEI():
    # dmlei只能32位Python使用
    # 该类会自动注册,程序退出时,会自动注销插件
    def __init__(self):
        try:
            self.obdm = win32com.client.Dispatch('dm.dmsoft')
        except:
            self.RegSystemDm()
            self.obdm = win32com.client.Dispatch('dm.dmsoft')

    def __del__(self):
        self.UnRegSystemDm()

    # <editor-fold desc="窗口API">
    def ClientToScreen(self,hwnd:int,x:int,y:int)->tuple:
        """
        Function:
            (Python中不可用)把窗口坐标转换为屏幕坐标
        parms:
            hwnd:
                指定窗口句柄
            x:
                窗口X坐标
            y:
                窗口Y坐标
        return:
            0代表失败,1代表成功
        """
        return self.obdm.ClientToScreen(hwnd,x,y)

    def EnumProcess(self,name:str)->str:
        """
        Function:
            根据指定进程名,枚举系统中符合条件的进程PID,并且按照进程打开顺序排序.
        parms:
            name:
                进程名,比如qq.exe
        return:
            返回所有匹配的进程PID,并按打开顺序排序,格式"pid1,pid2,pid3"
        """
        return self.obdm.EnumProcess(name)

    def EnumWindow(self,parent:int,title:str,class_name:str,filter:int)->str:
        """
        Function:
            (不实用,不建议使用)根据指定条件,枚举系统中符合条件的窗口,可以枚举到按键自带的无法枚举到的窗口
        parms:
            parent:
                获得的窗口句柄是该窗口的子窗口的窗口句柄,取0时为获得桌面句柄
            title:
                窗口标题. 此参数是模糊匹配.
            class_name:
                窗口类名. 此参数是模糊匹配.
            filter:
                取值定义如下
                1 : 匹配窗口标题,参数title有效
                2 : 匹配窗口类名,参数class_name有效.
                4 : 只匹配指定父窗口的第一层孩子窗口
                8 : 匹配父窗口为0的窗口,即顶级窗口
                16 : 匹配可见的窗口
                32 : 匹配出的窗口按照窗口打开顺序依次排列
        return:
            返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"
        """
        return self.obdm.EnumWindow(parent,title,class_name,filter)

    def EnumWindowByProcess(self,process_name:str,title:str,class_name:str,filter:int)->str:
        """
        Function:
            (不实用,不建议使用)根据指定进程以及其它条件,枚举系统中符合条件的窗口,可以枚举到按键自带的无法枚举到的窗口
        parms:
            process_name:
                进程映像名.比如(svchost.exe). 此参数是精确匹配,但不区分大小写.
            title:
                窗口标题. 此参数是模糊匹配.
            class_name:
                窗口类名. 此参数是模糊匹配.
            filter:
                取值定义如下
                1 : 匹配窗口标题,参数title有效
                2 : 匹配窗口类名,参数class_name有效
                4 : 只匹配指定映像的所对应的第一个进程. 可能有很多同映像名的进程，只匹配第一个进程的.
                8 : 匹配父窗口为0的窗口,即顶级窗口
                16 : 匹配可见的窗口
                32 : 匹配出的窗口按照窗口打开顺序依次排列
                这些值可以相加,比如4+8+16
        return:
            返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"
        """
        return self.obdm.EnumWindowByProcess(process_name,title,class_name,filter)

    def EnumWindowByProcessId(self,pid:int,title:str,class_name:str,filter:int)->str:
        """
        Function:
            (不实用,不建议使用)根据指定进程pid以及其它条件,枚举系统中符合条件的窗口,可以枚举到按键自带的无法枚举到的窗口
        parms:
            pid:
                进程pid.
            title:
                窗口标题. 此参数是模糊匹配.
            class_name:
                窗口类名. 此参数是模糊匹配.
            filter:
                取值定义如下
                1 : 匹配窗口标题,参数title有效
                2 : 匹配窗口类名,参数class_name有效
                8 : 匹配父窗口为0的窗口,即顶级窗口
                16 : 匹配可见的窗口
                这些值可以相加,比如2+8+16
        return:
            返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"
        """
        return self.obdm.EnumWindowByProcessId(pid,title,class_name,filter)

    def EnumWindowSuper(self,spec1,flag1,type1,spec2,flag2,type2,sort):
        """
        Function:
            (过于复杂,具体查看文档)根据两组设定条件来枚举指定窗口.
        parms:

        return:
            返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"
        """
        return self.obdm.EnumWindowSuper(spec1,flag1,type1,spec2,flag2,type2,sort)

    def FindWindow(self,class_name:str,title:str)->int:
        """
        Function:
            查找符合类名或者标题名的顶层可见窗口
        parms:
            class:
                窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.
            title:
                窗口标题,如果为空，则匹配所有.这里的匹配是模糊匹配.
        return:
            整形数表示的窗口句柄，没找到返回0
        """
        return self.obdm.FindWindow(class_name,title)

    def FindWindowByProcess(self,process_name:str,class_name:str,title:str)->int:
        """
        Function:
            根据指定的进程名字，来查找可见窗口.如果有多个符合条件结果,只返回第一个找到的
        parms:
            process_name:
                进程名. 比如(notepad.exe).这里是精确匹配,但不区分大小写.
            class_name:
                窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.
            title:
                窗口标题,如果为空，则匹配所有.这里的匹配是模糊匹配.
        return:
            整形数表示的窗口句柄，没找到返回0
        """
        return self.obdm.FindWindowByProcess(process_name,class_name,title)

    def FindWindowByProcessId(self,process_id:int,class_name:str,title:str)->int:
        """
        Function:
            根据指定的进程Id，来查找可见窗口.
        parms:
            process_id:
                进程id.
            class_name:
                窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.
            title:
                窗口标题,如果为空，则匹配所有.这里的匹配是模糊匹配.
        return:
            整形数表示的窗口句柄，没找到返回0
        """
        return self.obdm.FindWindowByProcessId(process_id,class_name,title)

    def FindWindowEx(self,parent:int,class_name:str,title:str)->int:
        """
        Function:
            查找符合类名或者标题名的顶层可见窗口,如果指定了parent,则在parent的第一层子窗口中查找.
        parms:
            parent:
                父窗口句柄，如果为空，则匹配所有顶层窗口
            class_name:
                窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.
            title:
                窗口标题,如果为空，则匹配所有. 这里的匹配是模糊匹配.
        return:
            整形数表示的窗口句柄，没找到返回0
        """
        return self.obdm.FindWindowEx(parent,class_name,title)

    def FindWindowSuper(self,spec1,flag1,type1,spec2,flag2,type2):
        """
        Function:
            具体用法较为复杂,可以查看文档查看
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.FindWindowSuper(spec1,flag1,type1,spec2,flag2,type2)

    def GetClientRect(self,hwnd:int)->tuple:
        """
        Function:
            获取窗口客户区域在屏幕上的位置
        parms:
            hwnd: 指定的窗口句柄
        return:
            返回一个tuple数组,该数组有五个元素
            第一个元素: 0代表获取失败,1代表获取成功
            第二个元素: 获取到的x1坐标
            第三个元素: 获取到的y1坐标
            第四个元素: 获取到的x2坐标
            第五个元素: 获取到的y2坐标
        """
        return self.obdm.GetClientRect(hwnd)

    def GetClientSize(self,hwnd:int)->tuple:
        """
        Function:
            获取窗口客户区域的宽度和高度
        parms:
            hwnd: 指定的窗口句柄
        return:
            返回一个tuple数据类型,总共三个元素
            第一个元素: 0代表失败,1代表成功
            第二个元素: 宽度
            第三个元素: 高度
        """
        return self.obdm.GetClientSize(hwnd)

    def GetForegroundFocus(self)->int:
        """
        Function:
            获取顶层活动窗口中具有输入焦点的窗口句柄
        parms:

        return:
            返回整型表示的窗口句柄
        """
        return self.obdm.GetForegroundFocus()

    def GetForegroundWindow(self)->int:
        """
        Function:
            获取顶层活动窗口,可以获取到按键自带插件无法获取到的句柄,在使用GetForegroundFocus函数没有效果时可以使用
        parms:

        return:
            返回整型表示的窗口句柄
        """
        return self.obdm.GetForegroundWindow()

    def GetMousePointWindow(self)->int:
        """
        Function:
            获取鼠标指向的可见窗口句柄,可以获取到按键自带的插件无法获取到的句柄
        parms:

        return:
            返回整型表示的窗口句柄
        """
        return self.obdm.GetMousePointWindow()

    def GetPointWindow(self,x:int,y:int)->tuple:
        """
        Function:
            获取给定坐标的可见窗口句柄,可以获取到按键自带的插件无法获取到的句柄
        parms:
            x:
                屏幕X坐标
            y:
                屏幕Y坐标
        return:
            返回整型表示的窗口句柄
        """
        return self.obdm.GetPointWindow(x,y)

    def GetProcessInfo(self,pid:int)->str:
        """
        Function:
            根据指定的pid获取进程详细信息,(进程名,进程全路径,CPU占用率(百分比),内存占用量(字节))
        parms:
            pid:
                进程pid
        return:
            返回值是一个str数据类型,格式  "进程名|进程路径|cpu|内存"
        """
        return self.obdm.GetProcessInfo(pid)

    def GetSpecialWindow(self,flag:int)->int:
        """
        Function:
            获取特殊窗口
        parms:
            flag:
                 取值定义如下
                    0 : 获取桌面窗口
                    1 : 获取任务栏窗口
        return:
            以整型数表示的窗口句柄
        """
        return self.obdm.GetSpecialWindow(flag)

    def GetWindow(self,hwnd:int,flag:int)->int:
        """
        Function:
            获取给定窗口相关的窗口句柄
        parms:
            hwnd:
                窗口聚丙
            flag:
                取值范围如下
                0 : 获取父窗口
                1 : 获取第一个儿子窗口
                2 : 获取First 窗口
                3 : 获取Last窗口
                4 : 获取下一个窗口
                5 : 获取上一个窗口
                6 : 获取拥有者窗口
                7 : 获取顶层窗口
        return:
            返回整型表示的窗口句柄
        """
        return self.obdm.GetWindow(hwnd,flag)

    def GetWindowClass(self,hwnd:int)->str:
        """
        Function:
            获取窗口的类名
        parms:
            hwnd:
                窗口句柄
        return:
            返回一个字符串,该字符串为窗口的类名
        """
        return self.obdm.GetWindowClass(hwnd)

    def GetWindowProcessId(self,hwnd:int)->int:
        """
        Function:
            获取指定窗口所在的进程ID.
        parms:
            hwnd:
                窗口句柄
        return:
            返回整型表示的是进程ID
        """
        return self.obdm.GetWindowProcessId(hwnd)

    def GetWindowProcessPath(self,hwnd:int)->str:
        """
        Function:
            获取指定窗口所在的进程的exe文件全路径.
        parms:
            hwnd:
                窗口句柄
        return:
            返回字符串表示的是exe全路径名
        """
        return self.obdm.GetWindowProcessPath(hwnd)

    def GetWindowRect(self,hwnd:int)->tuple:
        """
        Function:
            获取窗口在屏幕上的位置
        parms:
            hwnd:
                窗口句柄
        return:
            返回一直tuple数据类型,返回值有五个元素
            第一个元素: 0代表获取失败,1代表获取成功
            第二个元素: x1坐标
            第三个元素: y1坐标
            第四个元素: x2坐标
            第五个元素: y2坐标
        """
        return self.obdm.GetWindowRect(hwnd)

    def GetWindowState(self,hwnd:int,flag:int)->int:
        """
        Function:
            获取指定窗口的一些属性
        parms:
            hwnd:
                窗口句柄
            flag:
                取值范围如下
                0 : 判断窗口是否存在
                1 : 判断窗口是否处于激活
                2 : 判断窗口是否可见
                3 : 判断窗口是否最小化
                4 : 判断窗口是否最大化
                5 : 判断窗口是否置顶
                6 : 判断窗口是否无响应
                7 : 判断窗口是否可用(灰色为不可用)
                8 : 另外的方式判断窗口是否无响应,如果6无效可以尝试这个
                9 : 判断窗口所在进程是不是64位
        return:
            0代表不满足条件,1代表满足条件
        """
        return self.obdm.GetWindowState(hwnd,flag)

    def GetWindowThreadId(self,hwnd:int)->int:
        """
        Function:
            获取指定窗口所在的线程ID.
        parms:
            hwnd:
                窗口句柄
        return:
            返回整型表示的是线程ID
        """
        return self.obdm.GetWindowThreadId(hwnd)

    def GetWindowTitle(self,hwnd:int)->str:
        """
        Function:
            获取窗口的标题
        parms:
            hwnd:
                窗口句柄
        return:
            窗口的标题
        """
        return self.obdm.GetWindowTitle(hwnd)

    def MoveWindow(self,hwnd:int,x:int,y:int)->int:
        """
        Function:
            移动指定窗口到指定位置,窗口大小不变
        parms:
            hwnd:
                窗口句柄
            x:
                x坐标
            y:
                y坐标
        return:
            0代表失败,1代表成功
        """
        return self.obdm.MoveWindow(hwnd,x,y)

    def ScreenToClient(self,hwnd:int,x:int,y:int)->tuple:
        """
        Function:
            把屏幕坐标转换为窗口坐标
        parms:
            hwnd:
                窗口句柄
            x:
                屏幕x坐标
            y:
                屏幕y坐标
        return:
            返回值是一个tuple数据类型,总共三个元素
            第一个元素: 0代表失败,1代表成功
            第二个元素: 窗口中的x坐标
            第三个元素: 窗口中的y坐标
        """
        return self.obdm.ScreenToClient(hwnd,x,y)

    def SendPaste(self,hwnd:int)->int:
        """
        Function:
            (部分窗口不支持该API)向指定窗口发送粘贴命令. 把剪贴板的内容发送到目标窗口.
        parms:
            hwnd:
                窗口句柄
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SendPaste(hwnd)

    def SendString(self,hwnd:int,strtext:str)->int:
        """
        Function:
            向指定窗口发送文本数据
        parms:
            hwnd:
                指定的窗口句柄. 如果为0,则对当前激活的窗口发送.
            strtext:
                发送的文本
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SendString(hwnd,strtext)

    def SendString2(self,hwnd:int,strtext:str)->int:
        """
        Function:
            向指定窗口发送文本数据
        parms:
            hwnd:
                指定的窗口句柄. 如果为0,则对当前激活的窗口发送.
            strtext:
                发送的文本
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SendString2(hwnd,strtext)

    def SendStringIme(self,strtext:str)->int:
        """
        Function:
            向绑定的窗口发送文本数据.必须配合dx.public.input.ime属性.
        parms:
            strtext:
                发送的文本数据
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SendStringIme()

    def SendStringIme2(self,hwnd:int,strtext:str,mode:int)->int:
        """
        Function:
            利用真实的输入法，对指定的窗口输入文字.
        parms:
            hwnd:
                窗口句柄
            strtext:
                发送的文本数据
            mode:
                取值范围如下
                0 : 向hwnd的窗口输入文字(前提是必须先用模式200安装了输入法)
                1 : 同模式0,如果由于保护无效，可以尝试此模式.(前提是必须先用模式200安装了输入法)
                2 : 同模式0,如果由于保护无效，可以尝试此模式. (前提是必须先用模式200安装了输入法)
                200 : 向系统中安装输入法,多次调用没问题. 全局只用安装一次.
                300 : 卸载系统中的输入法. 全局只用卸载一次. 多次调用没关系.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SendStringIme2(hwnd,strtext,mode)

    def SetClientSize(self,hwnd:int,width:int,height:int)->int:
        """
        Function:
            设置窗口客户区域的宽度和高度
        parms:
            hwnd:
                指定的窗口句柄
            width:
                宽度
            height:
                过度
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetClientSize(hwnd,width,height)

    def SetWindowSize(self,hwnd:int,width:int,height:int)->int:
        """
        Function:
            设置窗口的大小
        parms:
            hwnd:
                指定的窗口句柄
            width:
                宽度
            height:
                高度
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetWindowSize(hwnd,width,height)

    def SetWindowState(self,hwnd:int,flag:int)->int:
        """
        Function:
            设置窗口的状态
        parms:
            hwnd:
                窗口句柄
            flag:
                取值范围如下
                0 : 关闭指定窗口
                1 : 激活指定窗口
                2 : 最小化指定窗口,但不激活
                3 : 最小化指定窗口,并释放内存,但同时也会激活窗口.(释放内存可以考虑用FreeProcessMemory函数)
                4 : 最大化指定窗口,同时激活窗口.
                5 : 恢复指定窗口 ,但不激活
                6 : 隐藏指定窗口
                7 : 显示指定窗口
                8 : 置顶指定窗口
                9 : 取消置顶指定窗口
                10 : 禁止指定窗口
                11 : 取消禁止指定窗口
                12 : 恢复并激活指定窗口
                13 : 强制结束窗口所在进程.
                14 : 闪烁指定的窗口
                15 : 使指定的窗口获取输入焦点
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetWindowState(hwnd,flag)

    def SetWindowText(self,hwnd:int,title:str)->int:
        """
        Function:
            设置窗口的标题
        parms:
            hwnd:
                指定窗口句柄
            title:
                标题
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetWindowText(hwnd,title)

    def SetWindowTransparent(self,hwnd:int,trans:int)->int:
        """
        Function:
            设置窗口的透明度
        parms:
            hwnd:
                指定窗口句柄
            trans:
                透明度,范围在(0-255),数字越小透明度越大,0为完全透明(不可见) 255为完全显示(不透明)
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetWindowTransparent(hwnd,trans)
    # </editor-fold>

    # <editor-fold desc="键鼠API">
    def EnableMouseAccuracy(self,enable:int)->int:
        """
        Function:
            设置当前系统鼠标的精确度开关.此接口仅仅对前台MoveR接口起作用.
        parms:
            enable:
                0 关闭指针精确度开关.  1打开指针精确度开关. 一般推荐关闭.
        return:
            设置之前的精确度开关.
        """
        self.obdm.EnableMouseAccuracy(enable)

    def GetCursorPos(self)->tuple:
        """
        Function:
            获取当前鼠标位置
        parms:

        return:
            返回一个tuple类型的返回值,总共三个元素
            第一个元素:0代表获取失败,1代表获取成功
            第二个元素:x坐标
            第三个元素:y坐标
        """
        return self.obdm.GetCursorPos()

    def GetCursorShape(self)->str:
        """
        Function:
            获取鼠标特征码.当BindWindow或者BindWindowEx中的mouse参数含有dx.mouse.cursor时,获取到的是后台鼠标特征，否则是前台鼠标特征.
        parms:

        return:
            返回鼠标对应的特征码
        """
        return self.obdm.GetCursorShape()

    def GetCursorShapeEx(self,type:int)->str:
        """
        Function:
            获取鼠标特征码. 当BindWindow或者BindWindowEx中的mouse参数含有dx.mouse.cursor时，获取到的是后台鼠标特征，否则是前台鼠标特征.
        parms:
            type:
                获取鼠标特征码的方式,当值为0时,跟GetCursorShape()函数是一致的.该参数可以设置两个值,分别是(0或者1)
        return:
            返回鼠标特征码
        """
        return self.obdm.GetCursorShapeEx(type)

    def GetCursorSpot(self)->str:
        """
        Function:
            (失效)获取鼠标热点位置.当BindWindow或者BindWindowEx中的mouse参数含有dx.mouse.cursor时,获取到的是后台鼠标热点位置，否则是前台鼠标热点位置.
        parms:

        return:
            成功时,返回x,y位置的字符串.
            失败时,返回空的字符串
        """
        return self.obdm.GetCursorSpot()

    def GetKeyState(self,Key:int)->int:
        """
        Function:
            获取指定的按键状态.(前台信息,不是后台)
        parms:
            Key:
                虚拟键码
        return:
            0代表弹起
            1代表按下
        """
        return self.obdm.GetKeyState(Key)

    def GetMouseSpeed(self)->int:
        """
        Function:
            获取系统鼠标的移动速度,一共分为11个级别,从1开始,11结束,这仅是前台鼠标的速度.后台不用理会这个.
        parms:

        return:
            0代表失败
            其他值,当前系统鼠标的速度
        """
        return self.obdm.GetMouseSpeed()

    def KeyDown(self,vk_code:int)->int:
        """
        Function:
            按住指定的虚拟键码
        parms:
            vk_code:
                虚拟按键码

        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyDown(vk_code)

    def KeyDownChar(self,key_str:str)->int:
        """
        Function:
            按住指定的虚拟键码
        parms:
            key_str:
                字符串描述的键码. 大小写无所谓.例如:'enter'
        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyDownChar(key_str)

    def KeyPress(self,vk_code:int)->int:
        """
        Function:
            按下指定的虚拟键码
        parms:
            vk_code:
                虚拟按键码
        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyPress(vk_code)

    def KeyPressChar(self,key_str:str)->int:
        """
        Function:
            按下指定的虚拟键码
        parms:
            key_str:
                字符串描述的键码. 大小写无所谓.例如:'enter'
        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyPressChar(key_str)

    def KeyPressStr(self,key_str:str,delay:int)->int:
        """
        Function:
            按下指定的虚拟键码
        parms:
            key_str:
                字符串描述的键码. 大小写无所谓.例如:'enter'
            delay:
                每按下一个按键，需要延时多久. 单位毫秒.这个值越大，按的速度越慢。
        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyPressStr(key_str,delay)

    def KeyUp(self,vk_code:int)->int:
        """
        Function:
            弹起来虚拟键vk_code
        parms:
            vk_code:
                虚拟键码
        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyUp(vk_code)

    def KeyUpChar(self,key_str:str)->int:
        """
        Function:
            弹起来虚拟键key_str
        parms:
            key_str:
                虚拟键码
        return:
            0代表失败,1代表成功
        """
        return self.obdm.KeyUpChar(key_str)

    def LeftClick(self)->int:
        """
        Function:
            按下鼠标左键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.LeftClick()

    def LeftDoubleClick(self)->int:
        """
        Function:
            双击鼠标左键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.LeftDoubleClick()

    def LeftDown(self)->int:
        """
        Function:
            按住鼠标左键
        parms:

        return:
             0代表失败,1代表成功
        """
        return self.obdm.LeftDown()

    def LeftUp(self)->int:
        """
        Function:
            弹起鼠标左键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.LeftUp()

    def MiddleClick(self)->int:
        """
        Function:
            按下鼠标中键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.MiddleClick()

    def MiddleDown(self)->int:
        """
        Function:
            按住鼠标中键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.MiddleDown()

    def MiddleUp(self)->int:
        """
        Function:
            弹起鼠标中键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.MiddleUp()

    def MoveR(self,rx:int,ry:int)->int:
        """
        Function:
            鼠标相对于上次的位置移动rx,ry.   如果您要使前台鼠标移动的距离和指定的rx,ry一致,最好配合EnableMouseAccuracy函数来使用.
            使用该参数最好使用   dm.EnableMouseAccuracy(0) // 关闭精确度开关
        parms:
            rx:
                相对于上次的X偏移
            ry:
                相对于上次的Y偏移
        return:
            0代表失败,1代表成功
        """
        return self.obdm.MoveR(rx,ry)

    def MoveTo(self,x:int,y:int)->int:
        """
        Function:
            把鼠标移动到目的点(x,y)
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.MoveTo(x,y)

    def MoveToEx(self,x:int,y:int,w:int,h:int)->int:
        """
        Function:
            把鼠标移动到目的范围内的任意一点
        parms:
            x:
                x坐标
            y:
                y坐标
            w:
                宽度
            h:
                高度
        return:
            返回要移动到的目标点. 格式为x,y
        """
        return self.obdm.MoveToEx(x,y,w,h)

    def RightClick(self)->int:
        """
        Function:
            按下鼠标右键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.RightClick()

    def RightDown(self)->int:
        """
        Function:
            按住鼠标右键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.RightDown()

    def RightUp(self)->int:
        """
        Function:
            弹起鼠标右键
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.RightUp()

    def SetKeypadDelay(self,type:str,delay:int)->int:
        """
        Function:
            设置按键时,键盘按下和弹起的时间间隔。高级用户使用。某些窗口可能需要调整这个参数才可以正常按键。
        parms:
            type:
                键盘类型,取值类型如下
                     "normal" : 对应normal键盘  默认内部延时为30ms
                     "windows": 对应windows 键盘 默认内部延时为10ms
                     "dx" :     对应dx 键盘 默认内部延时为50ms
            delay:
                延时,单位是毫秒
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetKeypadDelay()

    def SetMouseDelay(self,type:str,delay:int)->int:
        """
        Function:
            设置鼠标单击或者双击时,鼠标按下和弹起的时间间隔。高级用户使用。某些窗口可能需要调整这个参数才可以正常点击。
        parms:
            type:
                鼠标类型,取值范围有如下
                "normal" : 对应normal鼠标 默认内部延时为 30ms
                "windows": 对应windows 鼠标 默认内部延时为 10ms
                "dx" :     对应dx鼠标 默认内部延时为40ms
            delay:
                延时,单位是毫秒
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetMouseDelay(type,delay)

    def SetMouseSpeed(self,speed:int)->int:
        """
        Function:
            设置系统鼠标的移动速度.
        parms:
            spped:
                鼠标移动速度,最小1，最大11.  居中为6. 推荐设置为6
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetMouseSpeed(speed)

    def SetSimMode(self,mode:int)->int:
        """
        Function:
            设置前台键鼠的模拟方式.
        parms:
            mode:
                 0 正常模式(默认模式)
                 1 硬件模拟
                 2 硬件模拟2(ps2)（仅仅支持标准的3键鼠标，即左键，右键，中键，带滚轮的鼠标,2键和5键等扩展鼠标不支持）
                 3 硬件模拟3
        return:
             0 : 插件没注册
            -1 : 32位系统不支持
            -2 : 驱动释放失败.
            -3 : 驱动加载失败.可能是权限不够. 参考UAC权限设置. 或者是被安全软件拦截.如果是WIN10 1607之后的系统，出现这个错误，可参考这里
            -10: 设置失败
            -7 : 系统版本不支持. 可以用winver命令查看系统内部版本号. 驱动只支持正式发布的版本，所有预览版本都不支持.
             1 : 成功
        """
        self.obdm.SetSimMode(mode)

    def WaitKey(self,vk_code:int,time_out:int)->int:
        """
        Function:
            等待指定的按键按下 (前台,不是后台)
        parms:
            vk_code:
                虚拟按键码,当此值为0，表示等待任意按键。 鼠标左键是1,鼠标右键时2,鼠标中键是4.
            time_out:
                等待多久,单位毫秒. 如果是0，表示一直等待
        return:
            0代表失败,1代表成功
        """
        return self.obdm.WaitKey(vk_code,time_out)

    def WheelDown(self)->int:
        """
        Function:
            滚轮向下滚
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.WheelDown()

    def WheelUp(self)->int:
        """
        Function:
            滚轮向上滚
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.WheelUp()
    # </editor-fold>

    # <editor-fold desc="后台设置API">
    def BindWindow(self,hwnd:int,display:str,mouse:str,keypad:str,mode:int):
        """
        Function:
            绑定指定的窗口,并指定这个窗口的屏幕颜色获取方式,鼠标仿真模式,键盘仿真模式,以及模式设定,高级用户可以参考BindWindowEx更加灵活强大.
        parms:
            hwnd:
                绑定的窗口句柄
            display:
                取值范围如下
                "normal" : 正常模式,平常我们用的前台截屏模式
                "gdi" : gdi模式,用于窗口采用GDI方式刷新时. 此模式占用CPU较大. 参考SetAero  win10以上系统使用此模式，如果截图失败，尝试把目标程序重新开启再试试。
                "gdi2" : gdi2模式,此模式兼容性较强,但是速度比gdi模式要慢许多,如果gdi模式发现后台不刷新时,可以考虑用gdi2模式.
                "dx" : dx模式,等同于BindWindowEx中，display设置的"dx.graphic.2d|dx.graphic.3d",具体参考BindWindowEx
                "dx2" : dx2模式,用于窗口采用dx模式刷新,如果dx方式会出现窗口所在进程崩溃的状况,可以考虑采用这种.采用这种方式要保证窗口有一部分在屏幕外.win7 win8或者vista不需要移动也可后台.此模式占用CPU较大. 参考SetAero.   win10以上系统使用此模式，如果截图失败，尝试把目标程序重新开启再试试。
                "dx3" : dx3模式,同dx2模式,但是如果发现有些窗口后台不刷新时,可以考虑用dx3模式,此模式比dx2模式慢许多. 此模式占用CPU较大.参考SetAero. win10以上系统使用此模式，如果截图失败，尝试把目标程序重新开启再试试。
            mouse:
                取值范围如下
                "normal" : 正常模式,平常我们用的前台鼠标模式
                "windows": Windows模式,采取模拟windows消息方式 同按键自带后台插件.
                "windows2": Windows2 模式,采取模拟windows消息方式(锁定鼠标位置) 此模式等同于BindWindowEx中的mouse为以下组合 "dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.state.message"
                "windows3": Windows3模式，采取模拟windows消息方式,可以支持有多个子窗口的窗口后台.

                "dx": dx模式,采用模拟dx后台鼠标模式,这种方式会锁定鼠标输入.有些窗口在此模式下绑定时，需要先激活窗口再绑定(或者绑定以后激活)，否则可能会出现绑定后鼠标无效的情况.
                此模式等同于BindWindowEx中的mouse为以下组合"dx.public.active.api|dx.public.active.message|dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.state.api|dx.mouse.state.message|dx.mouse.api|dx.mouse.focus.input.api|dx.mouse.focus.input.message|dx.mouse.clip.lock.api|dx.mouse.input.lock.api|dx.mouse.cursor"

                "dx2"：dx2模式,这种方式类似于dx模式,但是不会锁定外部鼠标输入.有些窗口在此模式下绑定时，需要先激活窗口再绑定(或者绑定以后手动激活)，否则可能会出现绑定后鼠标无效的情况.
                此模式等同于BindWindowEx中的mouse为以下组合"dx.public.active.api|dx.public.active.message|dx.mouse.position.lock.api|dx.mouse.state.api|dx.mouse.api|dx.mouse.focus.input.api|dx.mouse.focus.input.message|dx.mouse.clip.lock.api|dx.mouse.input.lock.api| dx.mouse.cursor"
            keypad:
                取值范围如下
                "normal" : 正常模式,平常我们用的前台键盘模式
                "windows": Windows模式,采取模拟windows消息方式 同按键的后台插件.
                "dx": dx模式,采用模拟dx后台键盘模式。有些窗口在此模式下绑定时，需要先激活窗口再绑定(或者绑定以后激活)，否则可能会出现绑定后键盘无效的情况. 此模式等同于BindWindowEx中的keypad为以下组合
                "dx.public.active.api|dx.public.active.message| dx.keypad.state.api|dx.keypad.api|dx.keypad.input.lock.api"
            mode:
                取值范围如下
                 0 : 推荐模式此模式比较通用，而且后台效果是最好的.
                 2 : 同模式0,如果模式0有崩溃问题，可以尝试此模式. 注意0和2模式，当主绑定(第一个绑定同个窗口的对象)绑定成功后，那么调用主绑定的线程必须一致维持,否则线程一旦推出,对应的绑定也会消失.
                 101 : 超级绑定模式. 可隐藏目标进程中的dm.dll.避免被恶意检测.效果要比dx.public.hide.dll好. 推荐使用.
                 103 : 同模式101，如果模式101有崩溃问题，可以尝试此模式.
                 11 : 需要加载驱动,适合一些特殊的窗口,如果前面的无法绑定，可以尝试此模式. 此模式不支持32位系统
                 13 : 需要加载驱动,适合一些特殊的窗口,如果前面的无法绑定，可以尝试此模式. 此模式不支持32位系统
                需要注意的是: 模式101 103在大部分窗口下绑定都没问题。但也有少数特殊的窗口，比如有很多子窗口的窗口，对于这种窗口，在绑定时，一定要把
                鼠标指向一个可以输入文字的窗口，比如一个文本框，最好能激活这个文本框，这样可以保证绑定的成功.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.BindWindow(hwnd,display,mouse,keypad,mode)

    def BindWindowEx(self,hwnd:int,display:str,mouse:str,keypad:str,public:str,mode:int)->int:
        """
        Function:
            绑定指定的窗口,并指定这个窗口的屏幕颜色获取方式,鼠标仿真模式,键盘仿真模式 高级用户使用.
        parms:
            hwnd:
                指定窗口句柄
            display:
                取值范围有如下
                "normal" : 正常模式,平常我们用的前台截屏模式
                "gdi" : gdi模式,用于窗口采用GDI方式刷新时. 此模式占用CPU较大. 参考SetAero. win10以上系统使用此模式，如果截图失败，尝试把目标程序重新开启再试试。
                "gdi2" : gdi2模式,此模式兼容性较强,但是速度比gdi模式要慢许多,如果gdi模式发现后台不刷新时,可以考虑用gdi2模式.
                "dx"模式,用于窗口采用dx模式刷新,取值可以是以下任意组合，组合采用"|"符号进行连接. 支持BindWindow中的缩写模式.
                        比如dx代表" dx.graphic.2d| dx.graphic.3d"
                    1. "dx.graphic.2d"  2d窗口的dx图色模式
                    2. "dx.graphic.2d.2"  2d窗口的dx图色模式  是dx.graphic.2d的增强模式.兼容性更好.
                    3. "dx.graphic.3d"  3d窗口的dx图色模式,
                    4. "dx.graphic.3d.8"  3d窗口的dx8图色模式,  此模式对64位进程无效.
                    5. "dx.graphic.opengl"  3d窗口的opengl图色模式,极少数窗口采用opengl引擎刷新. 此图色模式速度可能较慢.
                    6. "dx.graphic.opengl.esv2"  3d窗口的opengl_esv2图色模式,极少数窗口采用opengl引擎刷新. 此图色模式速度可能较慢.
                    7. "dx.graphic.3d.10plus"  3d窗口的dx10 dx11 dx12图色模式
                "dx2" : dx2模式,用于窗口采用dx模式刷新,如果dx方式会出现窗口进程崩溃的状况,可以考虑采用这种.采用这种方式要保证窗口有一部分在屏幕外.win7 win8或者vista不需要移动也可后台. 此模式占用CPU较大. 参考SetAero. win10以上系统使用此模式，如果截图失败，尝试把目标程序重新开启再试试。
                "dx3" : dx3模式,同dx2模式,但是如果发现有些窗口后台不刷新时,可以考虑用dx3模式,此模式比dx2模式慢许多. 此模式占用CPU较大. 参考SetAero. win10以上系统使用此模式，如果截图失败，尝试把目标程序重新开启再试试。
            mouse:
                取值范围有如下
                "normal" : 正常模式,平常我们用的前台鼠标模式
                "windows": Windows模式,采取模拟windows消息方式 同按键的后台插件.
                "windows3": Windows3模式，采取模拟windows消息方式,可以支持有多个子窗口的窗口后台
                "dx"模式,取值可以是以下任意组合. 组合采用"|"符号进行连接. 支持BindWindow中的缩写模式,
                        比如windows2代表"dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.state.message"
                        1. "dx.mouse.position.lock.api"  此模式表示通过封锁系统API，来锁定鼠标位置.
                        2. "dx.mouse.position.lock.message" 此模式表示通过封锁系统消息，来锁定鼠标位置.
                        3. "dx.mouse.focus.input.api" 此模式表示通过封锁系统API来锁定鼠标输入焦点.
                        4. "dx.mouse.focus.input.message"此模式表示通过封锁系统消息来锁定鼠标输入焦点.
                        5. "dx.mouse.clip.lock.api" 此模式表示通过封锁系统API来锁定刷新区域。注意，使用这个模式，在绑定前，必须要让窗口完全显示出来.
                        6. "dx.mouse.input.lock.api" 此模式表示通过封锁系统API来锁定鼠标输入接口.
                        7. "dx.mouse.state.api" 此模式表示通过封锁系统API来锁定鼠标输入状态.
                        8. "dx.mouse.state.message" 此模式表示通过封锁系统消息来锁定鼠标输入状态.
                        9. "dx.mouse.api"  此模式表示通过封锁系统API来模拟dx鼠标输入.
                        10. "dx.mouse.cursor"  开启此模式，可以后台获取鼠标特征码.
                        11. "dx.mouse.raw.input"  有些窗口需要这个才可以正常操作鼠标.
                        12. "dx.mouse.input.lock.api2"  部分窗口在后台操作时，前台鼠标会移动,需要这个属性.
                        13. "dx.mouse.input.lock.api3"  部分窗口在后台操作时，前台鼠标会移动,需要这个属性.
            keypad:
                取值范围有如下
                "normal" : 正常模式,平常我们用的前台键盘模式
                "windows": Windows模式,采取模拟windows消息方式 同按键的后台插件.
                "dx"模式,取值可以是以下任意组合. 组合采用"|"符号进行连接. 支持BindWindow中的缩写模式.比如dx代表" dx.public.active.api|dx.public.active.message| dx.keypad.state.api|dx.keypad.api|dx.keypad.input.lock.api"
                    1. "dx.keypad.input.lock.api" 此模式表示通过封锁系统API来锁定键盘输入接口.
                    2. "dx.keypad.state.api" 此模式表示通过封锁系统API来锁定键盘输入状态.
                    3. "dx.keypad.api" 此模式表示通过封锁系统API来模拟dx键盘输入.
                    4. "dx.keypad.raw.input"  有些窗口需要这个才可以正常操作键盘.
            public:
                取值范围有如下
                取值可以是以下任意组合. 组合采用"|"符号进行连接 这个值可以为空
                    1. "dx.public.active.api" 此模式表示通过封锁系统API来锁定窗口激活状态.  注意，部分窗口在此模式下会耗费大量资源慎用.
                    2. "dx.public.active.message" 此模式表示通过封锁系统消息来锁定窗口激活状态.  注意，部分窗口在此模式下会耗费大量资源慎用. 另外如果要让此模式生效，必须在绑定前，让绑定窗口处于激活状态,否则此模式将失效. 比如dm.SetWindowState hwnd,1 然后再绑定.
                    3.  "dx.public.disable.window.position" 此模式将锁定绑定窗口位置.不可与"dx.public.fake.window.min"共用.
                    4.  "dx.public.disable.window.size" 此模式将锁定绑定窗口,禁止改变大小. 不可与"dx.public.fake.window.min"共用.
                    5.  "dx.public.disable.window.minmax" 此模式将禁止窗口最大化和最小化,但是付出的代价是窗口同时也会被置顶. 不可与"dx.public.fake.window.min"共用.
                    6.  "dx.public.fake.window.min" 此模式将允许目标窗口在最小化状态时，仍然能够像非最小化一样操作.. 另注意，此模式会导致任务栏顺序重排，所以如果是多开模式下，会看起来比较混乱，建议单开使用，多开不建议使用. 同时此模式不是万能的,有些情况下最小化以后图色会不刷新或者黑屏.
                    7.  "dx.public.hide.dll" 此模式将会隐藏目标进程的大漠插件，避免被检测..另外使用此模式前，请仔细做过测试，此模式可能会造成目标进程不稳定，出现崩溃。
                    8.  "dx.public.active.api2" 此模式表示通过封锁系统API来锁定窗口激活状态. 部分窗口遮挡无法后台,需要这个属性.
                    9.  "dx.public.input.ime" 此模式是配合SendStringIme使用. 具体可以查看SendStringIme接口.
                    10  "dx.public.graphic.protect" 此模式可以保护dx图色不被恶意检测.同时对dx.keypad.api和dx.mouse.api也有保护效果. 这个参数可能会导致某些情况下目标图色失效.一般出现在场景重新加载的时候. 重新绑定会恢复.
                    11  "dx.public.disable.window.show" 禁止目标窗口显示,这个一般用来配合dx.public.fake.window.min来使用.
                    12  "dx.public.anti.api" 此模式可以突破部分窗口对后台的保护.
                    13  "dx.public.km.protect" 此模式可以保护dx键鼠不被恶意检测.最好配合dx.public.anti.api一起使用. 此属性可能会导致部分后台功能失效.
                    14   "dx.public.prevent.block"  绑定模式1 3 5 7 101 103下，可能会导致部分窗口卡死. 这个属性可以避免卡死.
                    15   "dx.public.ori.proc"  此属性只能用在模式0 1 2 3和101下. 有些窗口在不同的界面下(比如登录界面和登录进以后的界面)，键鼠的控制效果不相同. 那可以用这个属性来尝试让保持一致. 注意的是，这个属性不可以滥用，确保测试无问题才可以使用. 否则可能会导致后台失效.
                    16  "dx.public.down.cpu" 此模式可以配合DownCpu来降低目标进程CPU占用.  当图色方式降低CPU无效时，可以尝试此种方式. 需要注意的是，当使用此方式降低CPU时，会让图色方式降低CPU失效
                    17  "dx.public.focus.message" 当后台绑定后,后台无法正常在焦点窗口输入文字时,可以尝试加入此属性. 此属性会强制键盘消息发送到焦点窗口. 慎用此模式,此模式有可能会导致后台键盘在某些情况下失灵.
                    18  "dx.public.graphic.speed" 只针对图色中的dx模式有效.此模式会牺牲目标窗口的性能，来提高DX图色速度，尤其是目标窗口刷新很慢时，这个参数就很有用了.
                    19  "dx.public.memory" 让本对象突破目标进程防护,可以正常使用内存接口. 当用此方式使用内存接口时，内存接口的速度会取决于目标窗口的刷新率.
                    20  "dx.public.inject.super" 突破某些难以绑定的窗口. 此属性仅对除了模式0和2的其他模式有效.
                    21  "dx.public.hack.speed" 类似变速齿轮，配合接口HackSpeed使用
                    22  "dx.public.inject.c" 突破某些难以绑定的窗口. 此属性仅对除了模式0和2的其他模式有效.
            mode:
                取值范围有如下
                    0 : 推荐模式此模式比较通用，而且后台效果是最好的.
                    2 : 同模式0,如果模式0有崩溃问题，可以尝试此模式.  注意0和2模式，当主绑定(第一个绑定同个窗口的对象)绑定成功后，那么调用主绑定的线程必须一直维持,否则线程一旦推出,对应的绑定也会消失.
                    101 : 超级绑定模式. 可隐藏目标进程中的dm.dll.避免被恶意检测.效果要比dx.public.hide.dll好. 推荐使用.
                    103 : 同模式101，如果模式101有崩溃问题，可以尝试此模式.
                    11 : 需要加载驱动,适合一些特殊的窗口,如果前面的无法绑定，可以尝试此模式. 此模式不支持32位系统
                    13 : 需要加载驱动,适合一些特殊的窗口,如果前面的无法绑定，可以尝试此模式. 此模式不支持32位系统
                    需要注意的是: 模式101 103在大部分窗口下绑定都没问题。但也有少数特殊的窗口，比如有很多子窗口的窗口，对于这种窗口，在绑定时，一定要把鼠标指向一个可以输入文字的窗口，比如一个文本框，最好能激活这个文本框，这样可以保证绑定的成功.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.BindWindowEx(hwnd,display,mouse,keypad,public,mode)

    def DownCpu(self,type:int,rate:int)->int:
        """
        Function:
            降低目标窗口所在进程的CPU占用.
        parms:
            type:
                当取值为0时,rate取值范围大于等于0 ,这个值越大表示降低CPU效果越好
                当取值为1时,rate取值范围大于等于0,表示以固定的FPS来降低CPU. rate表示FPS.  并且这时不能有dx.public.down.cpu.
            rate:
                取值取决于type. 为0表示关闭
        return:
            0代表失败,1代表成功
        注意:
            注意: 此接口必须在绑定窗口成功以后调用，
            而且必须保证目标窗口可以支持dx.graphic.3d或者dx.graphic.3d.8或者dx.graphic.2d或者dx.graphic.2d.2或者dx.graphic.opengl或者dx.graphic.opengl.esv2方式截图，或者使用dx.public.down.cpu(仅限type为0).否则降低CPU无效.
            因为降低CPU是通过降低窗口刷新速度或者在系统消息循环增加延时来实现，所以注意，开启此功能以后会导致窗口刷新速度变慢.
        """
        return self.obdm.DownCpu(type,rate)

    def EnableBind(self,enable:int)->int:
        """
        Function:
            设置是否暂时关闭或者开启后台功能. 默认是开启.  一般用在前台切换，或者脚本暂停和恢复时，可以让用户操作窗口.
        parms:
            enable:
                    0 全部关闭(图色键鼠都关闭,也就是说图色,键鼠都是前台,但是如果有指定dx.public.active.message时，在窗口前后台切换时，这个属性会失效.)
                    -1 只关闭图色.(也就是说图色是normal前台. 键鼠不变)
                    1 开启(恢复原始状态)
                    5 同0，也是全部关闭，但是这个模式下，就算窗口在前后台切换时，属性dx.public.active.message的效果也一样不会失效.
        return:
            0代表失败,1代表成功
        注意:
            注意切换到前台以后,相当于dm_ret = dm.BindWindow(hwnd,"normal","normal","normal",0),图色键鼠全部是前台.
            如果你经常有频繁切换后台和前台的操作，推荐使用这个函数.
            同时要注意,如果有多个对象绑定了同个窗口，其中任何一个对象禁止了后台,那么其他对象后台也同样失效.

        """
        return self.obdm.EnableBind(enable)

    def EnableFakeActive(self,enable:int)->int:
        """
        Function:
            设置是否开启后台假激活功能. 默认是关闭. 一般用不到. 除非有人有特殊需求.
        parms:
            enable:
                0代表关闭,1代表开启
        return:
            0代表失败,1代表成功
        注意:
            需要绑定之后才可以调用此函数,
            此接口的含义并不是关闭或者开启窗口假激活功能(dx.public.active.api或者dx.public.active.message).
            而是说有些时候，本来窗口没有激活并且在没有绑定的状态下，可以正常使用的功能，而在窗口绑定以后,并且窗口在非激活状态下,此时由于绑定的锁定导致无法使用.
            那么，你就需要把你的部分代码用EnableFakeActive来保护起来。这样就让插件认为你的这段代码是在窗口激活状态下执行.
            另外，此函数开启以后，有可能会让前台影响到后台. 所以如果不是特殊情况，最好是关闭.  开启这个还会把已经锁定的键盘鼠标(LockInput)强制解锁.
            有些时候，有人会故意利用这个前台影响后台的作用，做类似同步器的软件，那这个函数就很有作用了.
            另外,还有一些窗口对消息检测比较严格,那么需要开启这个接口才可以后台操作,或者组合键操作.
        """
        return self.obdm.EnableFakeActive(enable)

    def EnableIme(self,enable:int)->int:
        """
        Function:
            设置是否关闭绑定窗口所在进程的输入法.
            注意:此函数必须在绑定后调用才有效果.
        parms:
            enable:
                0代表关闭,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableIme(enable)

    def EnableKeypadMsg(self,enable:int)->int:
        """
        Function:
            是否在使用dx键盘时开启windows消息.默认开启.
            注意:此函数必须在绑定后调用才有效果.
        parms:
            enable:
                0代表禁止,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableKeypadMsg(enable)

    def EnableKeypadPatch(self,enable:int)->int:
        """
        Function:
            键盘消息发送补丁. 默认是关闭.
            注意:此函数必须在绑定后调用才有效果.
        parms:
            enable:
                0代表禁止,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableKeypadPatch(enable)

    def EnableKeypadSync(self,enable:int,time_out:int)->int:
        """
        Function:
            键盘消息采用同步发送模式.默认异步.
            注意:此接口必须在绑定之后才能调用。有些时候，如果是异步发送，如果发送动作太快,中间没有延时,有可能下个动作会影响前面的.而用同步就没有这个担心.
        parms:
            enable:
                0代表禁止,1代表开启
            time_out:
                单位是毫秒,表示同步等待的最大时间.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableKeypadSync(enable,time_out)

    def EnableMouseMsg(self,enable:int)->int:
        """
        Function:
            是否在使用dx鼠标时开启windows消息.默认开启.
            注意:此函数必须在绑定后调用才有效果.
        parms:
            enable:
                0代表禁止,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableMouseMsg(enable)

    def EnableMouseSync(self,enable:int,time_out:int)->int:
        """
        Function:
            鼠标消息采用同步发送模式.默认异步.
            注意:此函数必须在绑定后调用才有效果.
                有些时候，如果是异步发送，如果发送动作太快,中间没有延时,有可能下个动作会影响前面的.而用同步就没有这个担心.
        parms:
            enable:
                0代表禁止,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableMouseSync(enable,time_out)

    def EnableRealKeypad(self,enable:int)->int:
        """
        Function:
            键盘动作模拟真实操作,点击延时随机.
            注意:此接口对KeyPress KeyPressChar KeyPressStr起作用。具体表现是键盘按下和弹起的间隔会在
                当前设定延时的基础上,上下随机浮动50%. 假如设定的键盘延时是100,那么这个延时可能就是50-150之间的一个值.
                设定延时的函数是 SetKeypadDelay
        parms:
            enable:
                0代表关闭模拟,1代表开启模拟
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableRealKeypad(enable)

    def EnableRealMouse(self,enable:int,mousedelay:int,Mousetep:int)->int:
        """
        Function:
            鼠标动作模拟真实操作,带移动轨迹,以及点击延时随机.
            注意:此函数必须在绑定后调用才有效果.
                此接口同样对LeftClick RightClick MiddleClick LeftDoubleClick起作用。具体表现是鼠标按下和弹起的间隔会在
                当前设定延时的基础上,上下随机浮动50%. 假如设定的鼠标延时是100,那么这个延时可能就是50-150之间的一个值.设定延时的函数是 SetMouseDelay
        parms:
            enable:
                取值范围有如下
                0 关闭模拟
                1 开启模拟(直线模拟)
                2 开启模拟(随机曲线,更接近真实)
                3 开启模拟(小弧度曲线,弧度随机)
                4 开启模拟(大弧度曲线,弧度随机)
            mousedelay:
                单位是毫秒. 表示在模拟鼠标移动轨迹时,每移动一次的时间间隔.这个值越大,鼠标移动越慢. 必须大于0,否则会失败.
            Mousetep:
                表示在模拟鼠标移动轨迹时,每移动一次的距离. 这个值越大，鼠标移动越快速.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableRealMouse(enable,mousedelay,Mousetep)

    def EnableSpeedDx(self,enable:int)->int:
        """
        Function:
            设置是否开启高速dx键鼠模式。 默认是关闭.
            注意:此函数必须在绑定后调用才有效果.
                此函数开启的后果就是，所有dx键鼠操作将不会等待，适用于某些特殊的场合(比如避免窗口无响应导致宿主进程也卡死的问题).
                EnableMouseSync和EnableKeyboardSync开启以后，此函数就无效了.此函数可能在部分窗口下会有副作用，谨慎使用!!
        parms:
            enable:
                0代表关闭,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableSpeedDx(enable)

    def ForceUnBindWindow(self,hwnd:int)->int:
        """
        Function:
            强制解除绑定窗口,并释放系统资源.
            注意:此函数必须在绑定后调用才有效果.
                此接口一般用在BindWindow和BindWindowEx中
                使用了模式1 3 5 7或者属性dx.public.hide.dll后，在线程或者进程结束后，没有正确调用UnBindWindow而导致下次绑定无法成功时，可以先调用这个函数强制解除绑定，并释放资源，再进行绑定.
                此接口不可替代UnBindWindow. 只是用在非常时刻. 切记.
                一般情况下可以无条件的在BindWindow或者BindWindowEx之前调用一次此函数。保证此刻窗口处于非绑定状态.
                另外，需要注意的是,此函数只可以强制解绑在同进程绑定的窗口.  不可在不同的进程解绑别的进程绑定的窗口.(会产生异常)
        parms:
            hwnd:
                需要强制解除绑定的窗口句柄.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.ForceUnBindWindow(hwnd)

    def GetBindWindow(self)->int:
        """
        Function:
            获取当前对象已经绑定的窗口句柄. 无绑定返回0
        parms:

        return:
            返回绑定窗口的句柄,无绑定返回0
        """
        return self.obdm.GetBindWindow()

    def GetFps(self)->int:
        """
        Function:
            获取绑定窗口的fps.
            注意:此函数必须在绑定后调用才有效果.
        parms:

        return:
            返回窗口的fps数值
        """
        return self.obdm.GetFps()

    def HackSpeed(self,rate:int)->int:
        """
        Function:
            对目标窗口设置加速功能(类似变速齿轮),必须在绑定参数中有dx.public.hack.speed时才会生效.
            注意:此函数必须在绑定后调用才有效果.
        parms:
            rate:
                取值范围大于0. 默认是1.0 表示不加速，也不减速. 小于1.0表示减速,大于1.0表示加速. 精度为小数点后1位. 也就是说1.5 和 1.56其实是一样的.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.HackSpeed(rate)

    def IsBind(self,hwnd:int)->int:
        """
        Function:
            判定指定窗口是否已经被后台绑定. (前台无法判定)
            注意:此函数必须在绑定后调用才有效果.
        parms:
            hwnd:
                窗口句柄
        return:
            0代表没绑定或者窗口不存在
            1代表已经绑定
        """
        return self.obdm.IsBind(hwnd)

    def LockDisplay(self,lock:int)->int:
        """
        Function:
            锁定指定窗口的图色数据(不刷新).
            注意:此函数必须在绑定后调用才有效果.
                此接口只对图色为dx.graphic.3d  dx.graphic.3d.8 dx.graphic.2d  dx.graphic.2d.2 dx.graphic.3d.10plus有效
        parms:
            lock:
                0代表关闭锁定,1代表开启锁定
        return:
            0代表失败,1代表成功
        """
        return self.obdm.LockDisplay(lock)

    def LockInput(self,lock:int)->int:
        """
        Function:
            禁止外部输入到指定窗口
            注意:此函数必须在绑定后调用才有效果.
                此接口只针对dx键鼠. 普通键鼠无效.
                有时候，绑定为dx2 鼠标模式时(或者没有锁定鼠标位置或状态时)，在脚本处理过程中，在某个时候需要临时锁定外部输入，以免外部干扰，那么这个函数就非常有用.
                比如某个信息，需要鼠标移动到某个位置才可以获取，但这时，如果外部干扰，那么很可能就会获取失败，所以，这时候就很有必要锁定外部输入.
                当然，锁定完以后，记得要解除锁定，否则外部永远都无法输入了，除非解除了窗口绑定.
        parms:
            lock:
                0 关闭锁定
                1 开启锁定(键盘鼠标都锁定)
                2 只锁定鼠标
                3 只锁定键盘
                4 同1,但当您发现某些特殊按键无法锁定时,比如(回车，ESC等)，那就用这个模式吧. 但此模式会让SendString函数后台失效，或者采用和SendString类似原理发送字符串的其他3方函数失效.
                5 同3,但当您发现某些特殊按键无法锁定时,比如(回车，ESC等)，那就用这个模式吧. 但此模式会让SendString函数后台失效，或者采用和SendString类似原理发送字符串的其他3方函数失效.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.LockInput(lock)

    def LockMouseRect(self,x1:int,y1:int,x2:int,y2:int)->int:
        """
        Function:
            设置前台鼠标在屏幕上的活动范围.
            注意:调用此函数后，一旦有窗口切换或者窗口移动的动作，那么限制立刻失效.
                如果想一直限制鼠标范围在指定的窗口客户区域，那么你需要启动一个线程，并且时刻监视当前活动窗口，然后根据情况调用此函数限制鼠标范围.
        parms:
            x1:
                区域的左上X坐标. 屏幕坐标.
            y1:
                区域的左上Y坐标. 屏幕坐标.
            x2:
                区域的右下X坐标. 屏幕坐标.
            y2:
                区域的右下Y坐标. 屏幕坐标.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.LockMouseRect(x1,y1,x2,y2)

    def SetAero(self,enable:int)->int:
        """
        Function:
            设置开启或者关闭系统的Aero效果.
            注意:此函数必须在绑定后调用才有效果.
                如果您发现当图色后台为dx2 gdi dx3时，如果有发现目标窗口刷新速度过慢,那可以考虑关闭系统Aero. (当然这仅仅是可能的原因)
        parms:
            enable:
                0代表禁止,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetAero(enable)

    def SetDisplayDelay(self,time:int)->int:
        """
        Function:
            设置dx截图最长等待时间。内部默认是3000毫秒. 一般用不到调整这个
            注意:此函数必须在绑定后调用才有效果.
                此接口仅对图色为dx.graphic.3d   dx.graphic.3d.8  dx.graphic.2d   dx.graphic.2d.2有效. 其他图色模式无效.
                默认情况下，截图需要等待一个延时，超时就认为截图失败. 这个接口可以调整这个延时.
                某些时候或许有用.比如当窗口图色卡死(这时获取图色一定都是超时)，并且要判断窗口卡死，那么这个设置就很有用了
        parms:
            time:
                等待时间,单位是毫秒.
                注意这里不能设置的过小,否则可能会导致截图失败,从而导致图色函数和文字识别失败.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetDisplayDelay(time)

    def SetDisplayRefreshDelay(self,time:int)->int:
        """
        Function:
            设置opengl图色模式的强制刷新窗口等待时间. 内置为400毫秒.
            注意:此函数必须在绑定后调用才有效果.
        parms:
            time:
                等待时间，单位是毫秒。这个值越小,强制刷新的越频繁，相应的窗口可能会导致闪烁.
        return:
            0代表失败,1代表成功
        注意:
            此接口仅对   图色为dx.graphic.opengl有效. 其他图色模式无效.
            默认情况下，openg截图时，如果对应的窗口处于不刷新的状态,那么我们的所有图色接口都会无法截图,从而超时导致失效。
            所以特意设置这个接口，如果截图的时间超过此接口设置的时间,那么插件会对绑定的窗口强制刷新,从而让截图成功.
            但是强制刷新窗口是有代价的，会造成窗口闪烁。
            如果您需要截图的窗口，刷新非常频繁，那么一般用不到强制刷新，所以可以用这个接口把等待时间设置大一些，从而避免窗口闪烁.
            反之,如果您需要截图的窗口偶尔才刷新一次(比如按某个按钮，才刷新一次),那么您就需要用这个接口把等待时间设置小一些，从而提高图色函数的效率，但代价就是窗口可能会闪烁.
            当这个接口设置的值超过SetDisplayDelay设置的值(默认是3000毫秒)时,那么opengl截图的方式就退化到老版本(大概是6.1540版本)的模式.(也就是不会强制刷新的版本).
            如果您发现你的程序截图会截取到以前的图片,那么建议把此值加大(建议值2000).
            如果您发现你的程序偶尔会闪烁,导致窗口出现白色区域,那么可以尝试把此值设置为大于SetDisplayDelay的值(默认是3000毫秒),这样可以彻底杜绝刷新.
        """
        return self.obdm.SetDisplayRefreshDelay(time)

    def SwitchBindWindow(self,hwnd:int)->int:
        """
        Function:
            在不解绑的情况下,切换绑定窗口.(必须是同进程窗口)
            注意:此函数必须在绑定后调用才有效果.
                此函数一般用在绑定以后，窗口句柄改变了的情况。如果必须不解绑，那么此函数就很有用了。
        parms:
            hwnd:
                需要切换过去的窗口句柄
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SwitchBindWindow(hwnd)

    def UnBindWindow(self)->int:
        """
        Function:
            解除绑定窗口,并释放系统资源.一般在OnScriptExit调用
            注意:此函数必须在绑定后调用才有效果.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.UnBindWindow()
    # </editor-fold>

    # <editor-fold desc="汇编API">
    def AsmAdd(self,asm_ins:str)->int:
        """
        Function:
            添加指定的MASM汇编指令. 支持标准的masm汇编指令.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.AsmAdd(asm_ins)

    def AsmCall(self,hwnd:int,mode:int)->int:
        """
        Function:
            执行用AsmAdd加到缓冲中的指令.
        parms:
            hwnd:
                窗口句柄
            mode:
                取值范围如下
                0 : 在本进程中进行执行，这时hwnd无效. 注: 此模式会创建线程.
                1 : 对hwnd指定的进程内执行,注入模式为创建远程线程
                2 ：必须在对目标窗口进行注入绑定后,才可以用此模式(直接在目标进程创建线程).此模式下的call的执行是排队的,如果同时有多个call在此窗口执行,那么必须排队.所以执行效率不如模式1. 同时此模式受目标窗口刷新速度的影响,目标窗口刷新太慢，也会影响此模式的速度. 注: 此模式会创建线程.
                3 ：同模式2,但是此模式不会创建线程,而直接在hwnd所在线程执行.
                4 ：同模式0, 但是此模式不会创建线程,直接在当前调用AsmCall的线程内执行.
                5 : 对hwnd指定的进程内执行,注入模式为APC. 此模式必须开启memory盾。任意一个memory盾都可以.
                6 : 直接hwnd所在线程执行.
        return:
            获取执行汇编代码以后的EAX的值(32位进程),或者RAX的值(64位进程).一般是函数的返回值. 如果要想知道函数是否执行成功，请查看GetLastError函数.
            -200 : 执行中出现错误.
            -201 : 使用模式5时，没有开启memory盾.
        """
        return self.obdm.AsmCall(hwnd,mode)

    def AsmCallEx(self,hwnd:int,mode:int,base_addr:str)->int:
        """
        Function:
            执行用AsmAdd加到缓冲中的指令.  这个接口同AsmCall,但是由于插件内部在每次AsmCall时,都会有对目标进程分配内存的操作,这样会不够效率.
            所以增加这个接口，可以让调用者指定分配好的内存,并在此内存上执行call的操作.
        parms:
            hwnd:
                窗口句柄
            mode:
                0 : 在本进程中进行执行，这时hwnd无效. 注: 此模式会创建线程.
                1 : 对hwnd指定的进程内执行,注入模式为创建远程线程
                2 ：必须在对目标窗口进行注入绑定后,才可以用此模式(直接在目标进程创建线程).此模式下的call的执行是排队的,如果同时有多个call在此窗口执行,那么必须排队.所以执行效率不如模式1. 同时此模式受目标窗口刷新速度的影响,目标窗口刷新太慢，也会影响此模式的速度. 注: 此模式会创建线程.
                3 ：同模式2,但是此模式不会创建线程,而直接在hwnd所在线程执行.
                4 ：同模式0, 但是此模式不会创建线程,直接在当前调用AsmCall的线程内执行.
                5 : 对hwnd指定的进程内执行,注入模式为APC. 此模式必须开启memory盾。任意一个memory盾都可以.
                6 : 直接hwnd所在线程执行.
            base_addr:
                字符串: 16进制格式. 比如"45A00000",此参数指定的地址必须要求有可读可写可执行属性. 并且内存大小最少要200个字节. 模式6要求至少400个字节. 如果Call的内容较多,那么长度相应也要增加.   如果此参数为空,那么效果就和AsmCall一样.
        return:
            获取执行汇编代码以后的EAX的值(32位进程),或者RAX的值(64位进程).一般是函数的返回值. 如果要想知道函数是否执行成功，请查看GetLastError函数.
            -200 : 执行中出现错误.
            -201 : 使用模式5时，没有开启memory盾.
        """
        return self.obdm.AsmCallEx(hwnd,mode,base_addr)

    def AsmClear(self)->int:
        """
        Function:
            清除汇编指令缓冲区 用AsmAdd添加到缓冲的指令全部清除
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.AsmClear()

    def AsmSetTimeout(self,time_out:int,param:int)->int:
        """
        Function:
            此接口对AsmCall和AsmCallEx中的模式5和6中内置的一些延时参数进行设置.
        parms:
            time_out:
                (默认值10000) 单位毫秒
            param:
                (默认值100) 单位毫秒
        return:
            0代表失败,1代表成功
        注意:
            time_out同时影响模式5和6.单位是毫秒。 表示执行此AsmCall时，最长的等待时间. 超过此时间后，强制结束. 如果是-1，表示无限等待.
            比如，当执行某个寻路call时,需要到寻路结束，call才会返回. 那么就需要把此参数设置大一些，甚至设置为-1.
            param仅影响模式6.  这个值越大,越不容易引起目标进程崩溃，同时call的执行速度相对慢一些. 越小越容易崩溃,同时call的执行速度快一些. 可根据自己情况设置. 一般默认的就可以了.
        """
        return self.obdm.time_out,param(time_out,param)

    def Assemble(self,base_addr:int,is_64bit:int)->int:
        """
        Function:
            把汇编缓冲区的指令转换为机器码 并用16进制字符串的形式输出
        parms:
            base_addr:
                用AsmAdd添加到缓冲区的第一条指令所在的地址
            is_64bit:
                表示缓冲区的指令是32位还是64位. 32位表示为0,64位表示为1
        return:
            机器码，比如 "aa bb cc"这样的形式
        """
        return self.obdm.Assemble(base_addr,is_64bit)

    def DisAssemble(self,asm_code,base_addr:int,is_64bit:int)->int:
        """
        Function:
            把汇编缓冲区的指令转换为机器码 并用16进制字符串的形式输出
        parms:
            asm_code:
                机器码，形式如 "aa bb cc"这样的16进制表示的字符串(空格无所谓)
            base_addr:
                指令所在的地址
            is_64bit:
                表示asm_code表示的指令是32位还是64位. 32位表示为0,64位表示为1
        return:
            MASM汇编语言字符串.如果有多条指令，则每条指令以字符"|"连接.
        """
        return self.obdm.DisAssemble(asm_code,base_addr,is_64bit)
    # </editor-fold>

    # <editor-fold desc="基本设置API">
    def EnablePicCache(self,enable)->int:
        """
        Function:
            设置是否开启或者关闭插件内部的图片缓存机制. (默认是打开).
        parms:
            enable:
                0代表关闭,1代表打开
        return:
            0代表失败,1代表成功
        注意:
            有些时候，系统内存比较吃紧，这时候再打开内部缓存，可能会导致缓存分配在虚拟内存，这样频繁换页，反而导致图色效率下降.这时候就建议关闭图色缓存.
            所有图色缓存机制都是对本对象的，也就是说，调用图色缓存机制的函数仅仅对本对象生效. 每个对象都有一个图色缓存队列.
        """
        return self.obdm.EnablePicCache(enable)

    def GetBasePath(self)->str:
        """
        Function:
            获取注册在系统中的dm.dll的路径.
        parms:

        return:
            返回dm.dll所在路径
        """
        return self.obdm.GetBasePath()

    def GetDmCount(self)->int:
        """
        Function:
            返回当前进程已经创建的dm对象个数.
        parms:

        return:
            返回大漠插件对象的数量
        """
        return self.obdm.GetDmCount()

    def GetID(self)->int:
        """
        Function:
            返回当前大漠对象的ID值，这个值对于每个对象是唯一存在的。可以用来判定两个大漠对象是否一致
        parms:

        return:
            当前对象的ID值.
        """
        return self.obdm.GetID()

    def GetLastError(self)->int:
        """
        (不用理会的接口)获取插件命令的最后错误
        Returns:

        """
        return self.obdm.GetLastError()

    def GetPath(self)->str:
        """
        Function:
            获取全局路径.(可用于调试)
        parms:

        return:
            以字符串的形式返回当前设置的全局路径
        """

        return self.obdm.GetPath()

    def Reg(self,reg_code:str,ver_info:str)->int:
        """
        Function:
            调用此函数来注册，从而使用插件的高级功能.推荐使用此函数.
        parms:
            reg_code:
                注册码.
            ver_info:
                版本附加信息(附加码).
        return:
                0 : 失败 (未知错误)
                1 : 成功
                2 : 余额不足
                3 : 绑定了本机器，但是账户余额不足50元.
                4 : 注册码错误
                5 : 你的机器或者IP在黑名单列表中或者不在白名单列表中.
                6 : 非法使用插件.
                7 : 你的帐号因为非法使用被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac,否则可能会造成封号，或者封禁机器）
                8 : ver_info不在你设置的附加白名单中.
                77： 机器码或者IP因为非法使用，而被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac,否则可能会造成封号，或者封禁机器）
                     封禁是全局的，如果使用了别人的软件导致77，也一样会导致所有注册码均无法注册。解决办法是更换IP，更换MAC.
                -1 : 无法连接网络,(可能防火墙拦截,如果可以正常访问大漠插件网站，那就可以肯定是被防火墙拦截)
                -2 : 进程没有以管理员方式运行. (出现在win7 win8 vista 2008.建议关闭uac)
                -8 : 版本附加信息长度超过了20
                -9 : 版本附加信息里包含了非法字母.
                空 : 这是不可能返回空的，如果出现空，那肯定是当前使用的版本不对,老的插件里没这个函数导致返回为空.最好参考文档中的标准写法,判断插件版本号.
        """
        reg_code = "jv965720b239b8396b1b7df8b768c919e86e10f"
        ver_info = "jv8hjzz6z5u4700"
        return self.obdm.Reg(reg_code,ver_info)

    def RegEx(self,reg_code:str,ver_info:str,ip:str)->int:
        """
        不建议使用
        """
        return self.obdm.RegEx(reg_code,ver_info,ip)

    def RegExNoMac(self,reg_code:str,ver_info:str,ip:str)->int:
        """
        不建议使用
        """
        return self.obdm.RegExNoMac(reg_code,ver_info,ip)

    def RegNoMac(self,reg_code:str,ver_info:str)->int:
        return self.obdm.RegNoMac(reg_code,ver_info)

    def SetDisplayInput(self,mode:str)->int:
        """
        Function:
            设定图色的获取方式，默认是显示器或者后台窗口(具体参考BindWindow)
        parms:
            mode:
                1.     "screen" 这个是默认的模式，表示使用显示器或者后台窗口
                2.     "pic:file" 指定输入模式为指定的图片,如果使用了这个模式，则所有和图色相关的函数
                            均视为对此图片进行处理，比如文字识别查找图片 颜色 等等一切图色函数.
                            需要注意的是，设定以后，此图片就已经加入了缓冲，如果更改了源图片内容，那么需要
                            释放此缓冲，重新设置.
                3.     "mem:addr,size" 指定输入模式为指定的图片,此图片在内存当中. addr为图像内存地址,size为图像内存大小.
                            如果使用了这个模式，则所有和图色相关的函数,均视为对此图片进行处理.
                            比如文字识别 查找图片 颜色 等等一切图色函数.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetDisplayInput(mode)

    def SetEnumWindowDelay(self,delay:int)->int:
        """
        Function:
            设置EnumWindow  EnumWindowByProcess  EnumWindowSuper FindWindow以及FindWindowEx的最长延时. 内部默认超时是10秒.
            注意:有些时候，窗口过多，并且窗口结构过于复杂，可能枚举的时间过长. 那么需要调用这个函数来延长时间。避免漏掉窗口.
        parms:
            delay:
                单位毫秒
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetEnumWindowDelay(delay)

    def SetPath(self,path:str)->int:
        """
        Function:
            设置全局路径,设置了此路径后,所有接口调用中,相关的文件都相对于此路径. 比如图片,字库等.
        parms:
            path:
                路径,可以是相对路径,也可以是绝对路径
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetPath(path)

    def SetShowErrorMsg(self,show:int)->int:
        """
        Function:
            设置是否弹出错误信息,默认是打开.
        parms:
            show:
                0表示不打开,1表示打开
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetShowErrorMsg(show)

    def SpeedNormalGraphic(self,enable:int)->int:
        """
        Function:
            设置是否对前台图色进行加速. (默认是关闭). (对于不绑定，或者绑定图色为normal生效)( 仅对WIN8以上系统有效
        parms:
            enable:
                0代表关闭,1代表打开
        return:
            0代表失败,1代表成功
        注意:
            WIN8以上系统,由于AERO的开启,导致前台图色速度很慢,使用此接口可以显著提速.
            WIN7系统无法使用,只能通过关闭aero来对前台图色提速.
            每个进程,最多只能有一个对象开启此加速接口,如果要用开启别的对象的加速，那么要先关闭之前开启的.
            并且开启此接口后,仅能对主显示器的屏幕进行截图,分屏的显示器上的内容无法截图.
            另外需要注意,开启此接口后，程序CPU会有一定上升，因为这个方法是以牺牲CPU性能来提升速度的.
        """
        return self.obdm.SpeedNormalGraphic(enable)

    def Ver(self)->str:
        """
        Function:
            返回当前插件版本号
        parms:

        return:
            当前插件的版本描述字符串
        """
        return self.obdm.Ver()
    # </editor-fold>

    # <editor-fold desc="图色API">
    def AppendPicAddr(self,pic_info:str,addr:int,size)->str:
        """
        Function:
            对指定的数据地址和长度，组合成新的参数. FindPicMem FindPicMemE 以及FindPicMemEx专用
        parms:
            pic_info:
                老的地址描述串
            addr:
                数据地址
            size:
                数据长度
        return:
            新的地址描述串
        """
        return self.obdm.AppendPicAddr(pic_info,addr,size)

    def BGR2RGB(self,bgr_color:str)->str:
        """
        Function:
            把BGR(按键格式)的颜色格式转换为RGB
        parms:
            bgr_color:
                bgr格式的颜色字符串
        return:
            RGB格式的字符串
        """
        return self.obdm.BGR2RGB(bgr_color)

    def Capture(self,x1:int,y1:int,x2:int,y2:int,file:str)->int:
        """
        Function:
            抓取指定区域(x1, y1, x2, y2)的图像,保存为file(24位位图)
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            file:
                保存的文件名,保存的地方一般为SetPath中设置的目录,当然这里也可以指定全路径名.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.Capture(x1,y1,x2,y2,file)

    def CaptureGif(self,x1:int,y1:int,x2:int,y2:int,file:str,delay:int,time:int)->int:
        """
        Function:
            抓取指定区域(x1, y1, x2, y2)的动画，保存为gif格式
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            file:
                保存的文件名,保存的地方一般为SetPath中设置的目录,当然这里也可以指定全路径名.
            delay:
                动画间隔，单位毫秒。如果为0，表示只截取静态图片
            time:
                总共截取多久的动画，单位毫秒.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.CaptureGif(x1,y1,x2,y2,file,delay,time)

    def CaptureJpg(self,x1:int,y1:int,x2:int,y2:int,file:str,quality:int)->int:
        """
        Function:
            抓取指定区域(x1, y1, x2, y2)的图像,保存为file(JPG压缩格式)
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            file:
                保存的文件名,保存的地方一般为SetPath中设置的目录,当然这里也可以指定全路径名.
            quality:
                jpg压缩比率(1-100) 越大图片质量越好
        return:
            0代表失败,1代表成功
        """
        return self.obdm.CaptureJpg(x1,y1,x2,y2,file,quality)

    def CapturePng(self,x1:int,y1:int,x2:int,y2:int,file:str)->int:
        """
        Function:
            同Capture函数，只是保存的格式为PNG.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            file:
                保存的文件名,保存的地方一般为SetPath中设置的目录,当然这里也可以指定全路径名.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.CapturePng(x1,y1,x2,y2,file)

    def CapturePre(self,file:str)->int:
        """
        Function:
            抓取上次操作的图色区域，保存为file(24位位图)
        parms:
            file:
                保存的文件名,保存的地方一般为SetPath中设置的目录当然这里也可以指定全路径名.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.CapturePre(file)

    def CmpColor(self,x:int,y:int,color:str,sim:float)->int:
        """
        Function:
            比较指定坐标点(x,y)的颜色
        parms:
            x:
                X坐标
            y:
                Y坐标
            color:
                颜色字符串,可以支持偏色,多色,例如 "ffffff-202020|000000-000000" 这个表示白色偏色为202020,和黑色偏色为000000.颜色最多支持10种颜色组合. 注意，这里只支持RGB颜色
            sim:
                sim 双精度浮点数: 相似度(0.1-1.0)
        return:
            0代表颜色匹配
            1代表颜色不匹配
        """
        return self.obdm.CmpColor(x,y,color,sim)

    def EnableDisplayDebug(self,enable_debug:int)->int:
        """
        Function:
            开启图色调试模式，此模式会稍许降低图色和文字识别的速度.默认不开启.
        parms:
            enable_debug:
                0代表关闭,1代表开启
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableDisplayDebug(enable_debug)

    def EnableFindPicMultithread(self,enable:int)->int:
        """
        Function:
            当执行FindPicXXX系列接口时,是否在条件满足下(查找的图片大于等于4,这个值可以根据SetFindPicMultithreadCount来修改),开启多线程查找。 默认打开.
        parms:
            enable:
                0代表关闭,1代表开启
        return:
            0代表失败,1代表成功
        注意:
            如果担心开启多线程会引发占用大量CPU资源,那么可以考虑关闭此功能. 在以往版本,这个功能默认都是打开的.
            这个只是多线程查找的一个开关,另一个开关是SetFindPicMultithreadCount
        """
        return self.obdm.EnableFindPicMultithread(enable)

    def EnableGetColorByCapture(self,enable:int)->int:
        """
        Function:
            允许调用GetColor GetColorBGR GetColorHSV 以及 CmpColor时，以截图的方式来获取颜色。 默认关闭.
            注意:某些窗口上，可能GetColor会获取不到颜色，可以尝试此接口.
        parms:
            enable:
                0代表关闭,1代表开启
        return:
            0代表失败,1代表成功
        """

        return self.obdm.EnableGetColorByCapture(enable)

    def FindColor(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,dir:int)->int:
        """
        Function:
            查找指定区域内的颜色,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反查找指定区域内的颜色,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反
            该函数只会返回第一个找到的颜色
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".
                也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释. 注意，这里只支持RGB颜色
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FindColor(x1,y1,x2,y2,color,sim,dir)

    def FindColorBlock(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,count:int,width:int,height:int)->tuple:
        """
        Function:
            查找指定区域内的颜色块,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反
            该函数只会找到第一个符合条件的结果
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".
                也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释.注意，这里只支持RGB颜色
            sim:
                相似度,取值范围0.1-1.0
            count:
                在宽度为width,高度为height的颜色块中，符合color颜色的最小数量.(注意,这个颜色数量可以在综合工具的二值化区域中看到)
            width:
                颜色块的宽度
            height:
                颜色块的高度
        return:
            返回值是tuple数据类型,总共三个元素
            第一个元素: 0代表没有找到,1代表有找到
            第二个元素: X坐标
            第三个元素: Y坐标
        """
        return self.obdm.FindColorBlock(x1,y1,x2,y2,color,sim,count,width,height)

    def FindColorBlockEx(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,count:int,width:int,height:int)->str:
        """
        Function:
            (不建议使用,会出现比较多的结果)查找指定区域内的颜色块,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".
                也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释.注意，这里只支持RGB颜色
            sim:
                相似度,取值范围0.1-1.0
            count:
                在宽度为width,高度为height的颜色块中，符合color颜色的最小数量.(注意,这个颜色数量可以在综合工具的二值化区域中看到)
            width:
                颜色块的宽度
            height:
                颜色块的高度
        return:
            返回值是str数据类型,
            返回所有颜色块信息的坐标值,然后通过GetResultCount等接口来解析 (由于内存限制,返回的颜色数量最多为1800个左右)
        """
        return self.obdm.FindColorBlock(x1,y1,x2,y2,color,sim,count,width,height)

    def FindColorE(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,dir:int)->str:
        """
        Function:
            查找指定区域内的颜色,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反
            该函数只会返回第一个找到的颜色
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".
                也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释. 注意，这里只支持RGB颜色
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回X和Y坐标 形式如"x|y", 比如"100|200"
        """

        return self.obdm.FindColorE(x1,y1,x2,y2,color,sim,dir)

    def FindColorEx(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,dir:int)->str:
        """
        Function:
            (不建议使用,返回的结果非常的多,太杂乱)查找指定区域内的所有颜色,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".
                也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释. 注意，这里只支持RGB颜色
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回所有颜色信息的坐标值,然后通过GetResultCount等接口来解析 (由于内存限制,返回的颜色数量最多为1800个左右)
        """
        return self.obdm.FindColorEx(x1,y1,x2,y2,color,sim,dir)

    def FindMulColor(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float)->int:
        """
        Function:
            判断指定颜色是否全部在指定区域内
            如果颜色存在就返回1,颜色不存在或者不全就返回0
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".
                也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释. 注意，这里只支持RGB颜色
            sim:
                相似度,取值范围0.1-1.0
        return:
            0:没找到或者部分颜色没找到
            1:所有颜色都找到
        """
        return self.obdm.FindMulColor(x1,y1,x2,y2,color,sim,dir)

    def FindMultiColor(self,x1:int,y1:int,x2:int,y2:int,first_color:str,offset_color:str,sim:float,dir:int):
        """
        不建议使用,也不会使用,可查看文档
        """
        return self.obdm.FindMultiColor(x1,y1,x2,y2,first_color,offset_color,sim,dir)

    def FindMultiColorE(self,x1:int,y1:int,x2:int,y2:int,first_color:str,offset_color:str,sim:float,dir:int):
        """
        不建议使用,也不会使用,可查看文档
        """
        return self.obdm.FindMultiColorE(x1,y1,x2,y2,first_color,offset_color,sim,dir)

    def FindMultiColorEx(self,x1:int,y1:int,x2:int,y2:int,first_color:str,offset_color:str,sim:float,dir:int):
        """
        不建议使用,也不会使用,可查看文档
        """
        return self.obdm.FindMultiColorEx(x1,y1,x2,y2,first_color,offset_color,sim,dir)

    def FindPic(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->tuple:
        """
        Function:
            查找指定区域内的图片,图片必须是bmp格式的,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回值是一个tuple数据类型,总共三个元素
            第一个元素: 代表pic_name中的第几张图片,如果传入的是一张图片地址,那么此处为0
            第二个元素: x坐标(左上角)
            第三个元素: y坐标(左上角)
        """
        return self.obdm.FindPic(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicE(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->str:
        """
        Function:
            查找指定区域内的图片,图片必须是bmp格式的,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index|x|y", 比如"3|100|200"
        """
        return self.obdm.FindPicE(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicEx(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->str:
        """
        Function:
            查找指定区域内的图片,图片必须是bmp格式的,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,并且返回所有找到的图像的坐标.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)
        """
        return self.obdm.FindPicEx(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicExS(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->str:
        """
        Function:
            查找指定区域内的图片,图片必须是bmp格式的,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,并且返回所有找到的图像的坐标.
            此函数同FindPicEx.只是返回值不同.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回的是所有找到的坐标格式如下:"file,x,y| file,x,y..| file,x,y" (图片左上角的坐标)
        """
        return self.obdm.FindPicExS(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicMem(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:float)->tuple:
        """
        Function:
            查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_info:
                图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合.
                地址表示24位位图资源在内存中的首地址，用十进制的数值表示
                长度表示位图资源在内存中的长度，用十进制数值表示.
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回值是tuple数据类型,总共三个元素
            第一个元素: 0或者-1代表失败,1代表成功,
            第二个元素: x坐标
            第三个元素: y坐标
        """
        return self.obdm.FindPicMem(x1,y1,x2,y2,pic_info,delta_color,sim)

    def FindPicMemE(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:float)->str:
        """
        Function:
            查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_info:
                图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合.
                地址表示24位位图资源在内存中的首地址，用十进制的数值表示
                长度表示位图资源在内存中的长度，用十进制数值表示.
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index|x|y", 比如"3|100|200"
        """
        return self.obdm.FindPicMemE(x1,y1,x2,y2,pic_info,delta_color,sim)

    def FindPicMemEx(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:float)->str:
        """
        Function:
            查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 这个函数要求图片是数据地址.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_info:
                图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合.
                地址表示24位位图资源在内存中的首地址，用十进制的数值表示
                长度表示位图资源在内存中的长度，用十进制数值表示.
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
                返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)
                比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)
        """
        return self.obdm.FindPicMemEx(x1,y1,x2,y2,pic_info,delta_color,sim)

    def FindPicS(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->tuple:
        """
        Function:
            查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 此函数同FindPic.只是返回值不同.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                相似度,取值范围0.1-1.0
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回值是一个tuple数据类型,总共三个元素
            第一个元素: 返回图片的名字,如果没有找到,该元素就为空字符串
            第二个元素: x坐标(左上角)
            第三个元素: y坐标(左上角)
        """
        return self.obdm.FindPicS(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSim(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:int,dir:int)->tuple:
        """
        Function:
            (该函数不建议使用,很容易查找不出来结果,因为是根据百分比来查找的,建议95-97的数值)查找指定区域内的图片,图片必须是bmp格式的,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                最小百分比相似率. 表示匹配的颜色占总颜色数的百分比. 其中透明色也算作匹配色. 取值为0到100. 100表示必须完全匹配.
                0表示任意颜色都匹配. 只有大于sim的相似率的才会被匹配
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回值是一个tuple数据类型,总共三个元素
            第一个元素: 返回找到的图片的序号,
            第二个元素: x坐标(左上角)
            第三个元素: y坐标(左上角)
        """
        return self.obdm.FindPicSim(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSimE(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:int,dir:int)->str:
        """
        Function:
            (该函数不建议使用,很容易查找不出来结果,因为是根据百分比来查找的,建议95-97的数值)查找指定区域内的图片,图片必须是bmp格式的,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,只返回第一个找到的X Y坐标.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                最小百分比相似率. 表示匹配的颜色占总颜色数的百分比. 其中透明色也算作匹配色. 取值为0到100. 100表示必须完全匹配.
                0表示任意颜色都匹配. 只有大于sim的相似率的才会被匹配
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index|x|y", 比如"3|100|200"
        """
        return self.obdm.FindPicSimE(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSimEx(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:int,dir:int)->str:
        """
        Function:
            (该函数不建议使用,很容易查找不出来结果,因为是根据百分比来查找的,建议95-97的数值)查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,并且返回所有找到的图像的坐标.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_name:
                图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
            sim:
                最小百分比相似率. 表示匹配的颜色占总颜色数的百分比. 其中透明色也算作匹配色. 取值为0到100. 100表示必须完全匹配.
                0表示任意颜色都匹配. 只有大于sim的相似率的才会被匹配
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回的是所有找到的坐标格式如下:"id,sim,x,y|id,sim,x,y..|id,sim,x,y" (图片左上角的坐标)
        """
        return self.obdm.FindPicSimEx(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSimMem(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:int,dir:int)->tuple:
        """
        Function:
            (该函数不建议使用,很容易查找不出来结果,因为是根据百分比来查找的,建议95-97的数值)查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片, 只返回第一个匹配的X Y坐标. 这个函数要求图片是数据地址.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_info:
                图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合.
                地址表示24位位图资源在内存中的首地址，用十进制的数值表示
                长度表示位图资源在内存中的长度，用十进制数值表示.
            sim:
                最小百分比相似率. 表示匹配的颜色占总颜色数的百分比. 其中透明色也算作匹配色. 取值为0到100. 100表示必须完全匹配.
                0表示任意颜色都匹配. 只有大于sim的相似率的才会被匹配
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回值是tuple数据类型,总共三个元素
            第一个元素: 0或者-1代表失败,1代表成功,
            第二个元素: x坐标
            第三个元素: y坐标
        """
        return self.obdm.FindPicSimMem(x1,y1,x2,y2,pic_info,delta_color,sim,dir)

    def FindPicSimMemE(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:int,dir:int)->str:
        """
        Function:
            (该函数不建议使用,很容易查找不出来结果,因为是根据百分比来查找的,建议95-97的数值)查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片, 只返回第一个匹配的X Y坐标. 这个函数要求图片是数据地址.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_info:
                图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合.
                地址表示24位位图资源在内存中的首地址，用十进制的数值表示
                长度表示位图资源在内存中的长度，用十进制数值表示.
            sim:
                最小百分比相似率. 表示匹配的颜色占总颜色数的百分比. 其中透明色也算作匹配色. 取值为0到100. 100表示必须完全匹配.
                0表示任意颜色都匹配. 只有大于sim的相似率的才会被匹配
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index|x|y", 比如"3|100|200"
        """
        return self.obdm.FindPicSimMemE(x1,y1,x2,y2,pic_info,delta_color,sim,dir)

    def FindPicSimMemEx(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:int,dir:int)->str:
        """
        Function:
            (该函数不建议使用,很容易查找不出来结果,因为是根据百分比来查找的,建议95-97的数值)查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.
            这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 这个函数要求图片是数据地址.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            pic_info:
                图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合.
                地址表示24位位图资源在内存中的首地址，用十进制的数值表示
                长度表示位图资源在内存中的长度，用十进制数值表示.
            sim:
                最小百分比相似率. 表示匹配的颜色占总颜色数的百分比. 其中透明色也算作匹配色. 取值为0到100. 100表示必须完全匹配.
                0表示任意颜色都匹配. 只有大于sim的相似率的才会被匹配
            dir:
                0: 从左到右,从上到下
                1: 从左到右,从下到上
                2: 从右到左,从上到下
                3: 从右到左,从下到上
                4：从中心往外查找
                5: 从上到下,从左到右
                6: 从上到下,从右到左
                7: 从下到上,从左到右
                8: 从下到上,从右到左
        return:
            返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index|x|y", 比如"3|100|200"
        """
        return self.obdm.FindPicSimMemEx(x1,y1,x2,y2,pic_info,delta_color,sim,dir)

    def FindShape(self,x1:int,y1:int,x2:int,y2:int,offset_color:str,sim:float,dir:int)->tuple:
        """
        API接口过于复杂,不建议使用
        """
        return self.obdm.FindShape(x1,y1,x2,y2,offset_color,sim,dir)
    def FindShapeE(self,x1:int,y1:int,x2:int,y2:int,offset_color:str,sim:float,dir:int)->str:
        """
        API接口过于复杂,不建议使用
        """
        return self.obdm.FindShapeE(x1,y1,x2,y2,offset_color,sim,dir)
    def FindShapeEx(self,x1:int,y1:int,x2:int,y2:int,offset_color:str,sim:float,dir:int)->str:
        """
        API接口过于复杂,不建议使用
        """
        return self.obdm.FindShapeEx(x1,y1,x2,y2,offset_color,sim,dir)

    def FreePic(self,pic_name:str)->int:
        """
        Function:
            释放指定的图片,此函数不必要调用,除非你想节省内存.
        parms:
            pic_name:
                文件名比如"1.bmp|2.bmp|3.bmp" 等,可以使用通配符,比如
                "*.bmp" 这个对应了所有的bmp文件
                "a?c*.bmp" 这个代表了所有第一个字母是a 第三个字母是c 第二个字母任意的所有bmp文件
                "abc???.bmp|1.bmp|aa??.bmp" 可以这样任意组合.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FreePic(pic_name)

    def GetAveHSV(self,x1:int,y1:int,x2:int,y2:int)->str:
        """
        Function:
            获取范围(x1,y1,x2,y2)颜色的均值,返回格式"H.S.V"
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
        return:
            颜色字符串
        """
        return self.obdm.GetAveHSV(x1,y1,x2,y2)

    def GetAveRGB(self,x1:int,y1:int,x2:int,y2:int)->str:
        """
        Function:
            获取范围(x1,y1,x2,y2)颜色的均值,返回格式"RRGGBB"
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
        return:
            颜色字符串
        """
        return self.obdm.GetAveRGB(x1,y1,x2,y2)

    def GetColor(self,x:int,y:int)->str:
        """
        Function:
            获取(x,y)的颜色,颜色返回格式"RRGGBB",注意,和按键的颜色格式相反
        parms:
            x:
                X坐标
            y:
                Y坐标
        return:
            颜色字符串(注意这里都是小写字符，和工具相匹配)
        """
        return self.obdm.GetColor(x,y)

    def GetColorBGR(self,x:int,y:int)->str:
        """
        Function:
            获取(x,y)的颜色,颜色返回格式"BBGGRR"
        parms:
            x:
                X坐标
            y:
                Y坐标
        return:
            颜色字符串(注意这里都是小写字符，和工具相匹配)
        """
        return self.obdm.GetColorBGR(x,y)

    def GetColorHSV(self,x:int,y:int)->str:
        """
        Function:
            获取(x,y)的HSV颜色,颜色返回格式"H.S.V"
        parms:
            x:
                X坐标
            y:
                Y坐标
        return:
            颜色字符串
        """
        return self.obdm.GetColorBGR(x,y)

    def GetColorNum(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float)->int:
        """
        Function:
            获取指定区域的颜色数量,颜色格式"RRGGBB-DRDGDB",注意,和按键的颜色格式相反
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            color:
                格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020".
            sim:
                相似度,取值范围0.1-1.0
        return:
            颜色数量
        """
        return self.obdm.GetColorBGR(x1,y1,x2,y2,color,sim)

    def GetPicSize(self,pic_name:str)->str:
        """
        Function:
            获取指定图片的尺寸，如果指定的图片已经被加入缓存，则从缓存中获取信息.
            此接口也会把此图片加入缓存.
        parms:
            pic_name:
                文件名 比如"1.bmp"
        return:
            形式如 "w,h" 比如"30,20"
        """
        return self.obdm.GetPicSize(pic_name)

    def GetScreenData(self,x1:int,y1:int,x2:int,y2:int)->tuple:
        """
        Function:
            获取指定区域的图像,用二进制数据的方式返回,（不适合按键使用）方便二次开发.
        parms:
            .

        return:
            返回的是指定区域的二进制颜色数据地址,每个颜色是4个字节,表示方式为(00RRGGBB)
        """
        return self.obdm.GetScreenData(x1,y1,x2,y2)

    def GetScreenDataBmp(self,x1:int,y1:int,x2:int,y2:int)->tuple:
        """
        Function:
            获取指定区域的图像,用二进制数据的方式返回,（不适合按键使用）方便二次开发.
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
        return:
            返回值是一个tuple数据类型,总共三个元素
            第一个元素: 0代表失败,1代表成功
            第二个元素: 数据的指针地址
            第三个元素: 图片的数据长度
        """
        return self.obdm.GetScreenData(x1,y1,x2,y2)

    def ImageToBmp(self,pic_name:str,bmp_name:str)->int:
        """
        Function:
            转换图片格式为24位BMP格式.
        parms:
            pic_name:
                要转换的图片名
            bmp_name:
                要保存的BMP图片名
        return:
            0代表失败,1代表成功
        """
        return self.obdm.ImageToBmp(pic_name,bmp_name)

    def IsDisplayDead(self,x1:int,y1:int,x2:int,y2:int,t:int)->int:
        """
        Function:
            判断指定的区域，在指定的时间内(秒),图像数据是否一直不变.(卡屏). (或者绑定的窗口不存在也返回1)
        parms:
            x1:
                区域的左上X坐标
            y1:
                区域的左上Y坐标
            x2:
                区域的右下X坐标
            y2:
                区域的右下Y坐标
            t:
                需要等待的时间,单位是秒
        return:
                0 : 没有卡屏，图像数据在变化.
                1 : 卡屏. 图像数据在指定的时间内一直没有变化. 或者绑定的窗口不见了.
        """
        return self.obdm.IsDisplayDead(x1,y1,x2,y2,t)

    def LoadPic(self,pic_name:str)->int:
        """
        Function:
            预先加载指定的图片,这样在操作任何和图片相关的函数时,将省去了加载图片的时间。调用此函数后,没必要一定要调用FreePic,插件自己会自动释放.
            另外,此函数不是必须调用的,所有和图形相关的函数只要调用过一次，图片会自动加入缓存.
            如果想对一个已经加入缓存的图片进行修改，那么必须先用FreePic释放此图片在缓存中占用的内存，然后重新调用图片相关接口，就可以重新加载此图片.
        parms:
            pic_name:
                文件名比如"1.bmp|2.bmp|3.bmp" 等,可以使用通配符,比如
                "*.bmp" 这个对应了所有的bmp文件
                "a?c*.bmp" 这个代表了所有第一个字母是a 第三个字母是c 第二个字母任意的所有bmp文件
                "abc???.bmp|1.bmp|aa??.bmp" 可以这样任意组合.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.LoadPic(pic_name)

    def LoadPicByte(self,addr:int,size:int,pic_name:str)->int:
        """
        Function:
            预先加载指定的图片,这样在操作任何和图片相关的函数时,将省去了加载图片的时间。调用此函数后,没必要一定要调用FreePic,插件自己会自动释放.
            另外,此函数不是必须调用的,所有和图形相关的函数只要调用过一次，图片会自动加入缓存.
            如果想对一个已经加入缓存的图片进行修改，那么必须先用FreePic释放此图片在缓存中占用
            的内存，然后重新调用图片相关接口，就可以重新加载此图片. （当图色缓存机制打开时,具体参考EnablePicCache）
            此函数同LoadPic，只不过LoadPic是从文件中加载图片,而LoadPicByte从给定的内存中加载.
        parms:
            addr:
                BMP图像首地址.(完整的BMP图像，不是经过解析的. 和BMP文件里的内容一致)
            size:
                BMP图像大小.(和BMP文件大小一致)
            pic_name:
                文件名,指定这个地址对应的图片名. 用于找图时使用.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.LoadPicByte(addr,size,pic_name)

    def MatchPicName(self,pic_name:str)->str:
        """
        Function:
            根据通配符获取文件集合. 方便用于FindPic和FindPicEx
        parms:
            pic_name:
                文件名比如"1.bmp|2.bmp|3.bmp" 等,可以使用通配符,比如
                "*.bmp" 这个对应了所有的bmp文件
                "a?c*.bmp" 这个代表了所有第一个字母是a 第三个字母是c 第二个字母任意的所有bmp文件
                "abc???.bmp|1.bmp|aa??.bmp" 可以这样任意组合.
        return:
            返回的是通配符对应的文件集合，每个图片以|分割
        """
        return self.obdm.MatchPicName(pic_name)

    def RGB2BGR(self,rgb_color:str)->str:
        """
        Function:
            把RGB的颜色格式转换为BGR(按键格式)
        parms:
            rgb_color:
                rgb格式的颜色字符串
        return:
            BGR格式的字符串
        """
        return self.obdm.rgb_color(rgb_color)

    def SetExcludeRegion(self,mode:int,info:str)->int:
        """
        Function:
            设置图色,以及文字识别时,需要排除的区域.(支持所有图色接口,以及文字相关接口,但对单点取色,或者单点颜色比较的接口不支持)
        parms:
            mode:
                0: 添加排除区域
                1: 设置排除区域的颜色,默认颜色是FF00FF(此接口的原理是把排除区域设置成此颜色,这样就可以让这块区域实效)
                2: 请空排除区域
            info:
                根据mode的取值来决定
                当mode为0时,此参数指添加的区域,可以多个区域,用"|"相连. 格式为"x1,y1,x2,y2|....."
                当mode为1时,此参数为排除区域的颜色,"RRGGBB"
                当mode为2时,此参数无效
        return:
            0代表失败,1代表成功
        """

        return self.obdm.SetExcludeRegion(mode,info)

    def SetFindPicMultithreadCount(self,count:int)->int:
        """
        Function:
            当执行FindPicXXX系列接口时,当图片个数少于count时,使用单线程查找,否则使用多线程。 这个count默认是4.
        parms:
            count:
                图片数量. 最小不能小于2. 因为1个图片必定是单线程. 这个值默认是4.如果你不更改的话.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetFindPicMultithreadCount(count)

    def SetPicPwd(self,pwd:str)->int:
        """
        Function:
            设置图片密码，如果图片本身没有加密，那么此设置不影响不加密的图片，一样正常使用.
        parms:
            pwd:
                图片密码
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetPicPwd(pwd)
    # </editor-fold>

    # <editor-fold desc="文件API">
    def CopyFile(self,src_file:str,dst_file:str,over:int)->int:
        """
        Function:
            拷贝文件.
        parms:
            src_file:
                原始文件名
            dst_file:
                目标文件名
            over:
                取值范围如下
                0 : 如果dst_file文件存在则不覆盖返回.
                1 : 如果dst_file文件存在则覆盖.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.CopyFile(src_file,dst_file,over)

    def CreateFolder(self,folder:str)->int:
        """
        Function:
            创建指定目录.
            可以创建多级目录
            示例 : dm.CreateFolder "c:\123\456\789"
        parms:
            folder:
                目录名
        return:
            0代表失败,1代表成功
        """
        return self.obdm.CreateFolder(folder)

    def DecodeFile(self,file:str,pwd:str)->int:
        """
        Function:
            解密指定的文件.
        parms:
            file:
                文件名.
            pwd:
                密码.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.DecodeFile(file,pwd)

    def DeleteFile(self,file:str)->int:
        """
        Function:
            删除文件.
        parms:
            file:
                文件名
        return:
            0代表失败,1代表成功
        """
        return self.obdm.DeleteFile(file)

    def DeleteFolder(self,folder:str)->int:
        """
        Function:
            删除指定目录
        parms:
            folder:
                目录名
        return:
            0代表失败,1代表成功
        """
        return self.obdm.DeleteFolder(folder)

    def DeleteIni(self,section:str,key:str,file:str)->int:
        """
        Function:
            删除指定的ini小节.
        parms:
            section:
                小节名
            key:
                变量名. 如果这个变量为空串，则删除整个section小节.
            file:
                ini文件名.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.DeleteIni(section,key,file)

    def DeleteIniPwd(self,section:str,key:str,file:str,pwd:str)->int:
        """
        Function:
            删除指定的ini小节.
        parms:
            section:
                小节名
            key:
                变量名. 如果这个变量为空串，则删除整个section小节.
            file:
                ini文件名.
            pwd:
                密码
        return:
            0代表失败,1代表成功
        """
        return self.obdm.DeleteIniPwd(section,key,file,pwd)

    def DownloadFile(self,url:str,save_file:str,timeout:int)->int:
        """
        Function:
            从internet上下载一个文件.
        parms:
            url:
                下载的url地址.
            save_file:
                要保存的文件名.
            timeout:
                连接超时时间，单位是毫秒.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.DownloadFile(url,save_file,timeout)

    def EncodeFile(self,file:str,pwd:str)->int:
        """
        Function:
            加密指定的文件.
        parms:
            file:
                文件名.
            pwd:
                密码
        return:
            0代表失败,1代表成功
        """
        return self.obdm.EncodeFile(file,pwd)

    def EnumIniKey(self,section:str,file:str)->str:
        """
        Function:
            根据指定的ini文件以及section,枚举此section中所有的key名
        parms:
            section:
                小节名. (不可为空)
            file:
                ini文件名.
        return:
            每个key用"|"来连接，如果没有key，则返回空字符串. 比如"aaa|bbb|ccc"
        """
        return self.obdm.EnumIniKey(section,file)

    def EnumIniKeyPwd(self,section:str,file:str,pwd:str)->str:
        """
        Function:
            根据指定的ini文件以及section,枚举此section中所有的key名.可支持加密文件
        parms:
            section:
                小节名. (不可为空)
            file:
                ini文件名.
            pwd:
                密码
        return:
            每个key用"|"来连接，如果没有key，则返回空字符串. 比如"aaa|bbb|ccc"
        """
        return self.obdm.EnumIniKeyPwd(section,file,pwd)

    def EnumIniSection(self,file:str)->str:
        """
        Function:
            根据指定的ini文件,枚举此ini中所有的Section(小节名)
        parms:
            file:
                ini文件名.
        return:
            每个小节名用"|"来连接，如果没有小节，则返回空字符串. 比如"aaa|bbb|ccc"
        """
        return self.obdm.EnumIniSection(file)

    def EnumIniSectionPwd(self,file:str,pwd:str)->str:
        """
        Function:
            根据指定的ini文件,枚举此ini中所有的Section(小节名) 可支持加密文件
        parms:
            file:
                ini文件名.
            pwd:
                密码
        return:
            每个小节名用"|"来连接，如果没有小节，则返回空字符串. 比如"aaa|bbb|ccc"
        """
        return self.obdm.EnumIniSectionPwd(file,pwd)

    def GetFileLength(self,file:str)->int:
        """
        Function:
            获取指定的文件长度.
        parms:
            file:
                文件名
        return:
            0代表失败,1代表成功
        """
        return self.obdm.GetFileLength(file)

    def GetRealPath(self,path:str)->str:
        """
        Function:
            获取指定文件或目录的真实路径
        parms:
            path:
                路径名,可以是文件路径，也可以是目录. 这里必须是全路径
        return:
            真实路径,如果失败,返回空字符串
        """
        return self.obdm.GetRealPath(path)

    def IsFileExist(self,file:str)->int:
        """
        Function:
            判断指定文件是否存在.
        parms:
            file:
                文件名
        return:
            0代表不存在,1代表存在
        """
        return self.obdm.IsFileExist(file)

    def IsFolderExist(self,folder:str)->int:
        """
        Function:
            判断指定目录是否存在.
        parms:
            folder:
                目录名
        return:
            0代表不存在,1代表存在
        """
        return self.obdm.IsFolderExist(folder)

    def MoveFile(self,src_file:str,dst_file:str)->int:
        """
        Function:
            移动文件.
        parms:
            src_file:
                原始文件名
            dst_file:
                目标文件名.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.MoveFile(src_file,dst_file)

    def ReadFile(self,file:str)->str:
        """
        Function:
            从指定的文件读取内容.
        parms:
            file:
                文件
        return:
            读入的文件内容
        """
        return self.obdm.ReadFile(file)

    def ReadIni(self,section:str,key:str,file:str)->str:
        """
        Function:
            从Ini中读取指定信息.
        parms:
            section:
                小节名
            key:
                变量名
            file:
                ini文件名
        return:
            字符串形式表达的读取到的内容
        """
        return self.obdm.ReadIni(section,key,file)

    def ReadIniPwd(self,section:str,key:str,file:str,pwd:str)->str:
        """
        Function:
            从Ini中读取指定信息.可支持加密文件
        parms:
            section:
                小节名
            key:
                变量名.
            file:
                ini文件名.
            pwd:
                密码
        return:
            字符串形式表达的读取到的内容
        """
        return self.obdm.ReadIniPwd(section,key,file,pwd)

    def SelectDirectory(self)->str:
        """
        Function:
            弹出选择文件夹对话框，并返回选择的文件夹.
        parms:

        return:
            选择的文件夹全路径
        """
        return self.obdm.SelectDirectory()

    def SelectFile(self)->str:
        """
        Function:
            弹出选择文件对话框，并返回选择的文件.
        parms:

        return:
            选择的文件全路径
        """
        return self.obdm.SelectFile()

    def WriteFile(self,file:str,content:str)->int:
        """
        Function:
            向指定文件追加字符串.
        parms:
            file:
                文件名
            content:
                写入的字符串
        return:
            0代表失败,1代表成功
        """
        return self.obdm.WriteFile(file,content)

    def WriteIni(self,section:str,key:str,value:str,file:str)->int:
        """
        Function:
            向指定的Ini写入信息.
        parms:
            section:
                小节名
            key:
                变量名
            value:
                变量内容
            file:
                ini文件名
        return:
            0代表失败,1代表成功
        """

        return self.obdm.WriteIni(section,key,value,file)

    def WriteIniPwd(self,section:str,key:str,value:str,file:str,pwd:str)->int:
        """
        Function:
            向指定的Ini写入信息.支持加密文件
        parms:
            section:
                小节名
            key:
                变量名
            value:
                变量内容
            file:
                ini文件名
            pwd:
                密码
        return:
            0代表失败,1代表成功
        """

        return self.obdm.WriteIniPwd(section,key,value,file,pwd)
    # </editor-fold>

    # <editor-fold desc="系统API">
    def Beep(self,f:int,duration:int)->int:
        """
        Function:
            蜂鸣器.
        parms:
            f:
                频率
            duration:
                时长
        return:
            0代表失败,1代表成功
        """
        return self.obdm.Beep(f,duration)

    def CheckFontSmooth(self)->int:
        """
        Function:
            检测当前系统是否有开启屏幕字体平滑.
        parms:

        return:
            0 : 系统没开启平滑字体.
            1 : 系统有开启平滑字体.
        """
        return self.obdm.CheckFontSmooth()

    def CheckUAC(self)->int:
        """
        Function:
            检测当前系统是否有开启UAC(用户账户控制).
        parms:

        return:
            0 : 没开启UAC
            1 : 开启了UAC
        """
        return self.obdm.CheckUAC()

    def Delay(self,mis:int)->int:
        """
        Function:
            延时指定的毫秒,过程中不阻塞UI操作. 一般高级语言使用.按键用不到.
            注意:由于是com组件,调用此函数必须保证调用线程的模型为MTA.否则此函数可能会失效.
        parms:
            mis:
                毫秒数. 必须大于0.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.Delay(mis)

    def Delays(self,mis_min:int,mis_max:int)->int:
        """
        Function:
            延时指定范围内随机毫秒,过程中不阻塞UI操作. 一般高级语言使用.按键用不到.
            注意:由于是com组件,调用此函数必须保证调用线程的模型为MTA.否则此函数可能会失效.
        parms:
            mis_min:
                最小毫秒数. 必须大于0
            mis_max:
                最大毫秒数. 必须大于0
        return:
            0代表失败,1代表成功
        """
        return self.obdm.Delays(mis_min,mis_max)

    def DisableCloseDisplayAndSleep(self)->int:
        """
        Function:
            设置当前的电源设置，禁止关闭显示器，禁止关闭硬盘，禁止睡眠，禁止待机. 不支持XP.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.DisableCloseDisplayAndSleep()

    def DisableFontSmooth(self)->int:
        """
        Function:
            关闭当前系统屏幕字体平滑.同时关闭系统的ClearType功能.
            注意:关闭之后要让系统生效，必须重启系统才有效.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.DisableFontSmooth()

    def DisablePowerSave(self)->int:
        """
        Function:
            关闭电源管理，不会进入睡眠.
            注意:此函数调用以后，并不会更改系统电源设置. 此函数经常用在后台操作过程中. 避免被系统干扰.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.DisablePowerSave()

    def DisableScreenSave(self)->int:
        """
        Function:
            关闭屏幕保护.
            注意:调用此函数后，可能在系统中还是看到屏保是开启状态。但实际上屏保已经失效了.系统重启后，会失效。必须再重新调用一次.
                此函数经常用在后台操作过程中. 避免被系统干扰.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.DisableScreenSave()

    def EnableFontSmooth(self)->int:
        """
        Function:
            开启当前系统屏幕字体平滑.同时开启系统的ClearType功能.
            注意:开启之后要让系统生效，必须重启系统才有效.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.EnableFontSmooth()

    def ExitOs(self,type:int)->int:
        """
        Function:
            退出系统(注销 重启 关机)
        parms:
            type:
                0 : 注销系统
                1 : 关机
                2 : 重新启动
        return:
            0代表失败,1代表成功
        """
        return self.obdm.ExitOs(type)

    def GetClipboard(self)->str:
        """
        Function:
            获取剪贴板的内容
        parms:

        return:
            以字符串表示的剪贴板内容
        """
        return self.obdm.GetClipboard()

    def GetCpuType(self)->str:
        """
        Function:
            获取当前CPU类型(intel或者amd).
        parms:

        return:
            0 : 未知
            1 : Intel cpu
            2 : AMD cpu
        """
        return self.obdm.GetCpuType()

    def GetCpuUsage(self)->str:
        """
        Function:
            获取当前CPU的使用率. 用百分比返回.
        parms:

        return:
            0-100表示的百分比
        """
        return self.obdm.GetCpuUsage()

    def GetDir(self,type:int)->str:
        """
        Function:
            得到系统的路径
        parms:
            type:
                 0 : 获取当前路径
                 1 : 获取系统路径(system32路径)
                 2 : 获取windows路径(windows所在路径)
                 3 : 获取临时目录路径(temp)
                 4 : 获取当前进程(exe)所在的路径
        return:
            返回路径
        """
        return self.obdm.GetDir(type)

    def GetDiskModel(self,index:int)->str:
        """
        Function:
            获取本机的指定硬盘的厂商信息.
        parms:
            index:
                硬盘序号. 表示是第几块硬盘. 从0开始编号,最小为0,最大为5,也就是最多支持6块硬盘的厂商信息获取.
        return:
            字符串表达的硬盘厂商信息
        """
        return self.obdm.GetDiskModel(index)

    def GetDiskReversion(self,index:int)->str:
        """
        Function:
            获取本机的指定硬盘的修正版本信息.
        parms:
            index:
                硬盘序号. 表示是第几块硬盘. 从0开始编号,最小为0,最大为5,也就是最多支持6块硬盘的修正版本信息获取.
        return:
            字符串表达的修正版本信息
        """
        return self.obdm.GetDiskReversion(index)

    def GetDiskSerial(self,index:int)->str:
        """
        Function:
            获取本机的指定硬盘的序列号.
        parms:
            index:
                硬盘序号. 表示是第几块硬盘. 从0开始编号,最小为0,最大为5,也就是最多支持6块硬盘的序列号获取.
        return:
            字符串表达的硬盘序列号
        """
        return self.obdm.GetDiskSerial(index)

    def GetDisplayInfo(self)->str:
        """
        Function:
            获取本机的显卡信息.
        parms:

        return:
            字符串表达的显卡描述信息. 如果有多个显卡,用"|"连接
        """
        return self.obdm.GetDisplayInfo()

    def GetDPI(self)->int:
        """
        Function:
            判断当前系统的DPI(文字缩放)是不是100%缩放
        parms:

        return:
            0代表不是,1代表是
        """
        return self.obdm.GetDPI()

    def GetLocale(self)->int:
        """
        Function:
            判断当前系统使用的非UNICODE字符集是否是GB2312(简体中文)
            (由于设计插件时偷懒了,使用的是非UNICODE字符集，导致插件必须运行在GB2312字符集环境下).
        parms:

        return:
            0 : 不是GB2312(简体中文)
            1 : 是GB2312(简体中文)
        """
        return self.obdm.GetLocale()

    def GetMachineCode(self)->str:
        """
        Function:
            获取本机的机器码.(带网卡). 此机器码用于插件网站后台. 要求调用进程必须有管理员权限. 否则返回空串
            注意:此机器码包含的硬件设备有硬盘,显卡,网卡等. 其它不便透露. 重装系统不会改变此值.
                另要注意,插拔任何USB设备,(U盘，U盾,USB移动硬盘,USB键鼠等),以及安装任何网卡驱动程序,(开启或者关闭无线网卡等)都会导致机器码改变.
        parms:

        return:
            字符串表达的机器机器码
        """
        return self.obdm.GetMachineCode()

    def GetMachineCodeNoMac(self)->str:
        """
        Function:
            获取本机的机器码.(不带网卡) 要求调用进程必须有管理员权限. 否则返回空串.
            注意:此机器码包含的硬件设备有硬盘,显卡,等. 其它不便透露. 重装系统不会改变此值.
                另要注意,插拔任何USB设备,(U盘，U盾,USB移动硬盘,USB键鼠等),都会导致机器码改变.
        parms:

        return:
            字符串表达的机器机器码
        """
        return self.obdm.GetMachineCodeNoMac()

    def GetMemoryUsage(self)->int:
        """
        Function:
            获取当前内存的使用率. 用百分比返回.
        parms:

        return:
            0-100表示的百分比
        """
        return self.obdm.GetMemoryUsage()

    def GetNetTime(self)->str:
        """
        Function:
            从网络获取当前北京时间.
        parms:

        return:
            时间格式. 和now返回一致. 比如"2001-11-01 23:14:08"
        """
        return self.obdm.GetNetTime()

    def GetNetTimeByIp(self,ip:str)->str:
        """
        Function:
            根据指定时间服务器IP,从网络获取当前北京时间.
        parms:
            参数列表:
            参数列表:
        return:
            0代表失败,1代表成功
        """
        return self.obdm.GetNetTimeByIp(ip)

    def GetNetTimeSafe(self)->str:
        """
        Function:
            服务器压力太大,此函数不再支持。 请使用GetNetTimeByIp
        parms:

        return:
            时间格式. 和now返回一致. 比如"2001-11-01 23:14:08"
        """
        return self.obdm.GetNetTimeSafe()

    def GetOsBuildNumber(self)->int:
        """
        Function:
            得到操作系统的build版本号.  比如win10 16299,那么返回的就是16299. 其他类似
        parms:

        return:
            build 版本号,失败返回0
        """
        return self.obdm.GetOsBuildNumber()

    def GetOsType(self)->int:
        """
        Function:
            得到操作系统的类型
        parms:

        return:
            0 : win95/98/me/nt4.0
            1 : xp/2000
            2 : 2003/2003 R2/xp-64
            3 : win7/2008 R2
            4 : vista/2008
            5 : win8/2012
            6 : win8.1/2012 R2
            7 : win10/2016 TP
        """
        return self.obdm.GetOsType()

    def GetScreenDepth(self)->int:
        """
        Function:
            获取屏幕的色深.
        parms:

        return:
            返回系统颜色深度.(16或者32等)
        """
        return self.obdm.GetScreenDepth()

    def GetScreenHeight(self)->int:
        """
        Function:
            获取屏幕的高度.
        parms:

        return:
            返回屏幕的高度
        """
        return self.obdm.GetScreenHeight()

    def GetScreenWidth(self)->int:
        """
        Function:
            获取屏幕的宽度.
        parms:

        return:
            返回屏幕的宽度
        """
        return self.obdm.GetScreenWidth()

    def GetSystemInfo(self,type:str,method:str)->str:
        """
        Function:
            获取指定的系统信息.
        parms:
            type:
                取值范围如下
                 "cpuid" : 表示获取cpu序列号. method可取0和1
                 "disk_volume_serial id" : 表示获取分区序列号. id表示分区序号. 0表示C盘.1表示D盘.以此类推. 最高取到5. 也就是6个分区. method可取0
                 "bios_vendor" : 表示获取bios厂商信息. method可取0和1
                 "bios_version" : 表示获取bios版本信息. method可取0和1
                 "bios_release_date" : 表示获取bios发布日期. method可取0和1
                 "bios_oem" : 表示获取bios里的oem信息. method可取0
                 "board_vendor" : 表示获取主板制造厂商信息. method可取0和1
                 "board_product" : 表示获取主板产品信息. method可取0和1
                 "board_version" : 表示获取主板版本信息. method可取0和1
                 "board_serial" : 表示获取主板序列号. method可取0
                 "board_location" : 表示获取主板位置信息. method可取0
                 "system_manufacturer" : 表示获取系统制造商信息. method可取0和1
                 "system_product" : 表示获取系统产品信息. method可取0和1
                 "system_serial" : 表示获取bios序列号. method可取0
                 "system_uuid" : 表示获取bios uuid. method可取0
                 "system_version" : 表示获取系统版本信息. method可取0和1
                 "system_sku" : 表示获取系统sku序列号. method可取0和1
                 "system_family" : 表示获取系统家族信息. method可取0和1
                 "product_id" : 表示获取系统产品id. method可取0
                 "system_identifier" : 表示获取系统标识. method可取0
                 "system_bios_version" : 表示获取系统BIOS版本号. method可取0. 多个结果用"|"连接.
                 "system_bios_date" : 表示获取系统BIOS日期. method可取0
            method:
                获取方法. 一般从0开始取值.
        return:
            字符串表达的系统信息.
        """
        return self.obdm.GetSystemInfo(type,method)

    def GetTime(self)->int:
        """
        Function:
            获取当前系统从开机到现在所经历过的时间，单位是毫秒
        parms:

        return:
            时间(单位毫秒)
        """
        return self.obdm.GetTime()

    def Is64Bit(self)->int:
        """
        Function:
            判断当前系统是否是64位操作系统
        parms:

        return:
            0 : 不是64位系统
            1 : 是64位系统
        """
        return self.obdm.Is64Bit()

    def IsSurrpotVt(self)->int:
        """
        Function:
            判断当前CPU是否支持vt,并且是否在bios中开启了vt. 仅支持intel的CPU.
        parms:

        return:
            0 : 当前cpu不是intel的cpu,或者当前cpu不支持vt,或者bios中没打开vt.
            1 : 支持
        """
        return self.obdm.IsSurrpotVt

    def Play(self,media_file:str)->int:
        """
        Function:
            播放指定的MP3或者wav文件.
        parms:
            media_file:
                指定的音乐文件，可以采用文件名或者绝对路径的形式.

        return:
            0 : 失败
            非0表示当前播放的ID。可以用Stop来控制播放结束.
        """
        return self.obdm.Play(media_file)

    def RunApp(self,app_path:str,mode:int)->int:
        """
        Function:
            运行指定的应用程序.
        parms:
            app_path:
                指定的可执行程序全路径.
            mode:
                0:普通模式 1:加强模式

        return:
            0代表失败,1代表成功
        """
        return self.obdm.RunApp(app_path,mode)

    def SetClipboard(self,value:str)->int:
        """
        Function:
            设置剪贴板的内容
        parms:
            value:
                以字符串表示的剪贴板内容
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetClipboard(value)

    def SetDisplayAcceler(self,level:int)->int:
        """
        Function:
            设置当前系统的硬件加速级别.
        parms:
            level:
                取值范围为0-5.  0表示关闭硬件加速。5表示完全打开硬件加速.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetDisplayAcceler(level)

    def SetLocale(self)->int:
        """
        Function:
            设置当前系统的非UNICOD字符集. 会弹出一个字符集选择列表,用户自己选择到简体中文即可.
        parms:

        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetLocale()

    def SetScreen(self,width:int,height:int,depth:int)->int:
        """
        Function:
            设置系统的分辨率 系统色深
        parms:
            width:
                屏幕宽度
            height:
                屏幕高度
            depth:
                系统色深
        return:
            0代表失败,1代表成功
        """
        return self.obdm.SetScreen(width,height,depth)

    def SetUAC(self,enable:int)->int:
        """
        Function:
            设置当前系统的UAC(用户账户控制).
        parms:
            enable:
                0 : 关闭UAC
                1 : 开启UAC
        return:
            0代表操作失败,1代表操作成功
        """
        return self.obdm.SetUAC(enable)

    def ShowTaskBarIcon(self,hwnd:int,is_show:int)->int:
        """
        Function:
            显示或者隐藏指定窗口在任务栏的图标.
        parms:
            hwnd:
                指定的窗口句柄
            is_show:
                0为隐藏,1为显示
        return:
            0代表失败,1代表成功
        """
        return self.obdm.ShowTaskBarIcon(hwnd,is_show)

    def Stop(self,id:int)->int:
        """
        Function:
            停止指定的音乐.
        parms:
            id:
                Play返回的播放id.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.Stop(id)
    # </editor-fold>

    # <editor-fold desc="FoobarAPI">
    def CreateFoobarCustom(self,hwnd:int,x:int,y:int,pic_name:str,trans_color:str,sim:float)->int:
        """
        Function:
            根据指定的位图创建一个自定义形状的窗口
            该API函数需要绑定窗口后才可以使用
        parms:
            hwnd:
                指定的窗口句柄,如果此值为0,那么就在桌面创建此窗口
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            pic_name:
                位图名字
            trans_color:
                透明色(RRGGBB)
            sim:
                透明色的相似值 0.1-1.0
        return:
            创建成功的窗口句柄
        """
        return self.obdm.CreateFoobarCustom(hwnd,x,y,pic_name,trans_color,sim)

    def CreateFoobarEllipse(self,hwnd:int,x:int,y:int,w:int,h:int)->int:
        """
        Function:
            创建一个椭圆窗口
            该API函数需要绑定窗口后才可以使用
        parms:
            hwnd:
                指定的窗口句柄,如果此值为0,那么就在桌面创建此窗口
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            w:
                矩形区域的宽度
            h:
                矩形区域的高度
        return:
            创建成功的窗口句柄
        """
        return self.obdm.CreateFoobarEllipse(hwnd,x,y,w,h)

    def CreateFoobarRect(self,hwnd:int,x:int,y:int,w:int,h:int)->int:
        """
        Function:
            创建一个矩形窗口
        parms:
            hwnd:
                指定的窗口句柄,如果此值为0,那么就在桌面创建此窗口
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            w:
                矩形区域的宽度
            h:
                矩形区域的高度
        return:
            整形数 : 创建成功的窗口句柄
        """
        return self.obdm.CreateFoobarRect(hwnd,x,y,w,h)

    def CreateFoobarRoundRect(self,hwnd:int,x:int,y:int,w:int,h:int,rw:int,rh:int)->int:
        """
        Function:
            创建一个矩形窗口
        parms:
            hwnd:
                指定的窗口句柄,如果此值为0,那么就在桌面创建此窗口
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            w:
                矩形区域的宽度
            h:
                矩形区域的高度
            rw:
                圆角的宽度
            rh:
                圆角的高度
        return:
            整形数 : 创建成功的窗口句柄
        """
        return self.obdm.CreateFoobarRoundRect(hwnd,x,y,w,h,rw,rh)

    def FoobarClearText(self,hwnd:int)->int:
        """
        Function:
            清除指定的Foobar滚动文本区
        parms:
            hwnd:
                指定的窗口句柄,如果此值为0,那么就在桌面创建此窗口
        return:
            0 : 失败
            1 : 成功
        """
        return self.obdm.FoobarClearText(hwnd)

    def FoobarClose(self,hwnd:int)->int:
        """
        Function:
            关闭一个Foobar,注意,必须调用此函数来关闭窗口,用SetWindowState也可以关闭,但会造成内存泄漏.
        parms:
            hwnd:
                指定的Foobar窗口句柄
        return:
            0: 失败
            1: 成功
        """
        return self.obdm.FoobarClose(hwnd)

    def FoobarDrawLine(self,hwnd:int,x1:int,y1:int,x2:int,y2:int,color:str,style:int,width:int)->int:
        """
        Function:
            在指定的Foobar窗口内部画线条.
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
            x1:
                左上角X坐标(相对于hwnd客户区坐标)
            y1:
                左上角Y坐标(相对于hwnd客户区坐标)
            x2:
                右下角X坐标(相对于hwnd客户区坐标)
            y2:
                右下角Y坐标(相对于hwnd客户区坐标)
            color:
                填充的颜色值
            style:
                画笔类型. 0为实线. 1为虚线
            width:
                线条宽度.
        return:
            0 : 失败
            1 : 成功
        """
        return self.obdm.FoobarDrawLine(hwnd,x1,y1,x2,y2,color,style,width)

    def FoobarDrawPic(self,hwnd:int,x:int,y:int,pic_name:str,trans_color:str)->int:
        """
        Function:
            在指定的Foobar窗口绘制图像
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            pic_name:
                图像文件名
            trans_color:
                图像透明色
        return:
            0 : 失败
            1 : 成功
        """
        return self.obdm.FoobarDrawPic(hwnd,x,y,pic_name,trans_color)

    def FoobarDrawText(self,hwnd:int,x:int,y:int,w:int,h:int,text:str,color:str,align:int)->int:
        """
        Function:
            在指定的Foobar窗口绘制文字
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            w:
                矩形区域的宽度
            h:
                矩形区域的高度
            text:
                字符串
            color:
                文字颜色值
            align:
                取值范围如下
                1 : 左对齐
                2 : 中间对齐
                4 : 右对齐
        return:
            0 : 失败
            1 : 成功
        """
        return self.obdm.FoobarDrawText(hwnd,x,y,w,h,text,color,align)

    def FoobarFillRect(self,hwnd:int,x1:int,y1:int,x2:int,y2:int,color:str)->int:
        """
        Function:
            在指定的Foobar窗口绘制文字
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
            x1:
                左上角X坐标(相对于hwnd客户区坐标)
            y1:
                左上角Y坐标(相对于hwnd客户区坐标)
            x2:
                右下角X坐标(相对于hwnd客户区坐标)
            y2:
                右下角Y坐标(相对于hwnd客户区坐标)
            color:
                填充的颜色值
        return:
            0 : 失败
            1 : 成功
        """
        return self.obdm.FoobarFillRect(hwnd,x1,y1,x2,y2,color)

    def FoobarLock(self,hwnd)->int:
        """
        Function:
            锁定指定的Foobar窗口,不能通过鼠标来移动
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarLock(hwnd)

    def FoobarPrintText(self,hwnd:int,text:str,color:str)->int:
        """
        Function:
            向指定的Foobar窗口区域内输出滚动文字
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            text:
                文本内容
            color:
                文本颜色
        return:
            0代表失败,1代表成功
        """

        return self.obdm.FoobarPrintText(hwnd,text,color)

    def FoobarSetFont(self,hwnd:int,font_name:str,size:int,flag:int)->int:
        """
        Function:
            设置指定Foobar窗口的字体
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            font_name:
                系统字体名,注意,必须保证系统中有此字体
            size:
                字体大小
            flag:
                取值定义如下
                0 : 正常字体
                1 : 粗体
                2 : 斜体
                4 : 下划线
                文字可以是以上的组合 比如粗斜体就是1+2,斜体带下划线就是:2+4等.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarSetFont(hwnd,font_name,size,flag)

    def FoobarSetSave(self,hwnd:int,file:str,enable:int,header:str)->int:
        """
        Function:
            设置保存指定的Foobar滚动文本区信息到文件.
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            file:
                保存的文件名
            enable:
                取值范围如下
                0 : 关闭向文件输出 (默认是0)
                1 : 开启向文件输出
            header:
                输出的附加头信息. (比如行数 日期 时间信息) 格式是如下格式串的顺序组合.如果为空串，表示无附加头.
                "%L0nd%" 表示附加头信息带有行号，并且是按照十进制输出. n表示按多少个十进制数字补0对齐. 比如"%L04d%",输出的行号为0001  0002 0003等. "%L03d",输出的行号为001 002 003..等.
                "%L0nx%"表示附加头信息带有行号，并且是按照16进制小写输出. n表示按多少个16进制数字补0对齐. 比如"%L04x%",输出的行号为0009  000a 000b等. "%L03x",输出的行号为009 00a 00b..等.
                "%L0nX%"表示附加头信息带有行号，并且是按照16进制大写输出. n表示按多少个16进制数字补0对齐. 比如"%L04X%",输出的行号为0009  000A 000B等. "%L03X",输出的行号为009 00A 00B..等.
                "%yyyy%"表示年. 比如2012
                "%MM%"表示月. 比如12
                "%dd%"表示日. 比如28
                "%hh%"表示小时. 比如13
                "%mm%"表示分钟. 比如59
                "%ss%"表示秒. 比如48.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarSetSave(hwnd,file,enable,header)

    def FoobarSetTrans(self,hwnd:int,is_trans:int,color:str,sim:float)->int:
        """
        Function:
            设置指定Foobar窗口的是否透明
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            is_trans:
                是否透明. 0为不透明(此时,color和sim无效)，1为透明.
            color:
                透明色(RRGGBB)
            sim:
                透明色的相似值 0.1-1.0
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarSetTrans(hwnd,is_trans,color,sim)

    def FoobarStartGif(self,hwnd:int,x:int,y:int,pic_name:str,repeat_limit:int,delay:int)->int:
        """
        Function:
            在指定的Foobar窗口绘制gif动画.
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            pic_name:
                图像文件名
            repeat_limit:
                表示重复GIF动画的次数，如果是0表示一直循环显示.大于0，则表示循环指定的次数以后就停止显示.
            delay:
                表示每帧GIF动画之间的时间间隔.如果是0，表示使用GIF内置的时间，如果大于0，表示使用自定义的时间间隔.
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarStartGif(hwnd,x,y,pic_name,repeat_limit,delay)

    def FoobarStopGif(self,hwnd:int,x:int,y:int,pic_name:str)->int:
        """
        Function:
            停止在指定foobar里显示的gif动画.
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
            x:
                左上角X坐标(相对于hwnd客户区坐标)
            y:
                左上角Y坐标(相对于hwnd客户区坐标)
            pic_name:
                图像文件名
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarStopGif(hwnd,x,y,pic_name)

    def FoobarTextLineGap(self,hwnd:int,line_gap:int)->int:
        """
        Function:
            设置滚动文本区的文字行间距,默认是3
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            line_gap:
                文本行间距
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarTextLineGap(hwnd,line_gap)

    def FoobarTextPrintDir(self,hwnd:int,dir:int)->int:
        """
        Function:
            设置滚动文本区的文字输出方向,默认是0
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            dir:
                取值范围如下
                0 表示向下输出
                1 表示向上输出
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarTextPrintDir(hwnd,dir)

    def FoobarTextRect(self,hwnd:int,x:int,y:int,w:int,h:int)->int:
        """
        Function:
            设置指定Foobar窗口的滚动文本框范围,默认的文本框范围是窗口区域
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
            x:
                x坐标
            y:
                y坐标
            w:
                宽度
            h:
                高度
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarTextRect(hwnd,x,y,w,h)

    def FoobarUnlock(self,hwnd)->int:
        """
        Function:
            解锁指定的Foobar窗口,可以通过鼠标来移动
        parms:
            hwnd:
                指定的Foobar窗口句柄,此句柄必须是通过CreateFoobarxxx创建而来
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarUnlock(hwnd)

    def FoobarUpdate(self,hwnd:int)->int:
        """
        Function:
            刷新指定的Foobar窗口
        parms:
            hwnd:
                指定的Foobar窗口,注意,此句柄必须是通过CreateFoobarxxxx系列函数创建出来的
        return:
            0代表失败,1代表成功
        """
        return self.obdm.FoobarUpdate(hwnd)
    # </editor-fold>

    def RegSystemDm(self):
        os.system('regsvr32 dm.dll')
    def UnRegSystemDm(self):
        os.system('regsvr32 dm.dll /u')
    #
    #   缺少 内存 以及 文字识别
    #
