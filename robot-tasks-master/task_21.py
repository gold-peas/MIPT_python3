#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range(14):
        for x in range(i):
            move_right()
            fill_cell()
        move_down()
        while wall_is_on_the_left() == False:
            move_left()
    move_right()


if __name__ == '__main__':
    run_tasks()
