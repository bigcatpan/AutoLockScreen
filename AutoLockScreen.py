from win10toast import ToastNotifier
import time
from ctypes import windll
#import win32api,win32con
from tkinter import Tk, messagebox as msgbox

now = time.strftime("%H:%M:%S", time.localtime(time.time()))
alter_txt = u'''
当前时间 {} \n10秒钟之后将自动锁屏, 请及时保存工作内容, 
扭扭脖子, 起来走走, 喝点水呗！
'''.format(now)
sleep_time = 10
delay_time = 1800
while True:
    # windows通知模块，windows右下角通知不要禁止哈
    toaster = ToastNotifier()
    toaster.show_toast(u'休息，休息一会儿~', alter_txt, icon_path=None, threaded=True)
    time.sleep(sleep_time)
    # type = win32api.MessageBox(0, "马上休息了务必照顾好自己哦(^-^)", "提醒", win32con.MB_OKCANCEL)
    window = Tk()
    # 退出默认tk窗口
    window.withdraw()
    # 可关闭对话框
    result = msgbox.askokcancel('温馨提醒', '马上休息了务必照顾好自己哦(^-^)')
    user32 = windll.LoadLibrary('user32.dll')
    if (result):
        user32.LockWorkStation()
    # 判断是否解锁了屏保，如果没有, 休眠一段时间等待解锁
    while user32.GetForegroundWindow() == 0:
        time.sleep(5)
    # 延迟delay_time后再次循环
    time.sleep(delay_time)
