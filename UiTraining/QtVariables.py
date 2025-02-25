# Form implementation generated from reading ui file 'QtControlVariables.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, Property, Signal


class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 508)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TestHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.TestHeader.setGeometry(QtCore.QRect(160, 70, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TestHeader.setFont(font)
        self.TestHeader.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.TestHeader.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.TestHeader.setObjectName("TestHeader")
        self.EntryFieldLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.EntryFieldLabel.setGeometry(QtCore.QRect(160, 200, 141, 31))
        self.EntryFieldLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EntryFieldLabel.setObjectName("EntryFieldLabel")
        self.EntryField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.EntryField.setGeometry(QtCore.QRect(320, 210, 221, 26))
        self.EntryField.setObjectName("EntryField")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 250, 118, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 254, 241, 20))
        self.label.setObjectName("label")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(70, 250, 111, 31))
        self.backButton.setObjectName("propButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 310, 251, 91))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.EntryField.textChanged.connect(self.EntryFieldLabel.setText)
        # emulate this using a StringVar with signals only when return pressed
        self.entryInput = StrVar()

        # print(self.entryInput)
        self.EntryField.returnPressed.connect(self.returnPressed)
        self.pushButton.clicked.connect(self.resetLabel)

        self.backButton.clicked.connect(self.changeEntryField)
        # self.myObject = MyObject()
        # self.myValueChanged.connect(self.myObject.receiveSignal)
        self.entryInput.strValueChanged.connect(self.my_slot)
        self.entryInput.strValueChanged.connect(self.EntryField.setText)
        # self.entryChanged.strValueChanged.connect(self.EntryField.setText)

    def changeEntryField(self, data):
        # push data out to entry field via strVar instance
        self.entryInput.myValue = 'New entry input'

    def resetLabel(self):
        # reset the signal field label
        self.EntryFieldLabel.setText('Signal Field Label')

    @QtCore.Slot()
    def my_slot(self, data):
        self.EntryFieldLabel.setText(data)



    def returnPressed(self):
        print('Return pressed')
        self.entryInput.myValue = self.EntryField.text()
        print('entryInput: ' + self.EntryField.text())

    # used to emulate tkinter control variables.
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TestHeader.setText(_translate("MainWindow", "Build TkVar Simulator in PyQt"))
        self.EntryFieldLabel.setText(_translate("MainWindow", "Signal Entry  Field"))
        self.pushButton.setText(_translate("MainWindow", "Reset Button"))
        self.backButton.setText(_translate("MainWindow", "Change Button"))

        self.label.setText(_translate("MainWindow", "Button resets entry field label"))
        self.label_2.setText(_translate("MainWindow", "Entering data into field will alter Signal Entry Field. Pressing the button will put data into the EntryField from the button clicked event."))


class StrVar(QObject):

    strValueChanged= Signal(str)

    def __init__(self):
        super().__init__()
        self._my_value = ''

    @Property(str)
    def myValue(self):
        return self._my_value

    @myValue.setter
    def myValue(self,value):
        print('StrVar received: ' + value)
        if value != self._my_value:
            self._my_value = value
            self.strValueChanged.emit(value)

    # ppValSignal = Signal(str)   # this is my signal
    #
    # def emit_signal(self):
    #     self.ppValSignal.emit ("ppval change")
    #
    # def __init__(self):
    #     super().__init__()
    #     self.ppval = ''
    # def readPP(self):
    #         return self.ppval
    # def setPP(self,val):
    #     print ('set ppval')
    #     self.ppval = val
    #     self.ppval.emit("ppval changed")
    #
    # def PPChanged(self):
    #     print('Received signal changed')
    #
    # pp = Property(str, readPP, setPP, notify=emit_signal)
# class MyObject(QObject):
#     def __init__ (self):
#         super().__init__()
#     def receiveSignal(self):
#         print ('Signal received')

# aSlot = MyObject()

class IntVar(QObject):

    intValueChange = Signal(int)
    def __init__(self):
        super().__init__()
        self._my_value = 0

    @Property(str)
    def myValue(self):
        return self._my_value

    @myValue.setter
    def myValue(self,value):
        if value != self._my_value:
            self._my_value = value
            self.intValueChanged.emit(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
