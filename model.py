import numpy as np
import tensorflow as tf
import keras.backend as K

from keras.utils.data_utils import get_file
from keras.models import load_model

config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
K.set_session(session)


TF_MODEL_PATH = 'https://github.com/tboquet/deep-learning-models/releases/download/v0.1alpha/dcgan_generator_128_128.h5'


def get_dcgan_generator():
    model_path = get_file(
        'dcgan_model_tf_dim_ordering_tf_kernels.h5',
        TF_MODEL_PATH,
        cache_subdir='models')
    return load_model(model_path)


class Model(object):
    def __init__(self):
        self.generator = get_dcgan_generator()
        self.input_shape = self.generator.input_shape
        self.output_shape = self.generator.output_shape

    def generate(self, size=32, text=None):
        z = np.random.uniform(-1, 1, (size, ) + self.input_shape[1:])
        return self.generator.predict(z)
