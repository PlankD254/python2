#input in python
#Python uses the function input() to capture adn store input in the application

from traceback import print_tb


print("User profile Applcation")

first_name=input("First Name: ")
Last_name=input("Last Name:"  ) 
occupation=input("What do you do? : ")

#print("Your fisrt name is "+ first_name)
#print("Your last name is "+ Last_name)
#print("What do you do? "+ occupation)

#Another way of outputng information in pyhon is through formats and strings
print(f"Your first name is {first_name} and your job is {occupation} ")
#Handling  non-string input
age=int(input("Please enter your age: " ))

print(f"In two years, your ages will be {age + 2} ")
