# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100.

import sys
import textwrap
import time


INTRODUCTION = """

WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THE GOVERNMENT WANTS IT FOR THEIR GAIN.

WE CAN'T LET THAT HAPPEN.

ONE GOAL: SURVIVAL... and THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.

"""

CHOICES = """
    ----
    E. Status check
    Q. QUIT
    ----
"""


def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    # intro()

    # Variables
    done = False

    km_traveled = 0             # 100km traveled is the goal
    agents_distance = -20.0
    turns = 0                   # amount of turns taken
    tofu = 3                    # 3 is max tofu
    fuel = 50                   # 50 is a full tank
    hunger = 0                  # hunger increases with num


    while not done:
        # TODO: Check if reached END GAME

        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkms traveled: {km_traveled} kms")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind you.")
            print(f"\tYou have {tofu} tofu left.")
            print("\t------\n")
        elif users_choice == "q":
            done = True

        # Pause
        time.sleep(1)

        # TODO: Change the environment based on choice and RNG

    # Outroduction
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()
