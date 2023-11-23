import numpy as np
from PIL import Image


def main():
    size_x = 10
    size_y = 10
    img = create_img_matrix(size_x, size_y)
    top_layer = create_top_random_layer(size_x, size_y)
    bottom_layer = create_bottom_layer(img, top_layer)
    print(f"Image:\n {img}")
    print(f"Random Sheet: \n {top_layer}")
    print(f"Other Sheet: \n {bottom_layer}")
    images = [Image.open(f"{i}.bmp") for i in range(4)]
    original_image = Image.new("RGB", (10, 10))
    for row in range(10):
        for col in range(10):
            value = img[row][col]
            color = images[value].getpixel((0, 0))
            original_image.putpixel((col, row), color)
    original_image.save("original.bmp")

    random_image = Image.new("RGB", (10, 10))
    for row in range(10):
        for col in range(10):
            value = top_layer[row][col]
            color = images[value].getpixel((0, 0))
            random_image.putpixel((col, row), color)
    random_image.save("random.bmp")


def create_img_matrix(size_x: int, size_y: int):
    return np.random.randint(2, size=[size_x, size_y])


def create_top_random_layer(size_x: int, size_y: int):
    return np.random.randint(2, high=4, size=[size_x, size_y])


def create_bottom_layer(img_matrix, top_random_layer):
    bottom_layer = np.ones((len(img_matrix), len(img_matrix[0])), dtype=int)
    for i, line in enumerate(img_matrix):
        for j, pixel in enumerate(line):
            if pixel == 1 and top_random_layer[i][j] == 2:
                bottom_layer[i][j] = 2
            elif pixel == 1 and top_random_layer[i][j] == 3:
                bottom_layer[i][j] = 3
            elif pixel == 0 and top_random_layer[i][j] == 3:
                bottom_layer[i][j] = 2
            else:
                bottom_layer[i][j] = 3
    return bottom_layer


if __name__ == "__main__":
    main()
