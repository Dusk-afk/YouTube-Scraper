# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QPropertyAnimation, QParallelAnimationGroup, QPoint, QSequentialAnimationGroup, QSize)
import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.bg.setStyleSheet("background-image: url(:/BG/bg.png);")
        self.bg.setObjectName("bg")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(269, 20, 431, 111))
        self.titleLabel.setStyleSheet("image: url(:/BG/title.png);")
        self.titleLabel.setText("")
        self.titleLabel.setObjectName("titleLabel")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(361, 170, 281, 51))
        self.button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_1.setStyleSheet("QPushButton{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/BG/button_1.png);\n"
"}\n"
"QPushButton::Hover{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/BG/button_1_hover.png);\n"
"}")
        self.button_1.setText("")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(361, 255, 281, 51))
        self.button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_2.setStyleSheet("QPushButton{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/Button_2/button_2.png);\n"
"}\n"
"QPushButton::Hover{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/Button_2/button_2_hover.png);\n"
"}")
        self.button_2.setText("")
        self.button_2.setObjectName("button_2")
        self.discordButton = QtWidgets.QPushButton(self.centralwidget)
        self.discordButton.setGeometry(QtCore.QRect(443, 399, 111, 87))
        self.discordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.discordButton.setStyleSheet("QPushButton{\n"
"image: url(:/discord/discord_logo.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}\n"
"QPushButton::Hover{\n"
"image: url(:/BG/discord_logo_hover.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}")
        self.discordButton.setText("")
        self.discordButton.setObjectName("discordButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(341, 375, 321, 161))
        self.label.setStyleSheet("image: url(:/BG/bottom_text.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.bg.raise_()
        self.titleLabel.raise_()
        self.button_1.raise_()
        self.button_2.raise_()
        self.label.raise_()
        self.discordButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_1.clicked.connect(self.animationButton1)
        self.button_2.clicked.connect(self.animationButton2)
        self.discordButton.clicked.connect(self.animationDiscordButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bg.setText(_translate("MainWindow", "TextLabel"))


    def animationButton1(self):
        self.anim = QPropertyAnimation(self.button_1, b"pos")
        self.anim.setEndValue(QPoint(363, 173))
        self.anim.setDuration(100)
        self.anim_2 = QPropertyAnimation(self.button_1, b"size")
        self.anim_2.setEndValue(QSize(275, 45))
        self.anim_2.setDuration(100)
        self.anim_group_1 = QParallelAnimationGroup()
        self.anim_group_1.addAnimation(self.anim)
        self.anim_group_1.addAnimation(self.anim_2)

        self.anim_3 = QPropertyAnimation(self.button_1, b"pos")
        self.anim_3.setEndValue(QPoint(361, 170))
        self.anim_3.setDuration(100)
        self.anim_4 = QPropertyAnimation(self.button_1, b"size")
        self.anim_4.setEndValue(QSize(281, 51))
        self.anim_4.setDuration(100)
        self.anim_group_2 = QParallelAnimationGroup()
        self.anim_group_2.addAnimation(self.anim_3)
        self.anim_group_2.addAnimation(self.anim_4)

        self.anim_final_group = QSequentialAnimationGroup()
        self.anim_final_group.addAnimation(self.anim_group_1)
        self.anim_final_group.addAnimation(self.anim_group_2)
        self.anim_final_group.start()
   
    def animationButton2(self):
        self.anim = QPropertyAnimation(self.button_2, b"pos")
        self.anim.setEndValue(QPoint(363, 258))
        self.anim.setDuration(100)
        self.anim_2 = QPropertyAnimation(self.button_2, b"size")
        self.anim_2.setEndValue(QSize(275, 45))
        self.anim_2.setDuration(100)
        self.anim_group_1 = QParallelAnimationGroup()
        self.anim_group_1.addAnimation(self.anim)
        self.anim_group_1.addAnimation(self.anim_2)

        self.anim_3 = QPropertyAnimation(self.button_2, b"pos")
        self.anim_3.setEndValue(QPoint(361, 255))
        self.anim_3.setDuration(100)
        self.anim_4 = QPropertyAnimation(self.button_2, b"size")
        self.anim_4.setEndValue(QSize(281, 51))
        self.anim_4.setDuration(100)
        self.anim_group_2 = QParallelAnimationGroup()
        self.anim_group_2.addAnimation(self.anim_3)
        self.anim_group_2.addAnimation(self.anim_4)

        self.anim_final_group = QSequentialAnimationGroup()
        self.anim_final_group.addAnimation(self.anim_group_1)
        self.anim_final_group.addAnimation(self.anim_group_2)
        self.anim_final_group.start()

    def animationDiscordButton(self):
        self.anim = QPropertyAnimation(self.discordButton, b"pos")
        self.anim.setEndValue(QPoint(446, 402))
        self.anim.setDuration(100)
        self.anim_2 = QPropertyAnimation(self.discordButton, b"size")
        self.anim_2.setEndValue(QSize(105, 81))
        self.anim_2.setDuration(100)
        self.anim_group_1 = QParallelAnimationGroup()
        self.anim_group_1.addAnimation(self.anim)
        self.anim_group_1.addAnimation(self.anim_2)

        self.anim_3 = QPropertyAnimation(self.discordButton, b"pos")
        self.anim_3.setEndValue(QPoint(443, 399))
        self.anim_3.setDuration(100)
        self.anim_4 = QPropertyAnimation(self.discordButton, b"size")
        self.anim_4.setEndValue(QSize(111, 87))
        self.anim_4.setDuration(100)
        self.anim_group_2 = QParallelAnimationGroup()
        self.anim_group_2.addAnimation(self.anim_3)
        self.anim_group_2.addAnimation(self.anim_4)

        self.anim_final_group = QSequentialAnimationGroup()
        self.anim_final_group.addAnimation(self.anim_group_1)
        self.anim_final_group.addAnimation(self.anim_group_2)
        self.anim_final_group.start()
        webbrowser.open("https://discord.gg/F4E2TjgYqC")
        

import Resources



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
