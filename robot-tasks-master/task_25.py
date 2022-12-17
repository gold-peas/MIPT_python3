#!/usr/bin/python3

from pyrob.api import *

def move1():
        move_down()
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_left()
        fill_cell()
        move_up()
        fill_cell()

@task
def task_2_2():

    move_down()
    for i in range(4):
        move1()
        move_right()
        move_right()
        move_right()
    move1()
    move_left()
        

if __name__ == '__main__':
    run_tasks()
