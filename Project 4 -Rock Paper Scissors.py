"""
*******************************************************************************
Date: 
Programmer: Marco Jacome
Title: Exercise # - Name

Description: Write a game for Rock, Paper, Scissors

Rules
 - rock beats scissors
 - paper beats rock
 - scissors beats paper
*******************************************************************************
"""

# ASCII Art for Rock Paper Scissors
r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
'''

choice = [r, p, s]
"""Write your code below this line 👇"""

#Import required modules 
import random

# Initialize Rock, paper and scissors 
rock = 0
paper = 1
scissors = 2

# Prompt welcome to user
print("Welcome to Rock, Paper, Scissors game!")


# Get User Input
usr = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.👉 "))
usr_choice = choice[usr]
print(f"{usr_choice}")

# Get computer input from generated random integer(0-2)
cpu = random.randint(0,2)
cpu_choice = choice[cpu]
print(f"Computer chose: {cpu_choice}")


# Create nested list of user outcomes
"""....cpu col   rock           , paper            , scissors           """
"""            ------------------------------------------------------ """
usr_rock =     ["tied with cpu.", "lose."          ,"win!"          ]
usr_paper =    ["win!"          , "tied with cpu." ,"lose."         ]
usr_scissor =  ["lose."         , "win!"           ,"tied with cpu."]

match_outcomes = [usr_rock, usr_paper, usr_scissor]
results = match_outcomes[usr][cpu]
print(f"You {results}")













































