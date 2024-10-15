import turtle
import numpy as np
import time

# Initializations
drawing= True
win= turtle.Screen()
win.title("Canvas")
win.setup(width=1.0, height= 1.0)

canvas= win.getcanvas()

tom=turtle.Turtle()
cursor= turtle.Turtle()
tom.hideturtle()
turtle.tracer(0)
tom.width(5)
tom.speed(100)


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
            cursor.color(keys,keys)
            col_print(keys)
            break
            
    print("Exiting color_check")

def eraser_check(x,y):
    print("Just Entered into eraser_check func")

    
    
        
    if cursor.distance(eraser_pos)<50:
        eraser_select()
        print(f"pencolor: White")
        cursor.color("black","white")
        
    print("Exiting color_check")

def clear_check(x,y):
    print("Just Entered into eraser_check func")

    
    
        
    if cursor.distance(clear_pos)<30:
       cursor.clear()
        



def color_dot(x, pos):
    tom.penup()
    tom.goto(pos)
    tom.pendown()
    tom.dot(25,"Black")
    tom.dot(20, x)
    dot_pos[x]=tom.pos()



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
    clear_check(x,y)

    
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
tom.penup()
tom.goto(-625,-200)
tom.pendown() 
tom.width(2)
tom_head=0

#Outer color border

for _ in range(2):
    tom.fd(color_bar)
    tom_head+=90
    tom.setheading(tom_head)
    tom.fd(5*color_bar)
    tom_head+=90
    tom.setheading(tom_head)


#The colar dots

tom.penup()
tom.goto(-595, 270)
tom.pendown()
x= tom.xcor()
y=tom.ycor()
for color in colors:

    
        color_dot(color[0], tom.pos())
        
        x= tom.xcor()
        y=tom.ycor()

        tom.penup()
        tom.goto(x+40,y)
        tom.pendown()

        color_dot(color[1], tom.pos())
        
        tom.penup()
        tom.goto(x,y-30)
        tom.pendown()

tom.penup()
tom.goto(x-15,y-20)
tom.pendown()
tom.width(5)
tom.setheading(0)
for _ in range(4):
    tom.fd(75)
    tom.right(90)

tom.right(45)
tom.penup()
tom.fd((((75**2)*2)**(1/2)/2))
tom.pendown()
eraser_pos=tom.pos()
print(eraser_pos)

tom.write("Eraser", font=("Aerial", 15, "normal"), align="center")

clear_bar=35
tom.penup()
tom.goto(440,290)
tom.pendown() 
tom.width(5)
tom.setheading(0)

#Outer color border

for _ in range(2):
    tom.fd(5*clear_bar-50)
    tom.left(90)
    tom.fd(clear_bar)
    tom.left(90)

tom.penup()
tom.goto(500,290)
tom.pendown()
clear_pos=tom.pos()

tom.write("CLEAR", font=("Aerial", 20, "normal"), align="center")

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
cursor.speed(0) 
cursor.width(5)
cursor.shape("circle")
cursor.penup()
cursor.goto(0,0)
cursor.pendown()


#  for user interaction--------------------
win.listen()
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)



win.mainloop()

