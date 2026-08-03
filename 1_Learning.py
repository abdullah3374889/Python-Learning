# """print("hello world")
# name="Abdullah"
# age=23
# height=1.70
# male=True

# complexnum=2+3j

# print(len(name))
# name=name.upper()
# print(name[0:5])

# print(name,height)
# print(name.removeprefix("AB"))

# print(type(name))
# a=int(height)
# print(a)

# print(5//2)
# print(5**2)
# if(("H" in name) and ("P" not in name)):
#     print("han hai")

# x=int(input("Enter the number: "))
# print(f"My name is {name} and I am {age} years old. and i wrote the nubmer {x}.")
# print("My name is {} and I am {} years old.".format(name, age))
# print("My name is {0} and I am {1} years old. {0} likes coding.".format(name, age))
# print("Name: {n}, Age: {a}".format(n=name, a=age))

# #for variabel in sequece
# #for y in range(10):
# for y in range(0,10):
#     print(f"This is {y}")
# i=0
# while(i<10):
#     print(f"This is {i}")
#     i+=1
# # break continue pass=> does nothing
# # range(start, stop, step)

# try:
#     d=int(input("Enter your age: "))
#     print(f"you entered {d}")
# except ValueError:
#     print("You have not entered an integer.")
# else:
#     print("Good Job!")
# finally:
#     print("Execution finished")
#     """

# # a=int(223)
# # b="Abdullah"
# # c=2+3j
# # d=float(2.234)

# # friend=["hamamd", "Abdullah", "hassaan"]                            #"""its a list"""
# # ages=(23, 34, 33, 34, 33)                                                   #"""its a tuple"""
# # hammaad={"name": "hammad", "age": "24", "degree": "BSCS"}           #"""Dictionary"""
# # hammadyears = {2021, 2022, 2022, 2023}                                    #"""set"""

# # print(friend)
# # print(ages)
# # print(hammaad)
# # print(hammadyears)

# # friend.append("Bilal")
# # friend[0]="madu"
# # del friend[1]
# # friend.remove("hassaan")

# # hammaad["city"]="Mandi Bahauddin"
# # hammaad["age"]="21"
# # del hammaad["degree"]

# # hammadyears.add(323)
# # hammadyears.remove(2023)

# # print(friend)
# # print(ages)
# # print(hammaad)
# # print(hammadyears)


# for i in range (1,11):
#     print(f"5 X {i} = {5*i}")

# sum=int(0)
# for i in range (101):
#     sum=sum+i
# print(sum)

# fact=int(1)
# for i in range(5, 1, -1):
#     fact=fact*i
# print(fact)

# vowels=["a", 'e', 'i', 'o', 'u']
# sentence=input("Enter the sentence: ")
# vow=0
# i=len(sentence)
# for char in sentence:
#     if char in vowels:
#         vow+=1
# print(vow)


# string=input("Enter: ")
# reverse=""
# for char in string:
#     reverse=char + reverse
# print(reverse)

# or

# string=input("Enter: ")
# reverse=string[::-1]
# print(reverse)

#print fibonacci series

# a=int(input("Enter a number: "))
# n1=0
# n2=1
# while(n1<a):
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3

#frequencies of characters in string

# string = input("Enter a string: ")
# freq = {}
# for char in string:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# print("Character Frequencies:")
# for char in freq:
#     print(char, ":", freq[char])


#STARS
#left pyramid

# a=int(input("Enter the number: "))
# for i in range(a+1):
#     for j in range(i):
#         print("*", end="")
#     print()
# #or
# for i in range(a):
#     print(f'{"x "*(i+1)}')

#inverted left pyramid
# for i in range(a):
#     j=a-i
#     for h in range(j):
#         print("x", end="")
#     print()


#right pyramid
# for i in range(a):
#     print(f"{"  "*(a-i-1)}{"x "*(i+1)}")

#Full pyramid
# for i in range(a):
#     print(f'{" "*(a-i-1)}{"x"*(i*2+1)}')

#diamond
# for i in range(a*2-1): 
#     if(i<a):
#         print(f'{" "*(a-i-1)}{"x"*(i*2+1)}')
#     else:
#         print(f'{" "*(i-a+1)}{"x"*((a*2)-(i-a)*2-3)}')

#hollow square
# for i in range(a):
#     if(i==0 or (i+1)==a):
#         print(f'{"x "*a}')
#     else:
#         print(f'{"x "}{"  "*(a-2)}{"x"}')

#butterfly
# for i in range(a*2):
#     if(i<a):
#         print(f'{"*"*(i+1)}{"  "*(a-i-1)}{"*"*(i+1)}')
#     else:
#         print(f'{"*"*((a*2)-(i+1))}{"  "*(i-a+1)}{"*"*((a*2)-(i+1))}')
#or we can divide upper and lower parts
# for i in range(a):
#     print(f'{"x"*(i+1)}{"  "*(a-i-1)}{"x"*(i+1)}')
# for i in range(a, 1, -1):
#     print(f'{"x"*(i-1)}{"  "*(a-i+1)}{"x"*(i-1)}')

# def func1(a):
#     print(f"Hello {a}")

# func1("Alice")
# func1("Bob")
# func1("Charlie")

# create a funcition that calcualte the factorial of a number

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range (2, n + 1):
#             result *= i
#         return result

# a = int(input("Enter a number to calculate its factorial: "))
# print(f"Factorial of {a} is {factorial(a)}.")


# Create a function that counts the vowels in a string.
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

#student record system using class


# class Student:
#     def __init__(self, name, age, roll_number):
#         self.name = name
#         self.age = age
#         self.roll_number = roll_number

#     def display_info(self):
#         return f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}"


# s1 = Student("Alice", 20, "A001")
# s2 = Student("Bob", 21, "A002")
# s3 = Student("Charlie", 19, "A003")


# print(s1.display_info())
# print(s1.age)


# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def average(self):
#         return (self.m1 + self.m2 + self.m3) / 3

# s1 = Student("Alice", 85, 90, 78)
# print(f"{s1.name}'s average marks: {s1.average():.4f}")




# class Student:
#     @staticmethod
#     def hello():
#         print("Hello from the Student class!")

#     def welcome(self):
#         print("Welcome to the Student Record System!")

# s1 = Student()
# s1.welcome()

# s1.hello()
# Student.hello()  # Calling the static method directly from the class





# Inheritance
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"Car: {self.year} {self.make} {self.model}"

# class Toyota(Car):
#     def __init__(self, name):
#         print("Toyota class constructor called with name: ", name)

# c1 = Toyota("Corolla")
# c1.make = "Toyota"
# c1.model = "Corolla"
# c1.year = 2020
# print(c1.display_info())





f = open("sample.txt", "r")
data = f.read()
print(data)