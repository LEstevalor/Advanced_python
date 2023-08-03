"""
守护进程
但这段代码不适合在windows OS上运行，适合linux
"""
import os
import sys
import time


def daemonize():
    pid = os.fork()  # 创建一个新的子进程

    if pid > 0:
        sys.exit()

    os.setsid()  # 创建一个新的会话，并将子进程设置为该会话的会话领导者。这将使子进程脱离控制终端，从而实现守护进程的特性之一。
    os.umask(0)  # 设置子进程的文件创建模式

    pid = os.fork()

    if pid > 0:
        sys.exit()

    sys.stdout.flush()
    sys.stderr.flush()

    with open("/dev/null", "r") as stdin:
        os.dup2(stdin.fileno(), sys.stdin.fileno())

    with open("/dev/null", "a") as stdout:
        os.dup2(stdout.fileno(), sys.stdout.fileno())

    with open("/dev/null", "a") as stderr:
        os.dup2(stderr.fileno(), sys.stderr.fileno())


def run():
    while True:
        print("Daemon is running...")
        time.sleep(5)


if __name__ == "__main__":
    daemonize()
    run()
