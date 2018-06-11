import numpy as np


class Model:
    """Dummy model"""
    def generate(self, inputs):
<<<<<<< HEAD
        shape = (1000, 128, 128, 3)
        return np.random.uniform(size=np.prod(shape)).reshape(shape)
=======
        shape = (32, 128, 128, 3)
        return np.random.uniform(size=np.prod(shape)).reshape(shape).astype(np.uint8)
>>>>>>> bc48b034620d1cee4887d8982fec8b71018b3f93
