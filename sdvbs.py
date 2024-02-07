import turtle
z = str(input("что зделать черепашке????????"))
while z != "стоп":
    
    if z == "поднять":
        turtle.penup()
        print("перо поднято")
        z = str(input("что зделать черепашке????????"))
    if z == "опустить":
        turtle.pendown()
        print("перо опущено")
        z = str(input("что зделать черепашке????????"))
    if z == "вперёд":
        turtle.forward(100)
        print("черепашка пошла вперёд")
        z = str(input("что зделать черепашке????????"))
    if z == "назад":
        turtle.backward(100)
        print("черепашка пошда назад")
        z = str(input("что зделать черепашке????????"))
    if z == "направо":
        turtle.right(90)
        print("черепашка пошла направо")
        z = str(input("что зделать черепашке????????"))
    if z == "налево":
        turtle.left(90)
        print("черепашка пошла на лево")
        z = str(input("что зделать черепашке????????"))
    if z == "толщина":
        x = str(input("какая толщина???"))
        turtle.pensize(x)
        z = str(input("что зделать черепашке????????"))
    if z == "цвет":
        c = str(input("какой цвет"))
        turtle.pencolor(c)
        z = str(input("что зделать черепашке????????"))
    else:
        print("нет такой команды")
        z = str(input("что зделать черепашке????????"))