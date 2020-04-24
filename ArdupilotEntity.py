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

        xgyro = self.vehicle.raw_imu.xgyro
        ygyro = self.vehicle.raw_imu.ygyro
        zgyro = self.vehicle.raw_imu.zgyro
        print('--------')
        print(xgyro)
        print(ygyro)
        print(zgyro)

        velocity = self.vehicle.velocity

        fly_mode = self.vehicle.mode.name

        ned = self.vehicle.location.local_frame




        # coordinate = "{%s,%s,%s}" % (format(gps.lat, '4f'), format(gps.lon, '4f'), format(gps.alt, '4f'))
        #
        # # attitude = "{%s,%s,%s}" % (format(attitude_3axis.pitch, '9f'), format(attitude_3axis.yaw, '9f'), format(attitude_3axis.roll, '9f'))
        #
        # velocity = "{%s,%s,%s,%s}" % (fly_mode, format(velocity[0], '4f'), format(velocity[1], '4f'), format(velocity[2], '4f'))
        #
        # ned_coordinate = "{%s,%s,%s}" % (ned.north, ned.east, ned.down)

        # return [coordinate, attitude, velocity, ned_coordinate]





def gps_convertor(coordinate):
    split_decimal = math.modf( float( '%.4f' % (coordinate) ) )
    decimal = str( split_decimal[0] ).replace( '0.', '' )
    interger = str( split_decimal[1] ).replace( '.0', '' )
    int_value = int( interger + decimal )
    str_hex_data = str( hex( int_value ) ).replace( '0x', '' )
    return str_hex_data.zfill(6)