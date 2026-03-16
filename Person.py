class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        try:
            self.__age = int(age)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def greet(self):
        return "Hola " + self.name

    def __str__(self):
        return("Me llamo " + self.name + " y tengo " + str(self.__age) + " años")
