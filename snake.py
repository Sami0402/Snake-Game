from turtle import Turtle
POSITION = [(0,0),(-20,0),(-40,0)]
M = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.turtles.append(snake)
    def extend(self):
        self.add_segment(self.turtles[-1].position())
    def move(self):
        for turtle in range(len(self.turtles)-1,0,-1):
            x = self.turtles[turtle - 1].xcor()
            y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(x,y)
        self.head.forward(M)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for snake in self.turtles:
            snake.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
