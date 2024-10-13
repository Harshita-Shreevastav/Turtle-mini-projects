import turtle

# Initializations
drawing= True
win= turtle.Screen()
win.title("Canvas")
win.setup(width=1.0, height= 1.0)

canvas= win.getcanvas()

cursor= turtle.Turtle()
cursor.width(5)
cursor.speed(100)



colors=[["red", "DarkRed"],
        ["green", "DarkGreen"],
        ["blue", "DeepSkyBlue"],
       [ "yellow", "DarkGoldenrod"],
        ["orange", "coral"],
        ["pink", "DeepPink"],
        ["grey", "DarkGrey"],
        ["DarkOrchid", "DarkViolet"],
        ["brown","chocolate"],
        ["aquamarine", "DarkSeaGreen"],
        ["AliceBlue", "cornsilk"],
        ["DarkSalmon", "cyan"],
        ["White", "Black"]]






#Function to create color dots for color selection ------------

def color_dot(x, pos):
    cursor.penup()
    cursor.goto(pos)
    cursor.pendown()
    # cursor.dot(30,"Black")
    cursor.dot(25, x)



#Fuction that tell the cursor to START DRAWING AGAIN when the left mouse button is clicked

def continue_drawing():
    global drawing
    drawing = True
    canvas.bind("<ButtonPress-1>", on_click)

#Function that decreases or increases the cursor width on scrolling

def width_select(event):
    if event.delta>0:
        if cursor.width()<=10:
            new_width= cursor.width()+1
            cursor.width(new_width)

    if event.delta<0:
        if cursor.width()>=1:
            new_width= cursor.width()-1
            cursor.width(new_width)

#Function to stop drawing when mouse left button is released
def on_release(event):
    cursor.penup()
    drawing=False
    continue_drawing()

#Fuction that tell the cursor to START DRAWING when the left mouse button is clicked

def on_click(event):
    x = event.x - win.window_width() / 2  # Adjust for window center
    y = win.window_height() / 2 - event.y 
    cursor.penup() # Adjust for window center
    cursor.goto(x, y) 
    cursor.pendown() # Move the turtle to the mouse position
    canvas.bind("<MouseWheel>", width_select)
    
    canvas.bind("<Motion>", draw)


#Function that tracks the mouse movement and follows it -------

def draw(event):
    x = event.x - win.window_width() / 2  # Adjust for window center
    y = win.window_height() / 2 - event.y  # Adjust for window center
    cursor.goto(x, y)  # Move the turtle to the mouse position
    canvas.bind("<MouseWheel>", width_select)

#Customizing Canvas -----

# Placing the color selection bar

color_bar=100
cursor.penup()
cursor.goto(-625,-200)
cursor.pendown() 
cursor.width(2)
cursor_head=0

#Outer color border

for _ in range(2):
    cursor.fd(color_bar)
    cursor_head+=90
    cursor.setheading(cursor_head)
    cursor.fd(5*color_bar)
    cursor_head+=90
    cursor.setheading(cursor_head)


#The colar dots

cursor.penup()
cursor.goto(-595, 280)
cursor.pendown()

for color in colors:

    
        color_dot(color[0], cursor.pos())

        x= cursor.xcor()
        y=cursor.ycor()

        cursor.penup()
        cursor.goto(x+40,y)
        cursor.pendown()

        color_dot(color[1 ], cursor.pos())
        
        cursor.penup()
        cursor.goto(x,y-30)
        cursor.pendown()

# Cursor width

cursor.penup()
cursor.goto(x-8,y-40)
cursor.pendown()
cursor.setheading(0)
wid= 10
for _ in range(5):

    x= cursor.xcor()
    y=cursor.ycor()
    cursor.width(wid)
    cursor.fd(60)
    wid-=2

    cursor.penup()
    cursor.goto(x,y-15)
    cursor.pendown()



        


#  for user interaction--------------------
win.listen()
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)



win.mainloop()

