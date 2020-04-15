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


for i in range(0,30):
    airSensor = AnalogIn(mcp, MCP.P3)
    print(airSensor.value)
    sleep(1)

for i in range(0,30):
    iLED = AnalogIn(mcp, MCP.P2)
    print(iLED.value)
    sleep(1)
