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

    cp1 = devices[0]

    return cp1, client


def login(url, email, password):
    cp1, client = connect()
    cp1.shell(f'am start -n {adb_controls.chrome_incognito}')
    time.sleep(2)
    cp1.shell(f'input tap {adb_controls.search_bar}')
    cp1.shell(f'input text "{url}"')
    time.sleep(5)
    cp1.shell(f'input {adb_controls.enter}')
    time.sleep(8)
    cp1.shell(f'input swipe {adb_controls.swipe_down}')
    time.sleep(5)
    cp1.shell(f'input tap {adb_controls.login}')
    time.sleep(5)
    cp1.shell(f'input tap {adb_controls.email}')
    time.sleep(5)
    cp1.shell(f'input text "{email}"')
    time.sleep(5)
    cp1.shell(f'input {adb_controls.tab}')
    time.sleep(1)
    cp1.shell(f'input text "{password}"')
    time.sleep(5)
    cp1.shell(f'input {adb_controls.enter}')
    time.sleep(10)
    cp1.shell(f'input swipe {adb_controls.swipe_down}')


def comment(com, filename):
    cp1, client = connect()
    cp1.shell(f'input tap {adb_controls.comment}')
    time.sleep(5)
    cp1.shell(f'input swipe {adb_controls.swipe_down}')
    time.sleep(5)
    cp1.shell(f'input tap {adb_controls.comment_box}')
    time.sleep(5)
    cp1.shell(f'input text "{com}"')
    time.sleep(5)
    cp1.shell(f'input {adb_controls.tab}')
    time.sleep(5)
    cp1.shell(f'input {adb_controls.enter}')
    time.sleep(10)
    ss = cp1.screencap()
    screenshot.get_screen(filename, ss)
    time.sleep(10)
    cp1.shell(f'input {adb_controls.home}')
    time.sleep(1)
    cp1.shell(f'input swipe {adb_controls.notification}')
    time.sleep(1)
    cp1.shell(f'input tap {adb_controls.clear_incognito}')


def reaction(react):
    cp1, client = connect()
    time.sleep(5)
    if react == 1:
        cp1.shell(f'input swipe {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.like}')
        time.sleep(2)
    elif react == 2:
        cp1.shell(f'input swipe {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.heart}')
        time.sleep(3)
    elif react == 3:
        cp1.shell(f'input swipe {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.care}')
        time.sleep(3)
    elif react == 4:
        cp1.shell(f'input swipe {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.haha}')
        time.sleep(3)
    elif react == 5:
        cp1.shell(f'input swipe {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.wow}')
        time.sleep(3)
    elif react == 6:
        cp1.shell(f'input swipe {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.sad}')
        time.sleep(3)
    elif react == 7:
        cp1.shell(f'input {adb_controls.long_press}')
        cp1.shell(f'input tap {adb_controls.angry}')
        time.sleep(3)


# if __name__ == '__main__':
#     cp1, client = connect()
#     print(cp1)
