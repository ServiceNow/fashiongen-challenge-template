import numpy as np


class Model:
    """Dummy model"""
    def generate(self, inputs):
        shape = (32, 128, 128, 3)
        return np.random.uniform(size=np.prod(shape)).reshape(shape)
