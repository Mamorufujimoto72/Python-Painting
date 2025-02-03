import turtle
import random
ren = turtle.Turtle()
window = turtle.Screen()
WIN_width = 512
WIN_height = 512
ren.screen.setup(WIN_width, WIN_height)
turtle.tracer(False)




def waves(radius, degree, width, color):
    ren.color(color)
    ren.width(width)
    ren.rt(90)
    ren.circle(radius, degree)
    ren.rt(180)
    ren.circle(radius, degree)

def birds(radius, degree, width, color):
    ren.color(color)
    ren.width(width)
    ren.lt(90)
    ren.circle(radius, degree)
    ren.rt(180)
    ren.circle(radius, degree)

def jump(x, y):
    ren.pu()
    ren.goto(x, y)
    ren.pd()


def fill(stroke, fillin):
    ren.color(stroke, fillin)


def ocean():
    ren.pu()
    ren.goto(-256, 0)
    ren.pd()

    ren.fd(512)
    ren.rt(90)
    ren.fd(256)
    ren.rt(90)
    ren.fd(512)
    ren.rt(90)
    ren.fd(256)


def sun(size, width):
    ren.width(width)
    ren.circle(size)


def sky():
    ren.fd(512)
    ren.lt(90) 
    ren.fd(43)
    ren.lt(90)
    ren.fd(512)
    ren.lt(90)

colorBox = ["#f3ed41", "#f2de3f", "#f2cf3d", "#f2c03b", "#f2b139", "#f1a239"]  


jump(-256, 0)
ren.color("#f3ed41", "#f3ed41")
ren.begin_fill()
sky()
ren.end_fill()
ren.setheading(0)
jump(-256, 43)
ren.color("#f2de3f", "#f2de3f")
ren.begin_fill()
sky()
ren.end_fill()
ren.setheading(0)
jump(-256, 86)
ren.color("#f2cf3d", "#f2cf3d")
ren.begin_fill()
sky()
ren.end_fill()
ren.setheading(0)
jump(-256, 129)
ren.color("#f2c03b", "#f2c03b")
ren.begin_fill()
sky()
ren.end_fill()
ren.setheading(0)
jump(-256, 172)
ren.color("#f2b139", "#f2b139")
ren.begin_fill()
sky()
ren.end_fill()
ren.setheading(0)
jump(-256, 172+43)
ren.color("#f1a239", "#f1a239")
ren.begin_fill()
sky()
ren.end_fill()
ren.setheading(0)

jump(0, -100)
fill("#fafd78","#fafd78")
ren.begin_fill()
sun(120, 5)
ren.end_fill()


fill("#264653", "#264653")
ren.begin_fill()
ocean()
ren.end_fill()








for o in range(50):
    wave_x = random.randint(-256, 256)
    wave_y = random.randint(-256, 0)
    ren.pu()
    ren.goto(wave_x, wave_y)
    ren.pd()
    waves(5, 180, 2, "#37657f")
    ren.setheading(0)

for b in range(10):
    bird_w = random.randint(-256, 256)
    bird_y = random.randint(0, 256)
    ren.pu()
    ren.goto(bird_w, bird_y)
    ren.pd()
    birds(10, 150, 5, "white")
    ren.setheading(0)








def buttonclick(x,y): 
    print("You clicked at this coordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick,1) 
turtle.listen()  
turtle.speed(10) 
turtle.done()   
turtle.tracer(True)
window.exitonclick()