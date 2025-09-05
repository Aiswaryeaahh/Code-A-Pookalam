import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# --- Function to draw filled circle ---
def draw_circle(radius, color):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# --- Function to draw flower petals ---
def draw_flower(petal_radius, petal_count, color):
    t.color(color)
    for _ in range(petal_count):
        t.begin_fill()
        t.circle(petal_radius, 60)
        t.left(120)
        t.circle(petal_radius, 60)
        t.left(120)
        t.end_fill()
        t.left(360 / petal_count)

# --- Function to draw polka dots in a circular alignment ---
def draw_polka_ring(radius, dot_count, dot_size, color):
    t.color(color)
    for i in range(dot_count):
        angle = (360 / dot_count) * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(x, y - dot_size)  # adjust to center
        t.pendown()
        t.begin_fill()
        t.circle(dot_size)
        t.end_fill()

# --- Function to draw small flowers in a circular alignment ---
def draw_flower_ring(radius, flower_count, petal_radius, petals, color):
    for i in range(flower_count):
        angle = (360 / flower_count) * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(x, y)
        t.setheading(angle + 90)  # orient flower outward
        t.pendown()
        draw_flower(petal_radius, petals, color)
    
    # reset position back to center
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

# --- Concentric circles ---
draw_circle(250, "orange")    # outer circle
draw_circle(200, "#850E0E")   # middle circle (red)
draw_circle(150, "green")     # inner circle

# --- Polka dots arranged in circular rings ---
draw_polka_ring(175, 30, 8, "white")   # dots inside red ring
draw_polka_ring(190, 40, 8, "yellow")  # another layer closer to edge

# --- Small flowers arranged inside orange circle ---
draw_flower_ring(230, 18, 10, 6, "white")

# --- Starburst (centered) ---
t.penup()
t.goto(-114, -100)
t.pendown()
t.color("#FFFFFF", "#DE7812")   
t.begin_fill()
for i in range(72):        
    t.forward(230)         
    t.left(100)            
t.end_fill()

# --- Smaller circle inside ---
draw_circle(60, "#B266FF")

# --- Flower inside smaller circle ---
t.penup()
t.goto(0, 0)   # back to center
t.pendown()
draw_flower(60, 8, "yellow")   # smaller flower

# --- Tiny center circle inside flower ---
draw_circle(15, "violet")

t.hideturtle()
turtle.done()
