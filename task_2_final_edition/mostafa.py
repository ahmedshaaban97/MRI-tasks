# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shabaan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_phantom = QtWidgets.QLabel(self.centralwidget)
        self.lbl_phantom.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_phantom.sizePolicy().hasHeightForWidth())
        self.lbl_phantom.setSizePolicy(sizePolicy)
        self.lbl_phantom.setMinimumSize(QtCore.QSize(10, 10))
        self.lbl_phantom.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.lbl_phantom.setAutoFillBackground(False)
        self.lbl_phantom.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_phantom.setScaledContents(True)
        self.lbl_phantom.setObjectName("lbl_phantom")
        self.gridLayout.addWidget(self.lbl_phantom, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView_2 = PlotWidget(self.tab_15)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_6.addWidget(self.graphicsView_2)
        self.graphicsView_3 = PlotWidget(self.tab_15)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_6.addWidget(self.graphicsView_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kspace = QtWidgets.QPushButton(self.tab_16)
        self.kspace.setObjectName("kspace")
        self.horizontalLayout.addWidget(self.kspace)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton = QtWidgets.QPushButton(self.tab_16)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lbl_kspace = QtWidgets.QLabel(self.tab_16)
        self.lbl_kspace.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_kspace.sizePolicy().hasHeightForWidth())
        self.lbl_kspace.setSizePolicy(sizePolicy)
        self.lbl_kspace.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.lbl_kspace.setAutoFillBackground(False)
        self.lbl_kspace.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_kspace.setScaledContents(True)
        self.lbl_kspace.setObjectName("lbl_kspace")
        self.gridLayout_9.addWidget(self.lbl_kspace, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_9.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_9.addItem(spacerItem7, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_16, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_logan_2 = QtWidgets.QPushButton(self.tab)
        self.btn_logan_2.setObjectName("btn_logan_2")
        self.horizontalLayout_4.addWidget(self.btn_logan_2)
        self.CBox_size_2 = QtWidgets.QComboBox(self.tab)
        self.CBox_size_2.setObjectName("CBox_size_2")
        self.CBox_size_2.addItem("")
        self.CBox_size_2.addItem("")
        self.CBox_size_2.addItem("")
        self.CBox_size_2.addItem("")
        self.CBox_size_2.addItem("")
        self.CBox_size_2.addItem("")
        self.horizontalLayout_4.addWidget(self.CBox_size_2)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_browse_2 = QtWidgets.QPushButton(self.tab_2)
        self.btn_browse_2.setObjectName("btn_browse_2")
        self.horizontalLayout_6.addWidget(self.btn_browse_2)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.horizontalLayout_8.addWidget(self.tabWidget_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_2)
        self.btn_convert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convert.setObjectName("btn_convert")
        self.verticalLayout_5.addWidget(self.btn_convert)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.SP_theta = QtWidgets.QSpinBox(self.centralwidget)
        self.SP_theta.setMaximum(390)
        self.SP_theta.setProperty("value", 90)
        self.SP_theta.setObjectName("SP_theta")
        self.horizontalLayout_10.addWidget(self.SP_theta)
        self.SP_TE = QtWidgets.QSpinBox(self.centralwidget)
        self.SP_TE.setMaximum(1000000)
        self.SP_TE.setSingleStep(10)
        self.SP_TE.setProperty("value", 1500)
        self.SP_TE.setObjectName("SP_TE")
        self.horizontalLayout_10.addWidget(self.SP_TE)
        self.SP_TR = QtWidgets.QSpinBox(self.centralwidget)
        self.SP_TR.setMaximum(100000000)
        self.SP_TR.setSingleStep(10)
        self.SP_TR.setProperty("value", 5000)
        self.SP_TR.setObjectName("SP_TR")
        self.horizontalLayout_10.addWidget(self.SP_TR)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addLayout(self.verticalLayout_12)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_phantom.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("MainWindow", "Graphs"))
        self.kspace.setText(_translate("MainWindow", "Create K_space"))
        self.pushButton.setText(_translate("MainWindow", "Convert K_space to image"))
        self.lbl_kspace.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("MainWindow", "K_Space"))
        self.btn_logan_2.setText(_translate("MainWindow", "shabelogan"))
        self.CBox_size_2.setItemText(0, _translate("MainWindow", "20*20"))
        self.CBox_size_2.setItemText(1, _translate("MainWindow", "32*32"))
        self.CBox_size_2.setItemText(2, _translate("MainWindow", "64*64"))
        self.CBox_size_2.setItemText(3, _translate("MainWindow", "128*128"))
        self.CBox_size_2.setItemText(4, _translate("MainWindow", "256*256"))
        self.CBox_size_2.setItemText(5, _translate("MainWindow", "512*512"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Shabelogan Phantom"))
        self.btn_browse_2.setText(_translate("MainWindow", "browse"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Browse Phantom"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "phantom"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "T1 effect"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "T2 effect"))
        self.btn_convert.setText(_translate("MainWindow", "Convert"))
        self.label.setText(_translate("MainWindow", "Theta"))
        self.label_2.setText(_translate("MainWindow", "Time To Echo"))
        self.label_3.setText(_translate("MainWindow", "Time To Repeat"))

from pyqtgraph import PlotWidget