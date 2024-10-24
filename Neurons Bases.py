import os

from click.core import batch
from keras.layers import Activation
from keras.saving.saving_utils import model_call_inputs

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras .datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28*28).astype("float32") /255.0
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0

model = keras.Sequential(
    [
       layers.Dense(1024,activation='relu'),
        layers.Dense(512,activation='relu'),
        layers.Dense(256,activation='relu'),
        layers.Dense(128,activation='relu'),
        layers.Dense(64,activation='relu'),
        layers.Dense(10),
    ]
)

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=["accuracy"],
)

model.fit(x_train, y_train, batch_size=32, epochs=7, verbose=2)
model.evaluate(x_test, y_test, batch_size=32, verbose=2)










