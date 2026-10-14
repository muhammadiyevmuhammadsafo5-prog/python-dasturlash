# OOP - Object oriented prograamming(Obyekt yo'nalishi dasturlash) 

# snake case
# def python_programming():
    # pass

# camel case 
# class Pythonprogramming:
    # pass 



class Animal:
    def __init__(self, name: str):
        self.name = name

    def bark(self):
        print("wooow woow")

animal1 = Animal("dog")  
animal2 = Animal("cat")



# animal1.bark()




class Car:
    def __init__(self, name: str, colour: str, year: int):
        self.name = name 
        self.clour = colour
        self.year = year 
        self.age = 2026 - year

    def say_name(self):
            print("My name is", self.age, "year old")
        
    def say_age(self):
            print("I am" ,self.age, "year old")

    def honk(self):
         print("Beep Beeep")


car1 = Car("Cabalt", "White", 2020)
car2 = Car("Malibu 2", "Blue", 2024)

# car1.say_age()
# car2.say_name()



