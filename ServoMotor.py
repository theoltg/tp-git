class ServoMotor:
    def __init__(self,pinV,pinCOM,pinPMW, angle):
        self.pinV=pinV
        self.pinCOM=pinCOM
        self.pinPMW=pinPMW
        self.angle=None
        
    def Rotation(self):
        print("Rotation at {self.angle}°")