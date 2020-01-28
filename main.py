#! /bin/python3
import curses
import keyboard
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

class Settings:
    def __init__(self, input_key, wait_time):
        self.input_key = input_key
        self.wait_time = wait_time
        self.should_run = False
        self.walk_forwards = False
        self.repeats = 0

def press_key(settings: Settings):
    for i in range(int(settings.repeats)):
        keyboard.press(str(settings.input_key))
        time.sleep(int(settings.wait_time))


def check_walk():
    walk_forwards = False
    valid_response = False

    while not valid_response:
        valid_response = True
        walk_input = input("walk forwards? (Y/N)")
        if (walk_input == "Y" or walk_input == "y"):
            walk_forwards = True
        elif (walk_input == "N" or walk_input == "n"):
            walk_forwards = False
        else:
            print("Ansver Y or N")
            valid_response = False

    return walk_forwards


def get_settings():
    settings = Settings(
            input("What key?"),
            input("what time?"),
            )
    
    settings.walk_forwards = check_walk()
    if settings.walk_forwards:
        settings.repeats = input("how many repeats before walking?")

    return settings


def report_status(settings: Settings):
    print("pressing %s ... " %settings.input_key)
    print("waiting %s seconds" %settings.wait_time)

def walk_forwards(should_walk: bool):
    if walk_forwards:
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.release('w')


def run():
    settings = get_settings()

    settings.should_run = True

    while settings.should_run:
        press_key(settings)
        walk_forwards(settings.walk_forwards)
        report_status(settings)
        

def main():
    script_on = True
    while script_on:
        run()


if __name__ == "__main__":
    main()
