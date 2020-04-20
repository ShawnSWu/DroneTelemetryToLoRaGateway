from dronekit import connect
import json

print(">>>> Connecting with the UAV <<<")
vehicle = connect("/dev/ttyAMA0", baud=57600, heartbeat_timeout=30, wait_ready=True)

# #-- Read information from the autopilot:
vehicle.wait_ready('autopilot_version')
print('Autopilot version: %s' % vehicle.version)

gps = vehicle.location.global_relative_frame

attitude_3axis = vehicle.attitude

velocity = vehicle.velocity

fly_mode = vehicle.mode.name

battery = vehicle.battery

ned = vehicle.location.local_frame

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
    'battery': battery.voltage,
    'ned': {
        'north': ned.north,
        'east': ned.east,
        'down': ned.down
    }
}

drone_data_string = json.dumps(drone_data)

print(drone_data_string)