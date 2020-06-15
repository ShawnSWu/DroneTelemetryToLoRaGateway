from ArdupilotEntity import ArdupilotEntity
from time import sleep
import csv
from datetime import date
from datetime import datetime
import logging

logging.basicConfig(filename='DroneLog.log', filemode='w', format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.INFO)
pixhawk = ArdupilotEntity("/dev/ttyAMA0", 57600, 30)

logging.info( "===============================================================================" )

while True:
    logging.info("<---------------Waiting Drone take off--------------->")
    print("<---------------Waiting Drone take off--------------->")
    if pixhawk.vehicle.armed:
        today = '{month:02d}{day:02d}{year}'.format( year=date.today().year, month=date.today().month,
                                                     day=date.today().day )
        time = str( datetime.now().strftime( "%H%M%S" ) )
        file_name = today + '_' + time
        extension = ".csv"
        with open( "TrajectoryData/" + file_name + extension, "w+" ) as file:
            writer = csv.writer( file )
            writer.writerow( ['date', 'time', 'lat', 'lon', 'alt', 'x_gyro', 'y_gyro', 'z_gyro', 'x_acc', 'y_acc',
                'z_acc', 'north', 'east', 'down', 'pitch', 'yaw', 'roll', 'wind_speed', 'wind_direction' ] )
            while pixhawk.vehicle.armed:
                row_data = pixhawk.get_row_data()
                writer.writerow( row_data )
                print(row_data)
                logging.info( '{date} {time}, {row_data}'.format( date=today, time=time, row_data=row_data ) )
                logging.info( row_data )
                sleep( 3 )
        file.close()
        time = str( datetime.now().strftime( "%H:%M:%S" ) )
        logging.info( '{date} {time}, New file {file_name} has been created'.format(date=today, time=time, file_name=file_name ) )
        print('New file {file_name} has been created'.format( file_name=file_name ))
    sleep(4)
