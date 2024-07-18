import turtle
s = turtle.Screen()
t = turtle.Turtle()



def polygon (size, n):
    internal_angle = (n-2)*180/n
    external_angle = 180 - internal_angle
    for i in range(n):
        t.forward(size)
        t.right(external_angle)


sides = int(input("How many sided polygon: "))
sizes = int(input("How long do you want your sides?: "))
polygon(sizes, sides)
s.exitonclick()