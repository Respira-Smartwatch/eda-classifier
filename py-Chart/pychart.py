from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from random import randint
import sys  # We need sys so that we can pass argv to QApplication
import os

class PyChart(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        # Super - Obvi
        super(PyChart, self).__init__(*args, **kwargs)

        # Create a Graph widget
        self.graphWidget = pg.PlotWidget()
        # Set the central widtet to graph widget
        self.setCentralWidget(self.graphWidget)

        # Data
        #hour = [1,2,3,4,5,6,7,8,9,10]
        #temperature = [30,32,34,32,33,31,29,32,35,45]

        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]
        self.y2 = [randint(0,100) for _ in range(100)]

        # pen is a line marker, color is red
        pen = pg.mkPen(color=(255,0,0))    
        pen2 = pg.mkPen(color=(0,0,255))

        # Title
        self.graphWidget.setTitle("Graph", color="b", size="30pt")
        
        # Show the grid
        self.graphWidget.showGrid(x=True, y=True)

        # setting a whight background color
        self.graphWidget.setBackground('w')

        # Plotting
        # For static plotting
        #self.graphWidget.plot(hour, temperature, pen=pen)

        # For plot Streaming
        self.data_line = self.graphWidget.plot(self.x,self.y, pen=pen)
        self.data_line2 = self.graphWidget.plot(self.x, self.y2, pen=pen2)

        # Start a timer function
        self.timer = QtCore.QTimer()                        # Initialize a timer
        self.timer.setInterval(50)                          # Set the timer interval
        self.timer.timeout.connect(self.update_plot_data)   # Set timeout behaviour
        self.timer.start()                                  # Start timer


    def update_plot_data(self):

        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y2 = self.y2[1:]
        self.y.append(randint(0,100))
        self.y2.append(randint(0,100))

        self.data_line.setData(self.x, self.y)
        self.data_line2.setData(self.x, self.y2)



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = PyChart()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()