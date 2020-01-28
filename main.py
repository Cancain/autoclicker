#! /bin/python3
import time
import pynput

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
mouse_buttons = pynput.mouse.Button

class Settings:
    def __init__(self, input_key, wait_time):
        self.input_key = input_key
        self.wait_time = wait_time
        self.should_run = False
        self.walk_forwards = False
        self.should_doubleclick = False
        self.repeats = 0
        self.walk_time = 0

def press_key(settings: Settings):
    for i in range(int(settings.repeats)):
        keyboard.press(str(settings.input_key))
        time.sleep(int(settings.wait_time))
        report_status(settings)


def check_walk():
    walk_forwards = False
    valid_response = False

    while not valid_response:
        valid_response = True
        walk_input = input("walk forwards? (Y/N) ")
        if (walk_input == "Y" or walk_input == "y"):
            walk_forwards = True
        elif (walk_input == "N" or walk_input == "n"):
            walk_forwards = False
        else:
            print("Ansver Y or N ")
            valid_response = False

    return walk_forwards

def setup_doubleclick():
    should_doubleclick = False
    valid_response = False
    while not valid_response:
        valid_response = True
        click_input = input("Should doubleclick? (Y/N) ")

        if (click_input == "Y" or click_input == "y"):
            should_doubleclick = True
        elif (click_input == "N" or click_input == "n"):
            should_doubleclick = False
        else:
            print("Ansver Y or N ")
            valid_response = False

    return should_doubleclick


def setup_walk(settings: Settings):
    if settings.walk_forwards:
        settings.repeats = input("how many repeats before walking? ")
        settings.walk_time = input("Walk for? ... (seconds) ")

    settings.should_doubleclick = setup_doubleclick()


def get_settings():
    settings = Settings(
            input("What key? "),
            input("what time? "),
            )
    
    settings.walk_forwards = check_walk()
    setup_walk(settings)

    return settings


def report_status(settings: Settings):
    print("pressing %s ... " %settings.input_key)
    print("waiting %s seconds" %settings.wait_time)

def walk_forwards(wait_time: int):
    if wait_time != 0:
        print("walking for %s seconds" %wait_time)
        keyboard.press('w')
        time.sleep(int(wait_time))
        keyboard.release('w')

def doubleclick(should_doubleclick: bool):
    if should_doubleclick:
        print("doubleclicking...")
        mouse.press(mouse_buttons.left)
        mouse.release(mouse_buttons.left)
        time.sleep(0.1)
        mouse.press(mouse_buttons.left)
        mouse.release(mouse_buttons.left)

def countdown(count: int):
    print("Starting in...")
    for i in range(count):
        time.sleep(1)
        print(count - i)

def run():
    settings = get_settings()

    settings.should_run = True

    countdown(5)

    while settings.should_run:
        press_key(settings)
        walk_forwards(settings.walk_time)
        doubleclick(settings.should_doubleclick)
        print("\n-----------Finished rotation-----------\n")
        

def main():
    script_on = True
    while script_on:
        run()


if __name__ == "__main__":
    main()
