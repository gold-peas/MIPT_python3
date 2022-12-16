import turtle

turtle.shape('turtle')
turtle.left(180)
def stars(n):
    for i in range(n):
        turtle.forward(200)
        turtle.left(180 -(180/n))
        
stars(11)
turtle.exitonclick()
