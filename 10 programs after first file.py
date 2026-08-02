#count vowels in a string...
"""
sentence=input("Write your sentence: ")
vowels='aeiouAEIOU'
count=0
count=sum(2 for char in sentence if char in vowels)


x=int(input("Enter a number: "))
if (x<=2):
    print(f"Number {x} is a prime number.")
else:
    for i in range(2, x):
        if x%i==0:
            print(f"Number {x} is not a prime number")
            break
    else:
        print(f"Nummber {x} is a prime number.")


#square with stars
f='y'
while(f=='y'):
    num=int(input("Enter the width of the square: "))
    for i in range(num):
        for num2 in range(num):
            print("x ", end="")
        print("")
    f=input("Do you want to print another square? (y/n)")

#triangle with stars
f='y'
while(f=='y'):
    num=int(input("Enter the width of the triangle: "))
    for i in range(num):
        for num2 in range(i+1):
            print("x ", end="")
        print("")
    f=input("Do you want to print another square? (y/n)")

#triangle of numbers
f='y'
while(f=='y'):
    num=int(input("Enter the width of the triangle: "))
    for i in range(num):
        for num2 in range(i+1):
            print(f"{num2+1} ", end="")
        print("")
    f=input("Do you want to print another triangle? (y/n)")

#reverse triangle
f='y'
while(f=='y'):
    num=int(input("Enter the width of the triangle: "))
    for i in range(num):
        for num2 in range(num-i):
            print("x ", end="")
        print("")
    f=input("Do you want to print another triangle? (y/n)")

#pyramid
f='y'
while(f=='y'):
    num=int(input("Enter the width of the triangle: "))
    for i in range(num):
        for num2 in range(num):
            if num2<num-i-1:
                print(" ", end="")
            else:
                print("x ", end="")
        print("")
    f=input("Do you want to print another triangle? (y/n)")

f='y'
while(f=='y'):
    n=int(input("Enter the width of the pyramid: "))
    for i in range(1, n+1):
        print(" "*(n-i) + "x "*i)
    f=input("Do you want to print more? y/n: ")


f='y'
while(f=='y'):
    n=int(input("Enter the width of triangle: "))
    for i in range(n):
        print(" "*i + "x "*(n-i))
    f=input("Do you want ot print more? y/n: ")


f='y'
while(f=='y'):
    n=int(input("Enter the number: "))
    c=1
    for i in range(n):
        for j in range(i+1):
            print(f"{c} ", end="")
            c+=1
        print("")
    f=input("Do you want to pirnt more? y/n : ")


f='y'
while(f=='y'):
    n=int(input("Enter the width of the diamond: "))
    for i in range(1, n*2):
        if i<=n:
            print(" "*(n-i) + "x "*i)
        else:
            print(" "*(i-n)+"x "*(n*2-i))
    f=input("Do you wnat ot print more?: ")
"""

f='y'
while(f=='y'):
    n=int(input("Enter the width of the diamond: "))
    for i in range(1, n+1):
        if i==1 or i==n:
            print("x "*n)
        else:
            print("x "+"  "*(n-2)+"x ")
    f=input("Do you wnat ot print more?: ")