class Animal:
    def __init__(self, name=""):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")




class Dog(Animal):

    def __init__(self):
        # super().__init__("Doggy")
        super().__init__()

    def eat(self, name=""):
        print(f"{self.name} is eating dog food.")


cat = Animal("Kitty")
cat.eat()

dog = Dog()
dog.eat("Hong")