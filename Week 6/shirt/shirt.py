import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv)
                 < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_extensions = (".jpg", ".jpeg", ".png")

    input_ext = get_extension(input_file)
    output_ext = get_extension(output_file)

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_file) as image:
            shirt = Image.open("shirt.png")
            new_image = ImageOps.fit(image, shirt.size)
            new_image.paste(shirt, shirt)
            new_image.save(output_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_extension(filename):
    if '.' in filename:
        return '.' + filename.rsplit('.', 1)[-1].lower()
    return ''


if __name__ == "__main__":
    main()
