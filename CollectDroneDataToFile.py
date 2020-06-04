from ArdupilotEntity import ArdupilotEntity
from time import sleep
import csv
from datetime import date
from datetime import datetime

pixhawk = ArdupilotEntity("/dev/ttyAMA0", 57600, 30)

today = str(date.today())
time = str(datetime.now().strftime("%H:%M"))
file_name = today + '-' + time
extension = ".csv"

while True:
    with open( "TrajectoryData/" + file_name + extension, "w+" ) as file:
        while True:
            writer = csv.writer( file )
            row_data = pixhawk.get_row_data()
            writer.writerow( row_data )
            print(row_data)
            sleep( 2 )

