"""
Created by: Elliott Roach
Created on: oct 2024
This module is a Micro:bit MicroPython program
does light up all combination of RGB light
"""

from microbit import *

"""cleaning"""
display.clear()
pin14.write_digital(0)
pin15.write_digital(0)
pin16.write_digital(0)
Image.HAPPY

"""all RGB colers"""
while True:
    if button_a.is_pressed():
        """blue"""
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        """green"""
        pin13.write_digital(0)
        pin14.write_digital(1)
        pin15.write_digital(0)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        """red"""
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(1)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        """light blue"""
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(0)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        """purple"""
        pin13.write_digital(1)
        pin14.write_digital(0)
        pin15.write_digital(1)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        """dark green"""
        pin13.write_digital(0)
        pin14.write_digital(1)
        pin15.write_digital(1)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
        """white"""
        pin13.write_digital(1)
        pin14.write_digital(1)
        pin15.write_digital(1)
        sleep(1000)
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        sleep(1000)
