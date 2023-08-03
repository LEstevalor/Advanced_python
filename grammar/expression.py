"""
匿名表达式
"""
# 使用 lambda 函数计算两数之和
add = lambda x, y: x + y
print(add(1, 2))  # 输出：3

# 使用 lambda 函数对列表进行排序
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)
# 输出：[{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

"""
列表推导式
语法糖
"""
# 使用列表推导式计算 0 到 9 的平方
squares = [x ** 2 for x in range(10)]
print(squares)  # 输出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用列表推导式筛选出偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# 输出：[2, 4, 6, 8]
