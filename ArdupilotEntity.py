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

        coordinate = {
                'lat': gps.lat,
                'lon': gps.lon,
                'alt': gps.alt
        }

        attitude = {
                'p': attitude_3axis.pitch,
                'y': attitude_3axis.yaw,
                'r': attitude_3axis.roll,
        }

        velocity = {
            'm': fly_mode,
            'v': {
                'x': velocity[0],
                'y': velocity[1],
                'z': velocity[2]
            }
        }

        ned_coordinate = {
                'n': ned.north,
                'e': ned.east,
                'd': ned.down
        }

        return json.dumps([coordinate ,attitude, velocity, ned_coordinate])
