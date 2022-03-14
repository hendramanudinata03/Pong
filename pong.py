# Pong Game
# Simple Pong game written in Python.
#
# Tutorial I've followed: https://www.youtube.com/watch?v=C6jJg9Zan7w&t=211s


# Import Turtle for GUI
import turtle

# Initialize Turtle window
window = turtle.Screen()

# Turtle window setup
window.title("Pong!")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Initialize score
score = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=7, stretch_len=1)
paddleA.penup()
paddleA.goto(-360, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=7, stretch_len=1)
paddleB.penup()
paddleB.goto(360, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(-200, 0)
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

# Functions: Move paddle A Up
def paddleA_up():
	paddleA_y = paddleA.ycor()
	paddleA_y += 25
	paddleA.sety(paddleA_y)

# Functions: Move paddle A Down
def paddleA_down():
	paddleA_y = paddleA.ycor()
	paddleA_y -= 25
	paddleA.sety(paddleA_y)

# Functions: Move paddle B Up
def paddleB_up():
	paddleB_y = paddleB.ycor()
	paddleB_y += 25
	paddleB.sety(paddleB_y)

# Functions: Move paddle B Down
def paddleB_down():
	paddleB_y = paddleB.ycor()
	paddleB_y -= 25
	paddleB.sety(paddleB_y)

# Keyboard binding
window.listen()
window.onkeypress(paddleA_up, "Up")
window.onkeypress(paddleA_down, "Down")
window.onkeypress(paddleB_up, "Right")
window.onkeypress(paddleB_down, "Left")

# Main game loop
while True:
	# Always update the window
	window.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking
	# X coordinate
	if ball.xcor() > 380:
		ball.goto(0, 0)
		ball.dx *= -1
		ball.dx += 1
		score -= 1
		pen.clear()
		pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
	if ball.xcor() < -380:
		ball.goto(0, 0)
		ball.dx *= -1
		ball.dx -= 1
		score -= 1
		pen.clear()
		pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
	# Y coordinate
	if ball.ycor() > 280:
		ball.sety(280)
		ball.dy *= -1
	if ball.ycor() < -280:
		ball.sety(-280)
		ball.dy *= -1
	# Paddle A
	if paddleA.ycor() > 230:
		paddleA.sety(230)
	if paddleA.ycor() < -230:
		paddleA.sety(-230)
	# Paddle B
	if paddleB.ycor() > 230:
		paddleB.sety(230)
	if paddleB.ycor() < -230:
		paddleB.sety(-230)

	# Paddle and ball collisions
	if ball.xcor() < -340 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
		ball.dx *= -1
		ball.dx += 0.05
		score += 1
		pen.clear()
		pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
	if ball.xcor() > 340 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
		ball.dx *= -1
		ball.dx -= 0.05
		score += 1
		pen.clear()
		pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))
