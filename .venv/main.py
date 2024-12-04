import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.uic import loadUi


class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(255, 255, 0))

        for circle in self.circles:
            x, y, diameter = circle
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self):
        diameter = randint(10, 100)
        x = randint(0, self.width())
        y = randint(0, self.height())
        self.circles.append((x, y, diameter))
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        loadUi('UI.ui', self)
        self.draw_area = DrawingArea(self.centralwidget)
        self.verticalLayout.addWidget(self.draw_area)
        self.pushButton.clicked.connect(self.draw_area.add_circle)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())