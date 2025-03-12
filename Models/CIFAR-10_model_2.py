# -*- coding: utf-8 -*-
"""model 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1es2BFgOnojfEoVVRkKuIUgdExDzFIWgu
"""

# Achieves about 72% accuracy in 179 seconds using the t4 in colab

#install keras in colab
#!pip install tensorflow.keras

#Imports for the model
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

import time

#Create datasets after downloading CIFAR-10
cifar = tf.keras.datasets.cifar10
(train_images, train_labels), (test_images, test_labels) = cifar.load_data()
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

#32 x 32 x 3 since cifar is 32 x 32 rgb images
train_images = train_images.reshape((train_images.shape[0],32, 32, 3))
test_images = test_images.reshape((test_images.shape[0], 32, 32, 3))

model = models.Sequential([
    #use relu activation input is 32 x 32 x 3, since cifar is 32 x 32 rgb image
    layers.Conv2D(filters=16, kernel_size=(2, 2), activation = 'relu', padding = 'same', input_shape = (32, 32, 3)),

    layers.MaxPooling2D(2,2),

    layers.Conv2D(filters=32, kernel_size=(2, 2), activation = 'relu', padding = 'same'),

    layers.AveragePooling2D(2,2),

    layers.Conv2D(filters=64, kernel_size=(2, 2), activation = 'relu', padding = 'same'),

    layers.AveragePooling2D(2,2),

    layers.Conv2D(filters=128, kernel_size=(2, 2), activation = 'relu', padding = 'same'),

    layers.AveragePooling2D(2,2),

    layers.Conv2D(filters=256, kernel_size=(2, 2), activation = 'relu', padding = 'same'),

    layers.AveragePooling2D(2,2),

    layers.Flatten(),

    layers.Dense(units = 256, activation = 'sigmoid'),
    layers.Dense(units = 1024, activation = 'sigmoid'),
    layers.Dense(units=10, activation='softmax')
])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

#start training
start = time.time()
history = model.fit(train_images, train_labels,
                    epochs = 40,
                    batch_size=64,
                    validation_split = 0.1)

#print results
end = time.time()
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\nTest accuracy: {test_acc:.4f}')
print('training training took '+str(end - start)+' seconds')