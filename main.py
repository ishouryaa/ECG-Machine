# import wfdb
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#%%
df = pd.read_csv('ECG_ANN.csv')

#%%
y = df['100']

# %%
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split

X = df.iloc[:, :99].values


# %%

print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=123)

# %%

from keras.models import Sequential
from keras.layers import Dense


# %%


model = Sequential()
model.add(Dense(128, input_dim=99, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X_train, y_train, epochs=10)

scores = model.evaluate(X_test, y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

df = pd.read_csv('ecg_data.csv')
time_values = df['time'].tolist()
test_ecg = df['voltage'].tolist()
plt.plot(time_values,test_ecg)
plt.show()

ecg_new = test_ecg[0:99]
time_new = time_values[0:99]
plt.plot(time_new, ecg_new)
plt.show()

test_data = np.expand_dims(np.array(ecg_new),axis=0)
print(test_data)
testscores = model.predict(test_data)
print('My heart is behaving:', testscores)

# %%

# test = np.array(X_test[2])
# ynew = model.predict(test.reshape(1,99))
#
# test2 = np.array(X_test[6])
# ynew2 = model.predict(test2.reshape(1,99))
#
#
# y_test_new=np.array(y_test.tolist())
#
# # %%
#
# matplotlib.rcParams.update({'font.size': 20})
# # Graph to plot all peaks and data points together
# fig, ax = plt.subplots()
#
# ax.set(xlabel='Time (Samples)',
#        ylabel='Voltage(mV)',
#        title='ECG'
#        )
#
# ax.plot(X_test[6])
# ax.plot(X_test[2])
#
# plt.show()
#
