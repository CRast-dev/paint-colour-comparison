def get_original_pixel(image, coordinates, display_width):
    original_width, original_height = image.size
    display_height = int(original_height * display_width / original_width)

    x = int(coordinates["x"] * original_width / display_width)
    y = int(coordinates["y"] * original_height / display_height)
    return image.getpixel((x, y))