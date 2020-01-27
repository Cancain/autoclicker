#! /bin/python3
import pynput
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

def main():
    while 1:
        keyboard.press('4')
        time.sleep(40000)
        
if __name__ == "__main__":
    main()
