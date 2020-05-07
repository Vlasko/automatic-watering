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

crop= data['2020-04-28 09:10':]

plt.plot(crop.index, crop.iloc[:,0])
plt.hlines(1.33, crop.index[0], crop.index[-1], label='dry/humid')
plt.hlines(3.09, crop.index[0], crop.index[-1], label='humid/wet')
plt.vlines(pd.Timestamp('2020-04-30T12:45', tz='UTC'), 1.33, 3.09)
plt.vlines(pd.Timestamp('2020-05-01T12:45', tz='UTC'), 1.33, 3.09)
plt.vlines(pd.Timestamp('2020-05-02T12:45', tz='UTC'), 1.33, 3.09)
plt.vlines(pd.Timestamp('2020-05-03T12:45', tz='UTC'), 1.33, 3.09)
plt.vlines(pd.Timestamp('2020-05-04T12:45', tz='UTC'), 1.33, 3.09)
plt.vlines(pd.Timestamp('2020-05-05T12:45', tz='UTC'), 1.33, 3.09)
plt.vlines(pd.Timestamp('2020-05-06T12:45', tz='UTC'), 1.33, 3.09)
plt.show()

# output signal 0-4.2 V
# 0 ~300    : dry soil :      0~1.33 V
# 300~700   : humid soil :    1.33~3.09 V
# 700~950   : in water :      3.09~4.20 V
