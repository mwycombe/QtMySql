import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout, QHBoxLayout

from PySide6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Layout Template")

        def __init__(self):
            super(MainWindow, self).__init__()

            self.setWindowTitle("My App")

            self.layout1 = QHBoxLayout()
            self.layout2 = QVBoxLayout()
            layout3 = QVBoxLayout()

            self.layout2.addWidget(Color('red'))
            self.layout2.addWidget(Color('yellow'))
            self.layout2.addWidget(Color('purple'))

            self.layout1.addLayout(self.layout2)

            self.layout1.addWidget(Color('green'))

            self.layout3.addWidget(Color('red'))
            self.layout3.addWidget(Color('purple'))

            self.layout1.addLayout(self.layout3)

            widget = QWidget()
            widget.setLayout(self.layout1)
            self.setCentralWidget(widget)
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()