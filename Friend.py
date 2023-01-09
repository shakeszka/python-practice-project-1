# Learned how to use Class inheritance, super function and method/variable overwriting


class Friend:
    # Class variables
    friend = True
    best_friend = False  # This one is going be overwritten in the child class

    def __init__(self, name, age, height, gpa):
        self.name = name
        self.age = age
        self.height = height
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, height: {self.height}, GPA: {self.gpa}"

    def check_is_stupid(self):
        if self.gpa < 3.0:
            return False
        else:
            return True

    def display_is_stupid(self):
        result = self.check_is_stupid()

        if result:
            print(f"{self.name} is smart because his GPA is {self.gpa}")
        else:
            print(f"{self.name} is stupid because his GPA is {self.gpa}")


class BestFriend(Friend):
    best_friend = True  # overwritten class variable

    def __init__(self, name, age, height, gpa, how_long):
        # Using the super function to inherit the parent's construction methods
        super().__init__(name, age, height, gpa)
        self.how_long = how_long

    def check_is_best_friend(self):
        if self.best_friend:
            return True
        else:
            return False

    def display_is_best_friend(self):
        result = self.check_is_best_friend()

        if result:
            print(f"{self.name} is your best friend because you have known him for {self.how_long} years!")
        else:
            print(f"{self.name} is not you best friend because you have known him for {self.how_long} years!")
