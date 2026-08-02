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

a=int(input("Enter the number: "))
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
for i in range(a):
    print(f'{"x"*(i+1)}{"  "*(a-i-1)}{"x"*(i+1)}')
for i in range(a, 1, -1):
    print(f'{"x"*(i-1)}{"  "*(a-i+1)}{"x"*(i-1)}')

print("hello world")

print ("Alpha beta gamaam")
for y in range(100):
    print(y)


for x in range(10013):
    print(x)