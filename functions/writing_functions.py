# Standard Library Imports
import os
from datetime import datetime

# Third Party Imports

directory = os.getcwd()
#newDir = os.getcwd()+'/files/'

def make_dir(newDir):
    try:
        # Create target Directory
        os.mkdir(os.getcwd()+newDir)
    except FileExistsError:
        pass

def write_data(type, col1, col2):
    make_dir('/files/'+type)
    today = datetime.today().date()

    file_path = directory+'/files/'+type+'/'+str(today)+'_'+type+'.csv'

    f = open(file_path, 'a+')

    if os.stat(file_path).st_size == 0:
        f.write('Timestamp, Moisture (V), Moisture (Raw ADC)\r\n')
    f.write('{0},{1:0.2f}, {2:0.2f}\r\n'.format(
                        datetime.now().strftime('%Y-%m-%dT%H:%M:00Z'),
                        col1, col2))

def read_sensor(sensor, name):
    print(name, sensor.voltage)
    # output signal 0-4.2 V
    # 0 ~300    : dry soil :      0~1.33 V
    # 300~700   : humid soil :    1.33~3.09 V
    # 700~950   : in water :      3.09~4.20 V

def write_sensor(sensor, name):
    write_data(name, sensor.voltage, sensor.value)
