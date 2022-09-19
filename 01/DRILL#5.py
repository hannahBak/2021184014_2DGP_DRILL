import turtle

def restart():
    turtle.reset()

def W_move():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def A_move():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def S_move():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def D_move():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

turtle.shape('turtle')

turtle.onkey(W_move, 'w')
turtle.onkey(A_move, 'a')
turtle.onkey(S_move, 's')
turtle.onkey(D_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
