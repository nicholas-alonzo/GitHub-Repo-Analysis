import numpy as np
import pandas as pd
from pylab import rcParams
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
sns.set(style="white")

df=pd.read_csv("events.csv")
labels=df['type']
sizes=df['counts']
explode = np.zeros(len(sizes))
explode[2]=0.1
explode[13]=0.1
plt.figure(figsize=(8,8))
patches, texts =plt.pie(sizes,explode=explode,startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.title("Github Events Distribution 2011-2016")
plt.tight_layout()
plt.show()


df2=pd.read_csv("events_day.csv")
df2=df2.pivot(index='times', columns='type', values='counts')
df2 = df2.drop('PushEvent', 1)
df2.plot(figsize=(20,9))
plt.title("Time Series All Events 2011-2016")
plt.show()

corr = df2.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap,square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.title("Events correlations of 2011-2016")


rcParams['figure.figsize'] = 11, 9
df2['WatchEvent'].index=pd.DatetimeIndex(freq='w',start=0,periods=2149)
decomposition = sm.tsa.seasonal_decompose(df2['WatchEvent'])
fig = decomposition.plot()
plt.show()
