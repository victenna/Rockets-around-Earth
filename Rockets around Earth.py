import turtle,time
wn=turtle.Screen()
wn.bgpic('sky.gif')
wn.setup(900,900)
t=turtle.Turtle()
t.up()
s1=turtle.Shape("compound")
s2=turtle.Shape("compound")
s3=turtle.Shape("compound")

#Earth file images
image=[]
for i in range(45):
    i1=str(i)
    image.append(i1+'.gif')
wn.addshape(image[0])
turtle.shape(image[0])
#======================================
#Rocket polygons
poly1=((0,0),(25,0),(25,10),(0,10))
poly2=((25,0),(35,5),(25,10))
poly3=((0,10),(-5,19),(10,10))
poly4=((0,0),(-5,-10),(10,0))
poly5=((5,7),(15,7),(15,10),(5,10))
poly6=((0,3),(-10,-4),(-10,14),(0,8))

#Rocket1 geometry
s1.addcomponent(poly1,'red','black')
s1.addcomponent(poly2,'light blue','black')
s1.addcomponent(poly3,'gold','black')
s1.addcomponent(poly4,'yellow','black')
s1.addcomponent(poly5,'blue','black')    
s1.addcomponent(poly6,'yellow','black')
wn.addshape('geometry1',s1)

Rocket1=turtle.Turtle(shape='geometry1')
Rocket1.hideturtle()
Rocket1.shapesize(2)
Rocket1.tilt(90)
Rocket1.up()
Rocket1.goto(0,-400)
Rocket1.showturtle()
#=================================================
#Rocket2 geometry
s2.addcomponent(poly1,'light blue','black')
s2.addcomponent(poly2,'red','black')
s2.addcomponent(poly3,'gold','black')
s2.addcomponent(poly4,'brown','black')
s2.addcomponent(poly5,'blue','black')    
s2.addcomponent(poly6,'yellow','black')
wn.addshape('geometry2',s2)

Rocket2=turtle.Turtle(shape='geometry2')
Rocket2.hideturtle()
Rocket2.shapesize(1.4)
Rocket2.tilt(90)
Rocket2.up()
Rocket2.goto(-220,0)
Rocket2.lt(270)
Rocket2.showturtle()
#=================================================
#Sattelite polygons
poly1=((0,0),(30,0),(30,10),(0,10))   #red
poly2=((20,5),(40,-5),(40,15))
poly3=((0,3),(-10,-4),(-10,14),(0,8))
poly4=((10,0),(20,0),(20,-30),(10,-30))  #gold
poly5=((5,7),(15,7),(15,10),(5,10))
poly6=((10,10),(20,10),(20,40),(10,40))
clr=['red','gold','gainsboro','light blue']    

s3.addcomponent(poly1,'red','black')  #red
s3.addcomponent(poly3,'gold','black')
s3.addcomponent(poly4,'gainsboro','black')   #gold
s3.addcomponent(poly6,'light blue','black')
wn.addshape('geometry3',s3)
Sat1=turtle.Turtle(shape='geometry3')
Sat1.hideturtle()
Sat1.shapesize(2)
Sat1.tilt(0)
Sat1.up()
Sat1.goto(300,0)
Sat1.lt(90)
Sat1.showturtle()
#=================================================
#Earth motion anime files

turtle.tracer(3)
k=0
while True:
    k=k+1
    k0=k%44
    k1=k%44
    if k0<22:
        wn.bgpic('sky.gif')
    if k0>22:
        wn.bgpic('sky1.gif')
    wn.addshape(image[k1])
    t.shape(image[k1])
    Rocket1.circle(400,1)
    Rocket2.circle(220,3)
    Sat1.fd(10)
    angle=Sat1.heading()
    Sat1.setheading(angle+2)
    time.sleep(0.01)
