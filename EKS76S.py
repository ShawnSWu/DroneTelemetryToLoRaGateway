from time import sleep
import serial, binascii
import json


def convert_to_hex_string(data):
    hex_data = binascii.b2a_hex( json.dumps( data ).encode( 'utf-8' ) )
    return bytes.decode( hex_data )

class EKS76S:
    def __init__(self, com_port, baud_rate, timeout):
        self.com_port = com_port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial = serial.Serial(
            port=self.com_port,
            baudrate=self.baud_rate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=5
        )
        sleep(5)

    def join_abp(self):
        self.serial.write( 'mac join abp'.encode( encoding="utf-8" ) )
        self.serial.flush()
        result_byte = self.serial.read( 100 )
        result = bytes.decode( result_byte )
        result.replace( '\n', '' )
        result.replace( '\r', '' )
        result.replace( '>>', '' )
        return result.strip()

    def send_data_to_gateway(self, data):
        hex_data = binascii.b2a_hex( data.encode( 'utf-8' ) )
        hex_data_string = bytes.decode( hex_data )
        packget = 'mac tx ucnf 2 %s' % hex_data_string
        print(packget)
        self.serial.write( packget.encode( encoding="utf-8" ) )
        self.serial.flush()
        result_byte = self.serial.read( 30 )
        result = bytes.decode( result_byte )
        result.replace( '\n', '' )
        result.replace( '\r', '' )
        result.replace( '>>', '' )
        return result.strip()

    def send_bundle_data_to_gateway(self, array):
        coordinate = binascii.b2a_hex( json.dumps( array[0] ).encode( 'utf-8' ) )
        attitude = binascii.b2a_hex( json.dumps( array[1] ).encode( 'utf-8' ) )
        velocity = binascii.b2a_hex( json.dumps( array[2] ).encode( 'utf-8' ) )
        ned_coordinate = binascii.b2a_hex( json.dumps( array[3] ).encode( 'utf-8' ) )

        send_coordinate_command = 'mac tx ucnf 2 %s' % coordinate
        send_attitude_command = 'mac tx ucnf 2 %s' % attitude
        send_velocity_command = 'mac tx ucnf 2 %s' % velocity
        send_ned_coordinate_command = 'mac tx ucnf 2 %s' % ned_coordinate

        self.serial.write( send_coordinate_command.encode( encoding="utf-8" ) )
        self.serial.write( send_attitude_command.encode( encoding="utf-8" ) )
        self.serial.write( send_velocity_command.encode( encoding="utf-8" ) )
        self.serial.write( send_ned_coordinate_command.encode( encoding="utf-8" ) )

        result_byte = self.serial.read( 100 )
        result = bytes.decode( result_byte )
        result.replace( '\n', '' )
        result.replace( '\r', '' )
        result.replace( '>>', '' )
        print(result.strip())
        self.serial.flush()

    def is_joined(self):
        self.serial.write( 'mac get_join_status'.encode( encoding="utf-8" ) )
        self.serial.flush()
        result_byte = self.serial.read( 30 )
        result = bytes.decode( result_byte )
        result.replace( '\n', '' )
        result.replace( '\r', '' )
        result.replace( '>>', '' )
        return result.strip()



