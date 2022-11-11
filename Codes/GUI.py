import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow
import user_interface
import time
import cv2

# Our files
import audio_to_text
import text_to_audio
import vqa_v1

class MyMainForm(QMainWindow, user_interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.my_init()
        self.function_connect()

        self.log("Program start")
        self.camera(True)

    def btn_listen_clicked(self):
        # if not self.listen_statue:
        #     self.log("Start listening")
        #     self.btn_listen.setText("Listening...")
        #     self.listen_statue = True
        # else:
        #     self.log("Stop listening")
        #     self.btn_listen.setText("Push to ask")
        #     self.listen_statue = False
        self.btn_listen.setText("Listening...")
        self.capture()
        self.log("Start listening")
        # Disable function in case of multiple function call
        self.btn_listen.setDisabled(True)
        question_text = audio_to_text.audio_to_text()
        self.log("Your question:\n" + question_text['transcript'])
        self.log("Stop listening")
        answer_text = vqa_v1.ask_and_answer("./Cache/cache_img.png", question_text['transcript'], None)[0]
        self.log(answer_text)
        text_to_audio.text_to_audio(answer_text,"./Cache/cache_audio.mp3")
        self.btn_listen.setText("Push to ask")
        self.btn_listen.setDisabled(False)

    def capture(self):
        cv2.imwrite("./Cache/cache_img.png", self.image)

    def camera(self, cmd):
        if cmd:
            self.log("Open camera " + str(self.cam_num))
            if not self.camera_timer.isActive():
                flag = self.cap.open(self.cam_num)
                if not flag:
                    msg = QtWidgets.QMessageBox.warning(self, u"Warning",
                                                        u"Please check the connection between computer and camera",
                                                        buttons=QtWidgets.QMessageBox.Ok,
                                                        defaultButton=QtWidgets.QMessageBox.Ok)
                    self.label_display.setText("Camera not connected")
                else:
                    self.camera_timer.start(30)

                    # self.button_open_camera.setText(u'Close Cam')
            else:
                self.log("Close camera" + str(self.cam_num))
                self.camera_timer.stop()
                self.cap.release()
                # self.label_show_camera.clear()
                self.label_display.setText("CAMERA INPUT")
        else:
            pass

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (1400, 1050))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_display.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def my_init(self):
        self.cam_num = 0
        self.camera_timer = QtCore.QTimer()
        self.cap = cv2.VideoCapture()

        self.listen_statue = False

    def function_connect(self):
        self.camera_timer.timeout.connect(self.show_camera)
        self.btn_listen.clicked.connect(self.btn_listen_clicked)

    def log(self, text):
        prev_text = self.txt_log.toPlainText()
        time_now = time.strftime(prev_text + "\n" + "%H:%M:%S", time.localtime())
        self.txt_log.setText(time_now + ": " + text)
        self.txt_log.moveCursor(QTextCursor.End)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
