#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.07)
def task_9_3():
    x = 0
    while wall_is_on_the_right() == False:
        move_right()
        x += 1
        
    while wall_is_on_the_left() == False:
        move_left()

    for i in range(x + 1):
        for g in range(x):
            if (g == i or i + g == x) == False:
                fill_cell()
            move_right()
            
        if g == x - 1 and i != 0 and i != x:
            fill_cell()
        move_left(x)

        if i != x:
            move_down()
        
if __name__ == '__main__':
    run_tasks()
