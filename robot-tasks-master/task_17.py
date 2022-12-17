#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while cell_is_filled() == False:
        move_up()
    if cell_is_filled() == True:
        move_right()
        while cell_is_filled() == False:
            move_left()
            if cell_is_filled() == True:
                move_left()










if __name__ == '__main__':
    run_tasks()
