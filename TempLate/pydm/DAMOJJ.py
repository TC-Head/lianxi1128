import win32com.client
import os

class DMLEIJJ():
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
    def ClientToScreen(self,hwnd:int,x:int,y:int)->tuple:return self.obdm.ClientToScreen(hwnd,x,y)

    def EnumProcess(self,name:str)->str:return self.obdm.EnumProcess(name)

    def EnumWindow(self,parent:int,title:str,class_name:str,filter:int)->str:return self.obdm.EnumWindow(parent,title,class_name,filter)

    def EnumWindowByProcess(self,process_name:str,title:str,class_name:str,filter:int)->str:return self.obdm.EnumWindowByProcess(process_name,title,class_name,filter)

    def EnumWindowByProcessId(self,pid:int,title:str,class_name:str,filter:int)->str:return self.obdm.EnumWindowByProcessId(pid,title,class_name,filter)

    def EnumWindowSuper(self,spec1,flag1,type1,spec2,flag2,type2,sort):return self.obdm.EnumWindowSuper(spec1,flag1,type1,spec2,flag2,type2,sort)

    def FindWindow(self,class_name:str,title:str)->int:return self.obdm.FindWindow(class_name,title)

    def FindWindowByProcess(self,process_name:str,class_name:str,title:str)->int:return self.obdm.FindWindowByProcess(process_name,class_name,title)

    def FindWindowByProcessId(self,process_id:int,class_name:str,title:str)->int:return self.obdm.FindWindowByProcessId(process_id,class_name,title)

    def FindWindowEx(self,parent:int,class_name:str,title:str)->int:return self.obdm.FindWindowEx(parent,class_name,title)

    def FindWindowSuper(self,spec1,flag1,type1,spec2,flag2,type2):return self.obdm.FindWindowSuper(spec1,flag1,type1,spec2,flag2,type2)

    def GetClientRect(self,hwnd:int)->tuple:return self.obdm.GetClientRect(hwnd)

    def GetClientSize(self,hwnd:int)->tuple:return self.obdm.GetClientSize(hwnd)

    def GetForegroundFocus(self)->int:return self.obdm.GetForegroundFocus()

    def GetForegroundWindow(self)->int:return self.obdm.GetForegroundWindow()

    def GetMousePointWindow(self)->int:return self.obdm.GetMousePointWindow()

    def GetPointWindow(self,x:int,y:int)->tuple:return self.obdm.GetPointWindow(x,y)

    def GetProcessInfo(self,pid:int)->str:return self.obdm.GetProcessInfo(pid)

    def GetSpecialWindow(self,flag:int)->int:return self.obdm.GetSpecialWindow(flag)

    def GetWindow(self,hwnd:int,flag:int)->int:return self.obdm.GetWindow(hwnd,flag)

    def GetWindowClass(self,hwnd:int)->str:return self.obdm.GetWindowClass(hwnd)

    def GetWindowProcessId(self,hwnd:int)->int:return self.obdm.GetWindowProcessId(hwnd)

    def GetWindowProcessPath(self,hwnd:int)->str:return self.obdm.GetWindowProcessPath(hwnd)

    def GetWindowRect(self,hwnd:int)->tuple:return self.obdm.GetWindowRect(hwnd)

    def GetWindowState(self,hwnd:int,flag:int)->int:return self.obdm.GetWindowState(hwnd,flag)

    def GetWindowThreadId(self,hwnd:int)->int:return self.obdm.GetWindowThreadId(hwnd)

    def GetWindowTitle(self,hwnd:int)->str:return self.obdm.GetWindowTitle(hwnd)

    def MoveWindow(self,hwnd:int,x:int,y:int)->int:return self.obdm.MoveWindow(hwnd,x,y)

    def ScreenToClient(self,hwnd:int,x:int,y:int)->tuple:return self.obdm.ScreenToClient(hwnd,x,y)

    def SendPaste(self,hwnd:int)->int:return self.obdm.SendPaste(hwnd)

    def SendString(self,hwnd:int,strtext:str)->int:return self.obdm.SendString(hwnd,strtext)

    def SendString2(self,hwnd:int,strtext:str)->int:return self.obdm.SendString2(hwnd,strtext)

    def SendStringIme(self,strtext:str)->int:return self.obdm.SendStringIme()

    def SendStringIme2(self,hwnd:int,strtext:str,mode:int)->int:return self.obdm.SendStringIme2(hwnd,strtext,mode)

    def SetClientSize(self,hwnd:int,width:int,height:int)->int:return self.obdm.SetClientSize(hwnd,width,height)

    def SetWindowSize(self,hwnd:int,width:int,height:int)->int:return self.obdm.SetWindowSize(hwnd,width,height)

    def SetWindowState(self,hwnd:int,flag:int)->int:return self.obdm.SetWindowState(hwnd,flag)

    def SetWindowText(self,hwnd:int,title:str)->int:return self.obdm.SetWindowText(hwnd,title)

    def SetWindowTransparent(self,hwnd:int,trans:int)->int:return self.obdm.SetWindowTransparent(hwnd,trans)
    # </editor-fold>

    # <editor-fold desc="键鼠API">
    def EnableMouseAccuracy(self,enable:int)->int:        self.obdm.EnableMouseAccuracy(enable)

    def GetCursorPos(self)->tuple:return self.obdm.GetCursorPos()

    def GetCursorShape(self)->str:return self.obdm.GetCursorShape()

    def GetCursorShapeEx(self,type:int)->str:return self.obdm.GetCursorShapeEx(type)

    def GetCursorSpot(self)->str:return self.obdm.GetCursorSpot()

    def GetKeyState(self,Key:int)->int:return self.obdm.GetKeyState(Key)

    def GetMouseSpeed(self)->int:return self.obdm.GetMouseSpeed()

    def KeyDown(self,vk_code:int)->int:return self.obdm.KeyDown(vk_code)

    def KeyDownChar(self,key_str:str)->int:return self.obdm.KeyDownChar(key_str)

    def KeyPress(self,vk_code:int)->int:return self.obdm.KeyPress(vk_code)

    def KeyPressChar(self,key_str:str)->int:return self.obdm.KeyPressChar(key_str)

    def KeyPressStr(self,key_str:str,delay:int)->int:return self.obdm.KeyPressStr(key_str,delay)

    def KeyUp(self,vk_code:int)->int:return self.obdm.KeyUp(vk_code)

    def KeyUpChar(self,key_str:str)->int:return self.obdm.KeyUpChar(key_str)

    def LeftClick(self)->int:return self.obdm.LeftClick()

    def LeftDoubleClick(self)->int:return self.obdm.LeftDoubleClick()

    def LeftDown(self)->int:return self.obdm.LeftDown()

    def LeftUp(self)->int:return self.obdm.LeftUp()

    def MiddleClick(self)->int:return self.obdm.MiddleClick()

    def MiddleDown(self)->int:return self.obdm.MiddleDown()

    def MiddleUp(self)->int:return self.obdm.MiddleUp()

    def MoveR(self,rx:int,ry:int)->int:return self.obdm.MoveR(rx,ry)

    def MoveTo(self,x:int,y:int)->int:return self.obdm.MoveTo(x,y)

    def MoveToEx(self,x:int,y:int,w:int,h:int)->int:return self.obdm.MoveToEx(x,y,w,h)

    def RightClick(self)->int:return self.obdm.RightClick()

    def RightDown(self)->int:return self.obdm.RightDown()

    def RightUp(self)->int:return self.obdm.RightUp()

    def SetKeypadDelay(self,type:str,delay:int)->int:return self.obdm.SetKeypadDelay()

    def SetMouseDelay(self,type:str,delay:int)->int:return self.obdm.SetMouseDelay(type,delay)

    def SetMouseSpeed(self,speed:int)->int:return self.obdm.SetMouseSpeed(speed)

    def SetSimMode(self,mode:int)->int:        self.obdm.SetSimMode(mode)

    def WaitKey(self,vk_code:int,time_out:int)->int:return self.obdm.WaitKey(vk_code,time_out)

    def WheelDown(self)->int:return self.obdm.WheelDown()

    def WheelUp(self)->int:return self.obdm.WheelUp()
    # </editor-fold>

    # <editor-fold desc="后台设置API">
    def BindWindow(self,hwnd:int,display:str,mouse:str,keypad:str,mode:int):return self.obdm.BindWindow(hwnd,display,mouse,keypad,mode)

    def BindWindowEx(self,hwnd:int,display:str,mouse:str,keypad:str,public:str,mode:int)->int:return self.obdm.BindWindowEx(hwnd,display,mouse,keypad,public,mode)

    def DownCpu(self,type:int,rate:int)->int:return self.obdm.DownCpu(type,rate)

    def EnableBind(self,enable:int)->int:return self.obdm.EnableBind(enable)

    def EnableFakeActive(self,enable:int)->int:return self.obdm.EnableFakeActive(enable)

    def EnableIme(self,enable:int)->int:return self.obdm.EnableIme(enable)

    def EnableKeypadMsg(self,enable:int)->int:return self.obdm.EnableKeypadMsg(enable)

    def EnableKeypadPatch(self,enable:int)->int:return self.obdm.EnableKeypadPatch(enable)

    def EnableKeypadSync(self,enable:int,time_out:int)->int:return self.obdm.EnableKeypadSync(enable,time_out)

    def EnableMouseMsg(self,enable:int)->int:return self.obdm.EnableMouseMsg(enable)

    def EnableMouseSync(self,enable:int,time_out:int)->int:return self.obdm.EnableMouseSync(enable,time_out)

    def EnableRealKeypad(self,enable:int)->int:return self.obdm.EnableRealKeypad(enable)

    def EnableRealMouse(self,enable:int,mousedelay:int,Mousetep:int)->int:return self.obdm.EnableRealMouse(enable,mousedelay,Mousetep)

    def EnableSpeedDx(self,enable:int)->int:return self.obdm.EnableSpeedDx(enable)

    def ForceUnBindWindow(self,hwnd:int)->int:return self.obdm.ForceUnBindWindow(hwnd)

    def GetBindWindow(self)->int:return self.obdm.GetBindWindow()

    def GetFps(self)->int:return self.obdm.GetFps()

    def HackSpeed(self,rate:int)->int:return self.obdm.HackSpeed(rate)

    def IsBind(self,hwnd:int)->int:return self.obdm.IsBind(hwnd)

    def LockDisplay(self,lock:int)->int:return self.obdm.LockDisplay(lock)

    def LockInput(self,lock:int)->int:return self.obdm.LockInput(lock)

    def LockMouseRect(self,x1:int,y1:int,x2:int,y2:int)->int:return self.obdm.LockMouseRect(x1,y1,x2,y2)

    def SetAero(self,enable:int)->int:return self.obdm.SetAero(enable)

    def SetDisplayDelay(self,time:int)->int:return self.obdm.SetDisplayDelay(time)

    def SetDisplayRefreshDelay(self,time:int)->int:return self.obdm.SetDisplayRefreshDelay(time)

    def SwitchBindWindow(self,hwnd:int)->int:return self.obdm.SwitchBindWindow(hwnd)

    def UnBindWindow(self)->int:return self.obdm.UnBindWindow()
    # </editor-fold>

    # <editor-fold desc="汇编API">
    def AsmAdd(self,asm_ins:str)->int:return self.obdm.AsmAdd(asm_ins)

    def AsmCall(self,hwnd:int,mode:int)->int:return self.obdm.AsmCall(hwnd,mode)

    def AsmCallEx(self,hwnd:int,mode:int,base_addr:str)->int:return self.obdm.AsmCallEx(hwnd,mode,base_addr)

    def AsmClear(self)->int:return self.obdm.AsmClear()

    def AsmSetTimeout(self,time_out:int,param:int)->int:return self.obdm.AsmSetTimeout(time_out,param)

    def Assemble(self,base_addr:int,is_64bit:int)->int:return self.obdm.Assemble(base_addr,is_64bit)

    def DisAssemble(self,asm_code,base_addr:int,is_64bit:int)->int:return self.obdm.DisAssemble(asm_code,base_addr,is_64bit)
    # </editor-fold>

    # <editor-fold desc="基本设置API">
    def EnablePicCache(self,enable)->int:return self.obdm.EnablePicCache(enable)

    def GetBasePath(self)->str:return self.obdm.GetBasePath()

    def GetDmCount(self)->int:return self.obdm.GetDmCount()

    def GetID(self)->int:return self.obdm.GetID()

    def GetLastError(self)->int:return self.obdm.GetLastError()

    def GetPath(self)->str:return self.obdm.GetPath()

    def Reg(self)->int:
        reg_code = "jv965720b239b8396b1b7df8b768c919e86e10f"
        ver_info = "jv8hjzz6z5u4700"
        return self.obdm.Reg(reg_code,ver_info)

    def RegEx(self,reg_code:str,ver_info:str,ip:str)->int:return self.obdm.RegEx(reg_code,ver_info,ip)

    def RegExNoMac(self,reg_code:str,ver_info:str,ip:str)->int:return self.obdm.RegExNoMac(reg_code,ver_info,ip)

    def RegNoMac(self,reg_code:str,ver_info:str)->int:return self.obdm.RegNoMac(reg_code,ver_info)

    def SetDisplayInput(self,mode:str)->int:return self.obdm.SetDisplayInput(mode)

    def SetEnumWindowDelay(self,delay:int)->int:return self.obdm.SetEnumWindowDelay(delay)

    def SetPath(self,path:str)->int:return self.obdm.SetPath(path)

    def SetShowErrorMsg(self,show:int)->int:return self.obdm.SetShowErrorMsg(show)

    def SpeedNormalGraphic(self,enable:int)->int:return self.obdm.SpeedNormalGraphic(enable)

    def Ver(self)->str:return self.obdm.Ver()
    # </editor-fold>

    # <editor-fold desc="图色API">
    def AppendPicAddr(self,pic_info:str,addr:int,size)->str:return self.obdm.AppendPicAddr(pic_info,addr,size)

    def BGR2RGB(self,bgr_color:str)->str:return self.obdm.BGR2RGB(bgr_color)

    def Capture(self,x1:int,y1:int,x2:int,y2:int,file:str)->int:return self.obdm.Capture(x1,y1,x2,y2,file)

    def CaptureGif(self,x1:int,y1:int,x2:int,y2:int,file:str,delay:int,time:int)->int:return self.obdm.CaptureGif(x1,y1,x2,y2,file,delay,time)

    def CaptureJpg(self,x1:int,y1:int,x2:int,y2:int,file:str,quality:int)->int:return self.obdm.CaptureJpg(x1,y1,x2,y2,file,quality)

    def CapturePng(self,x1:int,y1:int,x2:int,y2:int,file:str)->int:return self.obdm.CapturePng(x1,y1,x2,y2,file)

    def CapturePre(self,file:str)->int:return self.obdm.CapturePre(file)

    def CmpColor(self,x:int,y:int,color:str,sim:float)->int:return self.obdm.CmpColor(x,y,color,sim)

    def EnableDisplayDebug(self,enable_debug:int)->int:return self.obdm.EnableDisplayDebug(enable_debug)

    def EnableFindPicMultithread(self,enable:int)->int:return self.obdm.EnableFindPicMultithread(enable)

    def EnableGetColorByCapture(self,enable:int)->int:return self.obdm.EnableGetColorByCapture(enable)

    def FindColor(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,dir:int)->int:return self.obdm.FindColor(x1,y1,x2,y2,color,sim,dir)

    def FindColorBlock(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,count:int,width:int,height:int)->tuple:return self.obdm.FindColorBlock(x1,y1,x2,y2,color,sim,count,width,height)

    def FindColorBlockEx(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,count:int,width:int,height:int)->str:return self.obdm.FindColorBlock(x1,y1,x2,y2,color,sim,count,width,height)

    def FindColorE(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,dir:int)->str:return self.obdm.FindColorE(x1,y1,x2,y2,color,sim,dir)

    def FindColorEx(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float,dir:int)->str:return self.obdm.FindColorEx(x1,y1,x2,y2,color,sim,dir)

    def FindMulColor(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float)->int:return self.obdm.FindMulColor(x1,y1,x2,y2,color,sim,dir)

    def FindMultiColor(self,x1:int,y1:int,x2:int,y2:int,first_color:str,offset_color:str,sim:float,dir:int):return self.obdm.FindMultiColor(x1,y1,x2,y2,first_color,offset_color,sim,dir)

    def FindMultiColorE(self,x1:int,y1:int,x2:int,y2:int,first_color:str,offset_color:str,sim:float,dir:int):return self.obdm.FindMultiColorE(x1,y1,x2,y2,first_color,offset_color,sim,dir)

    def FindMultiColorEx(self,x1:int,y1:int,x2:int,y2:int,first_color:str,offset_color:str,sim:float,dir:int):return self.obdm.FindMultiColorEx(x1,y1,x2,y2,first_color,offset_color,sim,dir)

    def FindPic(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->tuple:return self.obdm.FindPic(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicE(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->str:return self.obdm.FindPicE(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicEx(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->str:return self.obdm.FindPicEx(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicExS(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->str:return self.obdm.FindPicExS(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicMem(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:float)->tuple:return self.obdm.FindPicMem(x1,y1,x2,y2,pic_info,delta_color,sim)

    def FindPicMemE(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:float)->str:return self.obdm.FindPicMemE(x1,y1,x2,y2,pic_info,delta_color,sim)

    def FindPicMemEx(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:float)->str:return self.obdm.FindPicMemEx(x1,y1,x2,y2,pic_info,delta_color,sim)

    def FindPicS(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:float,dir:int)->tuple:return self.obdm.FindPicS(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSim(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:int,dir:int)->tuple:return self.obdm.FindPicSim(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSimE(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:int,dir:int)->str:return self.obdm.FindPicSimE(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSimEx(self,x1:int,y1:int,x2:int,y2:int,pic_name:str,delta_color:str,sim:int,dir:int)->str:return self.obdm.FindPicSimEx(x1,y1,x2,y2,pic_name,delta_color,sim,dir)

    def FindPicSimMem(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:int,dir:int)->tuple:return self.obdm.FindPicSimMem(x1,y1,x2,y2,pic_info,delta_color,sim,dir)

    def FindPicSimMemE(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:int,dir:int)->str:return self.obdm.FindPicSimMemE(x1,y1,x2,y2,pic_info,delta_color,sim,dir)

    def FindPicSimMemEx(self,x1:int,y1:int,x2:int,y2:int,pic_info:str,delta_color:str,sim:int,dir:int)->str:return self.obdm.FindPicSimMemEx(x1,y1,x2,y2,pic_info,delta_color,sim,dir)

    def FindShape(self,x1:int,y1:int,x2:int,y2:int,offset_color:str,sim:float,dir:int)->tuple:return self.obdm.FindShape(x1,y1,x2,y2,offset_color,sim,dir)

    def FindShapeE(self,x1:int,y1:int,x2:int,y2:int,offset_color:str,sim:float,dir:int)->str:return self.obdm.FindShapeE(x1,y1,x2,y2,offset_color,sim,dir)

    def FindShapeEx(self,x1:int,y1:int,x2:int,y2:int,offset_color:str,sim:float,dir:int)->str:return self.obdm.FindShapeEx(x1,y1,x2,y2,offset_color,sim,dir)

    def FreePic(self,pic_name:str)->int:return self.obdm.FreePic(pic_name)

    def GetAveHSV(self,x1:int,y1:int,x2:int,y2:int)->str:return self.obdm.GetAveHSV(x1,y1,x2,y2)

    def GetAveRGB(self,x1:int,y1:int,x2:int,y2:int)->str:return self.obdm.GetAveRGB(x1,y1,x2,y2)

    def GetColor(self,x:int,y:int)->str:return self.obdm.GetColor(x,y)

    def GetColorBGR(self,x:int,y:int)->str:return self.obdm.GetColorBGR(x,y)

    def GetColorHSV(self,x:int,y:int)->str:return self.obdm.GetColorBGR(x,y)

    def GetColorNum(self,x1:int,y1:int,x2:int,y2:int,color:str,sim:float)->int:return self.obdm.GetColorBGR(x1,y1,x2,y2,color,sim)

    def GetPicSize(self,pic_name:str)->str:return self.obdm.GetPicSize(pic_name)

    def GetScreenData(self,x1:int,y1:int,x2:int,y2:int)->tuple:return self.obdm.GetScreenData(x1,y1,x2,y2)

    def GetScreenDataBmp(self,x1:int,y1:int,x2:int,y2:int)->tuple:return self.obdm.GetScreenData(x1,y1,x2,y2)

    def ImageToBmp(self,pic_name:str,bmp_name:str)->int:return self.obdm.ImageToBmp(pic_name,bmp_name)

    def IsDisplayDead(self,x1:int,y1:int,x2:int,y2:int,t:int)->int:return self.obdm.IsDisplayDead(x1,y1,x2,y2,t)

    def LoadPic(self,pic_name:str)->int:return self.obdm.LoadPic(pic_name)

    def LoadPicByte(self,addr:int,size:int,pic_name:str)->int:return self.obdm.LoadPicByte(addr,size,pic_name)

    def MatchPicName(self,pic_name:str)->str:return self.obdm.MatchPicName(pic_name)

    def RGB2BGR(self,rgb_color:str)->str:return self.obdm.rgb_color(rgb_color)

    def SetExcludeRegion(self,mode:int,info:str)->int:return self.obdm.SetExcludeRegion(mode,info)

    def SetFindPicMultithreadCount(self,count:int)->int:return self.obdm.SetFindPicMultithreadCount(count)

    def SetPicPwd(self,pwd:str)->int:return self.obdm.SetPicPwd(pwd)
    # </editor-fold>

    # <editor-fold desc="文件API">
    def CopyFile(self,src_file:str,dst_file:str,over:int)->int:return self.obdm.CopyFile(src_file,dst_file,over)

    def CreateFolder(self,folder:str)->int:return self.obdm.CreateFolder(folder)

    def DecodeFile(self,file:str,pwd:str)->int:return self.obdm.DecodeFile(file,pwd)

    def DeleteFile(self,file:str)->int:return self.obdm.DeleteFile(file)

    def DeleteFolder(self,folder:str)->int:return self.obdm.DeleteFolder(folder)

    def DeleteIni(self,section:str,key:str,file:str)->int:return self.obdm.DeleteIni(section,key,file)

    def DeleteIniPwd(self,section:str,key:str,file:str,pwd:str)->int:return self.obdm.DeleteIniPwd(section,key,file,pwd)

    def DownloadFile(self,url:str,save_file:str,timeout:int)->int:return self.obdm.DownloadFile(url,save_file,timeout)

    def EncodeFile(self,file:str,pwd:str)->int:return self.obdm.EncodeFile(file,pwd)

    def EnumIniKey(self,section:str,file:str)->str:return self.obdm.EnumIniKey(section,file)

    def EnumIniKeyPwd(self,section:str,file:str,pwd:str)->str:return self.obdm.EnumIniKeyPwd(section,file,pwd)

    def EnumIniSection(self,file:str)->str:return self.obdm.EnumIniSection(file)

    def EnumIniSectionPwd(self,file:str,pwd:str)->str:return self.obdm.EnumIniSectionPwd(file,pwd)

    def GetFileLength(self,file:str)->int:return self.obdm.GetFileLength(file)

    def GetRealPath(self,path:str)->str:return self.obdm.GetRealPath(path)

    def IsFileExist(self,file:str)->int:return self.obdm.IsFileExist(file)

    def IsFolderExist(self,folder:str)->int:return self.obdm.IsFolderExist(folder)

    def MoveFile(self,src_file:str,dst_file:str)->int:return self.obdm.MoveFile(src_file,dst_file)

    def ReadFile(self,file:str)->str:return self.obdm.ReadFile(file)

    def ReadIni(self,section:str,key:str,file:str)->str:return self.obdm.ReadIni(section,key,file)

    def ReadIniPwd(self,section:str,key:str,file:str,pwd:str)->str:return self.obdm.ReadIniPwd(section,key,file,pwd)

    def SelectDirectory(self)->str:return self.obdm.SelectDirectory()

    def SelectFile(self)->str:return self.obdm.SelectFile()

    def WriteFile(self,file:str,content:str)->int:return self.obdm.WriteFile(file,content)

    def WriteIni(self,section:str,key:str,value:str,file:str)->int:return self.obdm.WriteIni(section,key,value,file)

    def WriteIniPwd(self,section:str,key:str,value:str,file:str,pwd:str)->int:return self.obdm.WriteIniPwd(section,key,value,file,pwd)
    # </editor-fold>

    # <editor-fold desc="系统API">
    def Beep(self,f:int,duration:int)->int:return self.obdm.Beep(f,duration)

    def CheckFontSmooth(self)->int:return self.obdm.CheckFontSmooth()

    def CheckUAC(self)->int:return self.obdm.CheckUAC()

    def Delay(self,mis:int)->int:return self.obdm.Delay(mis)

    def Delays(self,mis_min:int,mis_max:int)->int:return self.obdm.Delays(mis_min,mis_max)

    def DisableCloseDisplayAndSleep(self)->int:return self.obdm.DisableCloseDisplayAndSleep()

    def DisableFontSmooth(self)->int:return self.obdm.DisableFontSmooth()

    def DisablePowerSave(self)->int:return self.obdm.DisablePowerSave()

    def DisableScreenSave(self)->int:return self.obdm.DisableScreenSave()

    def EnableFontSmooth(self)->int:return self.obdm.EnableFontSmooth()

    def ExitOs(self,type:int)->int:return self.obdm.ExitOs(type)

    def GetClipboard(self)->str:return self.obdm.GetClipboard()

    def GetCpuType(self)->str:return self.obdm.GetCpuType()

    def GetCpuUsage(self)->str:return self.obdm.GetCpuUsage()

    def GetDir(self,type:int)->str:return self.obdm.GetDir(type)

    def GetDiskModel(self,index:int)->str:return self.obdm.GetDiskModel(index)

    def GetDiskReversion(self,index:int)->str:return self.obdm.GetDiskReversion(index)

    def GetDiskSerial(self,index:int)->str:return self.obdm.GetDiskSerial(index)

    def GetDisplayInfo(self)->str:return self.obdm.GetDisplayInfo()

    def GetDPI(self)->int:return self.obdm.GetDPI()

    def GetLocale(self)->int:return self.obdm.GetLocale()

    def GetMachineCode(self)->str:return self.obdm.GetMachineCode()

    def GetMachineCodeNoMac(self)->str:return self.obdm.GetMachineCodeNoMac()

    def GetMemoryUsage(self)->int:return self.obdm.GetMemoryUsage()

    def GetNetTime(self)->str:return self.obdm.GetNetTime()

    def GetNetTimeByIp(self,ip:str)->str:return self.obdm.GetNetTimeByIp(ip)

    def GetNetTimeSafe(self)->str:return self.obdm.GetNetTimeSafe()

    def GetOsBuildNumber(self)->int:return self.obdm.GetOsBuildNumber()

    def GetOsType(self)->int:return self.obdm.GetOsType()

    def GetScreenDepth(self)->int:return self.obdm.GetScreenDepth()

    def GetScreenHeight(self)->int:return self.obdm.GetScreenHeight()

    def GetScreenWidth(self)->int:return self.obdm.GetScreenWidth()

    def GetSystemInfo(self,type:str,method:str)->str:return self.obdm.GetSystemInfo(type,method)

    def GetTime(self)->int:return self.obdm.GetTime()

    def Is64Bit(self)->int:return self.obdm.Is64Bit()

    def IsSurrpotVt(self)->int:return self.obdm.IsSurrpotVt

    def Play(self,media_file:str)->int:return self.obdm.Play(media_file)

    def RunApp(self,app_path:str,mode:int)->int:return self.obdm.RunApp(app_path,mode)

    def SetClipboard(self,value:str)->int:return self.obdm.SetClipboard(value)

    def SetDisplayAcceler(self,level:int)->int:return self.obdm.SetDisplayAcceler(level)

    def SetLocale(self)->int:return self.obdm.SetLocale()

    def SetScreen(self,width:int,height:int,depth:int)->int:return self.obdm.SetScreen(width,height,depth)

    def SetUAC(self,enable:int)->int:return self.obdm.SetUAC(enable)

    def ShowTaskBarIcon(self,hwnd:int,is_show:int)->int:return self.obdm.ShowTaskBarIcon(hwnd,is_show)

    def Stop(self,id:int)->int:return self.obdm.Stop(id)
    # </editor-fold>

    # <editor-fold desc="FoobarAPI">
    def CreateFoobarCustom(self,hwnd:int,x:int,y:int,pic_name:str,trans_color:str,sim:float)->int:return self.obdm.CreateFoobarCustom(hwnd,x,y,pic_name,trans_color,sim)

    def CreateFoobarEllipse(self,hwnd:int,x:int,y:int,w:int,h:int)->int:return self.obdm.CreateFoobarEllipse(hwnd,x,y,w,h)

    def CreateFoobarRect(self,hwnd:int,x:int,y:int,w:int,h:int)->int:return self.obdm.CreateFoobarRect(hwnd,x,y,w,h)

    def CreateFoobarRoundRect(self,hwnd:int,x:int,y:int,w:int,h:int,rw:int,rh:int)->int:return self.obdm.CreateFoobarRoundRect(hwnd,x,y,w,h,rw,rh)

    def FoobarClearText(self,hwnd:int)->int:return self.obdm.FoobarClearText(hwnd)

    def FoobarClose(self,hwnd:int)->int:return self.obdm.FoobarClose(hwnd)

    def FoobarDrawLine(self,hwnd:int,x1:int,y1:int,x2:int,y2:int,color:str,style:int,width:int)->int:return self.obdm.FoobarDrawLine(hwnd,x1,y1,x2,y2,color,style,width)

    def FoobarDrawPic(self,hwnd:int,x:int,y:int,pic_name:str,trans_color:str)->int:return self.obdm.FoobarDrawPic(hwnd,x,y,pic_name,trans_color)

    def FoobarDrawText(self,hwnd:int,x:int,y:int,w:int,h:int,text:str,color:str,align:int)->int:return self.obdm.FoobarDrawText(hwnd,x,y,w,h,text,color,align)

    def FoobarFillRect(self,hwnd:int,x1:int,y1:int,x2:int,y2:int,color:str)->int:return self.obdm.FoobarFillRect(hwnd,x1,y1,x2,y2,color)

    def FoobarLock(self,hwnd)->int:return self.obdm.FoobarLock(hwnd)

    def FoobarPrintText(self,hwnd:int,text:str,color:str)->int:return self.obdm.FoobarPrintText(hwnd,text,color)

    def FoobarSetFont(self,hwnd:int,font_name:str,size:int,flag:int)->int:return self.obdm.FoobarSetFont(hwnd,font_name,size,flag)

    def FoobarSetSave(self,hwnd:int,file:str,enable:int,header:str)->int:return self.obdm.FoobarSetSave(hwnd,file,enable,header)

    def FoobarSetTrans(self,hwnd:int,is_trans:int,color:str,sim:float)->int:return self.obdm.FoobarSetTrans(hwnd,is_trans,color,sim)

    def FoobarStartGif(self,hwnd:int,x:int,y:int,pic_name:str,repeat_limit:int,delay:int)->int:return self.obdm.FoobarStartGif(hwnd,x,y,pic_name,repeat_limit,delay)

    def FoobarStopGif(self,hwnd:int,x:int,y:int,pic_name:str)->int:return self.obdm.FoobarStopGif(hwnd,x,y,pic_name)

    def FoobarTextLineGap(self,hwnd:int,line_gap:int)->int:return self.obdm.FoobarTextLineGap(hwnd,line_gap)

    def FoobarTextPrintDir(self,hwnd:int,dir:int)->int:return self.obdm.FoobarTextPrintDir(hwnd,dir)

    def FoobarTextRect(self,hwnd:int,x:int,y:int,w:int,h:int)->int:return self.obdm.FoobarTextRect(hwnd,x,y,w,h)

    def FoobarUnlock(self,hwnd)->int:return self.obdm.FoobarUnlock(hwnd)

    def FoobarUpdate(self,hwnd:int)->int:return self.obdm.FoobarUpdate(hwnd)
    # </editor-fold>

    def RegSystemDm(self):        os.system('regsvr32 dm.dll /s')
    def UnRegSystemDm(self):        os.system('regsvr32 dm.dll /u /s')

    #   缺少 内存 以及 文字识别

