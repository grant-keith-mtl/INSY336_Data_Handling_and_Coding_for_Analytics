# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import seed
from random import randint

#Part 1
print("Part 1")

#seeding the random functions
seed(1)

#getting user answer and validating input

while True:
    try:
        userInput = input("Rock, Paper, or Scissors?: ")
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if userInput!=("Rock"or"Paper"or"Scissors"):
        print("Sorry, that is not a valid answer!")
        continue
    else:
        break
print("You entered: ",userInput)

#function to get random computer answer
def computerAnswer():
    computerAnswer = randint(0,2)
    if computerAnswer==0:
        computerChose = "Rock"
        print("Computer chose: ", computerChose)
    elif computerAnswer==1:
        computerChose = "Paper"
        print("Computer chose: ", computerChose)
    else:
        computerChose = "Scissors"
        print("Computer chose: ", computerChose)
    return computerChose

#function to see who won
def winner(userInput,computerAnswer):
    if userInput=="Rock":
        if computerAnswer=="Rock":
            print("The User and Computer both chose Rock. This game is a Tie.")
        elif computerAnswer=="Paper":
            print("The User chose Rock and the Computer chose Paper. The Computer Wins!")
        else:
            print("The User chose Rock and the Computer chose Scissors. The User Wins!")       
    elif userInput=="Paper":
        if computerAnswer=="Rock":
            print("The User chose Paper and the Computer chose Rock. The User Wins!")
        elif computerAnswer=="Paper":
            print("The User and Computer both chose Paper. This gmame is a Tie.")
        else:
            print("The User chose Paper and the Computer chose Scissors. The Computer Wins!")
    else:
        if computerAnswer=="Rock":
            print("The User chose Scissors and the Computer chose Rock. The Computer Wins!")
        elif computerAnswer=="Paper":
            print("The User chose Scissors and the Computer chose Paper. The User Wins!")
        else:
            print("The User and Computer both chose Rock. This gmame is a Tie.")

#Running functions
winner(userInput,computerAnswer())

#Part 2
print("Part 2")

#While Loops
print("While Loops")
#First One
print("First Loop")
x = 1
while x<10:
    print("x = ",x)
    x+=2

#Second One
print("Second Loop")
x = 9
while x>0:
    print("x = ",x)
    x-=2

#Third One
print("Third Loop")
x = 1
sum = 0
while x<10:
    sum+=x
    x+=2
print("sum = ",sum)

#For Loops
print("For Loops")

#First Loop
print("First Loop")
for i in range(1,10,2):
    print("i = ",i)

#Second Loop
print("Second Loop")
for i in range(9,0,-2):
    print("i = ",i)
    
#Third Loop
print("Third Loop")
sum = 0
for i in range(1,10,2):
    sum+=i
print("Sum = ",sum)
























