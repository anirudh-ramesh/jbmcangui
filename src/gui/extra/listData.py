import json
import pickle
import pyqtgraph as pg
from threading import *
from PyQt5 import QtWidgets


class ListData():

    def __init__(self,mainwindow):
        super().__init__()    
        self.mainwindow = mainwindow

    def updateListData(self,table):
        
        while  (self.mainwindow.runThread):
            try:        
                    stream_data = self.mainwindow.database.xrevrange('data_stream', count=1)
                    for data_item in stream_data:
                        data_item = data_item[1][b'data']
                        data_item = pickle.loads(data_item)
                        data_item = json.dumps(data_item)
                        table.setRowCount(table.rowCount() + 1)
                        data_item = QtWidgets.QTableWidgetItem(data_item)
                        table.setItem(table.rowCount() - 1, 0, data_item)

            except:
                pass    
   

    
    def listData(self):
        table = pg.TableWidget()
        table.show()
        table.setRowCount(0)
        table.setColumnCount(1)

        # Set the headers for the columns
        table.setHorizontalHeaderLabels(["Data"])

        #Add the dummy data in column
        # data_item = QtWidgets.QTableWidgetItem('heo')
        # table.setItem(0, 0, data_item)    

        self.mainwindow.addTab(table, str(self.mainwindow.count()+1))
        self.updateStuff = Thread(target=self.updateListData, args=(table,))  
        self.updateStuff.start()