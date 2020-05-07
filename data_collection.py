# Standard Library Imports
from datetime import datetime

# Third Party Imports
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Local Application Imports
from functions.writing_functions import read_sensor, write_sensor

# Setup

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

def action():
    # create an analog input channel on pin 0
    moistureSensor= AnalogIn(mcp, MCP.P0)
    read_sensor(moistureSensor,'moisture')
    write_sensor(moistureSensor,'moisture')
    # create an analog input channel on pin 1
    liquidlevelSensor = AnalogIn(mcp, MCP.P1)
    read_sensor(liquidlevelSensor,'liquidlevel')
    write_sensor(liquidlevelSensor,'liquidlevel')

<<<<<<< HEAD
    action()
    print('Data collected at'+str(datetime.now()))
=======
if read_sensor > 1.90:
    action()
    print('Data collected at'+str(datetime.now()))
else:
    pass
>>>>>>> 27af9f5059db53992c8ceb9b06b4272138c4883d
