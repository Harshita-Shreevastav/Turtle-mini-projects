import turtle

drawing= True
win= turtle.Screen()
win.title("Canvas")
win.setup(width=1.0, height= 1.0)

colors=["red", "green", "blue", "yellow", "orange", "pink", "Black", "White", "cyan", ]



cursor= turtle.Turtle()
cursor.width(5)
cursor.speed(100)

def color_dot(x, pos):
    cursor.penup()
    cursor.goto(pos)
    cursor.pendown()
    cursor.dot(30,"Black")
    cursor.dot(27, x)


canvas= win.getcanvas()


def continue_drawing():
    global drawing
    drawing = True
    canvas.bind("<ButtonPress-1>", on_click)

def width_select(event):
    if event.delta>0:
        if cursor.width()<=10:
            new_width= cursor.width()+1
            cursor.width(new_width)

    if event.delta<0:
        if cursor.width()>=1:
            new_width= cursor.width()-1
            cursor.width(new_width)

def on_release(event):
    cursor.penup()
    drawing=False
    continue_drawing()


def on_click(event):
    x = event.x - win.window_width() / 2  # Adjust for window center
    y = win.window_height() / 2 - event.y 
    cursor.penup() # Adjust for window center
    cursor.goto(x, y) 
    cursor.pendown() # Move the turtle to the mouse position
    canvas.bind("<MouseWheel>", width_select)
    
    canvas.bind("<Motion>", draw)

# def left_draw():
#     new_heading= cursor.heading()+20
#     cursor.setheading(new_heading)
#     cursor.fd(20)

# def right_draw():
#     new_heading= cursor.heading()-20
#     cursor.setheading(new_heading)
#     cursor.fd(20)

# def up_draw():
#     cursor.setheading(90)
#     cursor.fd(20)

# def down_draw():
#     cursor.setheading(270)
#     cursor.fd(20)

def draw(event):
    x = event.x - win.window_width() / 2  # Adjust for window center
    y = win.window_height() / 2 - event.y  # Adjust for window center
    cursor.goto(x, y)  # Move the turtle to the mouse position
    canvas.bind("<MouseWheel>", width_select)
    


win.listen()
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)
# win.onkey(up_draw,"Up")
# win.onkey(left_draw,"Left")
# win.onkey(down_draw,"Down")
# win.onkey(right_draw,"Right")


win.mainloop()

