def polygon(t, sides, distance):
    angle = 360 / sides
    for times in range(sides):
        t.forward(100)
        t.left(angle)


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def pattern1(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("darkmagenta")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("darkmagenta")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)


def pattern2(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("mediumorchid")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("mediumorchid")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)


def pattern3(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("orchid")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("orchid")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)


def pattern4(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("plum")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("plum")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)


def pattern5(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("pink")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("pink")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)


def pattern6(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("lightpink")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("lightpink")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)


def pattern7(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("hotpink")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("hotpink")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)


def pattern8(t):
    for times in range(9):
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("deeppink")
        polygon(t, 3, 100)
        t.end_fill()
        t.left(90)
        t.forward(100)
        t.left(90)
        t.begin_fill()
        t.color("black")
        polygon(t, 4, 100)
        t.end_fill()
        t.begin_fill()
        t.color("deeppink")
        polygon(t, 3, 100)
        t.end_fill()
        t.forward(100)

        
        
        
