import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
sns.color_palette('hls', 8)
graph1 = pd.read_csv('graph1.csv')
graph2 = pd.read_csv('graph2.csv')
graph3 = pd.read_csv('graph3.csv')
# first graph - number of squirrel sighting per park
x = sns.barplot(data=graph1, x='Park_ID', y='Number of Squirrels')
plt.show()
# second graph - squirrels and activities throughout the park
y = sns.scatterplot(data=graph2, x='Park ID', y='Activity', hue='Activities')
plt.legend(bbox_to_anchor=(1.5, 2), loc='upper right', title='Activities')
plt.show()
# third graph - time and temperature
g3 = graph3.plot.hexbin(x='Park ID',
                        y='Temperature',
                        C='Total Time',
                        reduce_C_function=np.sum,
                        gridsize=10,
                        cmap='GnBu')
plt.show()
