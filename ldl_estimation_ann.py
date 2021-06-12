#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:09:52 2020

@author: hikmetcancubukcu
"""


#1. libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. data preprocessing


#2.1. data import


veriler_400_altı_train = pd.read_csv(r'/Users/hikmetcancubukcu/Desktop/ldl formül çalışması/test_train_data/train_400u.csv')
veriler_400_altı_test = pd.read_csv(r'/Users/hikmetcancubukcu/Desktop/ldl formül çalışması/test_train_data/test_400u.csv')



x_train = veriler_400_altı_train.iloc[:,:3].values
y_train = veriler_400_altı_train.iloc[:,3].values

x_test = veriler_400_altı_test.iloc[:,:3].values
y_test = veriler_400_altı_test.iloc[:,3].values



"""data standardization"""
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)


"""ANN"""

import keras
from keras.models import Sequential
from keras.layers import Dense


model = Sequential()
#input layer
model.add(Dense(3,  kernel_initializer="normal", activation= "relu", input_dim= 3))

#hidden layers
model.add(Dense(10,  kernel_initializer="normal", activation= "relu"))
model.add(Dense(5,  kernel_initializer="normal", activation= "relu"))

#output layer
model.add(Dense(1,  kernel_initializer="normal", activation= "linear"))


model.compile(optimizer="RMSprop", loss= "mean_squared_error", metrics=["acc","mae","mse"])
hist= model.fit(X_train, y_train,
          batch_size=200, epochs=100,
          validation_data=(X_test, y_test))

model.evaluate(X_test, y_test)[1]

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()


plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('ACC')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()


