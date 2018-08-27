import sys
from PIL import Image


def int_to_bin(numero):
    return bin(numero)[2:].zfill(8)


def modify_color(color, bit):
    color_bin = int_to_bin(color)
    color_modify = color_bin[:-1] + str(bit)
    return int(color_modify, 2)


def str_to_bits(message):
    bits = []
    for letter in message:
        letter_bin = int_to_bin(ord(letter))
        for bit in letter_bin:
            bits.append(bit)

    return bits


def insert_message_in_image(message_in_bits, pixel, count=0):
    length = len(message_in_bits)
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    if count < length:
        red_modify = modify_color(red, message_in_bits[count])
        count += 1
    else:
        red_modify = red

    if count < length:
        green_modify = modify_color(green, message_in_bits[count])
        count += 1
    else:
        green_modify = green

    if count < length:
        blue_modify = modify_color(blue, message_in_bits[count])
        count += 1
    else:
        blue_modify = blue

    pixel = (red_modify, green_modify, blue_modify)
    return count, pixel


def hide_text(message, path_image):
    image = Image.open(path_image)
    pixels = image.load()

    size = image.size
    width = size[0]
    height = size[1]

    message_in_bits = str_to_bits(message)
    count = 0
    for x in range(width):
        for y in range(height):
            count, pixels[x, y] = insert_message_in_image(message_in_bits, pixels[x, y], count)
        else:
            continue

    print("Mensagem Escrita")
    image.save("mario_copy.bmp")


if __name__ == "__main__":
    message = sys.argv[1]
    hide_text(message, "mario.bmp")
