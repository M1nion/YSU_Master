from numpy import *
import numpy as np

class Ceff(object):
    def __init__(self):

        self.Ceff_init()

    def Ceff_init(self):

        self.C1 = 0
        self.C2 = 0
        self.C3 = 0
        self.Ceff = 0
        self.dt = 0.0001
        self.dt2 = 0.01
        self.CeffSpeed = 0
        self.gender = 'x'
        self.weight = 0
        self.height = 0
        self.age = 0

    def Ceff_Para(self):
        self.V1 = 4.27
        self.V2 = 18.9-0.391*(self.age-53)
        self.V3 = 238

        if self.gender == 'male':
            self.lbm = 1.1*self.weight-128*(self.weight**2)/(self.height**2)
        elif self.gender == 'femal':
            self.lbm = 1.07*self.weight-148*(self.weight**2)/(self.height**2)
        else:
            pass
        self.Cl1 = 1.89+0.0456*(self.weight-77)-0.0681*(self.lbm-59)+0.0264*(self.height-177)
        self.Cl2 = 1.29-0.024*(self.age-53)
        self.Cl3 = 0.836

    def Ceffinal(self, u):
        self.count = 1
        while (self.count<1000):
            self.C = self.iteration1(self.C1, self.C2, self.C3, u)
            self.ceffinal = self.iteration2(self.C1)
            self.C1 = self.C[0][0]
            self.C2 = self.C[1][0]
            self.C3 = self.C[2][0]
            self.count = self.count + 1
        return self.ceffinal




    def fceff(self, ceff, C1):
        self.ke0 = 0.456
        self.ceffdot = self.ke0*(C1-ceff)
        return self.ceffdot

    def pkCeff(self, C1, C2, C3, u):
        self.k10 = self.Cl1/self.V1
        self.k12 = self.Cl2/self.V1
        self.k13 = self.Cl3/self.V1
        self.k21 = self.Cl2/self.V2
        self.k31 = self.Cl3/self.V3
        self.a1 = -(self.k10+self.k12+self.k13)
        self.b1 = self.k21*self.V2/self.V1
        self.c1 = self.k31*self.V3/self.V1
        self.d1 = 1/self.V1
        self.a2 = self.k12*self.V1/self.V2
        self.b2 = -self.k21
        self.a3 = self.k13*self.V1/self.V3
        self.b3 = -self.k31

        self.C1dot = self.a1*C1+self.b1*C2+self.c1*C3+self.d1*u
        self.C2dot = self.a2*C1-self.b2*C2
        self.C3dot = self.a3*C1-self.b3*C3

        self.cdot = [self.C1dot, self.C1dot, self.C1dot]
        self.Cdot= np.reshape(self.cdot, (3, 1))

        return self.C1dot, self.C2dot, self.C3dot

    def iteration1(self, C1, C2, C3, u):
        self.k1a, self.k1b, self.k1c = self.pkCeff(C1, C2, C3, u)
        self.k2a, self.k2b, self.k2c = self.pkCeff(C1+(self.dt/2*self.k1a),
                                                   C2+(self.dt/2*self.k1b),
                                                   C3+(self.dt/2*self.k1c), u)
        self.k3a, self.k3b, self.k3c = self.pkCeff(C1+(self.dt/2*self.k2a),
                                                   C2+(self.dt/2*self.k2b),
                                                   C3+(self.dt/2*self.k2c), u)
        self.k4a, self.k4b, self.k4c = self.pkCeff(C1+(self.dt*self.k3a),
                                                   C2+(self.dt*self.k3b),
                                                   C3+(self.dt*self.k3c), u)
        self.cc = [C1, C2, C3]
        self.CC = np.reshape(self.cc, (3, 1))
        self.k1 = [self.k1a, self.k1b, self.k1c]
        self.K1 = np.reshape(self.k1, (3, 1))
        self.k2 = [self.k2a, self.k2b, self.k2c]
        self.K2 = np.reshape(self.k2, (3, 1))
        self.k3 = [self.k3a, self.k3b, self.k3c]
        self.K3 = np.reshape(self.k3, (3, 1))
        self.k4 = [self.k4a, self.k4b, self.k4c]
        self.K4 = np.reshape(self.k4, (3, 1))
        self.CC = self.CC+self.dt/6*(self.K1+2*self.K2+2*self.K3+self.K4)
        return self.CC

    def iteration2(self, C1):
        self.ceff1 = self.fceff(self.Ceff, C1)
        self.ceff2 = self.fceff(self.Ceff+self.dt2/2 *self.ceff1, C1)
        self.ceff3 = self.fceff(self.Ceff+self.dt2/2 *self.ceff2, C1)
        self.ceff4 = self.fceff(self.Ceff+self.dt2*self.ceff3, C1)
        self.Ceff = self.Ceff + self.dt2/6*(self.ceff1+2*self.ceff2+2*self.ceff3+self.ceff4)
        return self.Ceff

    def BIS_calculate(self, ceff):
        self.EC50 = 4.700
        self.E0 = 100
        self.Emax = 100
        self.r = 3
        self.bis_calculate = self.E0-self.Emax*(ceff**self.r)/((ceff**self.r)+(self.EC50**self.r))
        return self.bis_calculate


