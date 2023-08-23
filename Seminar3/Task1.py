

class Dog():

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def fas(self):
        print("Гав Гав")


dog_1 = Dog()
dog_1.name = "Шарик"
print(dog_1.name)
dog_1.fas()