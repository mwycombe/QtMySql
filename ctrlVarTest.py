import sys

from PyQt5.QtWidgets import QLineEdit
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CtrlVar Mimic')
        self.setGeometry(200,200,500,500)

        self.layout = QVBoxLayout()

        self.entryField = QLineEdit()
        self.layout.addWidget(self.entryField)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

# create property class entry data handling

class entryFieldVar():


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()