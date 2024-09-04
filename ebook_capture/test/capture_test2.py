import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QRubberBand, QVBoxLayout, QWidget

class ScreenCaptureApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Screen Capture with PyQt5')

        # 레이블에 이미지 표시
        screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        self.label = QLabel(self)
        self.label.setPixmap(screenshot)
        self.setCentralWidget(self.label)

        # 레이블 위에 사각형을 그리기 위한 Rubber Band
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self.label)

        # 마우스 이벤트 설정
        self.label.mousePressEvent = self.mousePress
        self.label.mouseMoveEvent = self.mouseMove
        self.label.mouseReleaseEvent = self.mouseRelease

        self.show()

    def mousePress(self, event):
        # 마우스가 눌리면 시작 지점 저장
        self.origin = event.pos()
        self.rubberBand.setGeometry(QRect(self.origin, QSize()))
        self.rubberBand.show()

    def mouseMove(self, event):
        # 마우스가 움직이면 사각형 크기 조정
        self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseRelease(self, event):
        # 마우스를 놓으면 사각형 크기를 기반으로 캡쳐 수행
        self.rubberBand.hide()

        rect = self.rubberBand.geometry()
        screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), rect.x(), rect.y(), rect.width(), rect.height())

        # 캡쳐 이미지를 저장하거나 원하는 작업 수행
        screenshot.save('captured_region.png')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScreenCaptureApp()
    sys.exit(app.exec_())
