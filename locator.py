import serial
import threading
import logging
import struct
from config import Config
from sqlalchemy import create_engine
from kalmanfilter import KalmanFilter
from serialdao import SerialData
from datetime import datetime
from sqlalchemy.orm import Session
import json

class SerialController(threading.Thread):
    runFlag = False
    def __init__(self):
        self.database_engine = create_engine('sqlite:///db.sqlite')
        self.portname =  Config.serial_name
        self.serial_fd = None
        self.database_engine = None
        self.kalmanFilters = {}
        super(SerialController,self).__init__(name="Serial Thread")

    def open_serial(self):
        self.serial_fd = serial.Serial(self.portname,57600)
        self.runFlag = True
        self.start()

    def stop_serial(self):
        self.runFlag = False
        self.join()

    def run(self):
        while self.runFlag == True:
            magic = self.serial_fd.read()
            if magic!= b'0xa5':
                logging.warning("Bag magic number")
                continue
            data = self.serial_fd.read(47)
            tagId = data[0]
            sequence = struct.unpack('>B',data[1:3])
            data = data[11:]
            temperature = struct.unpack('<f',data[:4])
            voltage = struct.unpack('<f',data[4:8])
            angle = struct.unpack('<f',data[8:12])
            d1 = struct.unpack('<f',data[12:16])
            d2 = struct.unpack('<f',data[16:20])
            d3 = struct.unpack('<f',data[20:24])
            d4 = struct.unpack('<f',data[24:28])
            v1 = struct.unpack('<f',data[28:32])
            v2 = struct.unpack('<f',data[32:36])
            distance = [d1,d2,d3,d4]
            velocity = [v1,v2]
            self.handleData(tagId,sequence,distance,velocity,angle,temperature,voltage)

    def handleData(self,tagId,sequence,distances,velocity,angle,temperature,voltage):
        if tagId not in self.kalmanFilters.keys():
            self.kalmanFilters[tagId] = KalmanFilter()
        location = self.kalmanFilters[tagId].update(distances,velocity)
        item = SerialData()
        item.tagID=tagId
        item.sequence=sequence
        item.distance = json.dumps(distances)
        item.velocity = json.dumps(velocity)
        item.angle = angle
        item.voltage = voltage
        item.temperature = temperature
        item.create_time = datetime.now()
        s = Session(bind=self.database_engine)
        s.add(item)
        s.commit()
















