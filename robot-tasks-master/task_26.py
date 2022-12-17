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
     move_right()


def move2():
    move_left()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_up()


def down4():
    for d in range(4):
        move_down()


def right2():
    for r in range(2):
        move_right()

def left2():
    for l in range(2):
        move_left()
        
@task(delay=0.02)
def task_2_4():

    for x in range(2):
        for i in range(9):
            move1()
            right2()
        move1()
        down4()
        for g in range(9):
            move2()
            left2()
        move2()
        down4()
        
    for y in range(9):
        move1()
        right2()
    move1()

    while wall_is_on_the_left() == False:
            move_left()
    

if __name__ == '__main__':
    run_tasks()
