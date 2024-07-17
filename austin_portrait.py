import turtle
screen = turtle.Screen()
screen.title("Austin Portrait")
t = turtle.Turtle()
t.pensize(20)

t.color("yellow")
#austin's head
t.begin_fill()
t.circle(100)
t.end_fill()

t.color("yellow")
t.pensize(20)
t.forward(200)
t.backward(400)
t.forward(200)

t.pensize(40)
t.right(90)
t.forward(200)

t.right(45)
t.forward(200)
t.backward(200)

t.left(90)
t.forward(200)
t.backward(200)
screen.exitonclick()