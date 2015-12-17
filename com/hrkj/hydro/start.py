'''
Created on 2015年12月8日

@author: DAYDAYUP
'''
from com.hrkj.gui.mplCanvasWrapper import *
from PyQt4 import QtGui
 
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = MplCanvasWrapper()
    widget.resize(250, 150)
    widget.setWindowTitle("simple")
    widget.startPlot()
    widget.show()
    sys.exit(app.exec_())