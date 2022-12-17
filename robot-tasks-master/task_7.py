#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() == False:
            move_down()
    while wall_is_beneath() == True:
        move_right()
    while move_down():
        break
    while move_left():
        break
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
