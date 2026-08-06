import colorsys
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

h = 0
for i in range(200):
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)   # returns values between 0–1
    t.pencolor(r, g, b)                      # turtle accepts floats 0–1
    h += 0.005
    t.forward(i)
    t.left(59)

turtle.done()
