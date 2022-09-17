import tkinter as tk
from tkinter import Label, RAISED, Button
from tkinter.filedialog import asksaveasfilename

import cv2
import numpy as np
from mss import mss

fields = ('X-Coordinate', 'Y-Coordinate', 'Recording Width', 'Recording Height')


def record_screen(entries, ws, hs):
    # the y-coordinate of the upper-left corner
    top = int(entries['Y-Coordinate'].get())
    # print("top", top)
    # the x-coordinate of the upper-left corner,
    left = int(entries['X-Coordinate'].get())
    # print("top", top)
    # Width of Screen Recording:
    width = int(entries['Recording Width'].get())
    # print("top", top)
    # Height of Screen Recording:
    height = int(entries['Recording Height'].get())
    # print("top", top)

    if width == 0:
        # default width
        width = 800
    if height == 0:
        # default height
        height = 600

    monitor = {'top': top, 'left': left, 'width': width, 'height': height}
    sct = mss()
    winname = "Recording"
    sct.compression_level = 2

    # define the codec
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

    # Get the location where video needs to be saved
    file_name = asksaveasfilename(confirmoverwrite=True, defaultextension='.avi')
    # create the video write object
    out = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
    while True:
        # last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))

        # For Video recording
        img = cv2.resize(img, (width, height))
        frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # For Preview of Video
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
        cv2.moveWindow(winname, ws - (width+left), -100)

        out.write(frame)
        cv2.imshow(winname, frame)

        # print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(20) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    out.release()


def makeform(root, fields):
    entries = {}
    for field in fields:
        # print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field + " : ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries


# Define the user interface for Screen Recorder using Python
screen_recorder = tk.Tk()
screen_recorder.geometry("420x250")
screen_recorder.title("Screen Recorder")
ents = makeform(screen_recorder, fields)

# width of the screen
ws = screen_recorder.winfo_screenwidth()
# height of the screen
hs = screen_recorder.winfo_screenheight()

# Create and place the components
screen_button = Button(screen_recorder, text="Record Screen", command=(lambda e=ents: record_screen(e, ws, hs)),
                       relief=RAISED)
screen_button.pack(side=tk.LEFT, padx=5, pady=5)
info_label = Label(screen_recorder, text="Press 'q' to quit recording", bg="#02b9e5")
info_label.pack(side=tk.LEFT, padx=5, pady=5)
b3 = tk.Button(screen_recorder, text='Quit', command=screen_recorder.quit)
b3.pack(side=tk.LEFT, padx=5, pady=5)

screen_recorder.mainloop()
