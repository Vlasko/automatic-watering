# Standard Library Imports

# Third Party Imports
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Local Application Imports
from functions.writing_functions import write_data

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
moistureSensor = AnalogIn(mcp, MCP.P0)
# output signal 0-4.2 V
# 0 ~300    : dry soil :      0~1.33 V
# 300~700   : humid soil :    1.33~3.09 V
# 700~950   : in water :      3.09~4.20 V
write_data('moisture', moistureSensor.voltage, moistureSensor.value)

# create an analog input channel on pin 1
liquidlevelSensor = AnalogIn(mcp, MCP.P1)
write_data('liquidlevel', liquidlevelSensor.voltage, liquidlevelSensor.value)

write_data('liquidlevel',1,2)
