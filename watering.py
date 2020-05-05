# Standard Library Imports
from datetime import datetime
# Third Party Imports

# Local Application Imports
from functions.relay_control import switch

switch(3,14)

print('Plant watered at',datetime.now())
