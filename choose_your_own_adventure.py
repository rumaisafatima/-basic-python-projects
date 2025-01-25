name = input("Type Your Name")
print("Welcome",name,"to this adventure")

answer =input("You have gone on a dirt road and you have reached the end of the road either you can go to the left or to the right.which way would you like to go?").lower()

if answer == "left":
    answer= input("You come to a  river,you can walk around it or swim across?Type swim to swim and walk to walk across: ")
    if answer =="swim":
        print("You swam across and were eaten by a dolphin. ")
    elif answer == "walk":
        print("You walked for many miles ,ran out of water and you lost the game.  ")
    else:
     print("Not a Valid Option,You Lose")        

elif answer == "right":
        answer= input("You come to a bridge,it looks wobbly ,do you want to cross it or head back (cross/back)?")
        if answer =="back":           
            print("you go back and you lose ")

        elif answer == "cross":
            answer = input("You cross the bridge and meet the stranger.Do you talk to them (yes/no)?")

            if answer =="yes":
                print("You tlak to the stranger and they give you the gold. YOU WIN !") 
            elif answer == "no":
                print("You ignore the stranger and they are offended.YOU LOSE !")
            else:
                print("Not a valid option,You Lose.")          
        else:
            print("Not a Valid Option,You Lose")    
else:
     print("Not a Valid Option,You Lose")        

print("THANK YOU FOR TRYING",name.upper())     

