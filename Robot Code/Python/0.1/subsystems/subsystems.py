# Painstakingly programmed by Ian Fettes
# Lead Programmer, Smithville Tiger Trons
# 5503

import commands2.button
import robot
import limelight


class Commands:
    def intakeForwardCommand(self):
        commands2.button.JoystickButton.whileHeld(4, Subsystems.RunIntakeForward(self))

    def intakeReverseCommand(self):
        commands2.button.JoystickButton.whileHeld(2, Subsystems.RunIntakeReverse(self))

    def shooterCommand(self):
        commands2.button.JoystickButton.whileHeld(8, Subsystems.RunShooter(self))

    def servoCommand(self):
        commands2.button.JoystickButton.whileHeld(7, Subsystems.DisengageServo(self))
        commands2.button.JoystickButton.whenReleased(7, Subsystems.EngageServo(self))

    def climbUpCommand(self):
        commands2.button.JoystickButton.whileHeld(10, Subsystems.ClimbUp(self))

    def climbDownCommand(self):
        commands2.button.JoystickButton.whileHeld(9, Subsystems.ClimbDown(self))

    def enableLimelight(self):
        commands2.button.JoystickButton.whenPressed(1, limelight.Limelight.visionEnabled(self))

    def disableLimelight(self):
        commands2.button.JoystickButton.whenReleased(1, limelight.Limelight.visionDisabled(self))


class Subsystems:
    def RunIntakeForward(self):
        robot.RobotMain.__init__(self).intake.set(-0.5)

    def RunIntakeReverse(self):
        robot.RobotMain.__init__(self).intake.set(0.5)

    def RunShooter(self):
        robot.RobotMain.__init__(self).topShooter.set(-0.65)
        robot.RobotMain.__init__(self).bottomShooter.set(0.65)

    def DisengageServo(self):
        robot.RobotMain.__init__(self).servo.setAngle(90)

    def EngageServo(self):
        robot.RobotMain.__init__(self).servo.setAngle(0)

    def ClimbUp(self):
        robot.RobotMain.__init__(self).leftClimb.set(0.5)
        robot.RobotMain.__init__(self).rightClimb.set(0.5)

    def ClimbDown(self):
        robot.RobotMain.__init__(self).leftClimb.set(-0.5)
        robot.RobotMain.__init__(self).rightClimb.set(-0.5)
