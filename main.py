# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100.

import random
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

WIN = """

You pressed the button to open the gate.
This isn't the first time you've done this,
so you know how to time it exactly.
Just as the doors close, you slide right into HQ.
You know you did the right thing, the government
would have just torn the car apart.
They don't know its secrets...
that it holds the key to different worlds.
As you step out of the vehicle, Fido runs up to you.
"Thank you for saving me," he says.
As you take a couple of steps away from the car,
it makes a strange sound.
It changes it shape.
You've seen it before, but only on TV.
"...Bumblebee???"


------ Game Over ------
"""

LOSE_HUNGER = """

YOUR STOMACH IS EMPTY.
WHO KNEW THAT WHAT THE DOCTOR SAID WAS TRUE,
THAT HUMAN/ROBOT HYBRIDS WOULD NEED
TOFU TO SUSTAIN THEMSELVES.
YOUR ROBOT SYSTEMS START TO SHUT DOWN.
YOUR HUMAN EYES CLOSE.
THE LAST THING THAT YOU HEAR ARE SIRENS.
THEY GOTCHU. THEY GOT THE CAR.
WE FAILED...


------ GAME OVER ------
"""

CHOICES = """
    ----
    A. Eat some tofu.
    B. Continue ahead at a moderate speed.
    C. Speed ahead a full throttle.
    D. Stop for fuel at a refuelling station.
       (No food available)
    E. Status check
    Q. QUIT
    ----
"""


def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    # type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3
    MAX_DISTANCE_TRAVELED = 100
    TOFU_CHANCE = 0.03

    # Variables
    done = False

    km_traveled = 0
    agents_distance = -20.0
    turns = 0
    tofu = MAX_TOFU_LEVEL
    fuel = MAX_FUEL_LEVEL
    hunger = 21

    while not done:
        # TODO: Random events
        # Fido
        if random.random() < TOFU_CHANCE:
            # Fido pops up says something and refills tofu
            tofu = MAX_TOFU_LEVEL
            print()
            print("******** Your tofu is magically refilled!")
            print("******** \"You're welcome!\" a voice says.")
            print("******** It's Fido.")
            print("******** He's using his tofu cooking skills.")

        # Check if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELED:
            # WIN
            # Print win scenario (typing way)
            time.sleep(2)
            type_text_output(WIN)
            break
        elif hunger > 45:
            # LOSE - TOO HUNGRY
            # Print losing hunger scenario
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break
        elif agents_distance >= 0:
            # LOSE - AGENTS REACHED YOU
            pass

        # Showing hunger
        if hunger > 35:
            print("******** Your stomach rumbles. You need to eat something soon.")
        elif hunger > 20:
            print("******** Your hunger is small but manageable.")

        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice == "a":
            # Eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmmmm. Soybean goodness.")
                print("-------- Your hunger is sated.")
                print()
            else:
                print()
                print("-------- You have none left.")
                print()
        elif users_choice == "b":
            # Drive slow
            player_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(2, 7)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to Player
            print()
            print(f"-------- You travelved {player_distance_now} kms!")
            print()
        elif users_choice == "c":
            # Drive Fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to Player
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()
        elif users_choice == "d":
            # Refuel
            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()
        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkms traveled: {km_traveled} kms")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind you.")
            print(f"\tYou have {tofu} tofu left.")
            print("\t------\n")
        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)

        # Pause
        time.sleep(1.2)

    # Outroduction
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()
