from PIL import Image


def main():
    create_white_chunk()
    create_black_chunk()
    create_semi_black_2_chunk()
    create_semi_black_3_chunk()


def create_white_chunk():
    white_chunk = Image.new('RGBA', (2, 2), (255, 255, 255, 255))
    white_chunk.save('0.png')
    white_chunk.show()


def create_black_chunk():
    black_chunk = Image.new('RGBA', (2, 2), (0, 0, 0, 255))
    black_chunk.save('1.png')
    black_chunk.show()


def create_semi_black_2_chunk():
    semi_black_2_chunk = Image.new('RGBA', (2, 2), (0, 0, 0, 0))
    semi_black_2_chunk.putpixel((0, 1), (0, 0, 0, 255))
    semi_black_2_chunk.putpixel((1, 0), (0, 0, 0, 255))
    semi_black_2_chunk.save('2.png')
    semi_black_2_chunk.show()


def create_semi_black_3_chunk():
    semi_black_3_chunk = Image.new('RGBA', (2, 2), (0, 0, 0, 0))
    semi_black_3_chunk.putpixel((1, 0), (0, 0, 0, 255))
    semi_black_3_chunk.putpixel((0, 1), (0, 0, 0, 255))
    semi_black_3_chunk.save('3.png')
    semi_black_3_chunk.show()


if __name__ == "__main__":
    main()
