from configparser import ConfigParser
import os
import shutil
from tkinter import messagebox


# ANSI转义码
# 前景色
FONT_BLACK = '\033[30m'
FONT_RED = '\033[31m'
FONT_GREEN = '\033[32m'
FONT_YELLOW = '\033[33m'
FONT_BLUE = '\033[34m'
FONT_MAGENTA = '\033[35m'
FONT_CYAN = '\033[36m'
FONT_WHITE = '\033[37m'

# 背景色
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# 重置颜色
RESET_COLOR = '\033[0m'



def copy_file(src, dst, total_files, current_file):
    # 输出源文件路径
    print(FONT_RED + BG_WHITE +"任务状态[{} / {}] : [ [ {} ]  ->  [ {} ] ] ".format(current_file, total_files, src,dst) + RESET_COLOR)

    # 执行复制
    shutil.copy2(src=src, dst=dst)


def Create_File_To_Specified_Directory(TempLatePath:str,Create_To_Directory:str,Create_Name:str):
    print("任务提示 : 任务开始!")

    # 1.判断是否有传入自定义名称
    if Create_Name.__len__() == 0:
        Create_Name = os.path.basename(TempLatePath)
        print("任务提示 : 用户没有传入自定义[名称],将会使用[模板默认名称],默认名称为=[{}]".format(Create_Name))
    
    # 2.合并目标路径
    Create_AbsPath = os.path.join(Create_To_Directory,Create_Name)
    print("任务提示 : 即将开始复制文件模板到指定目录!")
    print("任务提示 : 创建的文件路径为[ {} ]".format(Create_AbsPath))
    
    # 3.开始复制任务
    Copy_Result = messagebox.askquestion(title="提示 : 请回车确认!",message="当前复制的文件数量为 [ 1 ] \n模板文件来自 [ {} ]\n创建的路径为 [ {} ]".format(TempLatePath,Create_AbsPath))
    if Copy_Result == "yes":
        shutil.copy2(src=TempLatePath,dst=Create_AbsPath)
        messagebox.showinfo(title="任务提示 : 完成状态!",message="当前任务已完成!")
    elif Copy_Result == "no":
        messagebox.showinfo(title="任务提示 : 暂停状态!",message="当前任务已暂停!")
    

def Cretae_Folder_To_Specified_Directory(TempLatePath:str,Create_To_Directory:str,Create_Name:str):
    print("任务提示 : 任务开始!")

    # 1.判断是否有传入自定义名称
    if Create_Name.__len__() == 0:
        Create_Name = os.path.basename(TempLatePath)
        print("任务提示 : 用户没有传入自定义[名称],将会使用[模板默认名称],默认名称为=[{}]".format(Create_Name))

    # 2.合并目标路径
    Create_AbsPath = os.path.join(Create_To_Directory, Create_Name)
    print("任务提示 : 即将开始复制文件夹模板到指定目录!")
    print("任务提示 : 创建的文件夹路径为[ {} ]".format(Create_AbsPath))

    # 3.创建目标文件夹
    os.makedirs(Create_AbsPath, exist_ok=True)

    # 4.遍历目标文件夹并逐个复制文件
    total_files = 0
    for foldername, subfolders, filenames in os.walk(TempLatePath):
        total_files += len(filenames)

    current_file = 0
    for foldername, subfolders, filenames in os.walk(TempLatePath):
        for filename in filenames:
            src = os.path.join(foldername, filename)
            dst = os.path.join(Create_AbsPath, filename)
            
            # 调用复制函数
            copy_file(src, dst, total_files, current_file + 1)
            
            current_file += 1

    messagebox.showinfo(title="任务提示 : 完成状态!", message="当前任务已完成!")
    
    
def Create(Start_Path:str,argv:list,ConfigFile_Path:str):
    print("提示 : 程序启动路径 \t{}".format(Start_Path))
    print("提示 : 配置文件路径 \t{}".format(ConfigFile_Path))
    print("提示 : 程序启动参数 \t{}".format(argv))
    
    # 1.判断参数的数量,并且进行赋值操作
    Arg_Length = len(argv)
    Section = ""
    Option = ""
    Create_Name = ""
    if(Arg_Length != 3 and Arg_Length != 4):
        print("错误提示 : 触发[Create]任务失败,请检查参数数量!")
        return -1
    elif(Arg_Length == 3):
        Section = argv[1]
        Option = argv[2]
    elif(Arg_Length == 4):
        Section = argv[1]
        Option = argv[2]
        Create_Name = argv[3]
    
    # 2.获取指定[Section Option]中的Key值
    config = ConfigParser()
    config.read(filenames=ConfigFile_Path,encoding='utf8')
    KeyValue = config.get(section=Section,option=Option)
    print("提示 : KeyValue = ",KeyValue)



    # 3.判断Key值的路径是否存在,验证真伪
    KeyValueBoolResult = os.path.exists(KeyValue)
    if KeyValueBoolResult == True:
        print("提示 : KeyValue 所指定的路径正确!")
    elif KeyValueBoolResult == False:
        print("提示 : KeyValue 所指定的路径不正确!")
        return -1

    # 4.判断Key值是[文件 / 文件夹]哪一种
    KeyValueBoolDirResult= os.path.isfile(KeyValue)
    if KeyValueBoolDirResult == True:
        print("提示 : KeyValue 所指向的路径为 [文件] !")
    elif KeyValueBoolDirResult == False:
        print("提示 : KeyValue 所指向的路径为 [文件夹] !")

    # 5.根据[KeyValueBoolDirResult]的值进行判断,决定是使用那个函数
    if KeyValueBoolDirResult == True:
        Create_File_To_Specified_Directory(TempLatePath=KeyValue,Create_To_Directory=Start_Path,Create_Name=Create_Name)
    elif KeyValueBoolDirResult == False:
        Cretae_Folder_To_Specified_Directory(TempLatePath=KeyValue,Create_To_Directory=Start_Path,Create_Name=Create_Name)
    