
"""
*******************************************************************************
Date: 02/15/2023
Programmer: Marco Jacome
Title:Project 2 - Tip Calculator

Description:

Create a program to calculate the tip for a bill based on user input, and

select the tip amount.


example:
--------    
if the bill was $150.00, split between  5 people, with 12% tip each

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Tip: There are 2 ways to round a number. You might have to do some Googling 

to solve this.💪

Write your code below this line 👇
*******************************************************************************
"""
# 1. Print title
print("Welcome to the tip calculator!")
print("------------------------------")

# 2. Get user input 
usr_total = input("What is the total bill? ..... $")
usr_tip = input("Select tip percentage of 10%, 12%. or 15% ...... %")
usr_people = input("How many people to split the bill? ...... ")

# 3. Convert user input to integer
total = float(usr_total)
tip_percent = float(usr_tip)/100
people = float(usr_people)

# 4. Calculate each person's payment with tip
payment_float = (total/people)*(1 + tip_percent)
payment = round(payment_float)

# 5. Display payment for each person with proper formating specifier 
print(f"\nEach person should pay: ${payment:0.2f}")

