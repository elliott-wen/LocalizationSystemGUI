from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt




class LocationPlot(QtGui.QWidget):

     def __init__(self,parent = None):
         QtGui.QWidget.__init__(self,parent)
         self.figure = plt.figure()
         self.canvas = FigureCanvas(self.figure)
         self.vbl = QtGui.QVBoxLayout()
         self.vbl.addWidget(self.canvas)
         self.setLayout(self.vbl)



