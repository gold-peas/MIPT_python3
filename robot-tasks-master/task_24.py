#!/usr/bin/python3

from pyrob.api import *


def move1():  
    move_up()
    fill_cell()
    move_right()
    move_down()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_up()

@task
def task_2_1():
    for i in range(2):
        move_right()
        move_down()
    fill_cell()
    move1()


if __name__ == '__main__':
    run_tasks()
