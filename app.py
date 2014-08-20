
from PyQt4 import QtGui
from config import Config
from mainwindow_ui import Ui_mainWindow
from anchorswindow import AnchorsWindow
from dynamicswindow import DynamicsWindow
from zoneswindow import ZonesWindow
import sys


class MainWindow(QtGui.QMainWindow):

    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.actionAnchor_Settings.triggered.connect(self.open_anchor_setting)
        self.ui.actionDynamic_Tags.triggered.connect(self.open_dynamic_setting)
        self.ui.actionDangerous_Zones_Settings.triggered.connect(self.open_zone_setting)

    def open_zone_setting(self):
        zonesWindow = ZonesWindow(parent = self)
        zonesWindow.exec()


    def open_anchor_setting(self):
        anchorWindow = AnchorsWindow(parent = self)
        anchorWindow.exec()


    def open_dynamic_setting(self):
        dynamicWindow = DynamicsWindow(parent = self)
        dynamicWindow.exec()





if __name__ == "__main__":
    Config.load_config()
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())