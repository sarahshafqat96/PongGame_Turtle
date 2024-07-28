from turtle import Turtle


class Paddle(Turtle):                               #Creating Paddle class
    def __init__(self, x_pos, y_pos):
        super().__init__()                          #Turtle as its super class
        self.shape("square")                        #Turtle/Paddle shapes will be square
        self.shapesize(5, 1)                        #They will be resized to look a little rectangular
        self.color("white")                         #Their color will be white
        self.teleport(x_pos, y_pos)                 #They will be sent to these co-ordinates
        self.penup()                                #Turtle/Paddles should not leave any trace lines

    def move_up(self):                              #Function to move the paddles up
        if self.ycor() < 240:                       #Max upper y-coordinate is 240 (screen limitation)
            y = self.ycor() + 30                    #If paddle is below 240, add 30 to its position when user presses up or w
            self.goto(self.xcor(), y)

    def move_down(self):                            #Function to move the paddles down
        if self.ycor() > -230:                      #Max lower y-coordinate is -230 (screen limitation)
            y = self.ycor() - 30                    #If paddle is above -230, add 30 to its position when user presses down or s
            self.goto(self.xcor(), y)

