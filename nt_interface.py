import sys
import time
from networktables import NetworkTables


NetworkTables.initialize(server="127.0.0.1")
data = NetworkTables.getTable("SmartDashboard")
time.sleep(1)  # Time to connect fully
if data.getNumber("Reef Side", -1) != -1:
    print("CONNECTED: SIMULATOR")
else:
    NetworkTables.initialize(
        server="roborio-8575-frc.local"
    )  # Replace TEAM with your team number
    data = NetworkTables.getTable("SmartDashboard")
    time.sleep(1)  # Time to connect fully
    if data.getNumber("Reef Side", -1) == -1:
        print("IMPORTANT: COULD NOT CONNECT/RETRIVE VALUES")
        import error_window
    else:
        print("CONNECTED: REAL ROBOT")


def getNum(key):

    return data.getNumber(key, 1.0)


def setNum(key, value):
    print(data.putNumber(key, value))
    data.putNumber(key, value)
