import random
# Main Menu
print("Press 0 for SinglePlayer(Bot)")
print("Press 1 for Two Players")
S1 = 0 # initial player1 score
S2 = 0 # initial player2 score
userinput = int(input("Chose: "))
print("")
# Main Game Loop (Singleplayer)
if (userinput == 0):
    player = input("Player Name: ")
    player1 = player.capitalize()
    player2 = str("Computer")
    print("")
    while True:
        a = input(f"{player1} {S1}, Snake/Water/Gun: ")
        if(a.upper() == "E"):
            exit()
        b = random.randint(0,2)
        if(b == 0):
            b = str("Snake")
        if(b == 1):
            b = str("Water")
        if(b == 2):
            b = str("Gun")
        print("Computer Chose", b)
        if(a.lower() == b.lower()):
            print("Draw!!")
            print(f"Score = {S1}")
        elif(a.capitalize() == "Snake" and b.capitalize() == "Water"):
            print(f"{player1} Won!!")
            S1 = S1 + 1
            print(f"Score = {S1}")
        elif(a.lower() == "snake" and b.lower() == "gun"):
            print(f"{player2} Won!!")
            if(S1 != 0):
                S1 = S1 - 1
            print(f"Score = {S1}")
        elif(a.capitalize() == "Water" and b.capitalize() == "Gun"):
            print(f"{player1} Won!!")
            S1 = S1 + 1
            print(f"Score = {S1}")
        elif(a.lower() == "water" and b.lower() == "snake"):
            print(f"{player2} Won!!")
            if(S1 != 0):
                S1 = S1 - 1
            print(f"Score = {S1}")
        elif(a.capitalize() == "Gun" and b.capitalize() == "Snake"):
            print(f"{player1} Won!!")
            S1 = S1 + 1
            print(f"Score = {S1}")
        elif(a.lower() == "gun" and b.lower() == "water"):
            print(f"{player2} Won!!")
            if(S1 != 0):
                S1 = S1 - 1
            print(f"Score = {S1}")
        else:
            print("Invalid Entries!!")
        wait = input()
# Main Game Loop (Two Players)
if (userinput == 1):
    player1 = input("Player 1: ").capitalize()
    player2 = input("Player 2: ").capitalize()
    print("")
    while True:
        a = input(f"{player1} {S1}, Snake/Water/Gun: ")
        if(a.upper() == "E"):
            exit()
        b = input(f"{player2} {S2}, Snake/Water/Gun: ")
        if(b.lower() == "e"):
            exit()
        if(a.lower() == b.lower()):
            print("Draw!!")
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        elif(a.capitalize() == "Snake" and b.capitalize() == "Water"):
            print(f"{player1} Won!!")
            S1 = S1 + 1
            if(S2 != 0):
                S2 = S2 - 1
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        elif(a.lower() == "snake" and b.lower() == "gun"):
            print(f"{player2} Won!!")
            S2 = S2 + 1
            if(S1 != 0):
                S1 = S1 - 1
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        elif(a.capitalize() == "Water" and b.capitalize() == "Gun"):
            print(f"{player1} Won!!")
            S1 = S1 + 1
            if(S2 != 0):
                S2 = S2 - 1
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        elif(a.lower() == "water" and b.lower() == "snake"):
            print(f"{player2} Won!!")
            S2 = S2 + 1
            if(S1 != 0):
                S1 = S1 - 1
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        elif(a.capitalize() == "Gun" and b.capitalize() == "Snake"):
            print(f"{player1} Won!!")
            S1 = S1 + 1
            if(S2 != 0):
                S2 = S2 - 1
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        elif(a.lower() == "gun" and b.lower() == "water"):
            print(f"{player2} Won!!")
            S2 = S2 + 1
            if(S1 != 0):
                S1 = S1 - 1
            print(f"{player1} = {S1}")
            print(f"{player2} = {S2}")
        else:
            print("Invalid Entries!!")
        wait = input()