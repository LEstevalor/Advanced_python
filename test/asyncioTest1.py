import asyncio
import time


async def count(n):
    while n > 0:
        n -= 1


async def main():
    task1 = asyncio.ensure_future(count(50000000))
    task2 = asyncio.ensure_future(count(50000000))
    await asyncio.gather(task1, task2)


# 单协程执行
start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(count(100000000))
end_time = time.time()
print("单协程执行时间：", end_time - start_time)

# 多协程执行
start_time = time.time()
loop.run_until_complete(main())
end_time = time.time()
print("多协程执行时间：", end_time - start_time)

"""
单协程执行时间： 4.209939241409302
多协程执行时间： 4.172176122665405
"""
