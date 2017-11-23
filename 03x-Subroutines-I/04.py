from math import atan,sqrt,pi
from turtlelab3x import turtle,home,shop,check
turtle.left(atan(shop.y/shop.x)/pi*180)
turtle.forward(sqrt(shop.x**2+shop.y**2))
turtle.right(atan(shop.y/shop.x)/pi*180)
#@ shop
turtle.left(atan((home.y-shop.y)/(home.x-shop.x))/pi*180)
turtle.forward(sqrt((home.x-shop.x)**2+(home.y-shop.y)**2))
check()
