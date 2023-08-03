from pathos.multiprocessing import ProcessingPool as _Pool
# 定义输入值列表
input_values_x = [1, 2, 3, 4, 5]
input_values_y = [[6,3], [7,1], [8,9], [9,7], [10,5]]


def task_function(x, y):
    return x + y[0] + y[1]

def hello():
    # 使用 ProcessPoolExecutor 创建一个进程池
    with _Pool(processes=5) as pool:
        # 使用 zip 函数将输入值列表组合在一起，并使用 map 方法将函数应用于组合后的元组
        results = pool.map(task_function, input_values_x, input_values_y)
        print(results)
        return
