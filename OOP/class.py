x = 1
y = 'hello'

def hello():
    print('Hello')

string = 'hello'
print(string.upper())

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
      
    def add(self, x):
        return x + 1
    
    def bark(self):
        print('WOOOF! WOOOF!')
        
d = Dog('Brian', 25)
d.bark()
print(type(d))

print(d.add(5))

print(d.get_name())
d.set_age(24)
print(d.get_age())