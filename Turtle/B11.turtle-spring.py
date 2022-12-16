import turtle

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
r = 50
def spring(r):
    for i in range(6):
        turtle.circle(-50, 180, 10)
        turtle.circle(-10, 180, 10)

spring(r)
turtle.exitonclick()
