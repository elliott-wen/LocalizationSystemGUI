import numpy as np
import math
from config import Config
class KalmanFilter():

    def __init__(self):
        updateFrequency = 1
        self.q = np.diag([2,2,2,0.5,0.5,0.01])
        self.x = np.array([[0.01,0.01,0.01,0.01,0.01,0.01]]).transpose()
        self.p = np.diag([1000000.0,1000000,1000000,1000000,1000000,1000000])
        self.i = np.diag([1.,1.,1.,1.,1.,1.])
        self.a = np.array([[1,0,0,updateFrequency,0,0], [0 ,1, 0,0, updateFrequency, 0],[0, 0, 1, 0, 0, updateFrequency],[0, 0, 0,1,0,0], [0,0,0,0,1,0],[0,0,0,0,0,1]],dtype=float)
        self.er = np.array([[0,0,0,0]],dtype=float)

    def update(self,distances,velocity):
        anchors = {1:(0,0,0),2:(100,0,0),3:(100,100,0),4:(0,100,0)}

        z = []
        meaningless_h = []
        r = np.diag([2,2,2,2,0.2,0.2,0.01])
        h = np.array([[1.0,1,1,0,0,0],[1,1,1,0,0,0],[1,1,1,0,0,0],[1,1,1,0,0,0],[ 0,0,0,1,0,0 ],[0,0,0,0,1,0],[0,0,0,0,0,1]])
        self.x =self.a.dot(self.x)
        self.p = self.a.dot(self.p).dot(self.a.transpose())+self.q

        for (key,distance) in distances.items():
            anchor = Config.anchors[key]
            temp = math.sqrt(math.pow(self.x[0][0]-anchor[0],2)+math.pow(self.x[1][0]-anchor[1],2)+math.pow(self.x[2][0]-anchor[2],2))
            meaningless_h.append(temp)
            h1 = (self.x[0][0]-anchor[0])/temp
            h2 =(self.x[1][0]-anchor[1])/temp
            h3 =(self.x[2][0]-anchor[2])/temp
            h[key-1][0]=h1
            h[key-1][1]=h2
            h[key-1][2]=h3

            if self.er[0][key-1]>1:
                r[key-1][key-1]=self.er[0][key-1]*self.er[0][key-1]
                if distance < 5:
                    r[key-1][key-1]=0.1*distance
            else:
                r[key-1][key-1]=0.15
            z.append(distance)

        dominate = np.mat(h.dot(self.p).dot(h.transpose()) + r)

        k = self.p.dot(h.transpose()).dot(dominate.I)

        z = z + velocity

        self.mz = np.array([z]).transpose()
        meaningless_h.append(self.x[3][0])
        meaningless_h.append(self.x[4][0])
        meaningless_h.append(self.x[5][0])
        self.mh = np.array([meaningless_h]).transpose()
        self.x =self.x + k.dot(self.mz-self.mh)
        self.p =(self.i - k.dot(h)).dot(self.p)

        return (float(self.x[0][0]),float(self.x[1][0]),float(self.x[2][0]))
