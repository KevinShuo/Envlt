# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scene_lib.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(423, 621)
        Form.setStyleSheet("QWidget#Form{\n"
                           "    background-color:#1A1F2B;\n"
                           "}\n"
                           "QFrame#main{\n"
                           "    background-color:#414654;\n"
                           "    border-radius:15px;\n"
                           "}\n"
                           "QLabel#head{\n"
                           "    background-color: rgb(41, 46, 59);\n"
                           "    border-radius:25px;\n"
                           "    padding:2px;\n"
                           "}\n"
                           "QLabel#name{\n"
                           "    color:#FFFFFF;\n"
                           "    font-size:15px;\n"
                           "    font-weight:bold;\n"
                           "    font-family:\"Segoe UI\";\n"
                           "    letter-spacing:2px;\n"
                           "\n"
                           "}\n"
                           "QLabel#date{\n"
                           "    color:#e0e0e0;\n"
                           "    font-size:13px;\n"
                           "    font-family:\"Calibri\";\n"
                           "}\n"
                           "QFrame#header_area{\n"
                           "    background-color:#292e3b;\n"
                           "    border-radius:10px;\n"
                           "}\n"
                           "\n"
                           "QTabWidget::pane { /* The tab widget frame */\n"
                           "    border-top: 1px solid #414654;\n"
                           "    background-color:#292e3b;\n"
                           "}\n"
                           "QTabBar::tab{\n"
                           "    font-size:13px;\n"
                           "    width:80%;\n"
                           "    font-family:\"Calibri\";\n"
                           "}\n"
                           "QTabWidget > QWidget{\n"
                           "    background-color:#292e3b;\n"
                           "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(Form)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_area = QtWidgets.QFrame(self.header)
        self.header_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_area.setObjectName("header_area")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_area)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.head = QtWidgets.QLabel(self.header_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.head.sizePolicy().hasHeightForWidth())
        self.head.setSizePolicy(sizePolicy)
        self.head.setMinimumSize(QtCore.QSize(32, 32))
        self.head.setText("")
        self.head.setPixmap(QtGui.QPixmap(r"C:\dev\maya\Envlt\src\ns_Envlt\ui\resources\User.png"))
        self.head.setScaledContents(False)
        self.head.setObjectName("head")
        self.horizontalLayout_2.addWidget(self.head)
        self.frame = QtWidgets.QFrame(self.header_area)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name)
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setObjectName("date")
        self.verticalLayout_2.addWidget(self.date)
        self.horizontalLayout_2.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.header_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\dev\maya\Envlt\src\ns_Envlt\ui\resources\note.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.header_area)
        self.verticalLayout.addWidget(self.header)
        self.tab_section = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_section.sizePolicy().hasHeightForWidth())
        self.tab_section.setSizePolicy(sizePolicy)
        self.tab_section.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_section.setObjectName("tab_section")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_section)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_section)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.common = QtWidgets.QWidget()
        self.common.setObjectName("common")
        self.tabWidget.addTab(self.common, "")
        self.add_tab = QtWidgets.QWidget()
        self.add_tab.setObjectName("add_tab")
        self.tabWidget.addTab(self.add_tab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.tab_section)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "hi.wangshuo"))
        self.date.setText(_translate("Form", "Good moring"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.common), _translate("Form", "Common"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_tab), _translate("Form", "+"))

