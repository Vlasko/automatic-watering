# Standard Library Imports
from time import sleep

# Third Party Imports
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Local Application Imports
from functions.writing_functions import make_dir, write_data

make_dir('files')

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

def read_sensor(sensor, name):
    print(name, sensor.voltage)
    # output signal 0-4.2 V
    # 0 ~300    : dry soil :      0~1.33 V
    # 300~700   : humid soil :    1.33~3.09 V
    # 700~950   : in water :      3.09~4.20 V

def write_sensor(sensor, name):
    write_data(name, sensor.voltage, sensor.value)
    
def action():
    # create an analog input channel on pin 0
    moistureSensor = AnalogIn(mcp, MCP.P0)
    read_sensor(moistureSensor,'moisture')
    write_sensor(moistureSensor,'moisture')
    # create an analog input channel on pin 1
    liquidlevelSensor = AnalogIn(mcp, MCP.P1)
    read_sensor(liquidlevelSensor,'liquidlevel')
    write_sensor(liquidlevelSensor,'liquidlevel')

while(1):
    action()
    sleep(1800)
