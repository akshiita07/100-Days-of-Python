# super class:
class Animal:
    def __init__(self):
        self.no_of_eyes=2
        
    def breathe(self):
        print("I can breathe")
        
# another class that inherits from this super class:
class Fish(Animal):
    def __init__(self):
        super().__init__()      #add super class here
        
    # to add new things to already inherited fnc:
    def breathe(self):
        super().breathe()
        print("I breathe underwater")       #extra fnc added here
        
    def swim(self):
        print("I can even swim")
        
nemo=Fish()
nemo.breathe()
nemo.swim()
print("I have",nemo.no_of_eyes,"eyes")