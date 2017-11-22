from math import atan,sqrt,pi
from turtlelab3 import turtle,home,check
turtle.left(atan(home.y/home.x)/pi*180)
turtle.forward(sqrt(home.x**2+home.y**2))
check()
