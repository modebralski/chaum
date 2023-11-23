from PIL import Image


def main():
    create_white_chunk()
    create_black_chunk()


def create_white_chunk():
    white_chunk = Image.new('RGBA', (2, 2), (255, 255, 255, 255))
    white_chunk.save('0.png')
    white_chunk.show()


def create_black_chunk():
    black_chunk = Image.new('RGBA', (2, 2), (0, 0, 0, 255))
    black_chunk.save('1.png')
    black_chunk.show()


if __name__ == "__main__":
    main()
