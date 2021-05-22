# Painstakingly programmed by Ian Fettes
# Lead Programmer, Smithville Tiger Trons
# 5503

import wpilib
import wpilib.drive
import rev
from subsystems import subsystems


class RobotMain(wpilib.TimedRobot):

    def __init__(self):
        super().__init__()
        self.topShooter = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.bottomShooter = rev.CANSparkMax(4, rev.MotorType.kBrushless)
        self.leftDrive = wpilib.VictorSP(0)
        self.rightDrive = wpilib.VictorSP(1)
        self.intake = wpilib.VictorSP(2)
        self.leftClimb = wpilib.PWMTalonFX(4)
        self.rightClimb = wpilib.PWMTalonFX(5)
        self.servo = wpilib.Servo(9)
        self.drive = wpilib.drive.DifferentialDrive(self.leftDrive, self.rightDrive)
        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.stick.getY() * 0.65, self.stick.getX() * 0.65)  # Drive Speed at 65%
        subsystems.Subsystems()
        subsystems.Commands()


if __name__ == "__main__":
    wpilib.run(RobotMain)
