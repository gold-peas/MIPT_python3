import turtle

turtle.shape("turtle")
def flower(r, n):
    for i in range(n):
        turtle.right(360/n)
        turtle.circle(r)

for i in range(1):
    flower(60, 6)
