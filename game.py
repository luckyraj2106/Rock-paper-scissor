import random
"""
rock = 0
paper = 1
scissor =-1

"""
computer = random.choice([0,1,-1])
youstr = input("enter your choice : ")
yourDict = {"R": 0 , "P": 1 , "S" : -1 }
reverseDict = {0:"rock", 1:"paper" , -1:"scissor"}

if youstr not in yourDict:
    print("Invalid input. Please enter R, P, or S.")
    exit()

you = yourDict[youstr]

print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == 0 and you == 1):
        print("you win!!")
        
    elif(computer == 0 and you == -1):
        print("you lose!!")
    
    elif(computer == 1 and you == -1):
        print("You win!!")

    elif(computer == 1 and you == 0):
        print("you lose!!")

    elif(computer == -1 and you == 0):
        print("You win!!")

    elif(computer == -1 and you == 1):
        print("You lose!!")

    else :
        print("something went wrong")