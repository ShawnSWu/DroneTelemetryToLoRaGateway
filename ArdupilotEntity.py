from dronekit import connect
from  my_vehicle import MyVehicle
from cayennelpp import CayenneLPP
import binascii

class ArdupilotEntity:
    def __init__(self, ip, baud, heartbeat_timeout):
        self.ip = ip
        self.baud = baud
        self.heartbeat_timeout = heartbeat_timeout
        print(">>>> Connecting with the UAV <<<")
        self.vehicle = connect(ip, baud=baud, heartbeat_timeout=heartbeat_timeout, wait_ready=True, vehicle_class=MyVehicle)

    def get_drone_data(self):
        payload = CayenneLPP()
        gps = self.vehicle.location.global_relative_frame
        imu = self.vehicle.raw_imu
        ned = self.vehicle.location.local_frame
        payload.addGPS(1, gps.lat, gps.lon, gps.alt)
        payload.addGyrometer(3, imu.xgyro, imu.ygyro, imu.zgyro)
        payload.addAccelerometer(6, imu.xacc, imu.yacc, imu.zacc)

        print("------------")
        print(gps)
        print(ned)

        cayenne_format_payload = binascii.hexlify(payload.getBuffer()).decode('utf8')
        return cayenne_format_payload