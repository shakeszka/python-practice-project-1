# In the process of writing this code, I got to know what Python PEP is and started learning its principles
# Function names should be lowercase, with words separated by underscores as necessary to improve readability
# Class names should normally use the CapWords convention
# I learnt how to use pickle module to save


from Friend import *

list_of_friends = {}


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


def display_the_list():
    count = 1

    for friend in list_of_friends.keys():
        print(f"{count}.", end=" ")
        # Getting the values from the Class
        print(f"{list_of_friends.get(friend.__str__())}")
        count += 1


def create_friends():
    number_of_friends = write_number_of_friends()

    for i in range(number_of_friends):
        # Checking if the input is the right format
        friend = check_the_inputs(i)

        # We get a tuple looking like this: friend(name, age, height, gpa). it is ordered and unchangeable
        list_of_friends[friend[0]] = list_of_friends.get(friend[0], Friend(name=friend[0], age=friend[1],
                                                                           height=friend[2], gpa=friend[3]))


create_friends()
display_the_list()
