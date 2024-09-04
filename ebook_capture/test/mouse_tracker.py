import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCursor

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mouse Tracker')

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Move or click the mouse")

        self.btnStart = QPushButton('Start Tracking', self)
        self.btnStart.clicked.connect(self.startTracking)

        self.btnStop = QPushButton('Stop Tracking', self)
        self.btnStop.clicked.connect(self.stopTracking)
        self.btnStop.setEnabled(False)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.btnStart)
        layout.addWidget(self.btnStop)

        self.tracking = False
        self.mouse_timer = QTimer(self)
        self.mouse_timer.timeout.connect(self.trackMouse)

        self.setGeometry(300, 300, 300, 150)
        self.show()

    def startTracking(self):
        self.tracking = True
        self.btnStart.setEnabled(False)
        self.btnStop.setEnabled(True)
        self.mouse_timer.start(100)  # Track mouse every 100 milliseconds

    def stopTracking(self):
        self.tracking = False
        self.btnStart.setEnabled(True)
        self.btnStop.setEnabled(False)
        self.mouse_timer.stop()

    def trackMouse(self):
        cursor_pos = QCursor.pos()
        self.label.setText(f"Mouse Position: ({cursor_pos.x()}, {cursor_pos.y()})")

    def mousePressEvent(self, event):
        if self.tracking:
            self.stopTracking()
            self.label.setText(f"Mouse Clicked at: ({event.x()}, {event.y()})")
        else:
            super().mousePressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTracker()
    sys.exit(app.exec_())
