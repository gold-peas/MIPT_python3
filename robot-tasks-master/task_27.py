#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    
    for i in range(10):
        for g in range(i):
            if wall_is_on_the_right() == False:
                move_right()
        if wall_is_on_the_right() == False:
            fill_cell()
        

if __name__ == '__main__':
    run_tasks()
