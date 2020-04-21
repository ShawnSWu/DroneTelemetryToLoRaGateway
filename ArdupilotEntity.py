from dronekit import connect

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

        coordinate = "{%s,%s,%s}" % gps.lat, gps.lon, gps.alt

        attitude = "{%s,%s,%s}" % attitude_3axis.pitch, attitude_3axis.yaw, attitude_3axis.roll

        velocity = "{%s,%s,%s,%s}" % fly_mode, velocity[0], velocity[1], velocity[2]

        ned_coordinate = "{%s,%s,%s}" % ned.north, ned.east, ned.down

        return [coordinate, attitude, velocity, ned_coordinate]
