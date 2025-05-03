import random

x = "1"  
points = 100  

while x == "1":
   
    dice1 = random.randint(1, 12)
    dice2 = random.randint(1, 12)
    roll = dice1 + dice2 

    
    points = points - 10

   
    print("You rolled", dice1, "and", dice2, ". Total:", roll)

    
    if dice1 == 1:
        print("+-----+")
        print("|     |")
        print("|  *  |")
        print("|     |")
        print("+-----+")

    if dice1 == 2:
        print("+-----+")
        print("| *   |")
        print("|     |")
        print("|   * |")
        print("+-----+")

    if dice1 == 3:
        print("+-----+")
        print("| *   |")
        print("|  *  |")
        print("|   * |")
        print("+-----+")

    if dice1 == 4:
        print("+-----+")
        print("| * * |")
        print("|     |")
        print("| * * |")
        print("+-----+")

    if dice1 == 5:
        print("+-----+")
        print("| * * |")
        print("|  *  |")
        print("| * * |")
        print("+-----+")

    if dice1 == 6:
        print("+-----+")
        print("| * * |")
        print("| * * |")
        print("| * * |")
        print("+-----+")

    if dice1 == 7:
        print("+-----+")
        print("| * * * |")
        print("|   *   |")
        print("| * * * |")
        print("+-----+")

    if dice1 == 8:
        print("+-----+")
        print("| * * * |")
        print("| *   * |")
        print("| * * * |")
        print("+-----+")

    if dice1 == 9:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("+-----+")

    if dice1 == 10:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("|   *   |")
        print("+-----+")

    if dice1 == 11:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("| *   * |")
        print("+-----+")

    if dice1 == 12:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("+-----+")

    
    if dice2 == 1:
        print("+-----+")
        print("|     |")
        print("|  *  |")
        print("|     |")
        print("+-----+")

    if dice2 == 2:
        print("+-----+")
        print("| *   |")
        print("|     |")
        print("|   * |")
        print("+-----+")

    if dice2 == 3:
        print("+-----+")
        print("| *   |")
        print("|  *  |")
        print("|   * |")
        print("+-----+")

    if dice2 == 4:
        print("+-----+")
        print("| * * |")
        print("|     |")
        print("| * * |")
        print("+-----+")

    if dice2 == 5:
        print("+-----+")
        print("| * * |")
        print("|  *  |")
        print("| * * |")
        print("+-----+")

    if dice2 == 6:
        print("+-----+")
        print("| * * |")
        print("| * * |")
        print("| * * |")
        print("+-----+")

    if dice2 == 7:
        print("+-----+")
        print("| * * * |")
        print("|   *   |")
        print("| * * * |")
        print("+-----+")

    if dice2 == 8:
        print("+-----+")
        print("| * * * |")
        print("| *   * |")
        print("| * * * |")
        print("+-----+")

    if dice2 == 9:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("+-----+")

    if dice2 == 10:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("|   *   |")
        print("+-----+")

    if dice2 == 11:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("| *   * |")
        print("+-----+")

    if dice2 == 12:
        print("+-----+")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
        print("+-----+")

    # Winnings using multiple if statements (NO dictionary)
    if roll == 2:
        winnings = 0
    if roll == 3:
        winnings = 2
    if roll == 4:
        winnings = 3
    if roll == 5:
        winnings = 5
    if roll == 6:
        winnings = 7
    if roll == 7:
        winnings = 10
    if roll == 8:
        winnings = 11
    if roll == 9:
        winnings = 13
    if roll == 10:
        winnings = 15
    if roll == 11:
        winnings = 17
    if roll == 12:
        winnings = 20
    if roll > 12: 
        winnings = 0

    points = points + winnings  

   
    print("You won", winnings, "points. Current points:", points)

    
    if points <= 0:
        print("You ran out of points! Game Over.")
        break

   
    x = input("Press 1 to roll again or 2 to exit: ")
    print("\n")
