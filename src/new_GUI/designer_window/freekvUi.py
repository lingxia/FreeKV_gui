# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freekvUi.ui'
#
# Created: Thu Sep 11 20:04:56 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_freekvUi(object):
    def setupUi(self, freekvUi):
        freekvUi.setObjectName(_fromUtf8("freekvUi"))
        freekvUi.resize(392, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/dp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        freekvUi.setWindowIcon(icon)
        self.demoGroupBox = QtGui.QGroupBox(freekvUi)
        self.demoGroupBox.setGeometry(QtCore.QRect(10, 120, 371, 201))
        self.demoGroupBox.setObjectName(_fromUtf8("demoGroupBox"))
        self.freekvTabWidget = QtGui.QTabWidget(self.demoGroupBox)
        self.freekvTabWidget.setGeometry(QtCore.QRect(10, 20, 351, 171))
        self.freekvTabWidget.setObjectName(_fromUtf8("freekvTabWidget"))
        self.basicTab = QtGui.QWidget()
        self.basicTab.setObjectName(_fromUtf8("basicTab"))
        self.label = QtGui.QLabel(self.basicTab)
        self.label.setGeometry(QtCore.QRect(0, 10, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.platformLabel = QtGui.QLabel(self.basicTab)
        self.platformLabel.setGeometry(QtCore.QRect(0, 50, 54, 21))
        self.platformLabel.setObjectName(_fromUtf8("platformLabel"))
        self.platformComboBox = QtGui.QComboBox(self.basicTab)
        self.platformComboBox.setGeometry(QtCore.QRect(60, 50, 161, 22))
        self.platformComboBox.setObjectName(_fromUtf8("platformComboBox"))
        self.appComboBox = QtGui.QComboBox(self.basicTab)
        self.appComboBox.setGeometry(QtCore.QRect(60, 10, 161, 22))
        self.appComboBox.setEditable(True)
        self.appComboBox.setObjectName(_fromUtf8("appComboBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/config_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.freekvTabWidget.addTab(self.basicTab, icon1, _fromUtf8(""))
        self.buildTab = QtGui.QWidget()
        self.buildTab.setObjectName(_fromUtf8("buildTab"))
        self.testDirLabel = QtGui.QLabel(self.buildTab)
        self.testDirLabel.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.testDirLabel.setObjectName(_fromUtf8("testDirLabel"))
        self.testLineEdit = QtGui.QLineEdit(self.buildTab)
        self.testLineEdit.setGeometry(QtCore.QRect(50, 10, 121, 20))
        self.testLineEdit.setObjectName(_fromUtf8("testLineEdit"))
        self.projectLabel = QtGui.QLabel(self.buildTab)
        self.projectLabel.setGeometry(QtCore.QRect(0, 50, 101, 20))
        self.projectLabel.setObjectName(_fromUtf8("projectLabel"))
        self.projectComboBox = QtGui.QComboBox(self.buildTab)
        self.projectComboBox.setGeometry(QtCore.QRect(98, 50, 71, 22))
        self.projectComboBox.setObjectName(_fromUtf8("projectComboBox"))
        self.projectComboBox.addItem(_fromUtf8(""))
        self.projectComboBox.addItem(_fromUtf8(""))
        self.ideLabel = QtGui.QLabel(self.buildTab)
        self.ideLabel.setGeometry(QtCore.QRect(0, 80, 21, 20))
        self.ideLabel.setObjectName(_fromUtf8("ideLabel"))
        self.ideComboBox = QtGui.QComboBox(self.buildTab)
        self.ideComboBox.setGeometry(QtCore.QRect(30, 80, 69, 22))
        self.ideComboBox.setStatusTip(_fromUtf8(""))
        self.ideComboBox.setObjectName(_fromUtf8("ideComboBox"))
        self.ideLineEdit = QtGui.QLineEdit(self.buildTab)
        self.ideLineEdit.setGeometry(QtCore.QRect(110, 80, 151, 20))
        self.ideLineEdit.setObjectName(_fromUtf8("ideLineEdit"))
        self.targetComboBox = QtGui.QComboBox(self.buildTab)
        self.targetComboBox.setGeometry(QtCore.QRect(240, 50, 91, 22))
        self.targetComboBox.setObjectName(_fromUtf8("targetComboBox"))
        self.targetLabel = QtGui.QLabel(self.buildTab)
        self.targetLabel.setGeometry(QtCore.QRect(190, 50, 31, 21))
        self.targetLabel.setObjectName(_fromUtf8("targetLabel"))
        self.libComboBox = QtGui.QComboBox(self.buildTab)
        self.libComboBox.setGeometry(QtCore.QRect(240, 10, 91, 22))
        self.libComboBox.setObjectName(_fromUtf8("libComboBox"))
        self.libComboBox.addItem(_fromUtf8(""))
        self.libComboBox.addItem(_fromUtf8(""))
        self.libLabel = QtGui.QLabel(self.buildTab)
        self.libLabel.setGeometry(QtCore.QRect(190, 10, 41, 20))
        self.libLabel.setObjectName(_fromUtf8("libLabel"))
        self.versionLabel = QtGui.QLabel(self.buildTab)
        self.versionLabel.setGeometry(QtCore.QRect(110, 110, 51, 16))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.ideVersionComboBox = QtGui.QComboBox(self.buildTab)
        self.ideVersionComboBox.setGeometry(QtCore.QRect(30, 110, 69, 22))
        self.ideVersionComboBox.setEditable(True)
        self.ideVersionComboBox.setObjectName(_fromUtf8("ideVersionComboBox"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/build_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.freekvTabWidget.addTab(self.buildTab, icon2, _fromUtf8(""))
        self.runTab = QtGui.QWidget()
        self.runTab.setObjectName(_fromUtf8("runTab"))
        self.debuggerLabel = QtGui.QLabel(self.runTab)
        self.debuggerLabel.setGeometry(QtCore.QRect(0, 10, 51, 21))
        self.debuggerLabel.setObjectName(_fromUtf8("debuggerLabel"))
        self.debuggerLineEdit = QtGui.QLineEdit(self.runTab)
        self.debuggerLineEdit.setGeometry(QtCore.QRect(150, 10, 181, 20))
        self.debuggerLineEdit.setObjectName(_fromUtf8("debuggerLineEdit"))
        self.debuggerComboBox = QtGui.QComboBox(self.runTab)
        self.debuggerComboBox.setGeometry(QtCore.QRect(48, 10, 91, 22))
        self.debuggerComboBox.setObjectName(_fromUtf8("debuggerComboBox"))
        self.serialLabel = QtGui.QLabel(self.runTab)
        self.serialLabel.setGeometry(QtCore.QRect(0, 50, 61, 21))
        self.serialLabel.setObjectName(_fromUtf8("serialLabel"))
        self.serialLineEdit = QtGui.QLineEdit(self.runTab)
        self.serialLineEdit.setGeometry(QtCore.QRect(50, 50, 91, 20))
        self.serialLineEdit.setObjectName(_fromUtf8("serialLineEdit"))
        self.debugPortLineEdit = QtGui.QLineEdit(self.runTab)
        self.debugPortLineEdit.setGeometry(QtCore.QRect(210, 50, 121, 20))
        self.debugPortLineEdit.setText(_fromUtf8(""))
        self.debugPortLineEdit.setObjectName(_fromUtf8("debugPortLineEdit"))
        self.debugPortLabel = QtGui.QLabel(self.runTab)
        self.debugPortLabel.setGeometry(QtCore.QRect(150, 50, 61, 21))
        self.debugPortLabel.setObjectName(_fromUtf8("debugPortLabel"))
        self.binaryLabel = QtGui.QLabel(self.runTab)
        self.binaryLabel.setGeometry(QtCore.QRect(0, 80, 41, 21))
        self.binaryLabel.setObjectName(_fromUtf8("binaryLabel"))
        self.binaryLineEdit = QtGui.QLineEdit(self.runTab)
        self.binaryLineEdit.setGeometry(QtCore.QRect(30, 80, 301, 20))
        self.binaryLineEdit.setObjectName(_fromUtf8("binaryLineEdit"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/run_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.freekvTabWidget.addTab(self.runTab, icon3, _fromUtf8(""))
        self.typeGroupBox = QtGui.QGroupBox(freekvUi)
        self.typeGroupBox.setGeometry(QtCore.QRect(10, 60, 161, 51))
        self.typeGroupBox.setObjectName(_fromUtf8("typeGroupBox"))
        self.buildCheckBox = QtGui.QCheckBox(self.typeGroupBox)
        self.buildCheckBox.setGeometry(QtCore.QRect(20, 20, 51, 17))
        self.buildCheckBox.setCheckable(True)
        self.buildCheckBox.setChecked(False)
        self.buildCheckBox.setObjectName(_fromUtf8("buildCheckBox"))
        self.runCheckBox = QtGui.QCheckBox(self.typeGroupBox)
        self.runCheckBox.setGeometry(QtCore.QRect(90, 20, 41, 17))
        self.runCheckBox.setObjectName(_fromUtf8("runCheckBox"))
        self.startButton = QtGui.QPushButton(freekvUi)
        self.startButton.setGeometry(QtCore.QRect(200, 80, 71, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))

        self.retranslateUi(freekvUi)
        self.freekvTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(freekvUi)

    def retranslateUi(self, freekvUi):
        freekvUi.setWindowTitle(_translate("freekvUi", "FreeKV Configuration", None))
        freekvUi.setStatusTip(_translate("freekvUi", "Configuration for FreeKV_demo", None))
        self.demoGroupBox.setTitle(_translate("freekvUi", "FreeKV_demo Configuration", None))
        self.freekvTabWidget.setStatusTip(_translate("freekvUi", "Select the type to configurate", None))
        self.label.setStatusTip(_translate("freekvUi", "App name to build/run", None))
        self.label.setText(_translate("freekvUi", "App Name", None))
        self.platformLabel.setStatusTip(_translate("freekvUi", "Platform to build/run", None))
        self.platformLabel.setText(_translate("freekvUi", "Platform", None))
        self.freekvTabWidget.setTabText(self.freekvTabWidget.indexOf(self.basicTab), _translate("freekvUi", "Basic", None))
        self.testDirLabel.setStatusTip(_translate("freekvUi", "Test code dirctory e.g. C:/mcu-sdk", None))
        self.testDirLabel.setText(_translate("freekvUi", "Test Dir", None))
        self.projectLabel.setStatusTip(_translate("freekvUi", "Generate project or not", None))
        self.projectLabel.setText(_translate("freekvUi", "Generate Project", None))
        self.projectComboBox.setItemText(0, _translate("freekvUi", "yes", None))
        self.projectComboBox.setItemText(1, _translate("freekvUi", "no", None))
        self.ideLabel.setStatusTip(_translate("freekvUi", "IDE and its dirctory with rigth version", None))
        self.ideLabel.setText(_translate("freekvUi", "IDE", None))
        self.targetLabel.setStatusTip(_translate("freekvUi", "Build target", None))
        self.targetLabel.setText(_translate("freekvUi", "Target", None))
        self.libComboBox.setItemText(0, _translate("freekvUi", "yes", None))
        self.libComboBox.setItemText(1, _translate("freekvUi", "no", None))
        self.libLabel.setStatusTip(_translate("freekvUi", "Build lib or not ", None))
        self.libLabel.setText(_translate("freekvUi", "Build Lib", None))
        self.versionLabel.setText(_translate("freekvUi", "*version", None))
        self.freekvTabWidget.setTabText(self.freekvTabWidget.indexOf(self.buildTab), _translate("freekvUi", "Build", None))
        self.debuggerLabel.setStatusTip(_translate("freekvUi", "Debugger name and dirctory", None))
        self.debuggerLabel.setText(_translate("freekvUi", "Debugger", None))
        self.serialLabel.setStatusTip(_translate("freekvUi", "Serial port", None))
        self.serialLabel.setText(_translate("freekvUi", "Serial Port", None))
        self.debugPortLabel.setStatusTip(_translate("freekvUi", "Debug port(Jlink SN)", None))
        self.debugPortLabel.setText(_translate("freekvUi", "Debug Port", None))
        self.binaryLabel.setStatusTip(_translate("freekvUi", "Binary dirctory", None))
        self.binaryLabel.setText(_translate("freekvUi", "Binary", None))
        self.freekvTabWidget.setTabText(self.freekvTabWidget.indexOf(self.runTab), _translate("freekvUi", "Run", None))
        self.typeGroupBox.setTitle(_translate("freekvUi", "Configuration Type", None))
        self.buildCheckBox.setStatusTip(_translate("freekvUi", "Configuration for build", None))
        self.buildCheckBox.setText(_translate("freekvUi", "Build", None))
        self.runCheckBox.setStatusTip(_translate("freekvUi", "Configuration for run", None))
        self.runCheckBox.setText(_translate("freekvUi", "Run", None))
        self.startButton.setStatusTip(_translate("freekvUi", "Start build/run", None))
        self.startButton.setText(_translate("freekvUi", "Start", None))
