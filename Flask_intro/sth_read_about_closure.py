# # https://www.geeklibrary.jp/counter-attack/closure/
# # 闭包用于捕获变量和保留状态，而装饰器用于修改函数的行为。
# # 1. 计数器：闭包可以用于创建计数器函数，以便在不引入全局变量的情况下跟踪某些事件的发生次数。

# def counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment


# # 创建两个独立的计数器
# counter1 = counter()
# counter2 = counter()

# print(counter1())  # 输出：1
# print(counter1())  # 输出：2
# print(counter2())  # 输出：1


# # 2. 缓存：闭包可用于创建缓存函数，以提高函数的执行效率，避免多次计算相同的结果。
# def memoize(func):
#     cache = {}

#     def wrapper(*args):
#         if args not in cache:
#             result = func(*args)
#             cache[args] = result
#             print(cache)  # Added by me
#         return cache[args]
#     return wrapper


# @memoize
# def expensive_function(n):
#     print(f"计算 {n} 的结果...")
#     return n * 2


# print(expensive_function(5))  # 计算 5 的结果... 输出：10
# print(expensive_function(5))  # 直接从缓存获取结果，不再计算 输出：10


# # 这我对只有一个缓存的结构不满意于是我找到以下代码可以储存多个缓存的装饰器
from collections import deque


def memoize_with_limit(limit):
    cache = {}
    cache_queue = deque(maxlen=limit)

    def memoize(func):
        def wrapper(*args):
            if args not in cache:
                result = func(*args)
                cache[args] = result
                cache_queue.append(args)
                print(cache_queue)
            return cache[args]
        return wrapper
    return memoize


@memoize_with_limit(3)  # 指定缓存大小为3
def expensive_function(n):
    print(f"计算 {n} 的结果...")
    return n * 2


print(expensive_function(5))  # 计算 5 的结果... 输出：10
print(expensive_function(3))  # 计算 3 的结果... 输出：6
print(expensive_function(7))  # 计算 7 的结果... 输出：14
# print(expensive_function(5))  # 直接从缓存获取结果，不再计算 输出：10
# print(expensive_function(4))  # 计算 4 的结果... 输出：8
# print(expensive_function(3))  # 直接从缓存获取结果，不再计算 输出：6

# 关于上述的包
# collections模块中的deque（发音为 "deck"）是一个双端队列（Double-Ended Queue）的数据结构，它可以在两端（前端和后端）高效地执行添加和删除操作。deque是Python标准库提供的一种数据结构，通常用于需要高效进行插入和删除操作的场景，尤其是在队列或栈的应用中。
# 以下是一些deque的特点和常见用法：
# 高效的插入和删除操作：与列表（list）不同，deque支持在两端执行快速的插入和删除操作。这使它特别适用于需要频繁在开头和结尾进行操作的场景。
# 有限大小的队列：您可以创建一个具有最大长度的deque，当元素超过这个长度时，最旧的元素会被自动丢弃，从而限制了队列的大小。
# 线程安全：deque提供了线程安全的操作，因此可以在多线程环境中使用，而不需要额外的同步。
# 支持迭代：您可以像遍历列表一样遍历deque中的元素。
# 下面是一个简单示例，展示了如何使用deque：

# from collections import deque

# # 创建一个空的deque
# my_deque = deque()

# # 在deque的右侧添加元素
# my_deque.append(1)
# my_deque.append(2)
# my_deque.append(3)

# # 在deque的左侧添加元素
# my_deque.appendleft(0)

# # 输出deque的内容
# print(my_deque)  # 输出：deque([0, 1, 2, 3])

# # 弹出右侧的元素
# right_element = my_deque.pop()
# print(right_element)  # 输出：3

# # 弹出左侧的元素
# left_element = my_deque.popleft()
# print(left_element)  # 输出：0


# `deque` 是一个非常有用的数据结构，特别适用于需要高效执行队列和栈操作的情况，同时还支持有限大小的队列和迭代。 


# # 3. 实现私有变量：闭包可以用于创建包含私有变量的对象，限制对变量的直接访问。
# def create_person(name, age):
#     private_data = {"name": name, "age": age}

#     def get_info():
#         return private_data
#     return get_info


# person = create_person("Alice", 30)
# print(person())  # 输出：{'name': 'Alice', 'age': 30}
# print(person()["name"])  # 输出：'Alice'


# # 4. 事件处理：闭包可用于创建事件处理程序，以便在事件发生时执行特定的函数。
# def event_handler(event_name):
#     def handler(callback):
#         def wrapper(*args, **kwargs):
#             print(f"触发事件 {event_name}")
#             result = callback(*args, **kwargs)
#             return result
#         return wrapper
#     return handler


# @event_handler("click")
# def button_click():
#     print("按钮被点击")


# button_click()  # 输出：触发事件 click \n 按钮被点击

# # 这些示例展示了闭包在Python编程中的实际用途，它们可用于创建封装、缓存、事件处理和状态管理等功能。闭包允许您在函数内部捕获和保持状态，同时提供了更高的代码封装和模块化。
