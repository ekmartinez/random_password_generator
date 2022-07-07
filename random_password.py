from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip
import random

class Ui_MainWindow(object):
    
    def generator(self):
        self.pushButton.setStyleSheet("background-color: rgb(255,255,255")
        self.pushButton.setText('Copy')
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "@%+\/'!#$^?:.(){}[]~-_^"
        passw = ""
        
        if self.checkBox.isChecked() and self.checkBox_2.isChecked()==False and \
            self.checkBox_3.isChecked()==False:
                charx = letters
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
               
        elif self.checkBox.isChecked() and self.checkBox_2.isChecked() and \
            self.checkBox_3.isChecked()==False:
                charx = letters + numbers
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
           
        elif self.checkBox.isChecked() and self.checkBox_2.isChecked()==False and \
            self.checkBox_3.isChecked():
                charx = letters + symbols
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
            
        elif self.checkBox.isChecked()==False and self.checkBox_2.isChecked() and \
            self.checkBox_3.isChecked()==False:
                charx = numbers
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
        
        elif self.checkBox.isChecked()==False and self.checkBox_2.isChecked() and \
            self.checkBox_3.isChecked():
                charx = numbers + symbols
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
                
        elif self.checkBox.isChecked()==False and self.checkBox_2.isChecked()==False and \
            self.checkBox_3.isChecked():
                charx = symbols
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
           
        elif self.checkBox.isChecked() and self.checkBox_2.isChecked() and \
            self.checkBox_3.isChecked():
                charx = letters + numbers + symbols
                for x in range(self.spinBox.value()):
                    passw += random.choice(charx)
                self.lineEdit.setText(passw)
                
    def about(self):
        txt = 'Random Password Generator ' + '\n\n' +\
            'I would always recommend using a professional password manager, ' +\
                'but if you need a quick random password for whatever reason, this tool will do.'
       
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Random Password Generator')
        msg.setIcon(msg.Information)
        msg.setText(txt)
        msg.exec_()
        
    def close(self):
        sys.exit()
        
    def copy(self):
        pyperclip.copy(self.lineEdit.text())
        self.pushButton.setText('Copied')
        self.pushButton.setStyleSheet("background-color: lightgreen")
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 376)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(130, 180, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(12)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(25)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 171, 16))
        self.label_3.setObjectName("label_3")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 191, 80))
        self.groupBox.setObjectName("groupBox")
        
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 111, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(True)
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setChecked(True)
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 60, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setChecked(True)
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 191, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        #exit
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 310, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close)
        
        #generate
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 40, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.generator)
        
        #copy
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 40, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.copy)
     
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 224, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about)
        
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random PwD"))
        self.label.setText(_translate("MainWindow", "Password Generator"))
        self.label_2.setText(_translate("MainWindow", "How many characters?"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Strong, fast, secure! "))
        self.groupBox.setTitle(_translate("MainWindow", "Include"))
        self.checkBox.setText(_translate("MainWindow", "Letters"))
        self.checkBox_2.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_3.setText(_translate("MainWindow", "Symbols"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Random Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate"))
        self.pushButton.setText(_translate("MainWindow", "Copy"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())