from turtlelab8 import turtle,radar,check
dic = {'e':0 , 'ne':45 , 'n':90, 'nw':135, 'w':180, 'sw':225, 's':270, 'se':315}
while radar.ball_direction()!='x':
    s = dic[radar.ball_direction()]
    turtle.left(s)
    turtle.forward(1)
    turtle.right(s)
check()
