
import wpilib
import wpilib.drive

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        self.leftDrive = wpilib.VictorSP(0)
        self.rightDrive = wpilib.VictorSP(1)

        self.drive = wpilib.drive.DifferentialDrive(self.leftDrive, self.rightDrive)
        self.stick = wpilib.Joystick(0)
 

    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.stick.getY() * 0.65, self.stick.getX() * 0.65) # Drive Speed at 65% 

if __name__ == "__main__":
    wpilib.run(MyRobot)