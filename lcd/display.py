from lcd.magic_numbers import *
import gc

class Display(object):
    
    def __init__(self, i2c, addr=DEFAULT_I2C_ADDR) -> None:
        self.device = i2c
        self.device_addr: int = addr
        self.curr_x: int = 0
        self.curr_y: int = 0
        self.backgound_on: bool = False
        self.display_on: bool = True
        self.cursor_on: bool = False

        """
            init:
            bg: off
            disp: on
        """
        self.display_toggle()
        self.background_toggle()
        self.clear()
        self.entry_mode()
        self.display_toggle()
        self.clear()
        self.cursor_toggle()

        gc.collect()

    def cursor_toggle(self):
        if self.cursor_on:
            #setting off
            self.__send_command(DISPLAY_CMD | DISPLAY_ON_MASK)
            self.cursor_on = False
        else:
            #setting on
            self.__send_command(DISPLAY_CMD | DISPLAY_ON_MASK | DISPLAY_CURSOR_ON_MASK)
            self.cursor_on = True
    
    def display_toggle(self, cursor_on=True, cursor_blink_on=False):
        if self.display_on:
            #setting off
            self.__send_command(DISPLAY_CMD)
            self.display_on = False
        else:
            #setting on
            self.__send_command(DISPLAY_CMD | DISPLAY_ON_MASK)
            self.display_on = True
        
    def background_toggle(self):
        if self.backgound_on:
            self.device.writeto(self.device_addr, bytes([BACKGROUND_OFF]))
            self.backgound_on = False
        else:
            self.device.writeto(self.device_addr, bytes([BACKGROUND_ON]))
            self.backgound_on = True

        gc.collect()

    def replace_last(self, seq: str):
        self.move_cursor(self.curr_x - 1, self.curr_y)
        self.show_str(seq)

    def move_cursor(self, col: int, row: int):
        assert col < COLS and row < ROWS
        self.curr_x = col
        self.curr_y = row

        addr = col & 0x3F
        if row & 0x1:
            addr += 0x40
        if row & 0x2:
            addr += COLS

        self.__send_command(DDRAM | addr)

    def show_str(self, seq: str) -> None:
        for c in seq:
            self.__set_mem(ord(c))
            self.curr_x += 1

            if self.curr_x == (COLS - 1):
                self.curr_y += 1
            if self.curr_y == (ROWS - 1):
                self.curr_y = 0

            self.move_cursor(self.curr_x, self.curr_y)

    def clear(self) -> None:
        self.__send_command(CLEAR)
        self.__send_command(HOME)
        self.curr_x = 0
        self.curr_y = 0

    def entry_mode(self) -> None:
        self.__send_command(ENTRY | ENTRY_INCREMENT)

    def __send_command(self, cmd: int) -> None:
        byte = (
            (self.backgound_on << 0x3) |
            (((cmd >> 0x4) & 0xF) << 0x4)    
        )
        self.device.writeto(self.device_addr, bytes([byte | M_E]))
        self.device.writeto(self.device_addr, bytes([byte]))

        byte = (
            (self.backgound_on << 0x3) |
            ((cmd & 0xF) << 0x4)    
        )
        self.device.writeto(self.device_addr, bytes([byte | M_E]))
        self.device.writeto(self.device_addr, bytes([byte]))

        gc.collect()
    
    def __set_mem(self, buf: int) -> None:
        byte = (
            M_RS |
            (self.backgound_on << 0x3) |
            (((buf >> 0x4) & 0xF) << 0x4)    
        )
        self.device.writeto(self.device_addr, bytes([byte | M_E]))
        self.device.writeto(self.device_addr, bytes([byte]))

        byte = (
            M_RS |
            (self.backgound_on << 0x3) |
            ((buf & 0xF) << 0x4)    
        )
        self.device.writeto(self.device_addr, bytes([byte | M_E]))
        self.device.writeto(self.device_addr, bytes([byte]))

        gc.collect()
        
if __name__ == '__main__':
    from machine import SoftI2C, Pin

    i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=9600)
    disp = Display(i2c)
    disp.show_str('kacper')
    disp.move_cursor(20, 3)