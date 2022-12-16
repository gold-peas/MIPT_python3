import turtle

turtle.shape("turtle")
def circle1(x, n):
        for i in range(10):
                turtle.left(90)
                turtle.circle(x, 360, n)
                turtle.penup()
                turtle.right(90)
                turtle.forward(25)
                turtle.pendown()
                x = (x + 25)
                n = (n + 1)
            
for i in range(1):
        circle1(50, 3)
        

