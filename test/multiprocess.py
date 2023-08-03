"""
多进程测试代码
"""
import multiprocessing
import time


def count(n):
    while n > 0:
        n -= 1


def main1():
    # 单进程执行
    start_time = time.time()
    count(100000000)
    end_time = time.time()
    print("单进程执行时间：", end_time - start_time)  # 单进程执行时间： 4.279423713684082

    # 多进程执行
    start_time = time.time()
    process1 = multiprocessing.Process(target=count, args=(50000000,))
    process2 = multiprocessing.Process(target=count, args=(50000000,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end_time = time.time()
    print("多进程执行时间：", end_time - start_time)  # 多进程执行时间： 2.2506167888641357


if __name__ == '__main__':
    main1()
