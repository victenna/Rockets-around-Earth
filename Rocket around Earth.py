import turtle,time
wn=turtle.Screen()
wn.bgcolor('navy')
wn.setup(900,900)
image1='Earth.gif'
wn.addshape(image1)
earth=turtle.Turtle()
earth.shape(image1)
earth.goto(0,0)

turtle.tracer(2)
s1=turtle.Shape("compound")

      
poly1=((0,0),(25,0),(25,10),(0,10))
poly2=((25,0),(35,5),(25,10))
poly3=((0,10),(-5,19),(10,10))
poly4=((0,0),(-5,-10),(10,0))
poly5=((5,7),(15,7),(15,10),(5,10))
poly6=((0,3),(-10,-4),(-10,14),(0,8))
clr=['red','light blue','gold','yellow','blue']    
s1.addcomponent(poly1,clr[0],'black')
s1.addcomponent(poly2,clr[1],'black')
s1.addcomponent(poly3,clr[2],'black')
s1.addcomponent(poly4,clr[3],'black')
s1.addcomponent(poly5,clr[4],'black')    
s1.addcomponent(poly6,clr[3],'black')
wn.addshape('geometry',s1)

Rocket=turtle.Turtle(shape='geometry')
Rocket.shapesize(2)
Rocket.tilt(90)
Rocket.showturtle()
Rocket.up()
Rocket.goto(0,-400)
Rocket.rt(0)
turtle.tracer(2)
while True:
    Rocket.circle(400,1)
    time.sleep(0.01)
