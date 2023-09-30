# # A practice with decorator
# class User:

#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False

#     def is_authenticated(function):
#         def wrapper(*args, **kwargs):
#             if args[0].is_logged_in is True:
#                 function(args[0])
#         return wrapper

#     @is_authenticated
#     def create_blog_post():
#         print(f"This is {user.name}'s new blog post.")


# user = User("Sally")
# user.is_logged_in = True
# user.create_blog_post()


# Another practice


def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(1, 2, 3)

