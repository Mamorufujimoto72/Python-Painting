import turtle
import random
ren=turtle.Turtle()
window = turtle.Screen()
WIN_width = 1280
WIN_height = 720
ren.screen.setup(WIN_width, WIN_height)
ren.speed(0)
turtle.bgcolor("gray")   
ren.hideturtle()
moon = turtle.Turtle()
window.tracer(False)


COLOR = (0.008, 0, 0.329)  # (154, 0, 254)
TARGET = (0, 1, 1)  # (221, 122, 80)

deltas = [(hue - COLOR[index]) / WIN_height for index, hue in enumerate(TARGET)]

turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIN_width/2, WIN_height/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(WIN_height//2, -WIN_height//2, -1)):

    turtle.forward(WIN_width * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

def stars(width, rotation):
    ren.lt(rotation)
    for i in range(5):
        ren.forward(width)
        ren.right(180-36)

ren.color("white", "white")

for b in range(50):
    rotation = random.randint(0, 360)
    width = random.randint(10, 80)
    bird_w = random.randint(-640, 640)
    bird_y = random.randint(40, 360)
    ren.pu()
    ren.goto(bird_w, bird_y)
    ren.pd()
    ren.begin_fill()
    stars(width, rotation)
    ren.end_fill()
    ren.setheading(0)


def jump(x, y):
    ren.pu()
    ren.goto(x, y)
    ren.pd()


def tower(lenght, width):
    ren.fd(width)
    ren.lt(90)
    ren.fd(lenght)
    ren.lt(90)
    ren.fd(width)
    ren.lt(90)
    ren.fd(lenght)
    ren.lt(90)
    ren.fd(width)

def sky_scrapper():
    ren.fd(220)
    ren.lt(90)
    ren.fd(400)
    ren.lt(90)
    ren.fd(20)
    ren.rt(90)
    ren.fd(50)
    ren.lt(90)
    ren.fd(20)
    ren.rt(90)
    ren.fd(60)
    ren.lt(90)
    ren.fd(20)
    ren.rt(90)
    ren.fd(70)
    ren.lt(90)
    ren.fd(20)
    ren.rt(90)
    ren.fd(80)
    ren.lt(90)
    ren.fd(20)
    ren.lt(90)
    ren.fd(80)
    ren.rt(90)
    ren.fd(20)
    ren.lt(90)
    ren.fd(70)
    ren.rt(90)
    ren.fd(20)
    ren.lt(90)
    ren.fd(60)
    ren.rt(90)
    ren.fd(20)
    ren.lt(90)
    ren.fd(50)
    ren.rt(90)
    ren.fd(20)
    ren.lt(90)
    ren.fd(400)
    ren.lt(90)
    ren.fd(180)
    




ren.setheading(0)
ren.color("black", "black")
jump(-640, -360)
ren.begin_fill()
tower(300,100)
ren.end_fill()
jump(-540, -360)
ren.begin_fill()
tower(600,200)
ren.end_fill()
jump(-340, -360)
ren.begin_fill()
tower(400, 200)
ren.end_fill()
jump(-140, -360)
ren.begin_fill()
sky_scrapper()
ren.end_fill()
jump(120, -360)
ren.begin_fill()
tower(200, 200)
ren.end_fill()
jump(320, -360)
ren.begin_fill()
tower(300,200)
ren.end_fill()
jump(520,-360)
ren.begin_fill()
tower(700,120)
ren.end_fill()




def buttonclick(x,y): 
    print("You clicked at this coordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick,1) 
turtle.listen()  
turtle.speed(10) 
turtle.done() 
window.tracer(False)
window.mainloop()
