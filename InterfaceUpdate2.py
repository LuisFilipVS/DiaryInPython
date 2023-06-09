# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceUpdate2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    '''
    Classe oriunda da conversão do arquivo de formato XML gerado a partir de um aquivo .ui,
    para criação de interfaces.
    

    '''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_Top = QtWidgets.QFrame(self.centralwidget)
        self.frame_Top.setGeometry(QtCore.QRect(0, 0, 500, 60))
        self.frame_Top.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_Top.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.frame_Top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Top.setObjectName("frame_Top")
        self.label_6 = QtWidgets.QLabel(self.frame_Top)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: black")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame_Botton = QtWidgets.QFrame(self.centralwidget)
        self.frame_Botton.setGeometry(QtCore.QRect(0, 440, 500, 60))
        self.frame_Botton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_Botton.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.frame_Botton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Botton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Botton.setObjectName("frame_Botton")
        self.label_7 = QtWidgets.QLabel(self.frame_Botton)
        self.label_7.setGeometry(QtCore.QRect(100, 20, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:black")
        self.label_7.setObjectName("label_7")
        self.frame_Content = QtWidgets.QFrame(self.centralwidget)
        self.frame_Content.setGeometry(QtCore.QRect(0, 60, 500, 380))
        self.frame_Content.setStyleSheet("background-color: rgb(173, 173, 173);\n"
"")
        self.frame_Content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Content.setObjectName("frame_Content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_Content)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_Content)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame_Content)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(350, 130, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"background-color: gray;\n"
"border-radius: 5px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid red;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"color:black\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: gray;\n"
"border-radius: 3px;\n"
"color:white\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.label_3.setStyleSheet("QLabel{\n"
"border: 1px solid black;\n"
"background-color: gray;\n"
"border-radius: 03px;\n"
"color:white\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_8.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: gray;\n"
"border-radius: 03px;\n"
"color:white\n"
"}\n"
"")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(290, 40, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 70, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 100, 191, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(110, 40, 171, 21))
        self.label_9.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: white;\n"
"border-radius: 3px;\n"
"color:black\n"
"}\n"
"\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(110, 70, 171, 21))
        self.label_10.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: white;\n"
"border-radius: 3px;\n"
"color:black\n"
"}\n"
"\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(110, 100, 171, 21))
        self.label_11.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: white;\n"
"border-radius: 3px;\n"
"color:black\n"
"}\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(110, 130, 41, 21))
        self.label_12.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: white;\n"
"border-radius: 3px;\n"
"color:black\n"
"}\n"
"\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(10, 130, 91, 21))
        self.label_13.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"background-color: gray;\n"
"border-radius: 03px;\n"
"color:white\n"
"}\n"
"")
        self.label_13.setObjectName("label_13")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 10, 71, 24))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border: 2px solid black;\n"
"background-color: gray;\n"
"border-radius: 5px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid red;\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"color:black\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Atividade Avaliativa\n"
"Paradigmas de Linguagem de Programação"))
        self.label_7.setText(_translate("MainWindow", "IFBA - VCA Powered by Luis Filipe"))
        self.label_4.setText(_translate("MainWindow", "Agenda"))
        self.label_5.setText(_translate("MainWindow", "Instruções:"))
        self.label.setText(_translate("MainWindow", "AGENDA - Criar novo Contato"))
        self.pushButton.setText(_translate("MainWindow", "Atualizar"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label_3.setText(_translate("MainWindow", "Telefone"))
        self.label_8.setText(_translate("MainWindow", "Email"))
        self.label_9.setText(_translate("MainWindow", "Nome"))
        self.label_10.setText(_translate("MainWindow", "Telefone"))
        self.label_11.setText(_translate("MainWindow", "Email"))
        self.label_12.setText(_translate("MainWindow", "--"))
        self.label_13.setText(_translate("MainWindow", "ID"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
