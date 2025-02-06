import turtle
ren=turtle.Turtle()
window = turtle.Screen()
WIN_width = 1280
WIN_height = 720
ren.screen.setup(WIN_width, WIN_height)
ren.speed(0)
turtle.bgcolor("gray")   
ren.hideturtle()
moon = turtle.Turtle()

image = "pngtree-yellow-moon-png-image_7253691-removebg-preview.gif"
window.addshape(image)
moon.shape(image)

moon.pu()
moon.goto(-10,300)
moon.pd()

moon.stamp()

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
ren.color("white", "black")
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

window.mainloop()
