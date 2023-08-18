import schedule
import time
import subprocess

def run_main_py():
    try:
        subprocess.run(["python", "./main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running main.py:", e)

# 设置每隔24小时调度一次
schedule.every(24).hours.do(run_main_py)

while True:
    schedule.run_pending()
    time.sleep(60)
