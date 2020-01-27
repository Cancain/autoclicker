#! /bin/python3
import curses
import keyboard
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

class Settings:
    input_key = ''
    wait_time = 0
    should_run = False


def press_key(settings: Settings):
    keyboard.press(str(settings.input_key))
    time.sleep(int(settings.wait_time))


def get_settings():
    settings = Settings()
    settings.input_key = input("What key?")
    settings.wait_time = input("Wait time?")
    return settings


def report_status(settings: Settings):
    print("pressing %s ... " %settings.input_key)
    print("waiting %s seconds" %settings.wait_time)


def run():
    settings = get_settings()

    settings.should_run = True

    while settings.should_run:
        press_key(settings)
        report_status(settings)
        

def main():
    script_on = True
    while script_on:
        run()


if __name__ == "__main__":
    main()
