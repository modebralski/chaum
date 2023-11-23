import numpy as np
from PIL import Image


def main():
    size_x = 10
    size_y = 10
    img = create_img_matrix(size_x, size_y)
    random_sheet = create_top_random_layer(size_x, size_y)
    other_sheet = np.ones((10, 10), dtype=int)
    print(f"Image:\n {img}")
    print(f"Random Sheet: \n {random_sheet}")
    for i, line in enumerate(img):
        for j, pixel in enumerate(line):
            if pixel == 1 and random_sheet[i][j] == 2:
                other_sheet[i][j] = 3
            elif pixel == 1 and random_sheet[i][j] == 3:
                other_sheet[i][j] = 2
            elif pixel == 0 and random_sheet[i][j] == 3:
                other_sheet[i][j] = 3
            else:
                other_sheet[i][j] = 2
    print(f"Other Sheet: \n {other_sheet}")
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
            value = random_sheet[row][col]
            color = images[value].getpixel((0, 0))
            random_image.putpixel((col, row), color)
    random_image.save("random.bmp")


def create_img_matrix(size_x: int, size_y: int):
    return np.random.randint(2, size=[size_x, size_y])


def create_top_random_layer(size_x: int, size_y: int):
    return np.random.randint(2, high=4, size=[size_x, size_y])


if __name__ == "__main__":
    main()
