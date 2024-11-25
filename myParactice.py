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

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#Fibbonacci sequence

sum=0
for fs in range(1,20,1):
    sum=fs+sum
    print(sum)

