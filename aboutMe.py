"""
Name: aboutMe.py
Author: Tiyler Lynum 
Purpose: Create a program that asks basic personal questions. 
"""

firstName = str(input("What is your First Name?"))
lastName = str(input("What is your Last Name?"))
age = int(input("How old are you?"))
graduatingClass = str(input("When are you graduating?"))
hobby = str(input(" What are your hobbies?"))
relationshipStatus = str(input("Are you single, dating, in a relationship, or married?"))
car = str(input("What kind of car do you have?"))
print ("Hello. Your name is,",firstName+lastName,".""You are",age,"years old." "You are graduating in",graduatingClass,"and have",hobby,"as hobbies.""You are",relationshipStatus,"and drive a",car,".")
