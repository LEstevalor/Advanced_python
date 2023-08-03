"""
守护线程

首先定义了一个run函数，该函数将在守护线程中运行
创建了一个名为daemon_thread的线程对象，并将其daemon属性设置为True，
以将其转换为守护线程。最后，我们启动守护线程，并在主线程中等待10秒。当主线程终止时，守护线程也将自动终止。
"""
import threading
import time


def run():
    while True:
        print("Daemon thread is running...")
        time.sleep(5)


if __name__ == "__main__":
    daemon_thread = threading.Thread(target=run)  # 线程对象
    daemon_thread.daemon = True
    daemon_thread.start()  # 启动守护线程

    # 主线程将等待10秒后结束
    time.sleep(10)
    print("Main thread is terminating")

"""
Daemon thread is running...
Daemon thread is running...
Main thread is terminating
Daemon thread is running...
"""
