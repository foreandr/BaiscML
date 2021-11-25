def f():
    a = 5
    b = 6
    c = 7
    return a, b, c


i, j, k = f()

from pywinauto.application import Application
import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'):  # if key 'q' is pressed
            print('a!')
            continue
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('q!')
            continue # finishing the loop
    except:
        break  # if user pre
