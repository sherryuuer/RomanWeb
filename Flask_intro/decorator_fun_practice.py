# import time
# current_time = time.time()
# # print(current_time)


# def speed_calc_decorator(function):
#     function()
#     finish_time = time.time()
#     time_period = finish_time - current_time
#     print(f"{function.__name__} run speed: {time_period}s")
# # __name__ can return the name of the function.


# # see I don't need to call the fast_function when I use decorator.
# # this @ seems called the decorator function!
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i


# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i


# fast_function()

# # Another way to do this above.
import time
current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        function()
        finish_time = time.time()
        time_period = finish_time - current_time
        print(f"{function.__name__} run speed: {time_period}s")
    return wrapper_function
# __name__ can return the name of the function.


# see I don't need to call the fast_function when I use decorator.
# this @ seems called the decorator function!
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
