class User:
    def __init__(self,name):
        self.name=name
        self.isLoggedIn=False
        
# decorator function:
def is_authenticated(function):
    def wrapperFnc(*args,**kwargs):
        if args[0].isLoggedIn==True:
            function(args[0])
    return wrapperFnc       #without ()
        
@is_authenticated
def create_blog(user):
    print(f"Blog created by {user.name}")

# create object of class:
newUser=User("Akshita")
newUser.isLoggedIn=Truee
create_blog(newUser)