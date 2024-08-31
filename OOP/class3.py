class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and am {self.age} years old")
        
    def speak(self):
        print('ooooooo')

class Cat(Pet):    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print('MEEEOW')
        
    def show(self):
        print(f"I am {self.name} and am {self.age} years old and am {self.color}")
        
class Dog(Pet): 
    def speak(self):
        print('Bark')
        
class Fish(Pet): 
    pass
        

p = Pet("TIM", 20) 
p.show()
c = Cat("guy", 5, "red")
c.show()
d = Dog("pom", 7)
d.show()

d.speak()
c.speak()

f = Fish("pom", 2)
f.speak()
