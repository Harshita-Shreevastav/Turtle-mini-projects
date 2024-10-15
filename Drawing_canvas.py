import turtle
import numpy as np
import time

# Initializations
drawing= True
win= turtle.Screen()
win.title("Canvas")
win.setup(width=1.0, height= 1.0)

canvas= win.getcanvas()

cursor= turtle.Turtle()
cursor.hideturtle()
turtle.tracer(0)
cursor.width(5)
cursor.speed(100)


dot_pos={}
pre_pos = (0,0) 
pre_key = ' ' 



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


def col_print(keys):
    text.clear()
    text.width(5)
    text.penup()
    text.pendown()
    text.write(f"Color:   {keys}", font=("Aerial", 15, "normal"), align="left")

def wid_print(wid):
    
    wid_c.clear()
    wid_c.width(5)
    
    wid_c.write(f"Width:   {wid}(Scroll to change the width))", font=("Aerial", 15, "normal"), align="left")

def eraser_select():

    eraser_c.setheading(0)
    eraser_c.begin_fill()
    for _ in range(4):
        eraser_c.fd(75)
        eraser_c.right(90)
    eraser_c.end_fill()

    eraser_c.right(45)
    eraser_c.penup()
    eraser_c.goto(eraser_pos)
    eraser_c.pendown()
    eraser_c.pencolor("white")
    eraser_c.write("Eraser", font=("Aerial", 15, "normal"), align="center")
    eraser_c.penup()
    eraser_c.goto(e_edge)
    eraser_c.pendown()
    eraser_c.color("black", "AntiqueWhite3")

def color_check(x,y):
    print("Just Entered into color_check func")

    
    for keys in dot_pos:
        pos=dot_pos[keys]
        
        if cursor.distance(pos)<13:
            print(f"pencolor: {keys}")
            eraser_c.clear()
            cursor.pencolor(keys)
            col_print(keys)
            break
            
    print("Exiting color_check")

def eraser_check(x,y):
    print("Just Entered into eraser_check func")

    
    
        
    if cursor.distance(eraser_pos)<50:
        eraser_select()
        print(f"pencolor: White")
        cursor.pencolor("white")
        
    print("Exiting color_check")



def color_dot(x, pos):
    cursor.penup()
    cursor.goto(pos)
    cursor.pendown()
    cursor.dot(25,"Black")
    cursor.dot(20, x)
    dot_pos[x]=cursor.pos()



#Fuction that tell the cursor to START DRAWING AGAIN when the left mouse button is clicked

def continue_drawing():
    print("Just entered into continue_drawing")
    print("Drawing = False")
    global drawing
    drawing = True
    print("Drawing = True")
    print("IExiting continue_drawing")
    canvas.bind("<ButtonPress-1>", on_click)

#Function that decreases or increases the cursor width on scrolling

def width_select(event):
    if event.delta>0:
        if cursor.width()<=10:
            new_width= cursor.width()+1
            cursor.width(new_width)
            
            wid_print(new_width)

    if event.delta<0:
        if cursor.width()>=1:
            new_width= cursor.width()-1
            cursor.width(new_width)
            
            wid_print(new_width)
            

#Function to stop drawing when mouse left button is released
def on_release(event):
    print("Just Entered into on_release func")
    cursor.penup()
    drawing=False
    print("Drawing = False")
    print("Exiting on_release")
    continue_drawing()

#Fuction that tell the cursor to START DRAWING when the left mouse button is clicked

def on_click(event):
    print('Entered into on_click fund')
    x = event.x - win.window_width() / 2  # Adjust for window center
    y = win.window_height() / 2 - event.y 

    cursor.penup() # Adjust for window center
    cursor.goto(x, y) 
    cursor.pendown() # Move the turtle to the mouse position
    
    print(cursor.pos())
    print("Going inside color_check func")
    eraser_check(x,y)
    color_check(x,y)

    
    print("Back Into on_click")    
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
cursor.goto(-595, 270)
cursor.pendown()
x= cursor.xcor()
y=cursor.ycor()
for color in colors:

    
        color_dot(color[0], cursor.pos())
        
        x= cursor.xcor()
        y=cursor.ycor()

        cursor.penup()
        cursor.goto(x+40,y)
        cursor.pendown()

        color_dot(color[1], cursor.pos())
        
        cursor.penup()
        cursor.goto(x,y-30)
        cursor.pendown()

cursor.penup()
cursor.goto(x-15,y-20)
cursor.pendown()
cursor.width(5)
cursor.setheading(0)
for _ in range(4):
    cursor.fd(75)
    cursor.right(90)

cursor.right(45)
cursor.penup()
cursor.fd((((75**2)*2)**(1/2)/2))
cursor.pendown()
eraser_pos=cursor.pos()
print(eraser_pos)

cursor.write("Eraser", font=("Aerial", 15, "normal"), align="center")

text=turtle.Turtle()
text.hideturtle()
text.speed(0)
text.pencolor("Black")

text.width(5)
text.penup()
text.goto(-400, 300)
text.pendown()
text.write("Color: Black", font=("Aerial", 15, "normal"), align="left")

wid_c=turtle.Turtle()
wid_c.hideturtle()
wid_c.speed(0)
wid_c.pencolor("Black")

wid_c.width(5)
wid_c.penup()
wid_c.goto(-100, 300)
wid_c.pendown()
wid_c.write("Width: 5(Scroll to change the width)", font=("Aerial", 15, "normal"), align="left")

eraser_c=turtle.Turtle()
eraser_c.hideturtle()
eraser_c.speed(0)
eraser_c.color("black", "AntiqueWhite3")

eraser_c.width(5)
eraser_c.penup()
eraser_c.goto(x-15,y-20)
e_edge=eraser_c.pos()
eraser_c.pendown()






# print(dot_pos)

# dot_array=np.array(dot_pos.values())
# print(f"Array: {dot_array}")






turtle.update()
turtle.tracer(1)
cursor.showturtle() 
cursor.speed(0) 
cursor.width(5)
cursor.penup()
cursor.goto(0,0)
cursor.pendown()


#  for user interaction--------------------
win.listen()
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)



win.mainloop()

