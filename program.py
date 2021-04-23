import pyautogui
pyautogui.sleep(5)  # countdown before autotyping begins
pos = pyautogui.position()  # 351 156
pyautogui.click(pos)


def read_write():
    with open('file.txt') as f:  # file name goes here
        lines = f.readlines()

    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.typewrite(['DOWN'])


readwrite()
