import turtle
import time
from mod_scr import *
wn=turtle.Screen()
wn.setup(1000,500)
turtle.tracer(4)
t=turtle.Turtle()
street=turtle.Turtle()
street.up()


car_image=['carr1.gif','carr2.gif','carr3.gif']
wn.addshape('long_street3.gif')
street.shape('long_street3.gif')
wn.addshape(car_image[0])
wn.addshape(car_image[1])
wn.addshape(car_image[2])

t.shape(car_image[0])
t.up()
t.goto(600,-180)
tposition=t.position()
street.goto(-500,0)

t1=turtle.Turtle()
wn.addshape('carr4.gif')
t1.shape('carr4.gif')
t1.up()
t1.goto(270,-80)
t2=t1.clone()
t2.up()
t2.goto(50,-180)
t3=t1.clone()
t3.goto(-140,-80)
t4=t1.clone()
t4.goto(-350,-180)
t1position=t1.position()
t2position=t2.position()
t3position=t3.position()
t4position=t4.position()


def up():
    t.setheading(90)
    t.fd(100)
    Y=t.ycor()
    t.setheading(0)

def down():
    t.setheading(-90)
    t.fd(100)
    Y=t.ycor()
    t.setheading(0)

wn.listen()
wn.onkey(up,'Up')
wn.onkey(down,'Down')

while True:
    street.goto(-500,0)
    t.goto(600,-80)
    i=-1
    while i<500:
        i=i+1
    #for i in range (500):
        tposition=t.position()
        t1position=t1.position()
        t2position=t2.position()
        t3position=t3.position()
        t4position=t4.position()
        delta1=abs(t1position-tposition)
        delta2=abs(t2position-tposition)
        delta3=abs(t3position-tposition)
        delta4=abs(t4position-tposition)
        if delta1<10 or delta2<10\
           or delta3<10 or delta4<10:
            t.hideturtle()
            scr()
            t.goto(600,-80)
            t.showturtle()
        
        
        i1=i%3
        t.shape(car_image[i1])
        
        street.fd(2)
        t.fd(-2)
        Y=t.ycor()
        if Y>-80:
            t.sety(-80)
        if Y<-180:
            t.sety(-180)
        X=street.xcor()
        #print(X)
        time.sleep(0.01)

        
