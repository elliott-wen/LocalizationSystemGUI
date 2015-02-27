import logging
import struct

import serial
from PyQt4 import QtCore

from particlefilter import ParticleFilter
from config import Config


# from kalmanfilter import KalmanFilter
# from serialdao import SerialData


class SerialController(QtCore.QThread):
    runFlag = False
    location_updated = QtCore.pyqtSignal(int, tuple)

    def __init__(self):
        #self.database_engine = create_engine('sqlite:///db.sqlite')
        super(SerialController, self).__init__()
        self.portname = Config.serial_name
        self.serial_fd = None
        self.database_engine = None
        self.filters = {}


    def open_serial(self):
        self.serial_fd = serial.Serial(self.portname, 115200)
        self.runFlag = True
        self.start()

    def stop_serial(self):
        self.runFlag = False
        self.join()

    def run(self):
        while self.runFlag == True:
            magic = self.serial_fd.read()
            if magic != b'\xa5':
                logging.warning("Bag magic number")
                continue

            data = self.serial_fd.read(9)
            tagId = data[0]
            anchorId = data[1] - 112
            sequence = data[2]
            rssi = data[3]
            distance = (float)(struct.unpack('>I', data[4:8])[0]) / 100

            checksum = data[8]
            #if anchorId == 1:
            #print("%d %d %f %d %d"%(tagId,anchorId,distance,rssi,sequence))
            self.handleData(tagId, anchorId, distance, rssi, sequence)

    def handleData(self, tagId, anchorId, distance, rssi, sequence):
        if tagId not in self.filters.keys():
            filter = ParticleFilter()
            filter.init_particles()
            self.filters[tagId] = filter
        location = self.filters[tagId].update(anchorId, distance)
        if location != None:
            self.location_updated.emit(tagId, location)
            #print(location)

            # item = SerialData()
            # item.tagID=tagId
            # item.sequence=sequence
            # item.distance = json.dumps(distances)
            # item.velocity = json.dumps(velocity)
            # item.angle = angle
            # item.voltage = voltage
            # item.temperature = temperature
            # item.create_time = datetime.now()
            # s = Session(bind=self.database_engine)
            # s.add(item)
            # s.commit()
















