import imageio
import pandas as pd

from model import Model


INPUT_PATH = '/data/dummy_input.csv'


def main():
    data = pd.read_csv(INPUT_PATH)
    text = data['description']
    model = Model()
    generated_images = model.generate(text)
    for i in range(len(generated_images)):
        imageio.imwrite('/results/{}.jpg'.format(i), generated_images[i, :, :, :])


if __name__ == '__main__':
    main()
