import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class DrawingArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)

        for color, x, y, diameter in self.circles:
            painter.setPen(color)
            painter.drawEllipse(x, y, diameter, diameter)

    def add_circle(self):
        diameter = randint(10, 100)
        x = randint(0, self.width())
        y = randint(0, self.height())
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((color, x, y, diameter))
        self.update()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.pushButton = QPushButton("Draw Circle")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.resize(400, 300)
        self.setWindowTitle("PyQt Circles")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        button = QPushButton("Draw Circle")
        layout.addWidget(button)

        self.draw_area = DrawingArea()
        layout.addWidget(self.draw_area)

        button.clicked.connect(self.draw_area.add_circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())