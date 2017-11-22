from turtlelab2x import turtle,home,shop,check
turtle.forward(shop.x)
turtle.left(90)
turtle.forward(shop.y)
turtle.forward(home.y-shop.y)
turtle.right(90)
turtle.forward(home.x-shop.x)
check()
