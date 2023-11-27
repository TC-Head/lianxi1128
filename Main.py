from Task.Create import *
import sys,os

#全局变量区
GLOBAL_INT_VAR = 0
GLOBAL_DOUBLE_VAR = 0.0
GLOBAL_STR_VAR = ""
GLOBAL_LIST_VAR = list()
GLOBAL_TUPLE_VAR = tuple()
GLOBAL_DICT_VAR = dict()
GLOBAL_SET_VAR = set()

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



# 函数区
def Set_Console_Color_Green():
    print(FONT_GREEN)

def Reset_Console_Color_Default():
    print(RESET_COLOR)

#函数区
def Function():
    # 1.获取启动程序的路径地址
    Start_Path = os.path.abspath('./')

    # 2.获取配置文件的路径地址
    ConfigFilePath =os.path.join(os.path.dirname(__file__),"config.ini")
    
    
    # 3.判断是否有对应的 Section
    config = ConfigParser()
    config.read(filenames=ConfigFilePath,encoding='utf8')
    
    if (sys.argv[1] in config.sections()) == False:
        print("错误提醒 : 请检查传入参数!")
        print("提示 : 配置文件中总共有 {} 个Section,请仔细选择!".format(len(config.sections())))
        [print("\t可用参数 : ",_) for _ in config.sections()]
        print("提示 : 程序已退出!")
        return -1
    
    if sys.argv[1] == "Create":
        Create(Start_Path=Start_Path,argv=sys.argv,ConfigFile_Path=ConfigFilePath)
    
    
    

#入口函数
if __name__ == "__main__" :
    Set_Console_Color_Green()
    Function()
    Reset_Console_Color_Default()