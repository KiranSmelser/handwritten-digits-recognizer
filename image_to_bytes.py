"""This program converts the raw data of an image file to a list of bytes.
"""

from PIL import Image

def main():
    img = Image.open("five-test.png")
    raw_data = list(img.getdata())
    print(raw_data)
    # Format image data.
    formatted_data = []
    for i in range(len(raw_data)):
        formatted_data.append(255 - raw_data[i][0])
    print(formatted_data)
main()