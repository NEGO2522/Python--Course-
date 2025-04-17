class Animal: # Parent class(super class)
    location = "Australia"
    def __init__(self,name):
        self.name =name

    def speak(self):
        print("Speaking now...")
    

class Dog(Animal): # Inherit Form Animal. This is How inheritance done in Python.
    def speak(self):
        super().speak() # We are using speak function of the parent class.
        print("Woof!")
    
class Cat(Animal): # Inherit From Animal. This is How inheritance done in Python.
    def speak(self):
        print("Meow!")

d = Dog("Sheru")
e = Cat("Pussi") 
d.speak()
e.speak()
print(e.name)
print(d.name)
# print(d.location)