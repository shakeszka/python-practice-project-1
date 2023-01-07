# In the process of writing this code, I got to know what Python PEP is and started learning its principles
# Function names should be lowercase, with words separated by underscores as necessary to improve readability
# Class names should normally use the CapWords convention
# I learnt how to use pickle module to save

import pickle
# importing os to remove a file
import os
from Friend import *

# Just checking how git works

def write_number_of_friends():
    # Using a while loop to iterate until a condition is met
    while True:
        try:
            global number_of_friends
            number_of_friends = int(input("Write a number of friends you want to add(less than 5): "))
        except ValueError:
            print("Write the number!(e.g. '1', '2', etc.)")
            continue
        else:
            if 0 < number_of_friends <= 5:
                return number_of_friends
            else:
                print("Write the number between 1 and 5")
                continue

    print(f"The number of friends: {number_of_friends}")


def display_the_list():
    for i in range(number_of_friends):
        with open('friends_data.pkl', 'rb') as inp:
            data = pickle.load(inp)



def check_the_inputs(friend_number):
    print(f"# ----- FRIEND #{friend_number + 1} -----")
    while True:
        name = input("Name: ")

        if name.isdigit():
            continue
        else:
            while True:
                age = input("Age: ")

                try:
                    int(age)
                except ValueError:
                    print("Write the number")
                    continue
                else:
                    while True:
                        height = input("Height: ")

                        try:
                            int(height)
                        except ValueError:
                            print("Write the number")
                            continue
                        else:
                            while True:
                                gpa = input("GPA: ")

                                try:
                                    float(gpa)
                                except ValueError:
                                    print("Write the float number")
                                    continue
                                else:
                                    return name.upper(), age, height, float(gpa)


def create_friends():
    number_of_friends = write_number_of_friends()

    for i in range(number_of_friends):
        # Checking if the input is the right format
        friend = check_the_inputs(i)

        # adding to a file
        with open('friends_data.pkl', 'wb') as outp:
            Friend(friend[0], friend[1], friend[2], friend[3])
            pickle.dump(friend, outp, pickle.HIGHEST_PROTOCOL)


# def display():
#     while True:
#         name = input("Who do you want to check? ").upper()
#
#         if name in list_of_friends:
#             pass
#         else:
#             print(f"{name} is not in the list of friends")


create_friends()

with open('friends_data.pkl', 'rb') as inp:
    data = pickle.load(inp)
    print(data)

os.remove("friends_data.pkl")


