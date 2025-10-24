from turtle import *
turt = Turtle()
sides = int(input("How many sides would you like? "))
angle = 360 / sides
for i in range (sides):
    turt.forward(50)
    turt.right(angle)