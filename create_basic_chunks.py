from PIL import Image


def main():
    create_white_chunk()


def create_white_chunk():
    image_0 = Image.new('RGBA', (2, 2), (255, 255, 255, 255))
    image_0.save('0.png')
    image_0.show()


if __name__ == "__main__":
    main()