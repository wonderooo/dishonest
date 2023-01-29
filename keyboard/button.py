from machine import Pin
from collections import deque
from time import ticks_ms, ticks_diff

class Button(object):
    def __init__(self, pin_fun: tuple, cmd_buffer: deque) -> None:
        self.pin_id = pin_fun[0]
        self.cmd = pin_fun[1]
        self.cmd_alt1 = pin_fun[2]
        self.cmd_alt2 = pin_fun[3]
        self.cmd_alt3 = pin_fun[4]

        self.cmd_buffer = cmd_buffer

        self.pin = Pin(self.pin_id, Pin.IN)
        self.pin.irq(trigger=Pin.IRQ_RISING, handler=self.high_state_handler)

        self.last = None
        self.strike = 0
    
    def high_state_handler(self, pin):
        if self.last is None:
            self.last = ticks_ms()
            self.cmd_buffer.append((self.cmd, 'static'))
        else:
            curr = ticks_ms()
            diff = ticks_diff(curr, self.last)
            #print('diff: ' + str(diff) + ' curr: ' + str(curr) + ' last: ' + str(self.last))
            if diff < 1000:
                self.last = curr
                self.strike += 1
                cmd = None

                if self.strike > 3:
                    self.strike = 0

                if self.strike == 0:
                    cmd = self.cmd
                elif self.strike == 1:
                    cmd = self.cmd_alt1
                elif self.strike == 2:
                    cmd = self.cmd_alt2
                elif self.strike == 3:
                    cmd = self.cmd_alt3

                self.cmd_buffer.append((cmd, 'replace'))
            else: 
                self.last = curr
                self.strike = 0
                self.cmd_buffer.append((self.cmd, 'static'))
