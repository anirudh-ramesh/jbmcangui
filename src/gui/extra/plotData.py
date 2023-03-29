import pickle
import pyqtgraph as pg
from threading import *

class PlotData():
    def __init__(self,mainwindow):
        super().__init__()      
        self.mainwindow = mainwindow

    def updatePlotData(self,plot):
        soc = None
        max = None
        soc_data = []
        soc_time = []
        max_data = []
        max_time = []
        while self.mainwindow.runThread:
            try:        
                    stream_data = self.mainwindow.database.xrevrange('data_stream', count=1)
                    stream_time = self.mainwindow.database.xrevrange('time_stream', count = 1)

                    data_item = stream_data[0]
                    data_item = data_item[1][b'data']
                    data_item = pickle.loads(data_item)

                    time_item = stream_time[0]
                    time_item = time_item[1][b'time']
                    time_item = float(time_item)

                    if ('B2V_SOC' in data_item ):
                        pen = pg.mkPen(color="b")
                        soc_data.append(data_item["B2V_SOC"])
                        soc_time.append(time_item)
                        if soc == None:
                            soc = plot.plot(soc_time,soc_data,name="B2V_SOC",pen= pen,symbol='+', symbolSize=20,symbolBrush=("b")) 
                        else:
                            pass
                            # if (len(soc_data)>10):
                            #     soc_data = soc_data[1:]
                            #     soc_time = soc_time[1:]
                        soc.setData(soc_time,soc_data)    
                    if('B2V_MaxChrgV' in data_item):
                        pen = pg.mkPen(color="r")
                        max_data.append(data_item["B2V_MaxChrgV"])
                        max_time.append(time_item)
                        if max == None:
                            max = plot.plot(max_time,max_data,name="B2V_MaxChrgV",pen= pen,symbol='+', symbolSize=20,symbolBrush=("r"))  
                        else:
                            pass
                            # if(len(max_data)>10):
                            #     max_data = max_data[1:]
                            #     max_time = max_time[1:]
                        max.setData(max_time,max_data)                                          
            except:
                pass 


    def plotData(self):
        plot = pg.PlotWidget()
        plot.addLegend()
        plot.showGrid(x=True,y=True)
        self.mainwindow.addTab(plot, str(self.mainwindow.count()+1))
        self.updateStuff = Thread(target=self.updatePlotData, args=(plot,))  
        self.updateStuff.start()  