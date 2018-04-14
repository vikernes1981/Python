import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL') # data from google

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]] # Names of columns we want to use
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0  # Percent of columns
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0 # More percent

df= df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close' # we can change this if we want
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01 * len(df))) # if we change 0.01 to 0.1 we get a lot higher values

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

x = preprocessing.scale(x)

#x = x[:-forecast_out+1]
#df.dropna(inplace=True)
y = np.array(df['label'])

x_train, x_test, y_train,y_test = cross_validation.train_test_split(x, y, test_size=0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)

print(accuracy)
#print(len(x), len(y))
#print(df.tail())
#print(df.head())
