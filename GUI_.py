#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate


class Ui_MainWindow2(QtWidgets.QWidget):

    def set_ui(self, localWindow):
        print("set_ui")
        global path, cache
        path = 'Cache/'
        cache = './Cache/'
        localWindow.setObjectName("localWindow")
        localWindow.resize(2560, 1600)
        localWindow.setMinimumSize(QtCore.QSize(2560, 1600))
        localWindow.setMaximumSize(QtCore.QSize(2560, 1600))

        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
        self.__flag_work = 0
        self.x = 0
        self.__layout_main = QtWidgets.QHBoxLayout()
        self.__layout_fun_button = QtWidgets.QVBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()

        self.button_open_camera = QtWidgets.QPushButton(u'Open Cam')
        self.button_capture = QtWidgets.QPushButton(u'Capture')
        self.button_path = QtWidgets.QPushButton(u'Save as')
        self.select_camera = QComboBox(self)
        self.button_close = QtWidgets.QPushButton(u'Quit')
        self.button_open_camera.setMinimumHeight(50)
        self.button_path.setMinimumHeight(50)
        self.button_capture.setMinimumHeight(50)
        self.select_camera.setMinimumHeight(50)
        self.button_close.setMinimumHeight(50)

        self.button_close.move(10, 100)

        # 信息显示
        self.label_show_camera = QtWidgets.QLabel()
        self.label_move = QtWidgets.QLabel()
        self.label_move.setFixedSize(200, 200)

        self.label_show_camera.setFixedSize(1921, 1441)
        self.label_show_camera.setStyleSheet("border:1px solid black;")
        self.label_show_camera.setText("相机未打开")
        self.label_show_camera.setAlignment(Qt.AlignCenter)
        self.label_show_camera.setAutoFillBackground(False)

        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_capture)
        self.__layout_fun_button.addWidget(self.button_path)
        self.__layout_fun_button.addWidget(self.select_camera)
        self.select_camera.addItem('CAMERA_0')
        self.select_camera.addItem('CAMERA_1')
        self.select_camera.addItem('CAMERA_2')
        self.select_camera.addItem('CAMERA_3')
        self.select_camera.addItem('CAMERA_4')
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_fun_button.addWidget(self.label_move)

        # delegate = AlignDelegate(self.select_camera)
        # self.select_camera.setItemDelegate(delegate)
        # self.select_camera.setEditable(True)
        # self.select_camera.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.select_camera.setToolTip("Make sure the camera you select is available")

        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)

        self.setLayout(self.__layout_main)
        self.label_move.raise_()
        self.setWindowTitle(u'VQA')
        self.slot_init()

    def slot_init(self):
        print("slot_init")
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.button_capture.clicked.connect(self.button_capture_click)
        self.button_path.clicked.connect(self.button_path_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)
        self.select_camera.currentIndexChanged[int].connect(self.select_camera_changed)

    def button_open_camera_click(self):
        print("button_open_camera_click")
        self.label_move.setText("")
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning",
                                                    u"Please check the connection between computer and camera",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
                self.label_show_camera.setText("相机未连接")
            else:
                self.timer_camera.start(30)

                self.button_open_camera.setText(u'Close Cam')
        else:
            self.label_move.setText("")
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText(u'Open Cam')
            self.label_show_camera.setText("相机未打开")

    def button_capture_click(self):
        self.label_move.setText("")
        global path, cache
        currentDateTime = QDateTime.currentDateTime();
        currentDateStr = currentDateTime.toString("hh_mm_ss");
        self.label_move.setText("")
        ret, frame = self.cap.read()
        if (ret):
            cv2.imwrite(path + "Capture_" + currentDateStr + '.jpeg', frame)
            cv2.imwrite(cache + "Cache" + '.jpeg', frame)
            self.label_move.setText("拍摄成功!")
        else:
            self.label_move.setText("相机未打开!")
        print("Capture")

    def button_path_click(self):
        self.label_move.setText("")
        global path
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select path for converted image", os.getcwd())
        print("Choose path")

    def select_camera_changed(self, i):
        self.CAM_NUM = int(i)
        print("Camera:" + str(i))

    def show_camera(self):
        # self.cap.set(3, 1080)
        # self.cap.set(4, 1920)
        flag, self.image = self.cap.read()
        # face = self.face_detect.align(self.image)
        # if face:
        #     pass

        show = cv2.resize(self.image, (1920, 1440))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow2()
    ui.set_ui(ui)
    ui.show()
    sys.exit(app.exec_())
