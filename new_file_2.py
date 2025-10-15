# import functools

# def add_prefix(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return f'PREFIX: {func(*args, **kwargs)}'
#     return wrapper

# def add_suffix(func):
#     def wrapper(*args, **kwargs):
#         return f'{func(*args, **kwargs)} :SUFFIX'
#     return wrapper
    
# @add_prefix
# @add_suffix
# def say(*args, **kwargs):
#     return ' '.join(args)

# print(say('test'))

# print(say.__name__)
# print(say.__doc__)


# import functools

# def shout(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper

# @shout
# def get_greeting(*names):
#     """Returns a greeting message for the given names."""
#     if names:
#         return f"hello {', '.join(names)}"
#     return "hello"

# # Test metadata preservation
# print(get_greeting.__name__)  # Output: get_greeting
# print(get_greeting.__doc__)   # Output: Returns a greeting message for the given names.

# # Test functionality
# print(get_greeting("Alice", "Bob"))  # Output: HELLO ALICE, BOB


# import functools

# def shout(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         word = func(*args, **kwargs)
#         return word.upper()
#     return wrapper

# @shout
# def get_greeting(*names):
#     '''Some docstring'''
#     return f"hello {', '.join(names)}"

# print(get_greeting.__name__)
# print(get_greeting.__doc__)

# print(get_greeting('Bob', 'Joe'))

from functools import wraps
import time

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return f'{func.__name__} took {end -start:.5f} seconds'
    return wrapper

@measure_time
def triangular_number(n):
    return sum([i for i in range(1, n + 1)])

print(triangular_number(10**6))

def cache_result(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key in cache:
            return cache[cache_key]
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result
    
    return wrapper

@cache_result
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
