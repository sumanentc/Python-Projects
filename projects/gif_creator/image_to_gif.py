import glob
import tkinter as tk

import imageio
import imageio.v3 as iio
from tkinter import filedialog, RAISED
import traceback

# Define the user interface for Reading the images using Python
from tkinter import LEFT, messagebox


# Function to convert Images to GIF
from pygifsicle import optimize


def convertToGIF(image_extension):
    # Getting the path of the folder with the images
    folder_selected = filedialog.askdirectory()
    path = folder_selected  # Get the path of the folder entered by the user
    ext = image_extension.get()  # Get the extension png or jpeg
    path_in = path + '/*.' + ext  # Creating the final path of the images
    path_out = path + "/MyGif.gif"  # Creating the path for GIF in the same folder as the images
    imgs = []  # list to store all the images
    try:
        file = sorted(glob.glob(path_in, recursive=True))  # Recursively getting the paths of all the images in the folder
        for im in file:
            imgs.append(iio.imread(im))  # Reading all the images
        imageio.mimsave(path_out, imgs)  # Converting the images to GIF and saving it
        optimize(path_out) # For overwriting the original one
        # Showing the message box on saving the gif
        messagebox.showinfo("GIF Generator", "GIF is saved successfully in the folder with Images!")
    except Exception :
        # Showing a message if not able to collect the images or convert them to gif
        print(traceback.format_exc())
        messagebox.showinfo("Error occurred!", "Please check the path of the folder or the extension of images.")


gif_creator = tk.Tk()
gif_creator.geometry("420x250")
gif_creator.title("GIF Creator")

# Creating the variables to get the path of folder and the extension of images
extension = tk.StringVar(gif_creator, 'png')

# Getting the extension of the image as either png or jpeg
tk.Label(gif_creator, text='Please select the extension of the images', bg="#02b9e5", justify=LEFT, anchor='w',
         font=('Times', 20, 'bold')).place(
    x=30, y=30)
r1 = tk.Radiobutton(gif_creator, text='png', variable=extension, value='png', font=('Times', 20, 'bold'))
r1.grid(row=1, column=1, padx=90, pady=90)
r2 = tk.Radiobutton(gif_creator, text='jpeg', variable=extension, value='jpeg', font=('Times', 20, 'bold'))
r2.grid(row=1, column=2, padx=10, pady=90)

# Button to convert the images into GIF and save the GIF
gif_button = tk.Button(gif_creator, text="Create GIF", bg="#02b9e5", font=('Times', 20, 'bold'),
          command=(lambda e=extension: convertToGIF(extension)), relief=RAISED).place(x=60, y=170)
tk.Button(gif_creator, text="Quit", bg="#02b9e5", font=('Times', 20, 'bold'),
          command=gif_creator.quit).place(x=250, y=170)

# Runs the window till it is closed by the user
gif_creator.mainloop()
