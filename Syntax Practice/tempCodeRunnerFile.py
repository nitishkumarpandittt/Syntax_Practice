
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {int(end - start)} seconds")
#         return result
#     return wrapper

# @timer
# def slow_fn():
#     time.sleep(2)
#     print("finished executtion")

# slow_fn()