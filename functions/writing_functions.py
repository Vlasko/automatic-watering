# Standard Library Imports
import os

# Third Party Imports
from datetime import datetime

directory = os.getcwd()
#newDir = os.getcwd()+'/files/'

def make_dir(newDir):
    try:
        # Create target Directory
        os.mkdir(os.getcwd()+'/files/'+newDir)
    except FileExistsError:
        pass

def write_data(type, col1, col2):
    make_dir(type)
    today = datetime.today().date()

    file_path = directory+'/files/'+type+'/'+str(today)+'_'+type+'.csv'

    f = open(file_path, 'a+')

    if os.stat(file_path).st_size == 0:
        f.write('Timestamp, Moisture (V), Moisture (Raw ADC)\r\n')
    f.write('{0},{1:0.2f}, {2:0.2f}\r\n'.format(
                        datetime.now().strftime('%Y-%m-%dT%H:%M:00Z'),
                        col1, col2))
