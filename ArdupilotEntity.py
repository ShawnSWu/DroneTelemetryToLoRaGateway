from dronekit import connect
import json

class ArdupilotEntity:
    def __init__(self, ip, baud, heartbeat_timeout):
        self.ip = ip
        self.baud = baud
        self.heartbeat_timeout = heartbeat_timeout
        print(">>>> Connecting with the UAV <<<")
        self.vehicle = connect(ip, baud=baud, heartbeat_timeout=heartbeat_timeout, wait_ready=True)

    def get_drone_data(self):
        gps = self.vehicle.location.global_relative_frame

        attitude_3axis = self.vehicle.attitude

        velocity = self.vehicle.velocity

        fly_mode = self.vehicle.mode.name

        ned = self.vehicle.location.local_frame

        drone_data_first_part = {
                'lat': gps.lat,
                'lon': gps.lon,
                'alt': gps.alt
        }

        drone_data_second_part = {
                'p': attitude_3axis.pitch,
                'y': attitude_3axis.yaw,
                'r': attitude_3axis.roll,
        }

        drone_data_third_part = {
            'm': fly_mode,
            'v': {
                'x': velocity[0],
                'y': velocity[1],
                'z': velocity[2]
            }
        }

        drone_data_fourth_part = {
                'n': ned.north,
                'e': ned.east,
                'd': ned.down
        }



        drone_data = {
            'position': {
                'lat': gps.lat,
                'lon': gps.lon,
                'alt': gps.alt
            },
            'attitude': {
                'pitch': attitude_3axis.pitch,
                'yaw': attitude_3axis.yaw,
                'roll': attitude_3axis.roll,
            },
            'velocity': {
                'vx': velocity[0],
                'vy': velocity[1],
                'vz': velocity[2]
            },
            'ned': {
                'north': ned.north,
                'east': ned.east,
                'down': ned.down
            }
        }

        print("-----------------------------------------")
        print(drone_data_first_part)
        print(drone_data_second_part)
        print(drone_data_third_part)
        print(drone_data_fourth_part)
        print("-----------------------------------------")

        return json.dumps(drone_data)
