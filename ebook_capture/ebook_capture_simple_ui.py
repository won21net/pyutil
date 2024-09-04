import os
from pathlib import Path, PurePath
import sys
import time

import keyboard
import pyautogui
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication

form_class = uic.loadUiType("./ebook_capture_simple.ui")[0]


class EbookCaptureSimpleWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._set_ui()

        keyboard.add_hotkey("ctrl+q", lambda: self.quit_program())
        keyboard.add_hotkey("ctrl+s", lambda: self.start())

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.starting = False
        self.capture_cnt = 1

    def _set_ui(self):
        self.btn_start.clicked.connect(self.start)

    def start(self):
        if self.starting:
            self.starting = False
            self.btn_start.setText("시작")
            self.timer.stop()
        else:
            self.btn_start.setText("중지")
            self.starting = True
            self.timer.start(1000)

    def on_timer_timeout(self):
        book_name = "불편한 편의점"  # 변경 ##########
        total_cnt = 246  # 변경 #########
        file_path = r"D:\Temp\ebook_capture"
        print(f"page: {self.capture_cnt}/{total_cnt}")

        region1 = (260, 120, 570, 660)
        region2 = (900, 120, 570, 660)
        try:
            pyautogui.screenshot(os.path.join(file_path, f"{book_name}_{self.capture_cnt}a.png"), region=region1)
            pyautogui.screenshot(os.path.join(file_path, f"{book_name}_{self.capture_cnt}b.png"), region=region2)
            self.capture_cnt += 1
        except Exception as e:
            print("오류:", e)
        # 다음 버튼 클릭
        x, y = 1560, 460
        pyautogui.click(x=x, y=y, interval=0.2)
        # print(f"x:{x}, y:{y} clicked!")
        time.sleep(0.5)

        if self.capture_cnt > total_cnt:
            self.btn_start.setText("시작")
            self.starting = False
            self.timer.stop()
            print("캡쳐 완료")

    def quit_program(self):
        print("ctrl+q was pressed")
        if self.starting:
            self.btn_start.setText("시작")
            self.starting = False
            self.timer.stop()
            print("캡쳐 중지")
        else:
            print("프로그램 종료됨")
            os._exit(0)
    #
    # def print_mouse_pos(self):
    #     print("ctrl+p was pressed")
    #     self.printing_mouse_pos = not self.printing_mouse_pos
    #     while self.printing_mouse_pos:
    #         print(f"Current Mouse Position:{pyautogui.position()}")
    #         time.sleep(1)
    #
    # def click_mouse(self):
    #     print("ctrl+m was pressed")
    #     x, y = 1560, 460
    #
    #     self.clicking_mouse = not self.clicking_mouse
    #     while self.clicking_mouse:
    #         pyautogui.click(x=x, y=y, interval=0.5)
    #         print(f"x:{x}, y:{y} clicked!")
    #         time.sleep(1)
    #
    # def stop_print_mouse_pos(self):
    #     print("ctrl+alt+p was pressed")
    #     self.printing_mouse_pos = False
    #
    # def stop_click_mouse(self):
    #     print("ctrl+alt+m was pressed")
    #     self.clicking_mouse = False
    #
    # def run1(self):
    #     while True:
    #         if keyboard.is_pressed("q"):
    #             print("프로그램 종료")
    #             break
    #
    #         elif keyboard.is_pressed("p"):
    #             while True:
    #                 print(f"Current Mouse Position:{pyautogui.position()}")
    #                 # time.sleep(0.5)
    #                 if keyboard.is_pressed("q"):
    #                     print("break p")
    #                     time.sleep(0.5)
    #                     break
    #
    #             print("exit while p")
    #
    #         elif keyboard.is_pressed("r"):
    #             x, y = 1560, 460
    #             while True:
    #                 pyautogui.click(x=x, y=y, interval=0.5)
    #                 print(f"x:{x}, y:{y} clicked!")
    #                 time.sleep(0.5)
    #
    #                 if keyboard.is_pressed("q"):
    #                     print("break r")
    #                     time.sleep(0.5)
    #                     break
    #             print("exit while r")
    #
    #         print("running...")
    #         time.sleep(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EbookCaptureSimpleWindow()
    window.show()
    app.exec_()
