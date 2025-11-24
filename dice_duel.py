# Description: This program is a 1v1 game between player vs CPU. The overall
# goal of this game is to beat the other player via getting the closest to 50
# points. If the user or the CPU gets 50 points, they win the game. If both
# user and CPU get the same points, it's a tie. If they get over 50 points,
# then they bust / lose the game. If both the player and the CPU get below 50
# points, the closest to 50 wins the game. This game lasts 10 turns featuring
# two special rules. One being that if a party rolls two of the same value
# they opposite part losses 10 points. The second special rule consists
# of skipping a turn: If the user has over 40 points, they can skip a turn
# but have only two skips. However, the computer has a 30% chance to skip
# their turn when over 40 points, but has unlimited skips. This description/
# guide is also said in our howToPlay() function and our research file!

# Purpose: The purpose of the program is to give the user a chance to think
# about how a computer plays and make decisions based on that. The first few
# parts of the game the user has a chance to analyze the computer rolls, their
# rolls, and how the special rule would help or hurt their chances of winning.
# The final part (after the parties are at 40 points and can use skips) gives
# the user the ability to critically think of how the skips can benefit them
# or can obstruct their chances of winning. After a few rounds of playing, the
# user learns how the game works and how they can strategize & analyze to win.
# Have fun!


# Test cases: 
# Where the input is occurring → Input / Situation → Output → Success

# Menu → A → “Please enter a valid option.” → Success
# Menu → b → “Please enter a valid option.” → Success
# Menu → -1 → “Please enter a valid option.” → Success
# Menu → 5 → “Please enter a valid option.” → Success
# Menu → % → “Please enter a valid option.” → Success

# Menu → 1 → Start the game and asks the user to enter their choice. → Success
# Menu → 2 → Prints how to play the game. → Success
# Menu → 3 → Prints goodbye and closes the program. → Success

# Main Game → -1 → “You did not press enter or ‘s’, try again.” → Success
# Main Game → 3 → “You did not press enter or ‘s’, try again.” → Success
# Main Game → B → “You did not press enter or ‘s’, try again.” → Success
# Main Game → S → “You did not press enter or ‘s’, try again.” → Success
# Main Game → % → “You did not press enter or ‘s’, try again.” → Success

# Main Game → s → (User does not have 40 or more points yet) “You do not
# have 40 or more points.” → Success

# Main Game → (press enter)→ - Game continues as expected and starts the
# turn. → Success

# Main Game → s → (User has 40 or more points) “You skipped your turn!”
# → Success

# Main Game → After 10 rounds, the user ends with 48 points and the computer
# has 52 points → “Computer busted, You Win!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 52 points and the computer
# has 48 points → “You busted, Computer Wins!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 50 points and the computer
# has 50 points → “It’s a tie, you both win!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 48 points and the computer
# has 48 points → “It’s a tie, you both lose!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 50 points and the computer
# has 48 points → “50 points, You Win!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 45 points and the computer
# has 50 points → “50 points, Computer Wins!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 49 points and the computer
# has 30 points → “You had more points, You Win!”, prints statistics. → Success

# Main Game → After 10 rounds, the user ends with 45 points and the computer
#has 49 points → “Computer has more points, Computer Wins!”, prints statistics.
# → Success

# Main Game → After 10 rounds, the user ends with 32 points and the computer
# has 32 points → “Same points, It’s a tie!”, prints statistics. → Success

# Main Game → After 10 turns the computer was declared as the winner for
# having more points is declared → “You ended with 45 points!, Computer ended
# with 49 points!, Your least points in a single turn were 4., Your most points
# in a single turn were 11., Your average points (including losses) were 4.09.,
# Computer’s least points in a single turn were 4., Computer’s most points in
# a single turn were 8., Computer’s average points (including losses) were
# 4.9.” After checking the average, minimum, and maximum with math, we can say
# all the math and output were correct (printed lists to check). → Success

# Main Game → User rolled a 5 and 5, computer was at 23 points → “The Computer
# loses 10 points! (13)” → Success

# Main Game → Computer rolled a 3 and 3, player was at 11 points → “The Player
# loses 10 points! (1)” → Success



# Modules - Import random and time module.
import random
import time


# Menu Function - 
def menu():

    # Tell the user the options.
    print("1. Play \n2. How To Play \n3. Quit\n")

    # Ask the user for their selection until they enter a proper selection
    # (1, 2, or 3). When one of the options are entered, return the selection
    # to the main program. Try and except is used to avoid any errors if the
    # user enters a string, float, or boolean value.
    while True:
        try:
            userMenu = int(input("Selection: "))
            if userMenu >= 1 and userMenu <= 3:
                return userMenu
            else:
                print("Please enter a valid option.")
        except:
            print("Please enter a valid option.")


# How To Play Function - 
def howToPlay():

    # Return the guide to main program.
    return "\nWelcome to Dice Duel Showdown - Fifty or Bust.\n\n\
In this game, your goal is to roll two dice and get the closest to 50 points \
\nwithin 10 turns without going over 50 points. While you are rolling, you are \
\ncompeting against a computer. If either you or the computer rolls the same \
\nnumber twice (eg. roll a 5 and 5, or 6 and 6, etc), the opposite player will \
\nlose 10 points. If you have more than 40 points, you will have 2 skips where \
\nyou can skip your roll if you choose to. If the computer is over 40 points, \
\nthey have a 30% chance of skipping their turn, and have infinite skips. If \
\nyou go over 50 points, the computer will automatically win, and if the \
\ncomputer goes over 50 points, you will automatically win. In case there is \
no \nwinner after the 10 turns, the party with the most points will be \
victorious \n(same points is a tie). If a party hits exactly 50 points, \
they will \nautomatically win. \n\nGood luck and have fun! \n"


# User Dice Roll Function
def userRoll(rolling):

    # Use time.sleep function from time module to generate three dot(...) 
    # animation before the program rolls.
    print("Rolling", end="")
    for dot in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

    # If the user is rolling (not skipping), run the dice rolls.
    if rolling == True:

        # Initialize the sum of the two dices to 0. 
        diceRollSum = 0

        # Run the dice roll twice and each time add the dice roll to
        # dice roll sum to find the total between the dices. Make a variable
        # for the previous dice roll to see if the both of them match.
        # Print their roll.
        for dice in range (2):
            diceRoll = random.randint(1,6)   
            print("Your roll was:", diceRoll)
            
            # After the second dice rolled, check if the dice rolls match,
            # if so, add -10 to the computer's dice roll list (to subtract 
            # 10 points). Print out a message containing their new points.
            if dice == 1:
                if diceRoll == diceRollPrev:
                    diceComputerListRolls.append(-10)
                    print("The Computer loses 10 points! (" + \
                          str(sum(diceComputerListRolls)) + ")")
            diceRollSum += diceRoll
            diceRollPrev = diceRoll

        # Add the sum of the dice roll to the user's list (so we can add the
        # points using the sum function.
        diceListRolls.append(diceRollSum)

    # If the user skipped, print a message telling them they skipped.
    else:
        print("You skipped your turn!\n")


# Computer Dice Roll Function
def computerRoll():

    # Initialize the sum of the two dices that computer rolls to 0. 
    diceRollComputerSum = 0

    # Run the dice roll twice for the computer and each time add the dice roll 
    # to the dice roll computer sum to find the total between the dices. Make 
    # a variable for the previous dice roll to see if the both of them match.
    # Print computer's roll.
    for dice in range (2):
        diceRoll = random.randint(1,6)   
        print("Computer's roll was:", diceRoll)

        # After the second dice rolled, check if the dice rolls match,
        # if so, add -10 to the users's dice roll list (to subtract 
        # 10 points). Print out a message containing their new points.
        if dice == 1:
            if diceRoll == diceRollComputerPrev:
                diceListRolls.append(-10)
                print("The Player loses 10 points! (" + \
                      str(sum(diceListRolls)) + ")")
        diceRollComputerSum += diceRoll
        diceRollComputerPrev = diceRoll
        
    # Add the sum of the dice roll to the computer's list (so we can add the
    # points using the sum function).
    diceComputerListRolls.append(diceRollComputerSum)


# Computer Skip Or Roll Function
def computerSkipOrRoll():

    # Initialize the computer skip variable to false.
    computerSkip = False

    # If the computer has more than or equal to 40 points, generate a skip
    # chance. If the choice lands on "R", then roll using the compter roll
    # function. If the choice lands on "S", then skip and set the skip
    # variable to true. Return the computer skip variable. 
    if sum(diceComputerListRolls) >= 40:

        # There is a 70% chance of roll and 30% chance to skip.
        skipChance = random.choice("RRRRRRRSSS")
        if skipChance == "S":
            computerSkip = True
            return computerSkip
        else:
            computerRoll()
            return computerSkip
    else:
        computerRoll()
        return computerSkip


# Game Function (containing dice roll functions) - 
def gameFunction():

    # Initialize the user skips to two.
    userSkips = 2

    # Loop the sequence 10 times (10 turns).
    for rolls in range (10):

        # Run the program indefinitely until a break is ran, then
        # move on to next turn.
        while True:

            # Ask the user if they want to roll or skip by using enter
            # or typing 's'. If they type another message, it asks them to
            # try again.
            rollInput = input("\nPress enter to roll or 's' to skip: ")

            # Print the turn number.
            print("\nTurn",rolls+1, "\n")

            # If the user rolls, initialize roll to True, and use it as
            # the argument with the user roll function so the program rolls
            # for the user. Print the amount of points the user it at.
            if rollInput == "":
                roll = True
                userRoll(roll)
                print("Your Points:", sum(diceListRolls), "\n")

                # Run the computer skip or roll function to determine
                # if the computer is skipping or rolling (if over 40 points).
                # If computer is running, compSkip will be false and will
                # print the computer's points afer the roll. If the computer
                # is skipping, compSkip will be true and a message
                # will pop up indicating the computer skipped.
                compSkip = computerSkipOrRoll()
                if compSkip == False:
                    print("Computer's Points:", sum(diceComputerListRolls))
                else:
                    print("Computer Skipped!\n")

                # Break the program after to go to next turn.
                break

            # If the user wants to skip, check if they have skips left and are
            # over 40 points. If not, print a message indicating that they
            # cannot skip and ask for input again. 
            elif rollInput == "s":
                if sum(diceListRolls) >= 40:
                    if userSkips > 0:

                        # Set roll to False and use it as the argument for
                        # the user roll function so the program skips instead
                        # of rolls. Subtract the amount of skips the user
                        # have by 1.
                        roll = False
                        userRoll(roll)
                        userSkips -= 1

                        # Run the computer skip or roll function to determine
                        # if the computer is skipping or rolling (if over 40
                        # points). If computer is running, compSkip will be
                        # false and will print the computer's points afer the
                        # roll. If the computer is skipping, compSkip will be
                        # true and a message will pop up indicating the
                        # computer skipped.
                        compSkip = computerSkipOrRoll()
                        if compSkip == False:
                            print("Computer's Points:", \
                                  sum(diceComputerListRolls))
                        else:
                            print("Computer Skipped!")
                            
                        # Break the program after to go to next turn.
                        break
                    else:
                        print("You have no more skips left.")
                else:
                    print("You do not have 40 or more points.") 
            else:
                print("You did not press enter or 's', try again.")

        # After each turn, check if either both parties busted, both
        # parties are at exactly 50, player is at 50 or busted, or computer
        # is at 50 or busted. If any of these conditions are true return
        # the message with the winner or if it is a tie. If not, print that
        # the game is stll continuing.
        if sum(diceComputerListRolls) > 50 and sum(diceListRolls) > 50: 
            return "\nIt's a tie, you both lose!"
        elif sum(diceComputerListRolls) == 50 and sum(diceListRolls) == 50:
            return "\nIt's a tie, you both win!"
        elif sum(diceListRolls) > 50:
            return "\nYou busted, Computer Wins!"
        elif sum(diceListRolls) == 50:
            return "\n50 points, You Win!"
        elif sum(diceComputerListRolls) > 50:
            return "\nComputer busted, You Win!"
        elif sum(diceComputerListRolls) == 50:
            return "\n50 points, Computer Wins!"
        else:
            print("\nContinuing...\n")

    # If 10 rounds passed and no winners are found, check which party has more
    # points (if under 50 points). The party with the most points wins.
    # If both parties have the same points, the game ends in a tie.
    if sum(diceListRolls) > sum(diceComputerListRolls):
        return "\nYou had more points, You Win!"
    elif sum(diceComputerListRolls) > sum(diceListRolls):
        return "\nComputer had more points, Computer Wins!"
    else:
        return "\nSame points, It's a tie!"


# Lowest Point Function (other than -10) - 
def leastPT(pointsList):

    # Sort the values of the list in a new variable then count the amount of
    # -10s. For how many times the program counted, remove -10 from the list.
    sortedPoints = sorted(pointsList)
    negativeTens = sortedPoints.count(-10)
    for ten in range (negativeTens):
        sortedPoints.remove(-10)

    # Find the lowest value at the very first index and return it.
    lowestValue = sortedPoints[0]
    return lowestValue    


# Statistics Function -   
def statistics():

    # Calculate the user and ccomputer total points by using the 'sum'
    # function with their lists.
    userTotalPTS = sum(diceListRolls)
    cpuTotalPTS = sum(diceComputerListRolls)

    # Calculate the user minimum by using the lowest point function.
    # Calculate the 'max' function with the user list to calculate the highest
    # point. Calculate the average by dividing the sum of the user list by the
    # total amount of values. Round this value to two decimal places too.
    userMin = leastPT(diceListRolls)
    userMax = max(diceListRolls)
    userAvg = round(sum(diceListRolls) / len(diceListRolls), 2)
    
    # Calculate the computer  minimum by using the lowest point function.
    # Calculate the 'max' function with the comp. list to calculate the highest
    # point. Calculate the average by dividing the sum of the comp. list by the
    # total amount of values. Round this value to two decimal places too.
    cpuMin = leastPT(diceComputerListRolls)
    cpuMax = max(diceComputerListRolls)
    cpuAvg = round(sum(diceComputerListRolls) / len(diceComputerListRolls), 2)

    # Print these values in a nicely formatted, spaced out, and labeled
    # way.
    print("\n\n", " "*5, "Statistics:\n")
    print("You ended with", userTotalPTS, "points!")
    print("Computer ended with", cpuTotalPTS, "points!\n")
    print("Your least points in a single turn were " + str(userMin) + ".")
    print("Your most points in a single turn were " + str(userMax) + ".")
    print("Your average points (including losses) were " + str(userAvg) + \
          ".\n")
    print("Computers's least points in a single turn were " + str(cpuMin) + ".")
    print("Computer's most points in a single turn were " + str(cpuMax) + ".")
    print("Computer's average points (including losses) were " +  str(cpuAvg) \
          + ".\n\n")  


# Main Program -


# Print a title message for when the program first opens.
print(" \
╔══╦╗    ╔══╗      ╔══╦╗      ╔╗\n \
╚╗╗╠╬═╦═╗╚╗╗╠╦╦═╦╗ ║══╣╚╦═╦╦╦╦╝╠═╦╦╦╦═╦╗\n \
╔╩╝║║═╣╩╣╔╩╝║║║╩╣╚╗╠══║║║╬║║║║╬║╬║║║║║║║\n \
╚══╩╩═╩═╝╚══╩═╩═╩═╝╚══╩╩╩═╩══╩═╩═╩══╩╩═╝\n \
", end="")
print("\
    ╔══╦╦══╦══╦═╦╗     ╔══╦╦╦══╦══╗        \n \
╔══╗║═╦╬╣═╦╩╗╔╩╗║║╔═╦╦╗║╔╗║║║══╬╗╔╝╔══╗    \n \
╚══╝║╔╝║║╔╝ ║║╔╩╗║║╬║╔╝║╔╗║║╠══║║║ ╚══╝    \n \
    ╚╝ ╚╩╝  ╚╝╚══╝╚═╩╝ ╚══╩═╩══╝╚╝         \n \
")


# Repeat this program forever until the user decides to quit (3 in menu).
while True:

    # Input - Ask the user for their menu choice.
    selection = menu()

    # Input, Process & Output - If the user wants to play, initialize the user
    # and computer lists and start the game function. After that, add the
    # statistics function to show the user the stats.
    if selection == 1:
        diceListRolls = []
        diceComputerListRolls = []
        print(gameFunction())
        statistics()

    # Process & Output - If the user wants to learn how to play, print the
    # howToPlay function which contains the guide.
    elif selection == 2:
        print(howToPlay())

    # Output - If the user wants to quit, print a goodbye message and break
    # the program.
    else:
        print("\nGoodbye!")
        break