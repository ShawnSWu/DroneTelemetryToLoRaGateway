from dronekit import connect
from  my_vehicle import MyVehicle
from cayennelpp import CayenneLPP
import binascii
from datetime import date
from datetime import datetime

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
        attitude = self.vehicle.attitude

        payload.addGPS(1, gps.lat, gps.lon, gps.alt)
        payload.addGyrometer(3, imu.xgyro, imu.ygyro, imu.zgyro)
        payload.addAccelerometer(5, imu.xacc, imu.yacc, imu.zacc)
        payload.addNED( 7, ned.north, ned.east, ned.down )
        payload.addAttitude(9, attitude.pitch, attitude.yaw, attitude.roll)

        print("------------")
        print(gps)
        print(ned)
        print(imu)
        print(attitude)
        print("------------")

        cayenne_format_payload = binascii.hexlify(payload.getBuffer()).decode('utf8')
        print(cayenne_format_payload)
        return cayenne_format_payload

    def get_row_data(self):
        today = str( date.today() )
        time = str( datetime.now().strftime( "%H:%M:%S" ) )
        gps = self.vehicle.location.global_relative_frame
        imu = self.vehicle.raw_imu
        ned = self.vehicle.location.local_frame
        attitude = self.vehicle.attitude
        return [today, time, gps.lat, gps.lon, gps.alt, imu.xgyro, imu.ygyro, imu.zgyro, imu.xacc, imu.yacc,
                imu.zacc, ned.north, ned.east, ned.down, attitude.pitch, attitude.yaw, attitude.roll, 0, 0 ]
