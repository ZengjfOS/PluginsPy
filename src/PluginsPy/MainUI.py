# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/PluginsPy/MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 931, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.PSVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.PSVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PSVerticalLayout.setObjectName("PSVerticalLayout")
        self.PSPluginsComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.PSPluginsComboBox.setObjectName("PSPluginsComboBox")
        self.PSVerticalLayout.addWidget(self.PSPluginsComboBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PSGridLayout = QtWidgets.QGridLayout()
        self.PSGridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.PSGridLayout.setContentsMargins(-1, 6, -1, 6)
        self.PSGridLayout.setObjectName("PSGridLayout")
        self.horizontalLayout_4.addLayout(self.PSGridLayout)
        self.PSRunPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PSRunPushButton.sizePolicy().hasHeightForWidth())
        self.PSRunPushButton.setSizePolicy(sizePolicy)
        self.PSRunPushButton.setObjectName("PSRunPushButton")
        self.horizontalLayout_4.addWidget(self.PSRunPushButton)
        self.PSVerticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.PSVerticalLayout.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.PSRegexTemplateComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.PSRegexTemplateComboBox.setObjectName("PSRegexTemplateComboBox")
        self.horizontalLayout_5.addWidget(self.PSRegexTemplateComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PSRegexLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PSRegexLabel.setObjectName("PSRegexLabel")
        self.horizontalLayout_2.addWidget(self.PSRegexLabel)
        self.PSRegexPlainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.PSRegexPlainTextEdit.setObjectName("PSRegexPlainTextEdit")
        self.horizontalLayout_2.addWidget(self.PSRegexPlainTextEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.PSXAxisLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PSXAxisLineEdit.setObjectName("PSXAxisLineEdit")
        self.horizontalLayout_3.addWidget(self.PSXAxisLineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.PSDataIndexLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.PSDataIndexLineEdit.setObjectName("PSDataIndexLineEdit")
        self.horizontalLayout_3.addWidget(self.PSDataIndexLineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.PSPlotTypeComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.PSPlotTypeComboBox.setObjectName("PSPlotTypeComboBox")
        self.horizontalLayout_3.addWidget(self.PSPlotTypeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.PSRegexPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PSRegexPushButton.setObjectName("PSRegexPushButton")
        self.horizontalLayout.addWidget(self.PSRegexPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.PSVisualLogPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PSVisualLogPushButton.setObjectName("PSVisualLogPushButton")
        self.horizontalLayout.addWidget(self.PSVisualLogPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PSTempPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PSTempPushButton.sizePolicy().hasHeightForWidth())
        self.PSTempPushButton.setSizePolicy(sizePolicy)
        self.PSTempPushButton.setObjectName("PSTempPushButton")
        self.verticalLayout.addWidget(self.PSTempPushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.PSVerticalLayout.addLayout(self.horizontalLayout_6)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setMidLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.PSVerticalLayout.addWidget(self.line_2)
        self.PSInfoPlainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.PSInfoPlainTextEdit.setObjectName("PSInfoPlainTextEdit")
        self.PSVerticalLayout.addWidget(self.PSInfoPlainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Android Log Analyze"))
        self.PSRunPushButton.setText(_translate("MainWindow", "Run"))
        self.label_4.setText(_translate("MainWindow", " Regex Template: "))
        self.PSRegexLabel.setText(_translate("MainWindow", " Regex: "))
        self.label.setText(_translate("MainWindow", " X Axis:"))
        self.label_2.setText(_translate("MainWindow", " DataIndex:"))
        self.label_3.setText(_translate("MainWindow", " PlotType: "))
        self.PSRegexPushButton.setText(_translate("MainWindow", "Regex"))
        self.PSVisualLogPushButton.setText(_translate("MainWindow", "Visual Log"))
        self.PSTempPushButton.setText(_translate("MainWindow", "Template"))
