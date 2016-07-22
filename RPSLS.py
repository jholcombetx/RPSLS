# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error 2"
        
    

def rpsls(player_choice): 
    print ""
    print "You have chosen " + player_choice +"."
    player_number = name_to_number(player_choice)
    comp_number = (random.randrange(0,5))
    comp_choice = number_to_name(comp_number)
    print "The computer has chosen " + str(comp_choice) + "."
    rpsls_number = (player_number - comp_number) % 5
    if rpsls_number == 4 or rpsls_number == 3:
        print "Computer wins!"
    elif rpsls_number == 1 or rpsls_number == 2:
        print "Player wins!"
    else:
        print "It's a tie."
    
    
 

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



# always remember to check your completed program against the grading rubric


