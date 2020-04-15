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

data

plt.plot(data.index, data.iloc[:,0])
plt.hlines(1.33, data.index[0], data.index[-1], label='dry/humid')
plt.hlines(3.09, data.index[0], data.index[-1], label='humid/wet')
plt.show()

# output signal 0-4.2 V
# 0 ~300    : dry soil :      0~1.33 V
# 300~700   : humid soil :    1.33~3.09 V
# 700~950   : in water :      3.09~4.20 V
