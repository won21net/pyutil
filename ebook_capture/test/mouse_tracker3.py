import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("마우스 트래커")
        self.setGeometry(300, 300, 300, 200)

        self.label_x = QLabel("x:", self)
        self.label_y = QLabel("y:", self)
        self.line_edit_x = QLineEdit(self)
        self.line_edit_y = QLineEdit(self)

        self.button_start = QPushButton("트랙 시작", self)
        self.button_stop = QPushButton("트랙 중지", self)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.label_x)
        self.layout.addWidget(self.line_edit_x)
        self.layout.addWidget(self.label_y)
        self.layout.addWidget(self.line_edit_y)
        self.layout.addWidget(self.button_start)
        self.layout.addWidget(self.button_stop)

        self.button_start.clicked.connect(self.on_button_start_clicked)
        self.button_stop.clicked.connect(self.on_button_stop_clicked)

        self.is_tracking = False

    def on_button_start_clicked(self):
        self.is_tracking = True
        self.start_tracking()

    def on_button_stop_clicked(self):
        self.is_tracking = False
        self.stop_tracking()

    def start_tracking(self):
        self.line_edit_x.setText("")
        self.line_edit_y.setText("")

        self.setMouseTracking(True)
        self.setFocus()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(100)

    def stop_tracking(self):
        self.setMouseTracking(False)
        self.timer.stop()

    def on_timer_timeout(self):
        if self.is_tracking:
            x, y = QCursor.pos().x(), QCursor.pos().y()
            self.line_edit_x.setText(str(x))
            self.line_edit_y.setText(str(y))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.stop_tracking()
            x, y = event.x(), event.y()
            self.line_edit_x.setText(str(x))
            self.line_edit_y.setText(str(y))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()