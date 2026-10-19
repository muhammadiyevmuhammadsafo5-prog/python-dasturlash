class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name)



# class Dog(Animal):
#     pass

# d1 = Dog("Rex")
# d1.speak()



class Bobo:
    pul = 100000
    age = 75

    def say_age(self):
        print(self.age)


class Ota(Bobo):
    name = "Ota"

    def build(self):
        print("uy quroladi")

class Bola(Ota, Bobo):
    age = 15

    def run(self):
        print("yurgirish")


bobo = Bobo ()
ota = Ota()
bola = Bola()

