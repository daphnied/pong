# @daphnied

import turtle
wn = turtle.Screen()
wn.title('Pong by @daphnied')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle Left
paddle_left = turtle.Turtle()
# animation speed
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color('pink')
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color('pink')
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('pink')
ball.penup()
ball.goto(0, 0)
# Moves ball up and diagonal 2px
# Right 2 px
ball.dx = 2
# Up 2 px
ball.dy = -2

# Function
# Move paddles up and down
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Keyboard binding
# Listen for keyboard input
wn.listen()
# Left paddle rises when w is pressed
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "p")
wn.onkeypress(paddle_right_down, "l")

#Main game loop
# Screen updates when loop runs
while True:
    wn.update()

    # Move the ball
    # Current x coord
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border - top and bottom
    # Height: 300 for top & bottom - ball: 20 (10 from ea)
    # Reverse ball direction
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy += -1

    if ball.ycor() < -290:
        ball.sety(290)
        ball.dy += -1
    # If ball is past the paddle and off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() -50):
        ball.setx(340)
        ball.dx *= -1


