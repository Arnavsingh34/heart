import turtle
import math
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Heart")
screen.tracer(0)

# Particle class
class VortexParticle:
    def __init__(self):
        self.reset()
        self.history = [(self.x, self.y)] * 5

    def reset(self):
        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color_base = random.random()
        # Each particle gets a fixed angle on the heart curve
        self.target_angle = random.uniform(0, 2 * math.pi)

    def update(self, t):
        self.history.append((self.x, self.y))
        self.history.pop(0)

        # Heart parametric equation
        scale = 15 + 3 * math.sin(t * 0.03)
        heart_x = 16 * math.sin(self.target_angle) ** 3 * scale
        heart_y = (
            13 * math.cos(self.target_angle)
            - 5 * math.cos(2 * self.target_angle)
            - 2 * math.cos(3 * self.target_angle)
            - math.cos(4 * self.target_angle)
        ) * scale

        # Move particle toward its heart position
        dx = heart_x - self.x
        dy = heart_y - self.y
        self.vx += dx * 0.002
        self.vy += dy * 0.002
        self.vx *= 0.95  # damping for smoother motion
        self.vy *= 0.95
        self.x += self.vx
        self.y += self.vy

# Create particles
particles = [VortexParticle() for _ in range(200)]
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Animation loop
t = 0
while True:
    pen.clear()
    for p in particles:
        p.update(t)
        pen.penup()
        pen.goto(p.x, p.y)
        # Color shimmer effect
        pen.dot(5, (abs(math.sin(t*0.01 + p.color_base)), 0.3, 0.8))
    screen.update()
    t += 1
