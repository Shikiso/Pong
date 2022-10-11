import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Class to create game objects
class game_object:
    location = (0,0)
    gameObj = None

    def __init__(self, location, type):
        self.location = location
        self.create_object()
        if type == "paddle":
            self.stretch()
        else:
            self.seperate_movement()
    
    def create_object(self):
        gameObj = turtle.Turtle()
        gameObj.speed(0)
        gameObj.shape("square")
        gameObj.color("white")
        gameObj.penup()
        gameObj.goto(self.location[0], self.location[1])

        self.gameObj = gameObj
    
    def stretch(self):
        self.gameObj.shapesize(stretch_wid=5, stretch_len=1)
    
    def seperate_movement(self):
        moveVal = 0.2
        self.gameObj.dx = moveVal
        self.gameObj.dy = moveVal

# Objects
paddle_a = game_object((-350, 0), "paddle").gameObj
paddle_b = game_object((350, 0), "paddle").gameObj
ball = game_object((0, 0), "ball").gameObj

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Movement Class
class paddle_movement:

    def __init__(self):
        wn.listen()
        wn.onkeypress(self.paddle_a_up, "w")
        wn.onkeypress(self.paddle_a_down, "s")
        wn.onkeypress(self.paddle_b_up, "Up")
        wn.onkeypress(self.paddle_b_down, "Down")

    def move(self, paddle, increase):
        y = paddle.ycor()
        y += increase
        paddle.sety(y)

    def paddle_a_up(self):
        self.move(paddle_a, 20)

    def paddle_a_down(self):
        self.move(paddle_a, -20)
    
    def paddle_b_up(self):
        self.move(paddle_b, 20)

    def paddle_b_down(self):
        self.move(paddle_b, -20)

# Keyboard binding
paddle_movement()

def write_score():
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Main game loop
while 1:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        write_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        write_score()

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        
