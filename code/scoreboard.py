from turtle import Turtle


class Score(Turtle):                                   #Creating Score class
    def __init__(self):
        super().__init__()                             #Turtle as its super class
        self.penup()                                   #Turtle should not leave any trace lines
        self.ht()                                      #Hide the turtle
        self.color("white")                            #Turtle's color will be white
        self.goto(0, 200)                        #Score will be displayed at top center
        self.r_score = 0                               #Initially the scores will be set to zero
        self.l_score = 0
        self.show_score()

    def increment_rscore(self):                        #Function to increment the right player's score
        self.r_score += 1

    def increment_lscore(self):                        #Function to increment the left player's score
        self.l_score += 1

    def show_score(self):                              #Function to display the score
        self.clear()
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=("Courier", 60, "normal"))
