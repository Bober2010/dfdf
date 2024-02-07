import turtle
x = str(input("какая толщина????Н"))
while x != "стоп":
    turtle.pensize(x)
    turtle.forward(50)
    x = str(input("какая толщина????Н"))