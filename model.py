import numpy as np
import tensorflow as tf
import keras.backend as K

from keras.models import load_model

config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
K.set_session(session)


TF_MODEL_PATH = '/temp_model/dcgan_generator_128_128.h5'


class Model(object):
    def __init__(self):
        self.generator = load_model(TF_MODEL_PATH)
        self.input_shape = self.generator.input_shape
        self.output_shape = self.generator.output_shape

    def generate(self, size=32, text=None):
        z = np.random.uniform(-1, 1, (size, ) + self.input_shape[1:])
        return self.generator.predict(z)
