# Form implementation generated from reading ui file 'listBoxTest.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
import ctrlVariables



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ListBox")
        MainWindow.resize(1060, 619)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listBoxView = QtWidgets.QListView(parent=self.centralwidget)
        self.listBoxView.setGeometry(QtCore.QRect(270, 180, 171, 201))
        self.listBoxView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listBoxView.setObjectName("listBoxView")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 281, 61))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.selectionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.selectionLabel.setGeometry(QtCore.QRect(580, 180, 161, 31))
        self.selectionLabel.setObjectName("selectionLabel")
        self.listSelection = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.listSelection.setGeometry(QtCore.QRect(750, 180, 161, 31))
        self.listSelection.setObjectName("listSelection")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Test area for ListBox emulation"))
        self.selectionLabel.setText(_translate("MainWindow", "Selection Made"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
