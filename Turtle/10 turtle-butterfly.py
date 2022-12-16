import turtle

turtle.shape('turtle')
turtle.left(90)
r = 50
def butterfly(r):
    for i in range(10):
        turtle.circle(r)
        turtle.circle(-r)
        r += 10

butterfly(r)
turtle.exitonclick()
