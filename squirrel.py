import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
sns.color_palette('hls', 8)
sq = pd.read_csv('squirrel-data.csv')
pk = pd.read_csv('park-data.csv', 'rb', encoding_errors='ignore')
graph1 = pd.read_csv('graph1.csv')
graph2 = pd.read_csv('graph2.csv')

# first graph - number of squirrel sighting per park + their activities
sns.barplot(data=graph1, x='Park_ID', y='Number of Squirrels')
plt.show()
sns.kdeplot(data=graph2, x='Park ID', hue='Activities',
            multiple='stack', palette='hls')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper right', title='Activities')
plt.show()
