#!/usr/bin/python3

from pyrob.api import *
def move1():
    for x in range(4):
        move_left()


@task
def task_7_6():
    x = 0
    while True:
        move_right()
        if cell_is_filled() == True:
            x += 1
        if x == 5:
            break

if __name__ == '__main__':
    run_tasks()
