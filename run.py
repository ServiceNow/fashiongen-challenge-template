import imageio
import numpy as np
import pandas as pd

from model import Model


INPUT_PATH = '/data/dummy_input.csv'


def main():
    data = pd.read_csv(INPUT_PATH)
    text = data['description']
    generator = Model()
    generated_images = generator.generate(32, text)
    generated_images = np.floor(((generated_images / 2.) + 0.5) * 255).astype(np.uint8)
    for i in range(len(generated_images)):
        imageio.imwrite('/results/{}.jpg'.format(i), generated_images[i, :, :, :])


if __name__ == '__main__':
    main()
