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

colors=["Red","Blue","Green","Purple"]

for color in colors:
    print(color)
    for i in color:
        print(i)

for each in range(1,11):
    print(each)

#Range with difference

for even in range(0,101,2):
    print(even)

for odd in range(1,100,2):
    print(odd)