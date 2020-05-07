# Standard Library Imports
from datetime import datetime
# Third Party Imports

# Local Application Imports
from functions.relay_control import switch
from functions.writing_functions import read_sensor

if read_sensor > 1.90:
    switch(3,14)
    print('Plant watered at',datetime.now())
else:
    pass
