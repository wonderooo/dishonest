from keyboard.button import Button
from keyboard.pin_assignment import *
from collections import deque

class Keyboard(object):
    def __init__(self, cmd_buffer: deque) -> None:
        self.b_0 = Button(NUM_0, cmd_buffer)
        self.b_1 = Button(NUM_1, cmd_buffer)
        self.b_2 = Button(NUM_2, cmd_buffer)
        self.b_3 = Button(NUM_3, cmd_buffer)
        self.b_4 = Button(NUM_4, cmd_buffer)
        self.b_5 = Button(NUM_5, cmd_buffer)
        self.b_6 = Button(NUM_6, cmd_buffer)
        self.b_7 = Button(NUM_7, cmd_buffer)
        self.b_8 = Button(NUM_8, cmd_buffer)
        self.b_9 = Button(NUM_9, cmd_buffer)
        self.b_add = Button(OPS_ADD, cmd_buffer)
        self.b_sub = Button(OPS_SUB, cmd_buffer)
        self.b_mul = Button(OPS_MUL, cmd_buffer)
        self.b_div = Button(OPS_DIV, cmd_buffer)
        self.b_sqr = Button(OPS_SQR, cmd_buffer)
        self.b_clr = Button(FUN_CLR, cmd_buffer)
        self.b_dot = Button(FUN_DOT, cmd_buffer)