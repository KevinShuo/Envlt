# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_new_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets
from ns_Envlt.ui.resources import envlt_rc


class Ui_create_scene(object):
    def setupUi(self, create_scene):
        create_scene.setObjectName("create_scene")
        create_scene.resize(413, 514)
        create_scene.setStyleSheet("QWidget#create_scene{\n"
                                   "    background-color:#292e3b;\n"
                                   "}\n"
                                   "\n"
                                   "QFrame#frame{\n"
                                   "    border:1px solid #414654;\n"
                                   "    border-radius:20px;\n"
                                   "    background-color:#414654;\n"
                                   "}\n"
                                   "\n"
                                   "QFrame#frame_3{\n"
                                   "    background-color:#292e3b;\n"
                                   "    border:1px solid #292e3b;\n"
                                   "    border-radius:10px;\n"
                                   "}\n"
                                   "QLabel{\n"
                                   "    color:#FFFFFF;\n"
                                   "    font-size:13px;\n"
                                   "    font-family:\"Georgia\"\n"
                                   "}\n"
                                   "\n"
                                   "QLabel#title{\n"
                                   "    font-size:20px;\n"
                                   "    font-weight:bold;\n"
                                   "    font-family:\"Arial Black\";\n"
                                   "    letter-spacing:2px;\n"
                                   "    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.197849 rgba(86, 100, 123, 255), stop:0.890323 rgba(180, 194, 220, 255));\n"
                                   "    font-style:oblique;\n"
                                   "}\n"
                                   "QPushButton{\n"
                                   "    border:none;\n"
                                   "    border-radius:10px;\n"
                                   "    background-color:#FF4D4D;\n"
                                   "    color:#F0F5F9;\n"
                                   "    height:2em;\n"
                                   "    font-family:\"Garamond\";\n"
                                   "    font-size:16px;\n"
                                   "    padding:1px;\n"
                                   "    font-weight:bold;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "    border:none;\n"
                                   "    border-radius:10px;\n"
                                   "    background-color:#ffecda;\n"
                                   "    color:#1E2022;\n"
                                   "    height:10em;\n"
                                   "    font-family:\"Garamond\";\n"
                                   "    font-size:16px;\n"
                                   "    padding:3px;\n"
                                   "    font-weight:bold;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    border:none;\n"
                                   "    border-radius:10px;\n"
                                   "    background-color:#1E2022;\n"
                                   "    color:#F0F5F9;\n"
                                   "    height:2em;\n"
                                   "    font-family:\"Garamond\";\n"
                                   "    font-size:16px;\n"
                                   "    padding:3px;\n"
                                   "    font-weight:bold;\n"
                                   "}\n"
                                   "QLineEdit,QTextEdit,QComboBox{\n"
                                   "    background-color:#414654;\n"
                                   "    color:#FFFFFF;\n"
                                   "    font-family:\"Georgia\";\n"
                                   "    font-size:13px;\n"
                                   "    border-radius:4px;\n"
                                   "}\n"
                                   "QRadioButton{\n"
                                   "    font-family:\"Arial Black\";\n"
                                   "    font-size:14px;\n"
                                   "    color:#e0e0e0;\n"
                                   "    font-style:oblique;\n"
                                   "}\n"
                                   "QRadioButton::indicator {\n"
                                   "    width: 16px;\n"
                                   "    height: 16px;\n"
                                   "}\n"
                                   "QRadioButton::indicator::unchecked {\n"
                                   "    image: url(:/create_new_scene/md-radio-button-off.png);\n"
                                   "}\n"
                                   "QRadioButton::indicator::checked,QRadioButton::indicator:unchecked:hover {\n"
                                   "    image: url(:/create_new_scene/md-radio-button-on.png);\n"
                                   "}\n"
                                   "")
        self.verticalLayout = QtWidgets.QVBoxLayout(create_scene)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(create_scene)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.choose_page = QtWidgets.QFrame(self.frame_4)
        self.choose_page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_page.setObjectName("choose_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.choose_page)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_create = QtWidgets.QRadioButton(self.choose_page)
        self.radioButton_create.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_create.setChecked(True)
        self.radioButton_create.setObjectName("radioButton_create")
        self.horizontalLayout_3.addWidget(self.radioButton_create)
        self.radioButton_clone = QtWidgets.QRadioButton(self.choose_page)
        self.radioButton_clone.setObjectName("radioButton_clone")
        self.horizontalLayout_3.addWidget(self.radioButton_clone)
        self.verticalLayout_5.addWidget(self.choose_page)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.new_widget = QtWidgets.QWidget()
        self.new_widget.setObjectName("new_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.new_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.new_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(self.new_widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_2 = QtWidgets.QLabel(self.new_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_image = QtWidgets.QLineEdit(self.new_widget)
        self.lineEdit_image.setObjectName("lineEdit_image")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_image)
        self.label_3 = QtWidgets.QLabel(self.new_widget)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit_description = QtWidgets.QTextEdit(self.new_widget)
        self.textEdit_description.setObjectName("textEdit_description")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_description)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.stackedWidget.addWidget(self.new_widget)
        self.clone_widget = QtWidgets.QWidget()
        self.clone_widget.setObjectName("clone_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.clone_widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.clone_widget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_choose_project = QtWidgets.QComboBox(self.clone_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_choose_project.sizePolicy().hasHeightForWidth())
        self.comboBox_choose_project.setSizePolicy(sizePolicy)
        self.comboBox_choose_project.setObjectName("comboBox_choose_project")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_choose_project)
        self.line = QtWidgets.QFrame(self.clone_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line)
        self.label_6 = QtWidgets.QLabel(self.clone_widget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_name_2 = QtWidgets.QLineEdit(self.clone_widget)
        self.lineEdit_name_2.setObjectName("lineEdit_name_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name_2)
        self.label_7 = QtWidgets.QLabel(self.clone_widget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_image_2 = QtWidgets.QLineEdit(self.clone_widget)
        self.lineEdit_image_2.setObjectName("lineEdit_image_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_image_2)
        self.label_8 = QtWidgets.QLabel(self.clone_widget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.textEdit_description_2 = QtWidgets.QTextEdit(self.clone_widget)
        self.textEdit_description_2.setObjectName("textEdit_description_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_description_2)
        self.verticalLayout_7.addLayout(self.formLayout_2)
        self.stackedWidget.addWidget(self.clone_widget)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_create = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_create.setObjectName("pushButton_create")
        self.horizontalLayout.addWidget(self.pushButton_create)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(create_scene)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(create_scene)

    def retranslateUi(self, create_scene):
        _translate = QtCore.QCoreApplication.translate
        create_scene.setWindowTitle(_translate("create_scene", "create_new_scene"))
        self.title.setText(_translate("create_scene", "Create new scene"))
        self.radioButton_create.setText(_translate("create_scene", "New"))
        self.radioButton_clone.setText(_translate("create_scene", "Clone"))
        self.label.setText(_translate("create_scene", "Name:"))
        self.lineEdit_name.setPlaceholderText(_translate("create_scene", "Please enter the scene name"))
        self.label_2.setText(_translate("create_scene", "Image:"))
        self.lineEdit_image.setPlaceholderText(_translate("create_scene", "Choose a image for the view"))
        self.label_3.setText(_translate("create_scene", "Desciption"))
        self.textEdit_description.setPlaceholderText(_translate("create_scene", "Please enter scene the description"))
        self.label_5.setText(_translate("create_scene", "Scene:"))
        self.label_6.setText(_translate("create_scene", "Name:"))
        self.lineEdit_name_2.setPlaceholderText(_translate("create_scene", "Please enter the scene name"))
        self.label_7.setText(_translate("create_scene", "Image:"))
        self.lineEdit_image_2.setPlaceholderText(_translate("create_scene", "Choose a image for the view"))
        self.label_8.setText(_translate("create_scene", "Description:"))
        self.textEdit_description_2.setPlaceholderText(_translate("create_scene", "Please enter scene the description"))
        self.pushButton_create.setText(_translate("create_scene", "Create"))
