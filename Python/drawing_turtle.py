from turtle import Turtle
import turtle
import random







def recursive_circles(turtle, radius, iterations):
    colors = ["red", "orange", "brown", "green", "blue", "purple"]
    color = random.choice(colors)
    radius = radius-1
    iterations = iterations-1
    turtle.color(color)
    turtle.circle(radius)
    turtle.right(90)
    for i in range(0,19):
        turtle.right(20)
        turtle.circle(radius - i)
    if(iterations >= 0):
        recursive_circles(turtle, radius, iterations)
    
def main():
    ANIMATION_SPEED = 0
    screen = turtle.Screen()
    leonardo = Turtle()
    leonardo.speed(ANIMATION_SPEED)
    recursive_circles(leonardo, 40, 3)
    screen.exitonclick()
main()

