from  turtle import *
pensize(50)
color('red')
speed(10)
down()
fillcolor('white')

for i in range(5):
    lt(72)
    fd(200)
    rt(180-36)
    fd(200)
    rt(180-72)
    fd(123.6)
    up()
    lt(180)
    fd(123.6)
    down()
    rt(72)
up()
lt(90)
fd(300)
lt(90)
fd(100)


write('С днём победы!!!', move=True, font=('Arial', 30, 'bold'))



