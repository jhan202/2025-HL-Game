import math


# Check that users have entered a valid
# option based on a list
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter .yes / no")




def instructions():
    print('''

*** Instructions ***

To begin choose the number of rounds and either customise
the game parameters o go with the default game ( where the 
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
the infinite mode.

Your goal is to try to guess the secret number without 
running out of guesses



Good Luck!
    ''')




# checks for an integer with optional upper /
# lower limit and an optional exit code for infinite mode
# / quitting the game
def int_check (question, low=None,  high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = " Please enter an integer"

    # if the number needs to be more than
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return reponse

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and reponse < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid , return it
            else:
                return response


        except ValueError:
            print(error)


# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("🔼🔼🔼 Welcome to The Higher Lower Game 🔽🔽🔽")
print()

want_instructions = yes_no ("Do you want to read the instructions? ")

#checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()



# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                        low=1, exit_code=" ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number?", low=low_num + 1)
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
        if mode == "infinite":
            rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} (Infinite mode)💿💿💿 "
        else:
            rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds}💿💿💿"

        print(rounds_heading)
        print()

        user_choice = input("Choose: ")

        if user_choice == "xxx":
            break


        rounds_played += 1

# if users are in infinite mode, increase number of rounds!
if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area
