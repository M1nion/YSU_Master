from numpy import *

class PID(object):
    def __init__(self):

        self.PID_init()

    def PID_init(self):
        self.err_last = 0
        self.err = 0
        self.ActualBIS = 100
        self.integral = 0

    def control_pid(self, Kp, Ki, Kd, setbis):
        self.SetBIS = setbis
        self.err = self.ActualBIS - self.SetBIS
        self.integral = self.integral + self.err*0.01
        self.diff = (self.err - self.err_last)/0.01
        self.err_last = self.err
        self.pidSpeed = Kp * self.err + Ki * self.integral + Kd * self.diff

        return self.pidSpeed



