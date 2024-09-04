import os
import time

import pyautogui
import keyboard

import sys
import threading
import time
import asyncio
import datetime

from PyQt5 import uic
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./ebook_capture.ui")[0]

class EbookCapture(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._set_ui()

        keyboard.add_hotkey("ctrl+q", lambda: self.quit_program())
        keyboard.add_hotkey("ctrl+p+1", lambda: self.print_mouse_pos())
        keyboard.add_hotkey("ctrl+m", lambda: self.click_mouse())
        # keyboard.add_hotkey("ctrl+alt+p", lambda: self.stop_print_mouse_pos())
        # keyboard.add_hotkey("ctrl+alt+m", lambda: self.stop_click_mouse())
        self.printing_mouse_pos = False
        self.clicking_mouse = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(100)

    def _set_ui(self):
        self.btn_tracking_11.clicked.connect(self.show_line)

    def show_line(self):
        pass

    def run(self):
        while True:
            print("running........")
            time.sleep(1)

    def quit_program(self):
        print("ctrl+q was pressed")
        if self.printing_mouse_pos:
            print("self.printing_mouse_pos 상태 =", self.printing_mouse_pos)
            self.printing_mouse_pos = False
        elif self.clicking_mouse:
            print("self.clicking_mouse 상태 =", self.clicking_mouse)
            self.clicking_mouse = False
        else:
            print("프로그램 종료됨")
            os._exit(0)

    def print_mouse_pos(self):
        print("ctrl+p was pressed")
        self.printing_mouse_pos = not self.printing_mouse_pos
        while self.printing_mouse_pos:
            print(f"Current Mouse Position:{pyautogui.position()}")
            time.sleep(1)

    def click_mouse(self):
        print("ctrl+m was pressed")
        x, y = 1560, 460

        self.clicking_mouse = not self.clicking_mouse
        while self.clicking_mouse:
            pyautogui.click(x=x, y=y, interval=0.5)
            print(f"x:{x}, y:{y} clicked!")
            time.sleep(1)

    def stop_print_mouse_pos(self):
        print("ctrl+alt+p was pressed")
        self.printing_mouse_pos = False

    def stop_click_mouse(self):
        print("ctrl+alt+m was pressed")
        self.clicking_mouse = False

    def run(self):
        while True:
            if keyboard.is_pressed("q"):
                print("프로그램 종료")
                break

            elif keyboard.is_pressed("p"):
                while True:
                    print(f"Current Mouse Position:{pyautogui.position()}")
                    # time.sleep(0.5)
                    if keyboard.is_pressed("q"):
                        print("break p")
                        time.sleep(0.5)
                        break

                print("exit while p")

            elif keyboard.is_pressed("r"):
                x, y = 1560, 460
                while True:
                    pyautogui.click(x=x, y=y, interval=0.5)
                    print(f"x:{x}, y:{y} clicked!")
                    time.sleep(0.5)

                    if keyboard.is_pressed("q"):
                        print("break r")
                        time.sleep(0.5)
                        break
                print("exit while r")

            print("running...")
            time.sleep(1)

    def on_timer_timeout(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EbookCapture()
    win.show()
    sys.exit(app.exec_())
