from dronekit import connect, Vehicle
from  my_vehicle import MyVehicle  #Our custom vehicle class
import math

class ArdupilotEntity:
    def __init__(self, ip, baud, heartbeat_timeout):
        self.ip = ip
        self.baud = baud
        self.heartbeat_timeout = heartbeat_timeout
        print(">>>> Connecting with the UAV <<<")
        self.vehicle = connect(ip, baud=baud, heartbeat_timeout=heartbeat_timeout, wait_ready=True, vehicle_class=MyVehicle)

    def get_drone_data(self):
        gps = self.vehicle.location.global_relative_frame

        lat_hex = gps_convertor(gps.lat)
        lon_hex = gps_convertor(gps.lon)
        alt_hex = gps_convertor(gps.lat)

        gps_hex_str = (lat_hex + lon_hex + alt_hex)
        print(gps_hex_str)

        xgyro = self.vehicle.raw_imu.xgyro
        ygyro = self.vehicle.raw_imu.ygyro
        zgyro = self.vehicle.raw_imu.zgyro


        xacc = self.vehicle.raw_imu.xacc
        yacc = self.vehicle.raw_imu.yacc
        zacc = self.vehicle.raw_imu.zacc

        velocity = self.vehicle.velocity

        fly_mode = self.vehicle.mode.name

        ned = self.vehicle.location.local_frame

        # return [coordinate, attitude, velocity, ned_coordinate]





def gps_convertor(coordinate):
    split_decimal = math.modf( float( '%.4f' % (coordinate) ) )
    decimal = str( split_decimal[0] ).replace( '0.', '' )
    interger = str( split_decimal[1] ).replace( '.0', '' )
    int_value = int( interger + decimal )
    str_hex_data = str( hex( int_value ) ).replace( '0x', '' )
    return str_hex_data.zfill(6)