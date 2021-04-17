# Created by Ian Fettes
# Lead Programmer of 5503

import wpilib
import wpilib.drive
import rev


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        # Drivetrain
        self.leftDrive = wpilib.VictorSP(0) # PWM 0
        self.rightDrive = wpilib.VictorSP(1) # PWM 1

        # Ball Shooter
        self.topShooter = rev.CANSparkMax(1) # CAN ID 1
        self.bottomShooter = rev.CANSparkMax(4) # CAN ID 4

        # Ball Intake
        self.intake = wpilib.VictorSP(5)

        # MISC
        self.joystick = wpilib.Joystick(0)
        self.drive = wpilib.drive.DifferentialDrive(self.leftDrive, self.rightDrive)


    def teleopPeroidic(self):
        self.drive.arcadeDrive(self.joystick.getY() * 0.65, self.joystick.getX() * 0.65) # Run Drivetrain at 65%

if __name__ == "__main__":
    wpilib.run(MyRobot)