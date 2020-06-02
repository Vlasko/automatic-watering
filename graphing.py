# Standard Library Imports
import os

# Third Party Imports
import matplotlib.pyplot as plt
import pandas as pd

# Local Application Imports

path = '/Users/gianluca/Documents/Projects/automatic-watering/files/moisture/'

def importData(path):
    data = pd.DataFrame()
    for file in os.listdir(path):
        df = pd.read_csv(path+file,
                    index_col='Timestamp', parse_dates=True)
        data = data.append(df)

    return data.sort_index()

data = importData(path)

log_data = open('/Users/gianluca/Documents/Projects/automatic-watering/log_files/watering_cron.log', 'r')

water_marks=[]
for line in log_data:
    columns = line.split(' at ')
    water_marks.append(columns[1][:16])

crop= data['2020-04-28 09:10':]

plt.plot(crop.index, crop.iloc[:,0])
plt.hlines(1.33, crop.index[0], crop.index[-1], label='dry/humid')
plt.hlines(1.90, crop.index[0], crop.index[-1], label='watering line', colors='g')
plt.hlines(3.09, crop.index[0], crop.index[-1], label='humid/wet')
for mark in water_marks:
    plt.vlines(pd.Timestamp(mark, tz='UTC'), 1.33, 3.09)
plt.show()

# output signal 0-4.2 V
# 0 ~300    : dry soil :      0~1.33 V
# 300~700   : humid soil :    1.33~3.09 V
# 700~950   : in water :      3.09~4.20 V
