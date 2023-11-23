import numpy as np
from PIL import Image


def main():
    img = np.random.randint(2, size=[10, 10])
    random_sheet = np.random.randint(2, high=4, size=[10, 10])
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


if __name__ == "__main__":
    main()
