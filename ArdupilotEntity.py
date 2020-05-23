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
        attitude = self.vehicle.attitude

        payload.addGPS(1, gps.lat, gps.lon, gps.alt)
        payload.addGyrometer(3, imu.xgyro, imu.ygyro, imu.zgyro)
        payload.addAccelerometer(6, imu.xacc, imu.yacc, imu.zacc)
        # payload.addAttitude(9, attitude.pitch, attitude.yaw, attitude.roll)

        print("------------")
        print(gps)
        print(ned)
        print(imu)
        print(attitude)
        print("------------")

        if ned.north and ned.north and ned.down is None:
            payload.addNED( 8, 0.0, 0.0, 0.0 )
        else:
            payload.addNED( 8, ned.north, ned.east, ned.down )



        cayenne_format_payload = binascii.hexlify(payload.getBuffer()).decode('utf8')
        print(cayenne_format_payload)
        return cayenne_format_payload