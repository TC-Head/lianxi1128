from DAMO import DMLEI
# from DAMOJJ import DMLEIJJ

# 1.先设置好 Python 解释器
# 2.将 DM.DLL 文件放置在 Main.py 同级目录下


#全局变量区
GLOBAL_INT_VAR = 0
GLOBAL_DOUBLE_VAR = 0.0
GLOBAL_STR_VAR = ""
GLOBAL_LIST_VAR = list()
GLOBAL_TUPLE_VAR = tuple()
GLOBAL_DICT_VAR = dict()
GLOBAL_SET_VAR = set()
dm = DMLEI()

#函数区
def Function():
    print("Hello World!")


#入口函数
if __name__ == "__main__" :
    Function()
    
