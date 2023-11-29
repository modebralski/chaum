import numpy as np
from PIL import Image
from create_array_from_bitmap import get_array_from_bitmap


def main():
    img_array = get_array_from_bitmap("test.bmp")
    size_x, size_y = img_array.shape
    print(size_x, size_y)
    top_layer_array = create_top_random_layer(size_x, size_y)
    bottom_layer_array = create_bottom_layer(img_array, top_layer_array)
    print(f"Image:\n {img_array}")
    print(f"Top Layer: \n {top_layer_array}")
    print(f"Bottom Layer: \n {bottom_layer_array}")
    img = create_img_from_array(img_array)
    img.save("img.png")
    top_layer = create_img_from_array(top_layer_array)
    top_layer.save("top_layer.png")
    bottom_layer = create_img_from_array(bottom_layer_array)
    bottom_layer.save("bottom_layer.png")
    top_and_bottom = join_top_and_bottom_layers(top_layer, bottom_layer)
    top_and_bottom.save("top_and_bottom.png")


def create_img_from_array(img_array):
    zero_image = Image.open("0.png")
    one_image = Image.open("1.png")
    two_image = Image.open("2.png")
    three_image = Image.open("3.png")
    img_size = img_array.shape[1] * 2, img_array.shape[0] * 2
    img = Image.new("RGBA", img_size, (0, 0, 0, 0))
    for row in range(img_array.shape[0]):
        for column in range(img_array.shape[1]):
            if img_array[row, column] == 0:
                img.paste(zero_image, (column * 2, row * 2))
            elif img_array[row, column] == 1:
                img.paste(one_image, (column * 2, row * 2))
            elif img_array[row, column] == 2:
                img.paste(two_image, (column * 2, row * 2))
            else:
                img.paste(three_image, (column * 2, row * 2))
    return img


def join_top_and_bottom_layers(top_layer, bottom_layer):
    img = Image.new("RGBA", top_layer.size, (0, 0, 0, 255))
    img.paste(top_layer, bottom_layer)
    img.show()
    return img


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
