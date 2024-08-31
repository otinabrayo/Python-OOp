class Person:
    num_of_pepo = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_pepol()
        # Person.num_of_pepo += 1
     
    @classmethod   
    def num_of_pepol(cls):
        return cls.num_of_pepo
    
    @classmethod
    def add_pepol(cls):
        cls.num_of_pepo += 1
        
        
        
p1 = Person('tim')
print(Person.num_of_pepo)
p2 = Person('ret')
print(Person.num_of_pepo)


# Person.num_of_pepo = 5
print(p2.num_of_pepo)

print(Person.num_of_pepol())