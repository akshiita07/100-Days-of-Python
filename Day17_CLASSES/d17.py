# To create a new custom class
class ClassName:
    pass     #no code has been written here so write pass to avoid indentation error

# To create object of this class:
objName=ClassName()

#To add custom attributes of this class:
objName.userId=7
objName.userName="Akshita"
print(f"Objects id: {objName.userId} and name: {objName.userName}")

# CREATING CONSTRUCTOR OF A CLASS USING __init__
class Class1:
    # this init fnc will be called every time a new object is created for this class:
    def __init__(self):
        print("Hi i am init fnc & u created a new object of Class1")
        
obj1=Class1()
obj2=Class1()

# CONSTRUCTOR & passing attributes
class Class2:
    def __init__(self,user_id,user_name):
        self.uId=user_id
        self.uName=user_name
        # to add default values
        self.followersCount=1000
        
obj1=Class2(27,"Saanvi")
print(f"CONSTRUCTOR: Objects id: {obj1.uId} and name: {obj1.uName} and followers count= {obj1.followersCount}")

# CREATE INSTAGRAM CLASS USING ATTRIBUTES & METHODS:
class Instagram:
    def __init__(self,user_id,user_name):
        self.uId=user_id
        self.uName=user_name
        self.followers=0
        self.following=0
    
    # method for counting followers & following
    def userFollowed(self,user):
        # jisko follow kiya uski followers inc
        user.followers+=1
        # jisne follow kiya: self uski following inc
        self.following+=1
        
user1=Instagram(1,"Dhruv")
print(f"Initially user1: Id:{user1.uId} Name:{user1.uName} Followers:{user1.followers} Following:{user1.following}")

user2=Instagram(2,"Aryan")
print(f"Initially user2: Id:{user2.uId} Name:{user2.uName} Followers:{user2.followers} Following:{user2.following}")

# now suppose user1 followed user2
user1.userFollowed(user2)
# dhruv followed aryan:
print(f"AFTER FOLLOWING--> user1: Id:{user1.uId} Name:{user1.uName} Followers:{user1.followers} Following:{user1.following}")
print(f"AFTER FOLLOWING--> user2: Id:{user2.uId} Name:{user2.uName} Followers:{user2.followers} Following:{user2.following}")