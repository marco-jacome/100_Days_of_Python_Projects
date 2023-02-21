"""
*******************************************************************************
Date: 02/20/2023
Programmer: Marco Jacome
Project: Treasure Island Game
*******************************************************************************
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')



game_over = ' Game Over.'
right = 'Fall into a hole!'
swim ='Attacked by trout!'
red = 'Burned by fire!'
blue = 'Eaten by beasts!'
win = 'You Win!'

#Game start
print("Welcome to Treasure Island Game.")
print("Your mission is to find the treasure. ")
print("Choose the way you want to go to find the treasure.")


#Stage 1
#Get user Direction
direction = input("Left(L),right(R), or Enter any letter to quit: ")
if direction == 'L':
    
    #Stage 2:Get user Action 
    action = input("Choose to swim or to wait. Swim(S), wait(W), or Enter any letter to quit: ")
    
    
    if action == "W":
        # Get user Color
        color = input("Which color door will you choose? Red(R), Blue(B), Yellow(Y), or Enter any letter to quit: ")
        
            
        if color  == "Y":
            #Win!
            print(win)
            
        elif color == "R":
              #game over
              print(red + game_over)
              
        elif color == "B":
              #game over
              print(blue + game_over)
        
        else:
            #Game over
            print(game_over)
    else:
        #game over    
        print(swim + game_over)
else:
 #game over
 print(right + game_over)