from graphics import *
from random import *


def move_horde():
    for ind, p in enumerate(horde):
        s = speeds[ind]
        p.undraw()
        p.x = p.x + s.x
        if p.x <= 0 or p.x >= win.width:
            p.x = p.x - s.x
            s.x = - s.x
        p.y = p.y + s.y
        if p.y <= 0 or p.y >= win.height:
            p.y = p.y - s.y
            s.y = - s.y
        p.draw(win)


if __name__ == '__main__':
    win = GraphWin("Окно для графики", 400, 400, False)
    win.flush()
    horde = []
    speeds = []
    for i in range(1000):
        point = Point(randint(0, win.width), randint(0, win.height))
        color = randint(0, 2)
        if color == 0:
            point.setOutline("red")
        elif color == 1:
            point.setOutline("#00AA00")
        else:
            point.setOutline("blue")
        horde.append(point)
        speed = Point(randint(-5, 5), randint(-5, 5))
        if speed.x == 0 or speed.y == 0:
            speed = Point(randint(1, 5), randint(1, 5))
        speeds.append(speed)
        point.draw(win)

    while win.checkMouse() is None:
        win.flush()
        move_horde()
        time.sleep(0.001)
    win.close()
