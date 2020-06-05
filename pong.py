# Pong in Python 3

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

# Ball

#Main game loop
# Screen updates when loop runs
while True:
    wn.update()
