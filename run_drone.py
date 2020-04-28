from ArdupilotEntity import ArdupilotEntity
from EKS76S import EKS76S
from time import sleep
import pigpio


# pixhawk = ArdupilotEntity("/dev/ttyAMA0", 57600, 30)
# drone_data = pixhawk.get_drone_data()
# print(drone_data)


another_tx = 36
pi = pigpio.pi()
pi.set_mode(another_tx, pigpio.OUTPUT)


lora_board = EKS76S("/dev/ttyAMA1", 57600, 10)

if lora_board.join_abp() is False:
    lora_board.join_abp()

result = lora_board.send_data_to_gateway("123456")

# print("Drone status")
# print(pixhawk.vehicle.is_armable)
# while True:
#     result = lora_board.send_data_to_gateway(pixhawk.get_drone_data())
#     print("-------->")
#     print(result)
#     sleep(3)

