# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Aug 19 11:30:26 2014
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1440, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = LocationPlot(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuApplication = QtGui.QMenu(self.menubar)
        self.menuApplication.setObjectName(_fromUtf8("menuApplication"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuAbout_2 = QtGui.QMenu(self.menubar)
        self.menuAbout_2.setObjectName(_fromUtf8("menuAbout_2"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionDynamic_Tags = QtGui.QAction(mainWindow)
        self.actionDynamic_Tags.setObjectName(_fromUtf8("actionDynamic_Tags"))
        self.actionDangerous_Zones_Settings = QtGui.QAction(mainWindow)
        self.actionDangerous_Zones_Settings.setObjectName(_fromUtf8("actionDangerous_Zones_Settings"))
        self.actionAnchor_Settings = QtGui.QAction(mainWindow)
        self.actionAnchor_Settings.setObjectName(_fromUtf8("actionAnchor_Settings"))
        self.actionHistory_Query = QtGui.QAction(mainWindow)
        self.actionHistory_Query.setObjectName(_fromUtf8("actionHistory_Query"))
        self.actionHistory_Event = QtGui.QAction(mainWindow)
        self.actionHistory_Event.setObjectName(_fromUtf8("actionHistory_Event"))
        self.menuSettings.addAction(self.actionDynamic_Tags)
        self.menuSettings.addAction(self.actionDangerous_Zones_Settings)
        self.menuSettings.addAction(self.actionAnchor_Settings)
        self.menuAbout.addAction(self.actionHistory_Query)
        self.menuAbout.addAction(self.actionHistory_Event)
        self.menubar.addAction(self.menuApplication.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuAbout_2.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Localization System", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "TagID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Location", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Time", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Event", None))
        self.menuApplication.setTitle(_translate("mainWindow", "Application", None))
        self.menuSettings.setTitle(_translate("mainWindow", "Settings", None))
        self.menuAbout.setTitle(_translate("mainWindow", "Query", None))
        self.menuAbout_2.setTitle(_translate("mainWindow", "About", None))
        self.actionDynamic_Tags.setText(_translate("mainWindow", "Dynamic Tag Settings", None))
        self.actionDangerous_Zones_Settings.setText(_translate("mainWindow", "Dangerous Zones Settings", None))
        self.actionAnchor_Settings.setText(_translate("mainWindow", "Anchor Settings", None))
        self.actionHistory_Query.setText(_translate("mainWindow", "History Trajectory", None))
        self.actionHistory_Event.setText(_translate("mainWindow", "History Event", None))

from locationplot import LocationPlot
