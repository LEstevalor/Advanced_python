"""
协程实验
适合python3.7即以后
"""
import asyncio
import time


async def count(n):
    while n > 0:
        n -= 1


async def main():
    task1 = asyncio.create_task(count(50000000))
    task2 = asyncio.create_task(count(50000000))
    await asyncio.gather(task1, task2)


# 单协程执行
start_time = time.time()
asyncio.run(count(100000000))
end_time = time.time()
print("单协程执行时间：", end_time - start_time)

# 多协程执行
start_time = time.time()
asyncio.run(main())
end_time = time.time()
print("多协程执行时间：", end_time - start_time)
