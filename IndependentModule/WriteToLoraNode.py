import serial
from time import sleep

COM_PORT = '/dev/ttyUSB0'
BAUD_RATES = 115200
ser = serial.Serial(
        port=COM_PORT,
        baudrate=BAUD_RATES,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5
)

sleep(7)

ser.write('mac join abp'.encode(encoding="utf-8"))

x=ser.read(100)
print(x)
sleep(2)

ser.flush()

ser.write('mac tx ucnf 2 123322'.encode(encoding="utf-8"))
y=ser.read(100)

print(y)

ser.flush()
