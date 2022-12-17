#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_5_10():
    fill_cell()

    while wall_is_beneath() == False:
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        while wall_is_on_the_left() == False:
            fill_cell()
            move_left()
        fill_cell()


if __name__ == '__main__':
    run_tasks()
