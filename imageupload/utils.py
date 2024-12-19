from PIL import Image

def extract_center_color(image_path):
    """
    Extracts the hex color from the center pixel(s) of an image.
    Efficiently handles large images by only processing necessary pixels.
    """
    with Image.open(image_path) as img:
        width, height = img.size

        center_x = width // 2
        center_y = height // 2

        if width % 2 == 1 and height % 2 == 1:
            pixel = img.getpixel((center_x, center_y))
            pixels = [pixel]
        else:
            pixels = [
                img.getpixel((center_x - 1, center_y - 1)),
                img.getpixel((center_x, center_y - 1)),
                img.getpixel((center_x - 1, center_y)),
                img.getpixel((center_x, center_y)),
            ]

        pixels = [pixel[:3] if len(pixel) > 3 else pixel for pixel in pixels]

        avg_color = tuple(sum(channel) // len(pixels) for channel in zip(*pixels))

        return '#{:02x}{:02x}{:02x}'.format(*avg_color)
