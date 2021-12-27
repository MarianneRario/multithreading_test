import time

from ppadb.client import Client as AdbClient

import adb_controls
import screenshot


def connect():
    client = AdbClient(host="127.0.0.1", port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    cp3 = devices[2]

    return cp3, client


def login(url, email, password):
    cp3, client = connect()
    cp3.shell(f'am start -n {adb_controls.chrome_incognito}')
    time.sleep(2)
    cp3.shell(f'input tap {adb_controls.search_bar}')
    cp3.shell(f'input text "{url}"')
    time.sleep(5)
    cp3.shell(f'input {adb_controls.enter}')
    time.sleep(8)
    cp3.shell(f'input swipe {adb_controls.swipe_down}')
    time.sleep(5)
    cp3.shell(f'input tap {adb_controls.login}')
    time.sleep(5)
    cp3.shell(f'input tap {adb_controls.emailc12}')
    time.sleep(5)
    cp3.shell(f'input text "{email}"')
    time.sleep(5)
    cp3.shell(f'input {adb_controls.tab}')
    time.sleep(1)
    cp3.shell(f'input text "{password}"')
    time.sleep(5)
    cp3.shell(f'input {adb_controls.enter}')
    time.sleep(10)
    cp3.shell(f'input swipe {adb_controls.swipe_down}')
    time.sleep(2)


def comment(com, filename):
    cp3, client = connect()
    cp3.shell(f'input tap {adb_controls.comment}')
    time.sleep(5)
    cp3.shell(f'input swipe {adb_controls.swipe_down}')
    time.sleep(5)
    cp3.shell(f'input tap {adb_controls.comment_box}')
    time.sleep(5)
    cp3.shell(f'input text "{com}"')
    time.sleep(5)
    cp3.shell(f'input {adb_controls.tab}')
    time.sleep(5)
    cp3.shell(f'input {adb_controls.enter}')
    time.sleep(10)
    ss = cp3.screencap()
    screenshot.get_screen(filename, ss)
    time.sleep(10)
    cp3.shell(f'input {adb_controls.home}')
    time.sleep(1)
    cp3.shell(f'input swipe {adb_controls.notification}')
    time.sleep(1)
    cp3.shell(f'input tap {adb_controls.clear_incognito}')


def reaction(react):
    cp3, client = connect()
    time.sleep(5)
    if react == 1:
        cp3.shell(f'input swipe {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.like}')
        time.sleep(2)
    elif react == 2:
        cp3.shell(f'input swipe {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.heart}')
        time.sleep(3)
    elif react == 3:
        cp3.shell(f'input swipe {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.care}')
        time.sleep(3)
    elif react == 4:
        cp3.shell(f'input swipe {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.haha}')
        time.sleep(3)
    elif react == 5:
        cp3.shell(f'input swipe {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.wow}')
        time.sleep(3)
    elif react == 6:
        cp3.shell(f'input swipe {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.sad}')
        time.sleep(3)
    elif react == 7:
        cp3.shell(f'input {adb_controls.long_press}')
        cp3.shell(f'input tap {adb_controls.angry}')
        time.sleep(3)
