"""_summary_
"""

from PIL import Image

def main():
    img = Image.open("five-test.png")
    raw_data = list(img.getdata())
    # Format image data.
    formatted_data = []
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            formatted_data.append(255 - raw_data[i][j])
    print(formatted_data)
main()