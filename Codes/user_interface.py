# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'source.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(10, 10, 1401, 801))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_display.setFont(font)
        self.label_display.setFrameShape(QtWidgets.QFrame.Box)
        self.label_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_display.setLineWidth(2)
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.txt_log = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_log.setGeometry(QtCore.QRect(1420, 10, 481, 801))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_log.setFont(font)
        self.txt_log.setReadOnly(True)
        self.txt_log.setObjectName("txt_log")
        self.btn_listen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listen.setGeometry(QtCore.QRect(10, 820, 1391, 211))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(42)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_listen.setFont(font)
        self.btn_listen.setObjectName("btn_listen")
        self.vol_down = QtWidgets.QPushButton(self.centralwidget)
        self.vol_down.setGeometry(QtCore.QRect(1410, 930, 91, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.vol_down.setFont(font)
        self.vol_down.setObjectName("vol_down")
        self.vol_up = QtWidgets.QPushButton(self.centralwidget)
        self.vol_up.setGeometry(QtCore.QRect(1410, 820, 91, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.vol_up.setFont(font)
        self.vol_up.setObjectName("vol_up")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(1510, 820, 391, 211))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.freq_func1 = QtWidgets.QPushButton(self.centralwidget)
        self.freq_func1.setGeometry(QtCore.QRect(1520, 830, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.freq_func1.setFont(font)
        self.freq_func1.setObjectName("freq_func1")
        self.freq_func3 = QtWidgets.QPushButton(self.centralwidget)
        self.freq_func3.setGeometry(QtCore.QRect(1520, 940, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.freq_func3.setFont(font)
        self.freq_func3.setObjectName("freq_func3")
        self.freq_func2 = QtWidgets.QPushButton(self.centralwidget)
        self.freq_func2.setGeometry(QtCore.QRect(1710, 830, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.freq_func2.setFont(font)
        self.freq_func2.setObjectName("freq_func2")
        self.freq_func4 = QtWidgets.QPushButton(self.centralwidget)
        self.freq_func4.setGeometry(QtCore.QRect(1710, 940, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.freq_func4.setFont(font)
        self.freq_func4.setObjectName("freq_func4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 18))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.actionCAM_0 = QtWidgets.QAction(MainWindow)
        self.actionCAM_0.setObjectName("actionCAM_0")
        self.actionCAM_1 = QtWidgets.QAction(MainWindow)
        self.actionCAM_1.setObjectName("actionCAM_1")
        self.actionCAM_2 = QtWidgets.QAction(MainWindow)
        self.actionCAM_2.setObjectName("actionCAM_2")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionVolumn_UP = QtWidgets.QAction(MainWindow)
        self.actionVolumn_UP.setObjectName("actionVolumn_UP")
        self.actionVolumn_Down = QtWidgets.QAction(MainWindow)
        self.actionVolumn_Down.setObjectName("actionVolumn_Down")
        self.actionVoice_1 = QtWidgets.QAction(MainWindow)
        self.actionVoice_1.setObjectName("actionVoice_1")
        self.actionVoice_2 = QtWidgets.QAction(MainWindow)
        self.actionVoice_2.setObjectName("actionVoice_2")
        self.actionInstruction = QtWidgets.QAction(MainWindow)
        self.actionInstruction.setObjectName("actionInstruction")
        self.actionContact_for_help = QtWidgets.QAction(MainWindow)
        self.actionContact_for_help.setObjectName("actionContact_for_help")
        self.actionCopyRight = QtWidgets.QAction(MainWindow)
        self.actionCopyRight.setObjectName("actionCopyRight")
        self.menuHelp.addAction(self.actionInstruction)
        self.menuHelp.addAction(self.actionContact_for_help)
        self.menuabout.addAction(self.actionCopyRight)
        self.menuSetting.addAction(self.actionVolumn_UP)
        self.menuSetting.addAction(self.actionVolumn_Down)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionCAM_0)
        self.menuSetting.addAction(self.actionCAM_1)
        self.menuSetting.addAction(self.actionCAM_2)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionVoice_1)
        self.menuSetting.addAction(self.actionVoice_2)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BU ENG EC601 A1_18 vqa"))
        self.label_display.setText(_translate("MainWindow", "CAMERA INPUT"))
        self.btn_listen.setText(_translate("MainWindow", "Push to ask"))
        self.vol_down.setText(_translate("MainWindow", "Vol\n"
"Down"))
        self.vol_up.setText(_translate("MainWindow", "Vol\n"
"UP"))
        self.freq_func1.setText(_translate("MainWindow", "Fun1"))
        self.freq_func3.setText(_translate("MainWindow", "Fun3"))
        self.freq_func2.setText(_translate("MainWindow", "Fun2"))
        self.freq_func4.setText(_translate("MainWindow", "Fun4"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuabout.setTitle(_translate("MainWindow", "About"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionCAM_0.setText(_translate("MainWindow", "CAM_0"))
        self.actionCAM_1.setText(_translate("MainWindow", "CAM_1"))
        self.actionCAM_2.setText(_translate("MainWindow", "CAM_2"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.actionVolumn_UP.setText(_translate("MainWindow", "Volumn UP"))
        self.actionVolumn_Down.setText(_translate("MainWindow", "Volumn Down"))
        self.actionVoice_1.setText(_translate("MainWindow", "Voice 1"))
        self.actionVoice_2.setText(_translate("MainWindow", "Voice 2"))
        self.actionInstruction.setText(_translate("MainWindow", "Guide"))
        self.actionContact_for_help.setText(_translate("MainWindow", "Contact for help"))
        self.actionCopyRight.setText(_translate("MainWindow", "Copyright"))
