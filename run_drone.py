from ArdupilotEntity import ArdupilotEntity
from EKS76S import EKS76S
from time import sleep

pixhawk = ArdupilotEntity("/dev/ttyAMA0", 57600, 30)
drone_data = pixhawk.get_drone_data()
print(drone_data)


lora_board = EKS76S('/dev/ttyUSB0', 115200, 5)

if lora_board.join_abp() is False:
    lora_board.join_abp()


while True:
    # result = lora_board.send_data_to_gateway("Test data")
    # print(result)

    print(pixhawk.get_drone_data())
    sleep(4)

