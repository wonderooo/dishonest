from lcd.display import Display
from keyboard.keyboard import Keyboard
from machine import SoftI2C, Pin
from collections import deque

if __name__ == '__main__':
    i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=9600)
    display = Display(i2c)

    queue: deque = deque((), 16)
    keyboard = Keyboard(queue)

    while True:
        if len(queue) > 0:
            char, cmd = queue.popleft()

            if cmd == 'replace':
                display.replace_last(char)
            else:
                display.show_str(char)
        
        