from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.patches
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

from config import Config


class LocationPlot(QtGui.QWidget):

     def __init__(self,parent = None):
         QtGui.QWidget.__init__(self,parent)
         self.figure = plt.figure(facecolor='white')
         self.canvas = FigureCanvas(self.figure)
         self.toolbar = NavigationToolbar(self.canvas, self)
         self.ax = self.figure.add_subplot(1, 1, 1)
         self.adjust_layout()
         self.set_up_anchors()
         self.set_up_danger_zones()
         self.vbl = QtGui.QVBoxLayout()
         self.vbl.addWidget(self.canvas)
         self.vbl.addWidget(self.toolbar)
         self.setLayout(self.vbl)
         self.figure.tight_layout()

     def adjust_layout(self):
         max_row = 0
         max_column = 0
         for key in Config.anchors:
             item = Config.anchors[key]
             if item[0] > max_row:
                 max_row = item[0]
             if item[1] > max_column:
                 max_column = item[1]
         self.ax.set_xlim([-0.2, max_column * 1.1])
         self.ax.set_ylim([-0.2, max_row * 1.1])
         self.ax.set_title("Location")

     def set_up_anchors(self):
         for key in Config.anchors:
             item = Config.anchors[key]
             rect_patch = matplotlib.patches.Rectangle((item[0], item[1]), (0.1), (0.1), color='red')
             self.ax.add_patch(rect_patch)

     def set_up_danger_zones(self):
         for rect in Config.zones:
             rect_patch = matplotlib.patches.Rectangle((rect[0], rect[1]), (rect[2] - rect[0]), (rect[3] - rect[1]),
                                                       color='red')
             rect_patch.set_alpha(0.1)
             self.ax.add_patch(rect_patch)

     def print_position(self, tagId, position):

         self.ax.scatter(position[0], position[1])
         self.canvas.draw()