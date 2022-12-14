from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.need_paint = False
        self.setupUi(self)
        self.initUI()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.need_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            s = randint(5, 250)
            qp.drawEllipse(randint(0, self.width() - s), randint(0, 350 - s), s, s)
            qp.end()

    def needPaint(self):
        self.need_paint = True
        self.repaint()
        self.need_paint = False

    def initUI(self):
        self.btn.clicked.connect(lambda x: self.needPaint())


if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec())
