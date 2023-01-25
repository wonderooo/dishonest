Lcd initialization steps:
1. i2clcd class init ->
2. lcdapi init ->
3. actual init process: 
   1. display off
   2. backlight on
   3. lcd clear 
   4. send entry cmd
   5. hide cursor
   6. display on

Display on/off

addr: 1dcb
d - display on/off
c - cursor on/off
b - cursor blink on/off

(0x1 << 3) | (((0x8 >> 4) & 0xF) << 4)

0x1 shift 3 l -> 0x8
0x8 shift 4 r -> 0x0
0x0 & 0xF -> 0x0
0x0 shift 4 l -> 0x0
0x8 or 0x0 ->
    1000
    0000
    ----
    1000 -> 0x8

0x8 or 0x4 ->
    1000
    0100 -> 1100

FIRST COMMAND: 1(1)00, 2nd 1 is d so lcd on
SECOND COMMAND: 1000, so lcd on apperantly


0x1 << 3 -> 0x8
0x8 & 0xF
    1000
    1111 -> 1000
0x8 << 4 -> 0x80

0x8 | 0x80 ->
    10000000
    00001000 -> 10001000

10001000
00000100 or
10001100 (0x8c)


Entry Mode

coms: 
0xc
0x8
0x6B
0x68

put char
'k' - 0x6B
0x6D
0x69
0xBD
0xB9

0110 1011
10 0110 1011 would be on 8 bit instruction set

10 0110
10 1011 that on 4 bit set
