import turtle
a=30
win= turtle.Screen()
win.title("Maze")
win.bgcolor("cyan")


cursor= turtle.Turtle()


# Function to Create maze

def create_maze():
    cursor.width(5)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.fd(60)
    cursor.setheading(0)

    cursor.fd(30)
    pos1=cursor.pos()#------done
    cursor.fd(30)
    pos2=cursor.pos()#------done
    cursor.fd(30)
    cursor.setheading(90)
    cursor.fd(30)
    cursor.setheading(0)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.fd(30)
    cursor.penup()
    cursor.bk(30)
    pos3=cursor.pos()#---------done
    cursor.goto(pos1)
    cursor.pendown()

    cursor.fd(30)
    cursor.setheading(0)
    cursor.fd(30)
    cursor.penup()
    cursor.bk(30)
    cursor.pendown()
    cursor.bk(30)
    cursor.setheading(90)
    cursor.fd(30)
    cursor.penup()
    cursor.bk(30)
    cursor.pendown()
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(270)
    cursor.fd(30)
    pos4=cursor.pos()#-----done
    cursor.setheading(180)
    cursor.fd(50)
    cursor.setheading(90)
    cursor.fd(30)
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.fd(30)

    cursor.penup()
    cursor.goto(pos4)
    cursor.pendown()

    cursor.bk(30)
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.bk(30)
    pos5=cursor.pos()#-----done
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.bk(30)

    cursor.penup()
    cursor.bk(30)
    cursor.pendown()
    cursor.bk(30)

    cursor.penup()
    cursor.goto(pos5)
    cursor.pendown()
    cursor.bk(30)
    cursor.setheading(180)
    cursor.bk(30)

    cursor.penup()
    cursor.goto(pos2)
    cursor.pendown()

    cursor.setheading(90)
    cursor.bk(30)
    cursor.setheading(180)
    cursor.bk(30)


    cursor.penup()
    cursor.goto(pos3)
    cursor.pendown()

    cursor.setheading(90)
    cursor.bk(90)
    pos6= cursor.pos()#----done
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.bk(65)

    cursor.penup()
    cursor.setheading(180)
    cursor.fd(30)
    cursor.pendown()
    cursor.setheading(90)
    cursor.fd(65)

    cursor.penup()
    cursor.setheading(90)
    cursor.bk(65)
    cursor.pendown()
    cursor.setheading(180)
    cursor.fd(60)
    cursor.setheading(90)
    cursor.bk(30)

    cursor.penup()

    cursor.fd(60)
    cursor.pendown()
    cursor.setheading(180)
    cursor.bk(30)
    cursor.setheading(90)
    cursor.fd(60)



    cursor.penup()
    cursor.goto(pos6)
    cursor.pendown()

    cursor.setheading(90)
    cursor.bk(90)

    pos7= cursor.pos()#-----done

    cursor.setheading(180)
    cursor.fd(60)
    cursor.setheading(90)
    cursor.bk(30)
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.fd(30)

    cursor.penup()
    cursor.goto(pos7)
    cursor.pendown()

    cursor.setheading(90)
    cursor.bk(60)
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.fd(30)
    cursor.penup()
    cursor.bk(30)
    cursor.pendown()
    cursor.setheading(180)
    cursor.fd(85)

    pos8=cursor.pos()#-----done


    cursor.setheading(90)
    cursor.fd(30)
    cursor.setheading(180)
    cursor.fd(30)
    cursor.penup()
    cursor.setheading(90)
    cursor.fd(30)
    cursor.pendown()
    cursor.fd(30)
    cursor.setheading(180)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.bk(60)

    cursor.penup()
    cursor.setheading(180)
    cursor.fd(30)
    cursor.pendown()
    cursor.setheading(180)
    cursor.fd(60)
    cursor.setheading(90)
    cursor.fd(30)
    cursor.setheading(180)
    cursor.bk(30)
    cursor.penup()
    cursor.bk(30)
    cursor.pendown()


    cursor.penup()
    cursor.goto(pos8)
    cursor.pendown()

    cursor.setheading(180)
    cursor.fd(180)
    print(cursor.pos())

    cursor.penup()
    cursor.setheading(90)
    cursor.fd(30)
    print(cursor.pos())
    cursor.pendown()


    cursor.fd(60)
    cursor.setheading(0)
    cursor.fd(60)
    cursor.penup()
    cursor.bk(60)
    cursor.pendown()

    cursor.setheading(90)
    cursor.fd(180)
    pos9= cursor.pos()#-------done

    cursor.setheading(180)
    cursor.bk(30)
    cursor.setheading(90)
    cursor.bk(60)
    cursor.setheading(180)
    cursor.bk(30)
    cursor.setheading(90)
    cursor.bk(30)
    cursor.setheading(180)
    cursor.bk(30)
    cursor.pen()
    cursor.fd(a)
    cursor.pendown()

    cursor.fd(a)
    cursor.setheading(90)
    cursor.bk(2*a)
    cursor.setheading(180)
    cursor.bk(a)

    cursor.penup()
    cursor.goto(pos9)
    cursor.pendown()

    cursor.setheading(90)
    cursor.fd(30)
    cursor.setheading(0)
    cursor.fd(90)
    pos10= cursor.pos()#------done

    cursor.setheading(90)
    cursor.bk(30)
    cursor.setheading(0)
    cursor.fd(30)
    cursor.setheading(90)
    cursor.bk(30)

    cursor.penup()
    cursor.goto(pos10)
    cursor.pendown()

    cursor.setheading(0)
    cursor.fd(60)
    cursor.setheading(90)
    cursor.bk(30)

    cursor.penup()
    cursor.fd(30)
    cursor.pendown()

    cursor.setheading(0)
    cursor.fd(150)

    cursor.penup()
    cursor.bk(90)
    cursor.pendown()

    cursor.setheading(90)
    cursor.bk(30)
    cursor.setheading(0)
    cursor.fd(60)

    cursor.penup()
    cursor.fd(38)
    cursor.setheading(90)
    cursor.fd(8)
    cursor.pendown()
    return

#Function to solve the maze


def text():
    cursor.color("green", "orange")

    turtle.hideturtle()
    turtle.pencolor("red")
    turtle.write("Puzzle Solved", font=("Algerian", 50, "normal"), align="center")

def dash_line(t):

    for _ in range(t//5):
        cursor.fd(5)
        cursor.penup()
        cursor.fd(5)
        cursor.pendown()

def move_up():
    cursor.setheading(90)
    dash_line(10)
    check_boundary()
def move_down():
    cursor.setheading(270)
    dash_line(10)

    check_boundary()
def move_left():
    cursor.setheading(180)
    dash_line(10)
    check_boundary()

def move_right():
    cursor.setheading(0)
    dash_line(10)
    check_boundary()

def stop_listening():
# Unbind all key events
    win.onkey(None, "Up")
    win.onkey(None, "Down")
    win.onkey(None, "Left")
    win.onkey(None, "Right")
    win.onkey(None, "W")
    win.onkey(None, "A")
    win.onkey(None, "S")
    win.onkey(None, "D")

    text()
    
# Checks coordinates for cursor for endpoint
def check_boundary():
    x_fixed= -150
    y_min=-150
    y_max= -120

    if  y_min < cursor.ycor()< y_max and cursor.xcor()<=x_fixed:
        print("Destination Reached")
        stop_listening()

 #This block of code below creates the maze   
cursor.speed(0)
cursor.hideturtle()
create_maze()

#This block of code below solves the maze  on user command
cursor.showturtle()
cursor.color("grey","green")
cursor.shape("turtle")
cursor.speed(10)
cursor.width(1)

win.listen()
win.onkey(move_up,"Up")
win.onkey(move_up,"W")

win.onkey(move_down,"Down")
win.onkey(move_down,"S")

win.onkey(move_left,"Left")
win.onkey(move_left,"A")

win.onkey(move_right,"Right")
win.onkey(move_right,"D")




















win.mainloop()


























