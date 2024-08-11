import turtle

# create object pookie from Turtle class:
pookie=turtle.Turtle()
# print this object:
print("Object is: ",pookie)

# Change shape of pookie to an actual turtle using shape METHOD
pookie.shape("turtle")
# Change color of pookie using color METHOD
pookie.color("DeepPink")
# Move pookie forward using forward METHOD
pookie.forward(100)

# another class in turtle module: Screen()
screenObj=turtle.Screen()
print("Attribute of screenObj: Canvas Height: ",screenObj.canvheight)
print("Attribute of screenObj: Canvas Width: ",screenObj.canvwidth)

# Call a METHOD ie function associated with object
screenObj.exitonclick()

