# Painstakingly programmed by Ian Fettes
# Lead Programmer, Smithville Tiger Trons
# 5503


from networktables import NetworkTables


class Limelight:
    def __init__(self):
        self.table = NetworkTables.getTable("limelight")
        tx = self.table.getNumber("tx", None)
        ty = self.table.getNumber("ty", None)
        ta = self.table.getNumber("ta", None)
        ts = self.table.getNumber("ts", None)

    def visionEnabled(self):
        self.table.putNumber("camMode", 0)  # Vision Processing Enabled
        self.table.putNumber("ledMode", 3)  # LED Array Enabled

    def visionDisabled(self):
        self.table.putNumber("camMode", 1)  # Operator Camera Enabled
        self.table.putNumber("ledMode", 1)  # LED Array Disabled
