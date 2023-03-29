import cantools
import random
import can
import redis
import pickle
from threading import *
import time

class CanData(Thread):

    def __init__(self,stopEvent,filepath):
        super().__init__()
        self.stopEvent = stopEvent
        self.database = redis.Redis(host='localhost', port=6379, db=0)
        # self.basepath = "C:\\Users\\speed\\OneDrive\\Desktop\\can_bus\\FOC_gui\\FOC_copy\\src\\can_part\\jbm\\JBM.DBC"
        self.basepath = filepath

    def cache_stream_data(self):
        data= self.decodeMessages(self.basepath)
        if(data == None):
            return
        
        hash_data = pickle.dumps(data[0])
        timestamp = data[1]
        self.database.xadd('data_stream',{'data':hash_data})
        self.database.xadd('time_stream',{'time':timestamp})

        # try:        
        #             # stream_data = self.database.xrevrange('data_stream', count=1)
        #             # for item in stream_data:
        #             #     item = item[1][b'data']
        #             #     item = pickle.loads(item)
        #             #     print(item)
        #             stream_data = self.database.xrevrange('time_stream', count=1)    
        #             for item in stream_data:
        #                 item = item[1][b'time'].decode("utf-8") 
        #                 print(float(item))
        # except:
        #         pass    


    def decodeMessages(self,filePath):
        db = cantools.database.load_file(filePath)
        with open('src\can_part\jbm\JBM_today_logs.txt', 'r') as file:
            lines = file.readlines()[1:]

        line = lines[random.randint(1, len(lines)-4)]
        words = line.split()
        arbitration_id = int(words[3],16)
        data_string = words[7:15]
        data = [int(hex_str, 16) for hex_str in data_string]
        try:
            message = can.Message(arbitration_id=arbitration_id, data=data,timestamp=time.time())
            # print(message)
            # print(db.decode_message(message.arbitration_id, message.data,message.timestamp))
            data = db.decode_message(message.arbitration_id, message.data)
            return [data,time.time()]
        except: 
            pass

    # def decodeMessages(self,filePath):
    #     db = cantools.database.load_file(filePath)
    #     can_bus = can.interface.Bus('can0', bustype='socketcan')
    #     try:
    #         message = can_bus.recv()
    #         data = db.decode_message(message.arbitration_id, message.data)
    #         return [data,message.timestamp]
    #     except: 
    #         pass

    def run(self):
        # Run the scheduler
        while not self.stopEvent.is_set():
            self.cache_stream_data()
            # time.sleep(1)

# canata = CanData()
# canata.run()        