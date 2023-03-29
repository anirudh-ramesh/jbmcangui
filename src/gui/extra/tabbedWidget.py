import redis
from threading import *
from PyQt5 import QtWidgets,QtCore
from src.can_part.main import CanData
from src.gui.extra.listData import ListData
from src.gui.extra.plotData import PlotData

              
class TabbedWidget(QtWidgets.QTabWidget,QtCore.QThread):

    def __init__(self,arg):
        super().__init__()

        self.setTabsClosable(True)
        self.setMovable(True)
        self.tabCloseRequested.connect(self.removeTabHandler)
        self.setStyleSheet('QTabBar::tab { height: 30px; width: 150px;}')
        self.runThread= True
        self.database = redis.Redis(host='localhost', port=6379, db=0)
        self.graphicHandler = ""
     

    def createNewTab(self,filePath):
        #create a condata object
        self.stopEvent = Event()
        self.candata = CanData(self.stopEvent,filePath)
        self.candata.start()
        self.runThread = True

        if(self.graphicHandler == "p"):
            self.plot = PlotData(self)
            self.plot.plotData()

        if(self.graphicHandler == "l"):
            self.listData = ListData(self)
            self.listData.listData()


    def removeTabHandler(self, index):  
        self.removeTab(index)
        self.runThread = False
        self.stopEvent.set()
        self.candata.join()
        self.stopEvent.clear()


    def openFile(self):
        # Open a file dialog to allow the user to select a file
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if filePath:
            # Call a function to read the contents of the file and upload it to the desired location
            self.createNewTab(filePath)

                           
    def startList(self):
        self.graphicHandler = "l"
        self.openFile()

    def startPlot(self):
        self.graphicHandler = "p"
        self.openFile()    