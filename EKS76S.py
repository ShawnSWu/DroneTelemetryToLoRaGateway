from time import sleep
import serial, binascii


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
        sleep( 5 )

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
        result_byte = self.serial.read( 100 )
        result = bytes.decode( result_byte )
        result.replace( '\n', '' )
        result.replace( '\r', '' )
        result.replace( '>>', '' )
        return result.strip()

    def send_bundle_data_to_gateway(self, array):
        for i in range( array ):
            hex_data = binascii.b2a_hex( array[i].encode( 'utf-8' ) )
            hex_data_string = bytes.decode( hex_data )
            packget = 'mac tx ucnf 2 %s' % hex_data_string
            print(packget)
            self.serial.write( packget.encode( encoding="utf-8" ) )
            self.serial.flush()
            result_byte = self.serial.read( 100 )
            result = bytes.decode( result_byte )
            result.replace( '\n', '' )
            result.replace( '\r', '' )
            result.replace( '>>', '' )
            print(result.strip())

    def is_joined(self):
        self.serial.write( 'mac get_join_status'.encode( encoding="utf-8" ) )
        self.serial.flush()
        result_byte = self.serial.read( 100 )
        result = bytes.decode( result_byte )
        result.replace( '\n', '' )
        result.replace( '\r', '' )
        result.replace( '>>', '' )
        return result.strip()
