# n = int(input("Enter a number: "))

# for i in range(0, n):
#     print("Hello World")



# for i in range(1, n+1):
#     print(i)

# for i in range(n, 0, -1):
#     print(i)

# for i in range(n, n*10+1, n):
#     print(i)

# sum = 0;

# for i in range(1, n+1):
#     sum += i;

# print(sum)

# factorial = 1;

# for i in range(1, n+1):
#     factorial *= i;

# print(factorial)

# oddSum = 0
# evenSum = 0

# for i in range(1, n+1, 2):
#     oddSum += i
# for i in range(0, n+1, 2):
#     evenSum += i

# print(oddSum, evenSum)

# for i in range(1, n, 1):
#     if(n%i == 0):
#         print(i)


# totalSum = 0
# for i in range(1, n, 1):
#     if(n%i == 0):
#         print(i, end = " + ")
#         totalSum += i

# print(end = "\n")
# if(totalSum == n):
#     print(f"{n} is a perfect number")
# else:
#      print(f"{n} is not a perfect number")


# for i in range(2, n+1):
#     if(i == n):
#         print(f"{n} is prime")
#         break
#     if(n%i == 0):
#         print(f"{n} is not prime")
#         break

# str = "helleherwer"

# revStr = ""
# for i in range(len(str)-1, -1, -1):
#     revStr += str[i]

# print(revStr)

# if revStr == str:
#     print("strings are palindrome")
# else:
#     print("strings are not palindrome")

# str = "P@#yn26at^&i5ve"
# char = digits = symbols = 0

# for i in str:
#     if((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')):
#         char += 1
#     elif((i >= '0' and i <= '9')):
#         digits += 1
#     else:
#         symbols += 1
# print(char, digits, symbols)

# a = 259

# while(a):
#     lastDigit = a%10
#     print(lastDigit)
#     a//=10

# a = int(input("Enter a number: "))
# n = a
# rev = 0
# while(a):
#     lastDigit = a%10
#     rev = rev * 10 + lastDigit
#     a//=10
# print(rev)

# if(rev == n):
#     print("Number is Palindrome")
# else:
#     print("Number is not a Palindrome")

# import random

# num = random.randint(1, 10)
# print(num)

# tries = 3
# count = 0
# while tries: 
#     guess = int(input("Guess the number between 1-10: "))
    
#     if num == guess:
#         print("Congratulations, You Won")
#         print("Tries:", count)
#         break
#     else:
#         tries -= 1
#         count += 1
#         if(tries == 0):
#             print("You lost !!!")
#         else:
#             print("Wrong, Guess Again")


# print("Hello")
# x = 10 / 0          # ZeroDivisionError   

# print("Hello")
# y = "5" + 5         # TypeError



# l = [10, 20, 12, 29, 30, 40]
# g = l[0]
# secondG = l[0]

# for i in l:
#     if i > g:
#         secondG = g
#         g = i
#     elif i > secondG:
#         secondG = i
    
# print(secondG)


# a, b, c = (1,2,3)
# print(a)
# print(type(b))
# print(c)

# a = [10, 10, 20, 20, 20, 30, 40]
# dict = {}

# for i in a:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)

# type hints

# def greet(name: str) -> str:
#     return f"Hello {name}"

# print(greet("Nitish"))
# print(greet(80))     # this doesn't give error

# tup: tuple[int] = (1,2,3,4)




def add(a: int, b: int) -> int:
    return a + b

print(add("10", "20"))

# mypy main.py to static type check
# main.py:189: error: Argument 1 to "add" has incompatible type "str"; expected "int"  [arg-type]
# main.py:189: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
# Found 2 errors in 1 file (checked 1 source file)


# iterables 

st = {1,4,5,5,6}

for i in st:
    print(i, end = " ")
print("\n")

# generator
    # uses yield keyword instead of return
    # it stores the value instead of returning
def simple_fn(limit):
    count = 0
    while(count <= limit):
        yield count
        count += 1

variable = simple_fn(5)
print(next(variable))
print(next(variable))
print(next(variable))
print(next(variable))
print(next(variable))
print(next(variable))

    
squares_list_comprehension = [x*x for x in range(5)]
print(squares_list_comprehension)

squares_generator_expression = (x*x for x in range(5))
print(next(squares_generator_expression))
print(next(squares_generator_expression))
print(next(squares_generator_expression))
print(next(squares_generator_expression))
print(next(squares_generator_expression))


# map -> applies a function to every item in an iterable,    returns a map object

numbers = [3,5,7]
squares = map(lambda x: x*x, numbers) 

print(list(squares))

# filter -> keeps the item that match the condition,   returns a filter object

num = [1,2,3,4,5,6,7]
evenNumbers = filter(lambda x: x%2 == 0, num)
print(list(evenNumbers))

# reduce -> combines all the items into a single value, we need to import it from functools,    returns a single value

from functools import reduce

num = [1,2,3,4,5]
summm = reduce(lambda a,b: a+b, num)
print(summm)

# closure -> a closure is a property of an inner function remember variables from outer function even when the outer function
# is finished execution...

# normally the local variables of a function is deleted... but in this case multiply needs
# factor variable to execute itself... hence python saves it for multiply function 

def multiplier(factor):
    def multiply(number):
        return number*factor
    return multiply

double = multiplier(2)
print(double.__closure__[0].cell_contents) # code to see saved variable
print(double(10))


# timer function using decorator, args and kwargs

# import time
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



from functools import wraps
                # used so that __name__ remembers function's name and metadata
def my_decorator(func):
    @wraps
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def greet(name):
    """This function greets the user."""
    print(f"Hello {name}")

print(greet.__doc__)
greet("Nitish")
print(f"function name is {greet.__name__}")


# class decorators -> it takes the function that takes a class, modifies it and returns it

def add_greetings(cls):
    cls.greet = lambda self: "Hello from decorated class"
    return cls

@add_greetings
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Nitish")
print(student.name)
print(student.greet())

# introspection -> means inspecting an object at runtime
        # python allows us to check what attributes and methods an object has

class Student:
    school = "CGC"

    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"My name is {self.name}")

student = Student("Nitish")

print(dir(student))
print(getattr(student, "name"))
print(getattr(student, "age", "Age not found"))
setattr(student, "age", 23)

print(student.age)

print(hasattr(student, "name"))