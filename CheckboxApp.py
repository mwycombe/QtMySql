import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Checkbox App")

        self.checkbox = QCheckBox()
        self.checkbox.setCheckState(Qt.CheckState.Checked)
        self.checkbox.setText('This is a checkbox')

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        self.checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(self.checkbox)

    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()