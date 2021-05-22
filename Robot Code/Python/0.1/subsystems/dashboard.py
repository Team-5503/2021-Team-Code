from networktables import NetworkTables

NetworkTables.initialize(server='roborio-5503-frc.local')

db = NetworkTables.getTable("SmartDashboard")

db.getNumber("tx")
db.getNumber("ty")
db.getNumber("ta")
db.getNumber("ts")