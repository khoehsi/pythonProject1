# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result = QtWidgets.QLabel(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 10, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.result.setFont(font)
        self.result.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.result.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.result.setLineWidth(2)
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.result.setObjectName("result")
        self.division_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.division_button.setGeometry(QtCore.QRect(270, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.division_button.setFont(font)
        self.division_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.division_button.setObjectName("division_button")
        self.seven_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.seven_button.setGeometry(QtCore.QRect(10, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.four_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four_button.setGeometry(QtCore.QRect(10, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.eight_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eight_button.setGeometry(QtCore.QRect(90, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.five_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five_button.setGeometry(QtCore.QRect(90, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.six_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.six_button.setGeometry(QtCore.QRect(180, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.nine_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nine_button.setGeometry(QtCore.QRect(180, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.three_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three_button.setGeometry(QtCore.QRect(180, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two_button.setGeometry(QtCore.QRect(90, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.one_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one_button.setGeometry(QtCore.QRect(10, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.zero_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(0, 390, 261, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.multiply_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiply_button.setGeometry(QtCore.QRect(270, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multiply_button.setFont(font)
        self.multiply_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.multiply_button.setObjectName("multiply_button")
        self.subtract_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.subtract_button.setGeometry(QtCore.QRect(270, 260, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.subtract_button.setFont(font)
        self.subtract_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.subtract_button.setObjectName("subtract_button")
        self.add_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(270, 330, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.add_button.setObjectName("add_button")
        self.equal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(270, 400, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equal_button.setFont(font)
        self.equal_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.equal_button.setObjectName("equal_button")
        self.clear_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(10, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.clear_button.setObjectName("clear_button")
        self.percent_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.percent_button.setGeometry(QtCore.QRect(180, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percent_button.setFont(font)
        self.percent_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.percent_button.setObjectName("percent_button")
        self.square_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.square_button.setGeometry(QtCore.QRect(350, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.square_button.setFont(font)
        self.square_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.square_button.setObjectName("square_button")
        self.squareroot_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.squareroot_button.setGeometry(QtCore.QRect(350, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.squareroot_button.setFont(font)
        self.squareroot_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.squareroot_button.setObjectName("squareroot_button")
        self.cube_root_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cube_root_button.setGeometry(QtCore.QRect(350, 330, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cube_root_button.setFont(font)
        self.cube_root_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.cube_root_button.setObjectName("cube_root_button")
        self.cube_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cube_button.setGeometry(QtCore.QRect(350, 260, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cube_button.setFont(font)
        self.cube_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.cube_button.setObjectName("cube_button")
        self.mode_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mode_button.setGeometry(QtCore.QRect(90, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mode_button.setFont(font)
        self.mode_button.setStyleSheet("BACKGROUND:rgb(254, 187, 71)")
        self.mode_button.setObjectName("mode_button")
        self.secondpage = QtWidgets.QFrame(parent=self.centralwidget)
        self.secondpage.setGeometry(QtCore.QRect(450, 120, 351, 341))
        self.secondpage.setObjectName("secondpage")
        self.label = QtWidgets.QLabel(parent=self.secondpage)
        self.label.setGeometry(QtCore.QRect(40, 230, 261, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.square_button_2 = QtWidgets.QPushButton(parent=self.secondpage)
        self.square_button_2.setGeometry(QtCore.QRect(200, 40, 113, 32))
        self.square_button_2.setObjectName("square_button_2")
        self.circle_button = QtWidgets.QPushButton(parent=self.secondpage)
        self.circle_button.setGeometry(QtCore.QRect(40, 40, 113, 32))
        self.circle_button.setObjectName("circle_button")
        self.triangle_button = QtWidgets.QPushButton(parent=self.secondpage)
        self.triangle_button.setGeometry(QtCore.QRect(200, 80, 113, 32))
        self.triangle_button.setObjectName("triangle_button")
        self.rectangle_button = QtWidgets.QPushButton(parent=self.secondpage)
        self.rectangle_button.setGeometry(QtCore.QRect(40, 80, 113, 32))
        self.rectangle_button.setObjectName("rectangle_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 37))
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
        self.result.setText(_translate("MainWindow", "0"))
        self.division_button.setText(_translate("MainWindow", "/"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.zero_button.setText(_translate("MainWindow", "0"))
        self.multiply_button.setText(_translate("MainWindow", "*"))
        self.subtract_button.setText(_translate("MainWindow", "-"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.clear_button.setText(_translate("MainWindow", "AC"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.square_button.setText(_translate("MainWindow", "x²"))
        self.squareroot_button.setText(_translate("MainWindow", "√"))
        self.cube_root_button.setText(_translate("MainWindow", "∛"))
        self.cube_button.setText(_translate("MainWindow", "x³"))
        self.mode_button.setText(_translate("MainWindow", "Mode"))
        self.square_button_2.setText(_translate("MainWindow", "Square"))
        self.circle_button.setText(_translate("MainWindow", "Circle"))
        self.triangle_button.setText(_translate("MainWindow", "Triangle"))
        self.rectangle_button.setText(_translate("MainWindow", "Rectangle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
