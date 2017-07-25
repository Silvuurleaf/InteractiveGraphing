import sys
#Importing PyQt5 library to construct widgets for Graphic User Interface (GUI) application
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QSlider, QApplication, QVBoxLayout, QHBoxLayout,
                             QApplication, QWidget, QLabel, QCheckBox, QRadioButton, QPlainTextEdit, QSizePolicy,
                             QMainWindow,QFrame, QFileDialog, QTableWidgetItem, QTableWidget, QMenu, QMessageBox,
                             QAction, QToolBar)
from PyQt5.QtCore import Qt, QAbstractTableModel, pyqtSignal


import matplotlib
matplotlib.use("Qt5Agg")


from numpy import arange, sin, pi

from matplotlib import pyplot as plt
plt.style.use(['ggplot'])


#Backend door for matplotlib importation required to use Pyqt with matpltlib libray
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationBar
from matplotlib.figure import Figure
import matplotlib.ticker as mticker

import csv
import pandas as pd
import numpy as np
import statistics

from functools import partial



class createFIG(FigureCanvas):
    def __init__(self):
        #super().__init__(Figure(tight_layout=True))
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)

        self.name = ""

        # xdata = [1,2,3,4,5]
        # ydata = [12,4,56,78,9]

        plt.figure()
        self.axes.set_xlabel('x label')

        #self.plotData(xdata,ydata)

        self.PlotSignal.connect(self.plotData)


    def plotData(self, xdata,ydata):
        print("plotting")
        self.axes.plot(xdata, ydata)
        self.draw()
        plt.show()

class update(createFIG):
    ###current work in progress not in use###
    def __init__(self):
        super(update, self).__init__()
    #def update(self):

        print("update")
        self.axes.cla()
        #set the axis bounds here with user inpurt
        self.axes.set_xlim([0,3])
        self.axes.set_xlabel('New label')
        createFIG()



class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Perspective")

        self.initializeUI()

    def initializeUI(self):

        xdata = [1,2,3,4,5]
        ydata = [12,4,56,78,9]

        #Main Widget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.plotbtn = QPushButton("Plot")
        self.plotbtn.clicked.connect(partial(self.initiatePlot, xdata, ydata))

        self.hMAIN = QHBoxLayout(self.main_widget)
        self.vboxLeft = QVBoxLayout()
        self.vboxLeft.addWidget(self.plotbtn)

        self.hbox1 = QHBoxLayout()

        self.vboxLeft.addLayout(self.hbox1)

        self.PlotLayout = QVBoxLayout()
        #self.PlotLayout.addWidget(self.Graph)
        #self.PlotLayout.addWidget(self.NavBar)

        self.hMAIN.addLayout(self.vboxLeft)
        self.hMAIN.addLayout(self.PlotLayout)



        self.show()
    def initiatePlot(self,x,y):
        PlotSignal = pyqtSignal(list, list)
        self.PlotSignal.emit(x, y)


def main():
        # main loop
        app = QtWidgets.QApplication(sys.argv)
        # instance
        window = MainWindow()
        window.show()
        # appWindow = MainWindow()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()


