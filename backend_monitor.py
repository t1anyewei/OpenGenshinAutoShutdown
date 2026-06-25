import time
import os
import psutil


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


if __name__ == "__main__":
    check_and_shutdown()