from ArdupilotEntity import ArdupilotEntity
from EKS76S import EKS76S
from time import sleep


pixhawk = ArdupilotEntity("/dev/ttyAMA0", 57600, 30)

lora_board = EKS76S('/dev/ttyUSB0', 115200, 5)

pixhawk.get_drone_data()

# while True:
#     print("<---------------Waiting Drone take off--------------->")
#     while pixhawk.vehicle.armed:
#         if lora_board.join_abp() is False:
#             lora_board.join_abp()
#         result = lora_board.send_data_to_gateway(pixhawk.get_drone_data())
#         print("-------->")
#         print(result)
#         sleep(3)
#
#     sleep(3)

