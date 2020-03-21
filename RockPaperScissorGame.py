import random

# Exercise 6 : Rock Paper Scissor Game

print("This is a rock paper scissor game.")
print("""Rules:-
            Rock >>> Scissor         
            Scissor >>> Paper
            Paper >>> Rock""")
lst = ['r','p','s']
Your_Point = 0
Computer_Point = 0
No_Of_Chances = 0
Turns = 10          # Use input function if you want the computer to ask for turns. 
while No_Of_Chances<Turns:
    inp= input(""" Choose:- 
                (r)Rock
                (p)Paper
                (s)Scissor \nEnter:-""" )
    
    rand = random.choice(lst)    #For Genrating random number

    if inp == rand :
        print("This is tie, 0 point to each.")
    
    # If User Enter S (Scissor.) 
    elif inp=="s" and rand=="r":
        Computer_Point = Computer_Point + 1
        print(f"You choose:- {inp} computer choose:- {rand} \n ")
        print("Computer wins 1 Point.")
        print(F"Computer point:- {Computer_Point} \nYour point:- {Your_Point} \n")
    elif inp=="s" and rand=="p":
        Your_Point = Your_Point + 1
        print(f"You choose:- {inp} computer choose:- {rand} \n ")
        print("you wins 1 Point.")
        print(F"Computer point:- {Computer_Point} \nYour point:- {Your_Point} \n")
    
    # If User Enter R (Rock.)
    elif inp=="r" and rand=="p":
        Computer_Point = Computer_Point + 1
        print(f"You choose:- {inp} computer choose:- {rand} \n ")
        print("Computer wins 1 Point.")
        print(F"Computer point:- {Computer_Point} \nYour point:- {Your_Point} \n")
    elif inp=="r" and rand=="s":
        Your_Point = Your_Point + 1
        print(f"You choose:- {inp} computer choose:- {rand} \n ")
        print("you wins 1 Point.")
        print(F"Computer point:- {Computer_Point} \nYour point:- {Your_Point} \n")
    
    # If User Enter P (Paper.)
    elif inp=="p" and rand=="s":
        Computer_Point = Computer_Point + 1
        print(f"You choose:- {inp} computer choose:- {rand} \n ")
        print("Computer wins 1 Point.")
        print(F"Computer point:- {Computer_Point} \nYour point:- {Your_Point} \n")
    elif inp=="s" and rand=="r":
        Your_Point = Your_Point + 1
        print(f"You choose:- {inp} computer choose:- {rand} \n ")
        print("you wins 1 Point.")
        print(F"Computer point:- {Computer_Point} \nYour point:- {Your_Point} \n")
    else:
        print("Sorry! You enter a Wrong Input")
    
    No_Of_Chances = No_Of_Chances + 1
    print(f"{Turns - No_Of_Chances} Chances left out of {Turns}. \n")

print("Game Over")

if Computer_Point == Your_Point:
    print("Its a Tie.")
elif Computer_Point > Your_Point:
    print("Computer Wins.")
else:
    print("You Win.") 
print(f"Score Board: \nComputer Points:-{Computer_Point}\nYour Points:-{Your_Point}")


