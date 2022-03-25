"""Creates a canvas to draw the digit on and saves it as .png file.
"""

from tkinter import *
from PIL import ImageGrab
from PIL import Image

def resize():
    """Resizes the image to be 28x28 pixels.
    """
    image = Image.open("num-test.png")
    image = image.crop((136, 136, 164, 164))
    image.save("num-test.png", "png")

def save(event):
    """Saves and resizes the contents of the canvas as a .png image file.
    Arguments:
        event: Cotntrol + s are presssed simultaneously.
    """
    x2=win.winfo_rootx()+canvas.winfo_x()
    y2=win.winfo_rooty()+canvas.winfo_y()
    x1=x2+canvas.winfo_width()
    y1=y2+canvas.winfo_height()
    print("Saving Digit...")
    print()
    # Saves and resizes the image.
    ImageGrab.grab().crop((x2,y2,x1,y1)).save("num-test.png")
    resize()
    win.destroy()

def start_position(event):
    """Determines the start position of the line.
    Arguments:
        event: Left mouse button is clicked.
    """
    global start_x, start_y
    start_x, start_y = event.x, event.y

def draw_line(event):
    """Draws a line between two points on the canvas.
    Arguments:
        event: mouse is left clicked and dragged.
    """
    global start_x, start_y
    # Draws the line.
    canvas.create_line((start_x, start_y, event.x, event.y), 
                      fill='black', 
                      width=1)
    start_x, start_y = event.x, event.y

def draw_with_mouse():
    global canvas
    global win
    win = Tk()
    win.geometry("300x300")
    canvas = Canvas(win, width=300, height=300, background='white')
    canvas.pack(anchor='nw', fill='both', expand=1)
    canvas.create_rectangle(135, 135, 165, 165, outline='black')
    canvas.create_text(150, 100, text="DRAW DIGIT INSIDE BOX",fill="black",font=('Helvetica 15 bold'))
    # Controls for canvas.
    win.bind('<ButtonPress-1>', start_position)
    win.bind('<B1-Motion>', draw_line)
    win.bind('<Control-s>', save)
    win.mainloop()