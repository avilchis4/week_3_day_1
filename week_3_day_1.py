# # # # Week3
# # # # This week we will work on :
# # # # Working With Strings


# # # # 1.   Working With Numbers
# # # # 2.   Getting Input From Users




# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game










# # Review
# create variables for the following :
# 1. age
age = 25 #interger variable
# 2. name
name = "John" #string variable
# 3. song
song = "happy birthday" #string variable
# 4. food
food = "apples" #string variables
# 5. number
number = 1000 #integer variables


# #now include the variables you just made print in the following...


# Once upon a time, there was a [age] old coder named [name].
#concatnation -- + signs around variables
print ("Once upon a time, there was a " + str(age) + " old coder named " + name + ".")
print ("There was a " + str(number) + " as well.")
# age and number in a sentence
print ("He is " + str(age) + " and has " + str(number) + ".")

date_of_birth = 2021
number2 = 123
number3 = 123.456
number4 = 123.33
number5 = 4555

print ("In " + str(date_of_birth) + " there were " + str(number2) + " babies born on September 10th and " + str(number5) + " babies born on September 9th. ")
print (f"The date of birth is {date_of_birth} and the number is {number2} and the number is {number3} and the number is {number4} and the number is {number5}. ")

# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
print (f"{name} like to hum the {song} while coding. It was so annoying that their teammates would throw {food} until {name} would stop singing. ")

# last_name
# email_address
# percent
# variable_name
# zero
# list # this is a keyword in python
# creating valid names

#addition
print (2+1)
#multiplication
print (2*2)
#division
print (6/2)
#modulo
print (7%4) # remainder of 7 divided by 4
# powers
print (2**3) # 2 to the power of 3
# # # get max and min number
print ("the max of 2 and 3 is",max (2,3))
print ("the min of 2 and 3 is",min (2,3))
#round a number
print ("round 3.9 is", round (3.9))
#absolute value means distance from zero
print ("the absolute value of -3 is",abs(-3))
#its always positive 
#order of operations
print ("2 + 10 * 10 + 3 is", (2 + 10 * 10 + 3))

# to do more you need special import from math library

from math import *

# floor method
print ("the floor of 3.7 is", floor(3.7))
#floor means round down
#ceil method
print("the ceil of 3.7",ceil(3.7))
#ceil rounds up
print ("the floor of 8.2 is",floor(8.2))
print ("the ceil of 8.2 is",ceil(8.2))

#how do we get input from users
#input ("what is your name?")
name = input ("what is your name? ")
print ("hello", name)
#basic math calculator
#ask for 2 numbers
num1 = int(input ("enter a number "))
num2 = int(input ("enter a another number "))
#print out statement where you add them together
print (num1 + num2)
#multiply
print (num1 * num2)
#max number
print (max(num1, num2))
#find remainder
print (num1 % num2)
#round number
print (round(num1))

num1 = int(input ("type a number "))
num2 = int(input ("type another number "))

print (num1 - num2)
print (num1 / num2)
print (min,num1 - num2)
print (abs,num1 - num2)
print (floor,(num1))
print (ceil,(num1))
print (num1 ** num2)



