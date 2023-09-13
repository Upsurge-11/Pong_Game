import turtle
# import  winsound

wn = turtle.Screen()

wn.title("Pong Game")

wn.bgcolor("black")

wn.setup(width=800, height=600)  # (0,0) is in centre.

wn.tracer(0)

# Scores

score_a = 0
score_b = 0

# Paddle A
paddleA = turtle.Turtle()    # module.class
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()    # module.class
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
Ball = turtle.Turtle()    # module.class
Ball.speed(0)
Ball.shape("square")
Ball.color("red")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.1
Ball.dy = 0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

# Functions


def paddleAUp():
    y=paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleADown():
    y=paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUp():
    y=paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleBDown():
    y=paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard Binding


wn.listen()
wn.onkeypress(paddleAUp, "w")
wn.onkeypress(paddleADown, "s")
wn.onkeypress(paddleBUp, "Up")
wn.onkeypress(paddleBDown, "Down")

# Game loop
running=True
while running:

    wn.update()

    # Move the ball

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border Checking

    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        # winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        # winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))


    # Paddle and ball collision
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddleB.ycor() + 40 and Ball.ycor() > paddleB.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1
        # winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddleA.ycor() + 40 and Ball.ycor() > paddleA.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
        # winsound.PlaySound("laser.wav", winsound.SND_ASYNC)