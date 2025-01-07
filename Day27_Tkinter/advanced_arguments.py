# ADVANCED PYTHON ARGUMENTS: to specify a wider range of inputs

# 1. while defining a fnc provide it wit default paramater values and when calling the fnc no need to specify default values again:
def addNumbers(a=1,b=2,c=3):
    print(a+b+c)
addNumbers()
addNumbers(b=5)        #for custom value of a particular parameter

# 2. fnc that can take UNLimited NO OF ARGUMENTS: *args
def addNumb(*args):
    print(args)     # returns tuple of all arguments passed
    sum=0
    for i in args:
        print(i)
        sum+=i
    print(sum)
addNumb(2,4,6,8)

# 3. MANY KEYWORDED ARGUMENTS: can work with arbitrary no of keyword arguments : **kwargs
def calculate(n,**kwargs):
    print(kwargs)     # returns dictionary of all arguments passed
    # loop thru dictionary:
    for key,value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    # add:
    n=n+kwargs["add"]
    print(n)
    # multiply:
    n=n*kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=2)

class Car:
    def __init__(self,**kwargs):
        # self.color=kwargs["color"]
        # self.model=kwargs["model"]  
        # using [""] will give error if one of the key-value pair is not defined so we use get: get will return nOne for arguments that are not defined
        self.color=kwargs.get("color")
        self.model=kwargs.get("model")  
# my_car=Car(color="red",model="x2")        #we get arguments as kwargs
my_car=Car(color="red")        #when only 1 kwarg argument defined
print(my_car.color)
print(my_car.model)

# ques:
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
# args as tuple() and kwargs as {"key":value} dictionary