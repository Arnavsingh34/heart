import turtle
import math
import random

# ================================
# SETUP SCREEN
# ================================

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("🎂HAPPY BIRTHDAY🎂")
screen.tracer(0)
screen.colormode(1.0)

# ================================
# Main Turtle
# ================================

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# ================================
# Particle Class
# ================================

class BirthdayParticle:

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.uniform(-430, 430)
        self.y = random.uniform(-330, 330)

        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

        self.angle = random.uniform(0, 2 * math.pi)

        self.color_base = random.random()

    def update(self, t):

        # Heart parametric Equation
        scale = 15 + 3 * math.sin(t * 0.03)

        heart_x = (
            16 * math.sin(self.angle) ** 3
        ) * scale
        heart_y = (
            13 * math.cos(self.angle)
            -5 * math.cos(2 * self.angle)
            -2 * math.cos(3 * self.angle)
            - math.cos(4 * self.angle)
        ) * scale

        # Move Particle Toward Heart
        dx = heart_x - self.x
        dy = heart_y - self.y
        self.vx += dx * 0.002
        self.vy += dy * 0.002

        # Smooth Movement
        self.vx *= 0.96
        self.vy *= 0.96

        self.vx += self.vx
        self.vy += self.vy
# ==============================
# Create Heart Particles
# ==============================

particles = (
    BirthdayParticle()
    for _ in range(300)
)


# ==============================
# Confetti
# ==============================

confetti = []

for _ in range(100):

    confetti.append({
        "x": random.randint(-440, 440),
        "y": random.randint(-330, 330),
        "speed": random.uniform(0.5, 2),
        "size": random.randint(3, 7),
        "phase": random.random() * 6.28
    })

# ==============================
# Draw heart Particles
# ==============================

def draw_particles(t):

    for p in particles:

        p.update(t)

        pen.penup()
        pen.goto(p.x, p.y)

        # RGB Color Animation
        r = abs(math.sin(t * 0.002 + p.color_base))
        g = abs(math.sin(t * 0.002 + p.color_base + 2))
        b = abs(math.sin(t * 0.002 + p.color_base + 4))

        pen.color(r, g, b)
        pen.dot(5)

# ================================
# Draw Confetti
# ================================

def draw_confetti(t):

    colors  = (
        "red",
        "yellow",
        "cyan",
        "lime",
        "magenta",
        "orange",
        "white",
    )

    for i, c in enumerate(confetti):

        c["y"] -= c["speed"]

        c["x"] += math.sin(
            t * 0.003 + c["phase"]
        ) * 0.5

        # Reset When it reaches Bottom
        if c["y"] < -350:

            c["y"] = 350
            c["x"] = random.randint(-440, 440)

        pen.penup()
        pen.goto(c["x"], c["y"])

        pen.color(colors[i % len(colors)])

        pen.dot(c["size"])

# ============================
# Draw Happy Birthday
# ============================

def draw_text(t):

        pen.penup()
        pen.goto(0, 250)

        # Changing Colors
        colors = (
            "red",
            "orange",
            "yellow",
            "lime",
            "cyan",
            "blue",
            "magenta",
        )

        color = colors[int(t / 5) % len(colors)]

        pen.color(color)

        pen.write(
            "HAPPY BIRTHDAY ASHISH",
            align="center",
            font=("Courier new",30, "bold")
        )

        # second line

        pen.goto(0, 140)

        pen.color("green")

        pen.write(
            "May this year bring you everything your heart has been quietly wishing for.",
            align="center",
            font=("Counter new", 16, "normal")
        )




# ============================
# Small Hearts
# ============================

def draw_small_hearts(t):

    positions = (
        (-300, 170),
        (300, 170),
        (-330, 40),
        (330, 40)
    )

    for i, (x, y) in enumerate(positions):

        pulse = 1 + 0.2 * math.sin(
            t * 0.008 + i
        )

        pen.penup()
        pen.goto(x, y)

        pen.color(
            ("red", "pink", "magenta", "hot pink")[i]
        )

        pen.write(
            "❤️❤️❤️",
            align="center",
            font=(
                "Arial",
                int(30 * pulse),
                "bold"
            )
        )



# ========================
# Animation Loop
# ========================


t = 0

while True:

    pen.clear()

    # Background particles
    draw_confetti(t)

    # Heart particle Animation
    draw_particles(t)



    # Small Hearts
    draw_small_hearts(t)

    # Birthday Text
    draw_text(t)

    

    # Update Screen
    screen.update()


    t  += 1