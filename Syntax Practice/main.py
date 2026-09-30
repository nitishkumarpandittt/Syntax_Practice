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