from dronekit import connect, Vehicle
from  my_vehicle import MyVehicle  #Our custom vehicle class
import math
from cayennelpp import CayenneLPP

class ArdupilotEntity:
    def __init__(self, ip, baud, heartbeat_timeout):
        self.ip = ip
        self.baud = baud
        self.heartbeat_timeout = heartbeat_timeout
        print(">>>> Connecting with the UAV <<<")
        self.vehicle = connect(ip, baud=baud, heartbeat_timeout=heartbeat_timeout, wait_ready=True, vehicle_class=MyVehicle)

    """
    
    payload = 'lon(length=6)'+'la(length=6)t'+'alt(length=6)'+'xgyro(length=4)'+'ygyro(length=4)'+'zgyro(length=4)'+'xacc(length=4)'+'yacc(length=4)'+'zacc(length=4)'
               
    
    
    
       
    """
    def get_drone_data(self):
        payload = CayenneLPP()

        gps = self.vehicle.location.global_relative_frame
        imu = self.vehicle.raw_imu

        payload.addGPS(1, gps.lat, gps.lon, gps.alt)
        payload.addGyrometer(2, imu.xgyro, imu.ygyro, imu.zgyro)
        payload.addAccelerometer(2, imu.xacc, imu.yacc, imu.zacc)

        print("payload")
        print(payload.getBuffer())


        # lon_hex = gps_convertor(gps.lon) #-180 ~ 180
        # lat_hex = gps_convertor(gps.lat) #-90 ~ 90
        # alt_hex = gps_convertor(gps.lat)
        # gps_hex_str = (lat_hex + lon_hex + alt_hex)
        # print("GPS:")
        # print(gps)

        # xgyro = self.vehicle.raw_imu.xgyro # Angular speed around X axis (millirad /sec)
        # ygyro = self.vehicle.raw_imu.ygyro # Angular speed around Y axis (millirad /sec)
        # zgyro = self.vehicle.raw_imu.zgyro # Angular speed around Z axis (millirad /sec)
        # print("xgyro:")
        # print(xgyro)
        # print("ygyro:")
        # print(ygyro)
        # print("zgyro:")
        # print(zgyro)

        xacc = self.vehicle.raw_imu.xacc  # x acceleration (mg)
        yacc = self.vehicle.raw_imu.yacc  # y acceleration (mg)
        zacc = self.vehicle.raw_imu.zacc  # z acceleration (mg)

        fly_mode = self.vehicle.mode.name

        ned = self.vehicle.location.local_frame

        return payload.getBuffer()





def gps_convertor(coordinate):
    split_decimal = math.modf( float( '%.4f' % (coordinate) ) )
    decimal = str( split_decimal[0] ).replace( '0.', '' )
    interger = str( split_decimal[1] ).replace( '.0', '' )
    int_value = int( interger + decimal )
    str_hex_data = str( hex( int_value ) ).replace( '0x', '' )
    return str_hex_data.zfill(6)