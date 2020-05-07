# Standard Library Imports
from datetime import datetime
# Third Party Imports
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Local Application Imports
from functions.relay_control import switch
from functions.writing_functions import read_sensor

# Setup
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
moistureSensor= AnalogIn(mcp, MCP.P0)

if read_sensor(moistureSensor,'moisture') > 1.90:
    switch(3,14)
    print('Plant watered at',datetime.now())
else:
    print('Plant not watered at',datetime.now())
    pass
