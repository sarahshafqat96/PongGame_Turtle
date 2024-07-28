from turtle import Turtle


class Ball(Turtle):                         #Creating Ball class
    def __init__(self):
        super().__init__()                  #Turtle as its super class
        self.shape("circle")                #Turtle/Ball shape is set as circle
        self.color("white")                 #Turtle/Ball color will be white
        self.penup()                        #Turtle/Ball should not leave any trace lines
        self.x_pos = 10                     #Turtle/Ball will initially go to these x,y co-ordinates
        self.y_pos = 10
        self.ball_speed = 0.1               #Turtle/Ball initial speed will be 0.1

    def ball_move(self):                    #Function to move the ball
        x = self.xcor() + self.x_pos        #If Ball is moving in  certain direction, it will keep
        y = self.ycor() + self.y_pos        #Moving in that direction with +10 paces
        self.goto(x, y)

    def y_bounce(self):                     #Function for bouncing in y direction
        self.y_pos *= -1                    #Invert the ball's current y c-ordinate by multiplying it with -1

    def x_bounce(self):                     #Function for bouncing in x direction
        self.x_pos *= -1                    #Invert the ball's current x co-ordinate by multiplying it with -1
