import turtle

def bezier_curve(t):
    x = 3*(1-t)**2*t + 9*(1-t)*t**2 + 4*t**3
    y = 2*(1-t)**3 - 6*(1-t)**2*t + 3*t**3
    return x, y

turtle.speed(0)
turtle.penup()
turtle.goto(0, 200)

for t in range(0, 100):
    x, y = bezier_curve(t/100)
    turtle.pendown()
    turtle.goto(x * 50, 200 - y * 50)  # Ajuste de escala para melhor visualização

turtle.done()