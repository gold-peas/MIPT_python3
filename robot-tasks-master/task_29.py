#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    x = 0
    while wall_is_on_the_right() == False:
        
        if cell_is_filled() == True:
            x += 1
        else:
            x = 0
        if x == 3:
            break
        move_right()

        
if __name__ == '__main__':
    run_tasks()
