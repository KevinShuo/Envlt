# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Envlt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_mainWindows(object):
    def setupUi(self, mainWindows):
        mainWindows.setObjectName("mainWindows")
        mainWindows.resize(749, 574)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindows.sizePolicy().hasHeightForWidth())
        mainWindows.setSizePolicy(sizePolicy)
        mainWindows.setStyleSheet("QWidget#mainWindows{\n"
                                  "    background-color:#292e3b;\n"
                                  "}\n"
                                  "\n"
                                  "QStackedWidget#about{\n"
                                  "    background-color:transparent;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget{\n"
                                  "border:none\n"
                                  "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(mainWindows)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(mainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 45))
        self.frame.setStyleSheet("QFrame#Head{\n"
                                 "    background-color:#414654;\n"
                                 "    border-radius:17px;\n"
                                 "}\n"
                                 "QFrame#Head QLabel#title{\n"
                                 "    color:#1E2022;\n"
                                 "    font-size:16px;\n"
                                 "    font-weight:bold;\n"
                                 "    Padding:2px;\n"
                                 "    font-family:Comic Sans MS,serif;\n"
                                 "    letter-spacing:2px;\n"
                                 "    font-style:oblique;\n"
                                 "}\n"
                                 "\n"
                                 "QFrame#Head QPushButton#new_button,QFrame#Head QPushButton#about_button,QFrame#Head QPushButton#project{\n"
                                 "    color:#e0e0e0;\n"
                                 "    background-color:transparent;\n"
                                 "    font-size:15px;\n"
                                 "    font-weight:bold;\n"
                                 "    font-family:Segoe UI,serif;\n"
                                 "    width:50%;\n"
                                 "}\n"
                                 "\n"
                                 "QFrame#Head QPushButton#new_button:hover,QFrame#Head QPushButton#about_button:hover,QFrame#Head QPushButton#project:hover{\n"
                                 "    color:#FFFFFF;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Head = QtWidgets.QFrame(self.frame)
        self.Head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Head.setObjectName("Head")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Head)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title = QtWidgets.QLabel(self.Head)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.about_button = QtWidgets.QPushButton(self.Head)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_button.sizePolicy().hasHeightForWidth())
        self.about_button.setSizePolicy(sizePolicy)
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        self.project = QtWidgets.QPushButton(self.Head)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project.sizePolicy().hasHeightForWidth())
        self.project.setSizePolicy(sizePolicy)
        self.project.setObjectName("project")
        self.horizontalLayout.addWidget(self.project)
        self.new_button = QtWidgets.QPushButton(self.Head)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_button.sizePolicy().hasHeightForWidth())
        self.new_button.setSizePolicy(sizePolicy)
        self.new_button.setMinimumSize(QtCore.QSize(0, 0))
        self.new_button.setObjectName("new_button")
        self.horizontalLayout.addWidget(self.new_button)
        self.verticalLayout_2.addWidget(self.Head)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(mainWindows)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.about = QtWidgets.QWidget()
        self.about.setStyleSheet("QLabel#main_title{\n"
                                 "    color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.21501 rgba(224, 224, 224, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "    font-size:60px;\n"
                                 "    font-family:Impact;\n"
                                 "    letter-spacing:2px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#main_title:hover,QLabel#subtitle:hover,QLabel#subtitle_2:hover{\n"
                                 "    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.197849 rgba(86, 100, 123, 255), stop:0.890323 rgba(180, 194, 220, 255));\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#subtitle,QLabel#subtitle_2{\n"
                                 "    color:#e0e0e0;\n"
                                 "    font-family:Segoe UI;\n"
                                 "    font-size:13px;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.about.setObjectName("about")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.about)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.main_title = QtWidgets.QLabel(self.about)
        self.main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title.setObjectName("main_title")
        self.verticalLayout_4.addWidget(self.main_title)
        self.subtitle = QtWidgets.QLabel(self.about)
        self.subtitle.setTextFormat(QtCore.Qt.PlainText)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")
        self.verticalLayout_4.addWidget(self.subtitle)
        self.subtitle_2 = QtWidgets.QLabel(self.about)
        self.subtitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle_2.setObjectName("subtitle_2")
        self.verticalLayout_4.addWidget(self.subtitle_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.about)
        self.project_2 = QtWidgets.QWidget()
        self.project_2.setStyleSheet("QScrollArea{\n"
                                     "    background-color:transparent;\n"
                                     "}\n"
                                     "\n"
                                     "QWidget#project_view{\n"
                                     "    background-color:transparent;\n"
                                     "}")
        self.project_2.setObjectName("project_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.project_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.project_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.project_view = QtWidgets.QWidget()
        self.project_view.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.project_view.setObjectName("project_view")
        self.scrollArea.setWidget(self.project_view)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.project_2)
        self.new_2 = QtWidgets.QWidget()
        self.new_2.setObjectName("new_2")
        self.stackedWidget.addWidget(self.new_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(mainWindows)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindows)

    def retranslateUi(self, mainWindows):
        _translate = QtCore.QCoreApplication.translate
        mainWindows.setWindowTitle(_translate("mainWindows", "Form"))
        self.title.setText(_translate("mainWindows", "Environment"))
        self.about_button.setText(_translate("mainWindows", "About"))
        self.project.setText(_translate("mainWindows", "Project"))
        self.new_button.setText(_translate("mainWindows", "New"))
        self.main_title.setText(_translate("mainWindows", "Environment tools"))
        self.subtitle.setText(_translate("mainWindows", "A tool that collects assets, libs, scatters and render"))
        self.subtitle_2.setText(_translate("mainWindows", "Support: ABC and USD"))


from ns_Envlt.ui.resources import envlt_rc
