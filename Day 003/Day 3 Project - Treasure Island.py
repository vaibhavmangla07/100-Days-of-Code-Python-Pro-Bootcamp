print(''' _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
                                       
                                       ''')

print("Welcome to Treasure Island.\n"
      "Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()

if(choice1 == "left"):
    choice2 = input("You've come to a lake. There is an island in the middle of the lake."
                    'Type\' "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if(choice2 == "wait"):
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors."
                        'One "red", one "yellow" and one "blue". Which colour do you choose?\n')
        if(choice3 == "red"):
            print("It's a room full of fire. Game Over!.")
        elif(choice3 == "yellow"):
            print("You found the treasure! You Win!")
        elif(choice3 == "blue"):
            print("You enter a room of beasts. Game Over!.")
        else:
            print("Wrong Input. Game Over!")
    else:
        print("You got attacked by angry trout. Game Over!")
else:
    print("You fell in hole. GAME OVER!")