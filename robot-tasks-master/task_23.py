#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    move_right()
    while wall_is_on_the_right() == False:
        if wall_is_above() == False:
            while wall_is_above() == False:
                move_up()
                fill_cell()

        if wall_is_above() == True:
            while wall_is_beneath() == False:
                move_down()
            move_right()

    if wall_is_on_the_right() == True:
        while wall_is_above() == False:
            move_up()
            fill_cell()
    if wall_is_above() == True:
        while wall_is_beneath() == False:
            move_down()

    while wall_is_beneath() == True:
        move_left()


if __name__ == '__main__':
    run_tasks()
