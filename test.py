from time import sleep
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan1 = AnalogIn(mcp, MCP.P0)

#Output signal 0-4.2 V
# 0 ~300    : dry soil :      0~1.33 V
# 300~700   : humid soil :    1.33~3.09 V
# 700~950   : in water :      3.09~4.20 V

chan2 = AnalogIn(mcp, MCP.P1)

while(1):
    print('Moisture Sensor')
    print('Raw ADC Value: ', chan1.value)
    print('ADC Voltage: ' + str(chan1.voltage) + 'V \n')
    sleep(1)
#    print('Liquid Level')
#    print('Raw ADC Value: ', chan2.value)
#    print('ADC Voltage: ' + str(chan2.voltage) + 'V \n')
#    sleep(1)
