import turtle

turtle.left(90)
count1 = 0

while (count1 <= 500):
    turtle.penup()
    turtle.goto(count1,0)
    turtle.pendown()
    turtle.forward(500)
    count1 = count1 + 100
    
turtle.right(90)
count = 0
while (count <= 500):
    turtle.penup()
    turtle.goto(0,count)
    turtle.pendown()
    turtle.forward(500)
    count = count + 100
