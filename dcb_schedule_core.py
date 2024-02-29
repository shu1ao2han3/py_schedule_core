#定时任务
import schedule
import time
import subprocess
#Windows平台特有模块，用于设置隐藏窗口
import msvcrt  
#配置文件
import configparser

# ------------------------公用方法-------------------------
# 从配置文件中加载配置信息
def readPropertyFromFile(properties):
    try:
        config = configparser.ConfigParser()
        config.read('dcb_schedule_core.properties')
        prop = config.get('dcb_schedule_core', properties)
        return prop
    except Exception as e:
        print(f"获取属性{properties}值失败,原因：{e}")
        return ""

#python调用exe
def run_exe(progName):
    try:
        output = subprocess.check_output([f'{progName}'], startupinfo=startupinfo, stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        errmsg = f"命令执行失败，返回码：{e.returncode}，输出：{e.output}"
        print(errmsg)

# ------------------主任务-----------------------
# 创建STARTUPINFO结构体实例并设置dwFlags为 subprocess.STARTF_USESHOWWINDOW，wShowWindow为SW_HIDE
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

# 设置定时任务
# 获取应用程序及启动时间的字典
relationDict = eval(readPropertyFromFile("relationDict"))
for exeName in relationDict:
    gapTime = eval(relationDict[exeName])
    print(f"{exeName},{gapTime}")
    # 定时任务设置不变
    schedule.every(gapTime).seconds.do(run_exe, exeName)

while True:
    schedule.run_pending()
    time.sleep(1)
