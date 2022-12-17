#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()

    for i in range(6):
        fill_cell()
        while cell_is_filled() == True:
            while wall_is_on_the_right() == False:
                fill_cell()
                move_right()
            while wall_is_on_the_right() == True:
                move_down()
                move_left()
            while wall_is_on_the_left() == False:
                fill_cell()
                move_left()
            while wall_is_on_the_left() == True:
                move_down()
                move_right()



if __name__ == '__main__':
    run_tasks()
