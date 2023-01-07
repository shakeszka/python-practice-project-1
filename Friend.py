import pickle

class Friend:
    def __init__(self, name, age, height, gpa):
        self.name = name
        self.age = age
        self.height = height
        self.gpa = gpa

    def check_if_stupid(self):
        if self.gpa < 3.0:
            return False
        else:
            return True

    def display_stupid(self):
        result = self.check_if_stupid()

        if result:
            print(f"{self.name} is smart because his GPA is {self.gpa}")
        else:
            print(f"{self.name} is stupid because his GPA is {self.gpa}")
