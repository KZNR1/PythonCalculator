from PyQt6 import QtCore, QtGui, QtWidgets, QtTest

class Ui_MainForm(object):
    def mDot(self):
        cText = self.MainLabel.text()
        self.MainLabel.setText(cText + ".")
    
    def num0(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("0")
        else:
            self.MainLabel.setText(cText + "0")

    def num1(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("1")
        else:
            self.MainLabel.setText(cText + "1")
        
    def num2(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("2")
        else:
            self.MainLabel.setText(cText + "2")
        
    def num3(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("3")
        else:
            self.MainLabel.setText(cText + "3")
        
    def num4(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("4")
        else:
            self.MainLabel.setText(cText + "4")
    
    def num5(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("5")
        else:
            self.MainLabel.setText(cText + "5")
    
    def num6(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("6")
        else:
            self.MainLabel.setText(cText + "6")

    def num7(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("7")
        else:
            self.MainLabel.setText(cText + "7")
        
    def num8(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("8")
        else:
            self.MainLabel.setText(cText + "8")
        
    def num9(self):
        cText = self.MainLabel.text()
        if cText == "0":
            self.MainLabel.setText("9")
        else:
            self.MainLabel.setText(cText + "9")
        
    def mClear(self):
        self.MainLabel.setText("0")
        
    def mDelete(self):
        cText = self.MainLabel.text()
        if len(cText) == 1:
            self.MainLabel.setText("0")
        else:
            self.MainLabel.setText(cText[:len(cText)-1])
        
    def mDivide(self):
        cText = self.MainLabel.text()
        if "0" not in cText[0]:
            self.MainLabel.setText(cText + " / ")
        
    def mMultiply(self):
        cText = self.MainLabel.text()
        if "0" not in cText[0]:
            self.MainLabel.setText(cText + " * ")
        
    def mSubtraction(self):
        cText = self.MainLabel.text()
        if "0" not in cText[0]:
            self.MainLabel.setText(cText + " - ")
        
    def mPlus(self):
        cText = self.MainLabel.text()
        if "0" not in cText[0]:
            self.MainLabel.setText(cText + " + ")
        
    def mEquals(self):
        cText = self.MainLabel.text()
        global disableButton
        try:
            cTotal = str(eval(cText))
            self.MainLabel.setText(cTotal)
        except:
            self.MainLabel.setText("There's an error!")
            QtTest.QTest.qWait(1000)
            self.MainLabel.setText("0")
    
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(320, 300)
        MainForm.setToolTipDuration(-1)
        MainForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.pushBtn_Multiply = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Multiply.sizePolicy().hasHeightForWidth())
        self.pushBtn_Multiply.setSizePolicy(sizePolicy)
        self.pushBtn_Multiply.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Multiply.setObjectName("pushBtn_Multiply")
        self.gridLayout.addWidget(self.pushBtn_Multiply, 2, 3, 1, 1)
        self.pushBtn_7 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_7.sizePolicy().hasHeightForWidth())
        self.pushBtn_7.setSizePolicy(sizePolicy)
        self.pushBtn_7.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_7.setObjectName("pushBtn_7")
        self.gridLayout.addWidget(self.pushBtn_7, 2, 0, 1, 1)
        self.pushBtn_8 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_8.sizePolicy().hasHeightForWidth())
        self.pushBtn_8.setSizePolicy(sizePolicy)
        self.pushBtn_8.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_8.setObjectName("pushBtn_8")
        self.gridLayout.addWidget(self.pushBtn_8, 2, 1, 1, 1)
        self.pushBtn_6 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_6.sizePolicy().hasHeightForWidth())
        self.pushBtn_6.setSizePolicy(sizePolicy)
        self.pushBtn_6.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_6.setObjectName("pushBtn_6")
        self.gridLayout.addWidget(self.pushBtn_6, 3, 2, 1, 1)
        self.pushBtn_5 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_5.sizePolicy().hasHeightForWidth())
        self.pushBtn_5.setSizePolicy(sizePolicy)
        self.pushBtn_5.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_5.setObjectName("pushBtn_5")
        self.gridLayout.addWidget(self.pushBtn_5, 3, 1, 1, 1)
        self.pushBtn_4 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_4.sizePolicy().hasHeightForWidth())
        self.pushBtn_4.setSizePolicy(sizePolicy)
        self.pushBtn_4.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_4.setObjectName("pushBtn_4")
        self.gridLayout.addWidget(self.pushBtn_4, 3, 0, 1, 1)
        self.pushBtn_3 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_3.sizePolicy().hasHeightForWidth())
        self.pushBtn_3.setSizePolicy(sizePolicy)
        self.pushBtn_3.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_3.setObjectName("pushBtn_3")
        self.gridLayout.addWidget(self.pushBtn_3, 4, 2, 1, 1)
        self.MainLabel = QtWidgets.QLabel(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainLabel.sizePolicy().hasHeightForWidth())
        self.MainLabel.setSizePolicy(sizePolicy)
        self.MainLabel.setStyleSheet("font: 16pt \"Microsoft Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.MainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.MainLabel.setIndent(2)
        self.MainLabel.setObjectName("MainLabel")
        self.gridLayout.addWidget(self.MainLabel, 0, 0, 1, 4)
        self.pushBtn_Dot = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Dot.sizePolicy().hasHeightForWidth())
        self.pushBtn_Dot.setSizePolicy(sizePolicy)
        self.pushBtn_Dot.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Dot.setObjectName("pushBtn_Dot")
        self.gridLayout.addWidget(self.pushBtn_Dot, 5, 2, 1, 1)
        self.pushBtn_2 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_2.sizePolicy().hasHeightForWidth())
        self.pushBtn_2.setSizePolicy(sizePolicy)
        self.pushBtn_2.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_2.setObjectName("pushBtn_2")
        self.gridLayout.addWidget(self.pushBtn_2, 4, 1, 1, 1)
        self.pushBtn_1 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_1.sizePolicy().hasHeightForWidth())
        self.pushBtn_1.setSizePolicy(sizePolicy)
        self.pushBtn_1.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_1.setObjectName("pushBtn_1")
        self.gridLayout.addWidget(self.pushBtn_1, 4, 0, 1, 1)
        self.pushBtn_Subtraction = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Subtraction.sizePolicy().hasHeightForWidth())
        self.pushBtn_Subtraction.setSizePolicy(sizePolicy)
        self.pushBtn_Subtraction.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Subtraction.setObjectName("pushBtn_Subtraction")
        self.gridLayout.addWidget(self.pushBtn_Subtraction, 3, 3, 1, 1)
        self.pushBtn_Plus = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Plus.sizePolicy().hasHeightForWidth())
        self.pushBtn_Plus.setSizePolicy(sizePolicy)
        self.pushBtn_Plus.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Plus.setObjectName("pushBtn_Plus")
        self.gridLayout.addWidget(self.pushBtn_Plus, 4, 3, 1, 1)
        self.pushBtn_Divide = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Divide.sizePolicy().hasHeightForWidth())
        self.pushBtn_Divide.setSizePolicy(sizePolicy)
        self.pushBtn_Divide.setStyleSheet("QPushButton {\n"
"    font: 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Divide.setObjectName("pushBtn_Divide")
        self.gridLayout.addWidget(self.pushBtn_Divide, 1, 3, 1, 1)
        self.pushBtn_Equals = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Equals.sizePolicy().hasHeightForWidth())
        self.pushBtn_Equals.setSizePolicy(sizePolicy)
        self.pushBtn_Equals.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(82, 159, 217);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 150, 203);\n"
"}")
        self.pushBtn_Equals.setObjectName("pushBtn_Equals")
        self.gridLayout.addWidget(self.pushBtn_Equals, 5, 3, 1, 1)
        self.pushBtn_9 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_9.sizePolicy().hasHeightForWidth())
        self.pushBtn_9.setSizePolicy(sizePolicy)
        self.pushBtn_9.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_9.setObjectName("pushBtn_9")
        self.gridLayout.addWidget(self.pushBtn_9, 2, 2, 1, 1)
        self.pushBtn_0 = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_0.sizePolicy().hasHeightForWidth())
        self.pushBtn_0.setSizePolicy(sizePolicy)
        self.pushBtn_0.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(236, 236, 236);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_0.setObjectName("pushBtn_0")
        self.gridLayout.addWidget(self.pushBtn_0, 5, 0, 1, 2)
        self.pushBtn_Clear = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Clear.sizePolicy().hasHeightForWidth())
        self.pushBtn_Clear.setSizePolicy(sizePolicy)
        self.pushBtn_Clear.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Clear.setObjectName("pushBtn_Clear")
        self.gridLayout.addWidget(self.pushBtn_Clear, 1, 0, 1, 2)
        self.pushBtn_Delete = QtWidgets.QPushButton(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn_Delete.sizePolicy().hasHeightForWidth())
        self.pushBtn_Delete.setSizePolicy(sizePolicy)
        self.pushBtn_Delete.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(226, 226, 226);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.pushBtn_Delete.setObjectName("pushBtn_Delete")
        self.gridLayout.addWidget(self.pushBtn_Delete, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)
        
        self.pushBtn_Dot.clicked.connect(self.mDot)
        self.pushBtn_0.clicked.connect(self.num0)
        self.pushBtn_1.clicked.connect(self.num1)
        self.pushBtn_2.clicked.connect(self.num2)
        self.pushBtn_3.clicked.connect(self.num3)
        self.pushBtn_4.clicked.connect(self.num4)
        self.pushBtn_5.clicked.connect(self.num5)
        self.pushBtn_6.clicked.connect(self.num6)
        self.pushBtn_7.clicked.connect(self.num7)
        self.pushBtn_8.clicked.connect(self.num8)
        self.pushBtn_9.clicked.connect(self.num9)
        self.pushBtn_Clear.clicked.connect(self.mClear)
        self.pushBtn_Delete.clicked.connect(self.mDelete)
        self.pushBtn_Divide.clicked.connect(self.mDivide)
        self.pushBtn_Multiply.clicked.connect(self.mMultiply)
        self.pushBtn_Subtraction.clicked.connect(self.mSubtraction)
        self.pushBtn_Plus.clicked.connect(self.mPlus)
        self.pushBtn_Equals.clicked.connect(self.mEquals)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Calculator"))
        self.pushBtn_Multiply.setText(_translate("MainForm", "✕"))
        self.pushBtn_7.setText(_translate("MainForm", "7"))
        self.pushBtn_8.setText(_translate("MainForm", "8"))
        self.pushBtn_6.setText(_translate("MainForm", "6"))
        self.pushBtn_5.setText(_translate("MainForm", "5"))
        self.pushBtn_4.setText(_translate("MainForm", "4"))
        self.pushBtn_3.setText(_translate("MainForm", "3"))
        self.MainLabel.setText(_translate("MainForm", "0"))
        self.pushBtn_Dot.setText(_translate("MainForm", "."))
        self.pushBtn_2.setText(_translate("MainForm", "2"))
        self.pushBtn_1.setText(_translate("MainForm", "1"))
        self.pushBtn_Subtraction.setText(_translate("MainForm", "−"))
        self.pushBtn_Plus.setText(_translate("MainForm", "+"))
        self.pushBtn_Divide.setText(_translate("MainForm", "÷"))
        self.pushBtn_Equals.setText(_translate("MainForm", "="))
        self.pushBtn_9.setText(_translate("MainForm", "9"))
        self.pushBtn_0.setText(_translate("MainForm", "0"))
        self.pushBtn_Clear.setText(_translate("MainForm", "Clear"))
        self.pushBtn_Delete.setText(_translate("MainForm", "⌫"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())
