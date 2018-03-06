import numpy as np


class Model:
    """Dummy model"""
    def generate(self, inputs):
        return np.random.normal((32, 128, 128, 3))
