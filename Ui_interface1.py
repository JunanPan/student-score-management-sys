# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Pyqt_project\PyQt教程\成绩查询系统-数据库界面\interface1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.lineEdit_5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_13.addWidget(self.lineEdit_6)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.page_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_14.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_14.addWidget(self.lineEdit_7)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_15.addWidget(self.lineEdit_8)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.comboBox = QtWidgets.QComboBox(self.page_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBox)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem9)
        self.label_10 = QtWidgets.QLabel(self.page_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_16.addWidget(self.lineEdit_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem10)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_16.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_11 = QtWidgets.QLabel(self.page_6)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_18.addWidget(self.label_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_18.addWidget(self.lineEdit_10)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem12)
        self.pushButton_5 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_19.addWidget(self.pushButton_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_19)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_12 = QtWidgets.QLabel(self.page_7)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_21.addWidget(self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_21.addWidget(self.lineEdit_11)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem13)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_13 = QtWidgets.QLabel(self.page_7)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_22.addWidget(self.label_13)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_22.addWidget(self.lineEdit_12)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_22)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem14)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_14 = QtWidgets.QLabel(self.page_7)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_23.addWidget(self.label_14)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_7)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_23.addWidget(self.lineEdit_13)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_23)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem15)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_24.addWidget(self.pushButton_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_24)
        self.gridLayout_7.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_15 = QtWidgets.QLabel(self.page_8)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_26.addWidget(self.label_15)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_26.addWidget(self.lineEdit_14)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem16)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem17)
        self.pushButton_7 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_27.addWidget(self.pushButton_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_27)
        self.gridLayout_8.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_8)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuk = QtWidgets.QMenu(self.menubar)
        self.menuk.setObjectName("menuk")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.menuk.addAction(self.action)
        self.menuk.addAction(self.action_2)
        self.menuk.addAction(self.action_3)
        self.menu.addAction(self.action_10)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_5.addAction(self.action_8)
        self.menu_5.addAction(self.action_9)
        self.menubar.addAction(self.menuk.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "课程号："))
        self.label_2.setText(_translate("MainWindow", "课程名："))
        self.label_3.setText(_translate("MainWindow", "学分："))
        self.pushButton.setText(_translate("MainWindow", "修改"))
        self.label_4.setText(_translate("MainWindow", "课程号："))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.label_5.setText(_translate("MainWindow", "请输入学号："))
        self.pushButton_3.setText(_translate("MainWindow", "查询"))
        self.label_6.setText(_translate("MainWindow", "学号："))
        self.label_7.setText(_translate("MainWindow", "姓名："))
        self.label_8.setText(_translate("MainWindow", "年龄："))
        self.label_9.setText(_translate("MainWindow", "性别："))
        self.comboBox.setItemText(0, _translate("MainWindow", "男"))
        self.comboBox.setItemText(1, _translate("MainWindow", "女"))
        self.label_10.setText(_translate("MainWindow", "班级："))
        self.pushButton_4.setText(_translate("MainWindow", "添加或修改"))
        self.label_11.setText(_translate("MainWindow", "学号："))
        self.pushButton_5.setText(_translate("MainWindow", "删除"))
        self.label_12.setText(_translate("MainWindow", "学号："))
        self.label_13.setText(_translate("MainWindow", "课程号："))
        self.label_14.setText(_translate("MainWindow", "成绩："))
        self.pushButton_6.setText(_translate("MainWindow", "添加或修改"))
        self.label_15.setText(_translate("MainWindow", "学号："))
        self.pushButton_7.setText(_translate("MainWindow", "删除"))
        self.menuk.setTitle(_translate("MainWindow", "开课情况查询"))
        self.menu.setTitle(_translate("MainWindow", "学生成绩查询"))
        self.menu_2.setTitle(_translate("MainWindow", "学生信息维护"))
        self.menu_3.setTitle(_translate("MainWindow", "学生成绩维护"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.menu_5.setTitle(_translate("MainWindow", "退出"))
        self.action.setText(_translate("MainWindow", "查询所有课程"))
        self.action_2.setText(_translate("MainWindow", "修改课程信息"))
        self.action_3.setText(_translate("MainWindow", "删除课程信息"))
        self.action_4.setText(_translate("MainWindow", "添加和修改学生记录"))
        self.action_5.setText(_translate("MainWindow", "删除学生记录"))
        self.action_6.setText(_translate("MainWindow", "添加和修改学生成绩"))
        self.action_7.setText(_translate("MainWindow", "删除学生成绩"))
        self.action_8.setText(_translate("MainWindow", "关闭程序"))
        self.action_9.setText(_translate("MainWindow", "返回登录界面"))
        self.action_10.setText(_translate("MainWindow", "学生成绩查询"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
