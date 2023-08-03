"""
GIL代码测试
包括多线程代码测试
"""
import threading
import time

def count(n):
    while n > 0:
        n -= 1

# 单线程执行
start_time = time.time()
count(100000000)
end_time = time.time()
print("单线程执行时间：", end_time - start_time)  # 单线程执行时间： 4.452801704406738

# 多线程执行
start_time = time.time()
t1 = threading.Thread(target=count, args=(50000000,))
t2 = threading.Thread(target=count, args=(50000000,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print("多线程执行时间：", end_time - start_time)  # 多线程执行时间： 4.272630214691162