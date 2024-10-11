import turtle
a=30
win= turtle.Screen()
win.title("Maze")
win.bgcolor("cyan")


cursor= turtle.Turtle()
cursor.speed(0)
cursor.hideturtle()
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

cursor.penup()
cursor.setheading(90)
cursor.fd(30)
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

#turtle solving
cursor.showturtle()
cursor.color("grey","green")
cursor.shape("turtle")
t=15
def dash_line(t,x):
    cursor.seth(x)
    for _ in range(t//5):
        cursor.fd(5)
        cursor.penup()
        cursor.fd(5)
        cursor.pendown()

cursor.speed(1)
cursor.width(1)

dash_line(t,180)

dash_line(t,270)

dash_line(3*t,180)

dash_line(2*t-10,90)

dash_line(t,180)

dash_line(2*t-10,270)

dash_line(2*t-15,180)

dash_line(2*t-15,270)

dash_line(2*t-20,180)

dash_line(2*t-15,90)

dash_line(2*t-15,180)

dash_line(2*t-15,90)

dash_line(2*t-15,180)

dash_line(3*t-15,270)

dash_line(2*t-20,0)

dash_line(t,270)

dash_line(t,0)

dash_line(2*t-15,270)

dash_line(t,180)

dash_line(4*t-5,270)

dash_line(t,0)

dash_line(2*t-10,270)

dash_line(4*t,180)



cursor.color("green", "orange")

turtle.hideturtle()
turtle.pencolor("red")
turtle.write("Puzzle Solved", font=("Algerian", 50, "normal"), align="center")

















win.mainloop()


























