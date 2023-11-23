import numpy as np
from PIL import Image


def main():
    size_x = 10
    size_y = 10
    img_array = create_img_matrix(size_x, size_y)
    top_layer_array = create_top_random_layer(size_x, size_y)
    bottom_layer_array = create_bottom_layer(img_array, top_layer_array)
    print(f"Image:\n {img_array}")
    print(f"Random Sheet: \n {top_layer_array}")
    print(f"Other Sheet: \n {bottom_layer_array}")
    zero_image = Image.open('0.png')
    one_image = Image.open('1.png')
    two_image = Image.open('2.png')
    three_image = Image.open('3.png')
    img_size = img_array.shape[0] * 2, img_array.shape[1] * 2
    img = Image.new('RGBA', img_size, (0, 0, 0, 0))
    for row in range(img_array.shape[0]):
        for column in range(img_array.shape[1]):
            if img_array[row, column] == 0:
                img.paste(zero_image, (column * 2, row * 2))
            else:
                img.paste(one_image, (column * 2, row * 2))
    img.save("img.png")
    img.show()


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
