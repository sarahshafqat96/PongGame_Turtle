from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

#Setting up the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Creating objects of our classes
right_paddle = Paddle(375, 0)
left_paddle = Paddle(-375, 0)
ball = Ball()
score = Score()
ball_speed = 0

#Binding keyboard keys with right and left paddle movement
#The left player can move their paddle up and down using "w" and "s", whereas
#The right player will use keyboard arrow keys "up" and "down" to move the paddle
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.listen()

game_is_on = True

while game_is_on:
    if ball.ycor() > 280 or ball.ycor() < -280:                 #Checking collision with walls
        ball.y_bounce()                                         #If there is collision, ball bounces in the y-direction

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.x_bounce()                                         #If ball collides with paddles, it will bounce in the x-direction
        if ball.ball_speed >= 0.04:                             #If ball speed is greater than 0.04 (0.04 is the max speed)
            ball.ball_speed = ball.ball_speed - 0.01            #Then increase its speed by 0.01.

    if ball.xcor() > 380:                                       #If ball misses the right paddle
        score.increment_lscore()                                #Left player's score will increase
        ball.goto(0, 0)                                         #Ball will reset itself at center
    if ball.xcor() < -380:                                      #Similarly if ball missed the left paddle
        score.increment_rscore()                                #Right player's score will increase
        ball.goto(0, 0)                                         #Ball will reset itself at center

    ball.ball_move()                                            #Call the move function from Ball class
    score.show_score()                                          #Display the score
    time.sleep(ball.ball_speed)                                 #Using time.sleep function to control ball's speed
    screen.update()                                             #Update the screen


screen.exitonclick()                                            #Screen will exit when "X" is "clicked
