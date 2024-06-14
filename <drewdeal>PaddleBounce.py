
"""
Created on Thur Jun 13 16:12:41 2024

@author: drewdeal

this game makes the player play a tennis like game with the ball and keep it 
from touching the ground before you lose.
"""
import turtle
import random


screen = turtle.Screen()
screen.title("Paddle Bounce ")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  


paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=8)
paddle.penup()
paddle.goto(0, -250)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-200, 200), 250)
ball.dx = 2.5  
ball.dy = -2.5  


def paddle_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)


def paddle_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 20)


screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")


while True:
    screen.update()

  
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        
        if (paddle.xcor() - 50 <= ball.xcor() <= paddle.xcor() + 50) and ball.ycor() < -240:
            ball.sety(250)  
            ball.dy *= -1  

   
    if ball.ycor() < -290:
        screen.bgcolor("red")
        ball.hideturtle()
        paddle.hideturtle()
        break


game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("white")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


screen.mainloop()
