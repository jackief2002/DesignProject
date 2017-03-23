import turtle


boots = turtle.Turtle()
from polygons2 import *
boots.speed(0)




for times in range(1):
    jump(boots, -795 + times * 100, 315)
    pattern1(boots)


for times in range(1):
    jump(boots, -795 + times * 100, 215)
    pattern2(boots)


for times in range(1):
    jump(boots, -795 + times * 100, 115)
    pattern3(boots)


for times in range(1):
    jump(boots, -795 + times * 100, 15)
    pattern4(boots)


for times in range(1):
    jump(boots, -795 + times * 100, -85)
    pattern5(boots)


for times in range(1):
    jump(boots, -795 + times * 100, -185)
    pattern6(boots)


for times in range(1):
    jump(boots, -795 + times * 100, -285)
    pattern7(boots)


for times in range(1):
    jump(boots, -795 + times * 100, -385)
    pattern8(boots)


