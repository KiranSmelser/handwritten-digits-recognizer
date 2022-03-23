"""This program converts the raw data of an image file to a list of bytes.
"""

from PIL import Image

def image_to_byte():
    img_name = input("Please enter file name: ").strip()
    img = Image.open(img_name)
    raw_data = list(img.getdata())
    # Format image data.
    formatted_data = []
    for i in range(len(raw_data)):
        formatted_data.append(255 - raw_data[i][0])
    return formatted_data