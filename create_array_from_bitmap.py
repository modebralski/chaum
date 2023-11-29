import numpy as np
from PIL import Image


def main():
    bmp_image = Image.open("test.bmp")
    image_array = np.array(bmp_image)
    binary_array = (image_array != 0).astype(int)
    print(binary_array)


if __name__ == "__main__":
    main()
