print("New file")
# print("Hellow how are \"hehha\"\ you")
# print("Hy",8,9,sep="~",end="--")
# print("yes")
# print(15/3)
# print(15//3)
# print(17%3)
# print(2**70)

#Calculator

# value_one=int(input("Enter First value : "))
# value_two=int(input("Enter Second value : "))

# print(f"Sum of {value_one} and {value_two} is = ",value_one+value_two)
# print(f"Multiplication of {value_one} and {value_two} is = ",value_one*value_two)
# print(f"Division of {value_one} and {value_two} is = ",value_one/value_two)

#Type Casting

# c=1.1
# d=9
# print(c+d)

# Exercise

# import time
# timestamp=time.strftime('%H:%M:%S')
# print('Current Time ::',timestamp)
# Hour=int(time.strftime('%H'))
# Minute=int(time.strftime('%M'))
# Second=int(time.strftime('%S'))

# if 5<=Hour<12:
#     print('Good Morning')
# elif 12 <= Hour < 17:
#     print('Good Afternoon')
# elif 17 <= Hour < 21:
#     print('Good Evening')
# else:
#     print('Good Night')

#Match Case in Python

# x=int(input('Enter any number between 1 to 5 :'))

# match x:
#     case 0:
#         print(x,' The number you enter is  zero')
#     case 1:
#         print(x, 'The number you enter is  one')
#     case 2:
#         print(x, 'The number you enter is  two')
#     case 3:
#         print(x, 'The number you enter is  three')
#     case 4:
#         print(x, 'The number you enter is  four')
#     case 5:
#         print(x, 'The number you enter is  five')
#     case _:
#         print(x,' The number does not lies between 1 to 5')

#For Loop in python

# colors=["Red","Blue","Green","Purple"]

# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for each in range(1,11):
#     print(each)

#Range with difference

# for even in range(0,101,2):
#     print(even)

# for odd in range(1,100,2):
#     print(odd)

#While Loop
# i=0
# while i<5:
#     print(i)
#     i=i+1

#Break and Continue

# for x in range(1,21):
#     print("5 x ",x ,"=",5*x)
#     if (x==10):
#         break

# for y in range(1,21):
#     if (y==10):
#         print("10 is here")
#         continue
#     print("4 x ",y ,"=",4*y)

#Function

#if you want to define function body latter then you write pass in function body

# def calculateGemMean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)

# calculateGemMean(50,10)

#Dictionary and tuple type in function argument

#Tuple

# def average(*number):
#     print(type(number))
#     sum=0
#     for i in number:
#         sum=sum+i
#     print("Average is ",sum/len(number))

# average(5,4,3)

# def name(**name):
#     print(type(name))
#     print("Hello ",name["fname"],name['mname'],name["lname"])

# name(fname="Ali",mname="Ahmed",lname="Khan")

#List in Python

# list=[4,9,8,4,3,1,3,2,8]
# print(list)
# print(list[0])
# for i in list:
#     print(i)
# print(len(list))
# #for negavtive index it would be len(list) minus negative index in our case length is 3 and -1 it gives 2 so on -1 we get 8
# print(list[-1])

# #in keyword with if condition , same thing apply for string also

# if 19 in list:
#     print("Yes")
# else:
#     print("No")

# print(list[1:9:2])

#list method

# myList=[1,23,1,2,3,2,14]
# print(myList)
# myList.append(7)
# myList.reverse()
# print(myList)

# secondlist=myList
# secondlist[0]=100
# print(myList)

# #the upper methods change the orignal list recommended to use .copy function

# thirdlist=myList.copy()
# thirdlist[0]=90
# thirdlist.insert(3,9000)
# thirdlist.extend(secondlist)
# merge=thirdlist+myList+secondlist
# print(merge)
# print(thirdlist)

#Tuple

#tuple are not editable or change able

# tup=(12,22,221)
# count=tup.count(12)
# print(count)
# print(tup)

#String formating in python

# name="Ali"
# country="Pakistan"
# price=2.2220303

# print(f"My name is {name} and i am form {country}")
# print(f"My name is {name} and i am form {country}, in my country the price of meet is {price:.2f}")

#doc string method

# def square(n):
#     '''Take n and print squares of it'''
#     print(n**2)

# square(5)

# print(square.__doc__)

#Factorial Recursion

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

#Fibbonacci sequence
# def fibonacci_recursive(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# n = 10
# for i in range(n):
#     print(fibonacci_recursive(i), end=" ")

#set in python and its method

# s1={2,1,3,4,32,12,1,2,5}
# s2={12,11,32,14,1,12,51}
# print(s1)
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# s3=s1.symmetric_difference(s2)
# print(s3)

#Dictionary

# disc={
#     "Ali":"is a good boy",
#     "Jhelum":"Is my Home Town",
# }

# print(disc["Ali"])

# for key in disc.keys():
#     print(f"The Value of key {key} is {disc[key]}")

#Set unordered disctionary ordered

#For lopp with else in python

# for i in range(5):
#     print(i)
#     if i==3:
#         break
# else:
#     print('Loop break')

#Error Handling in Python

# a=input("Enter number for table : ")
# print(f"Multiplication of table {a} is : ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
    
# print("Out of program")

#Finally Keyword

# try:
#     l=[1,5,7,8]
#     i=int(input("Enter index : "))
#     print(l[i])
# except:
#     print("Some Error Occur")
# finally:
#     print("I am always executed")

#Custom Error
# num=int(input("Enter and number less than 3 or greater than 12 : "))

# if 3<= num <= 12:
#     raise ValueError("Value Should be not in range")

#Encryption Exercise

# def encryDeycry():
#     msg=input("Enter your message : ")

#     def decryption(msg):
#         msg_length=len(msg)
#         if msg_length<=3:
#             reverse_msg=msg[::-1]
#             print(reverse_msg)
#             encryDeycry()

#         elif 3< msg_length <=7:
#             format_msg=msg[1:-1]
#             reverse_msg=format_msg[::-1]
#             print(reverse_msg)
#             encryDeycry()

#         elif 8<= msg_length <=20:
#             format_msg=msg[3:-3]
#             reverse_msg=format_msg[::-1]
#             print(reverse_msg)
#             encryDeycry()

#     decryption(msg)

# encryDeycry()

#Short Hand Expression

# a=200
# b=30

# c=9 if a>b else 2

# print(c)

#Enumerate Function in Python to get index also

# marks=[12,13,14,11,21,323,232,112,55,343]

# for index,mark in enumerate(marks):
#     print(f"At index {index} is {mark}")

#Virtual Environment in Python
#python -m venv myenv
#How to Activate this virtual environment
#myenv/Scripts/activate
#How to disclose or deactivate virtual environment
#exit()
#How to get list of all packages in virtual environment
#pip freeze
#pip freeze > requirements.txt
#How to activate all virtual environment packages in our virtual environment
#pip freeze -r requirements.txt
#It activate all packagesin our virtual environment

# import math
# floatnum=math.floor(4.0909)
# squareroot=math.floor(math.sqrt(81))
# print(squareroot)
# print(floatnum)
# # print(dir(math))

# # from paractice import welcome, otherfile
# import paractice

# print(paractice.welcome())
# print(paractice.otherfile)


# import os

# if(not os.path.exists("PythonData")):
#     os.mkdir("PythonData")
# for i in range (1,100):
#     os.mkdir(f"PythonData/Day{i}")
#list
#folders=os.listdir("PythonData")
# for i in range (1,100):
#     os.rename(f"PythonData/Day{i}",f"Tutorial {i}")
file=open('myfile.txt','w')
text=file.write("Yes yo do it")
print(text)
file.close()