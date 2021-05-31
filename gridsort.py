import os
import re

def doThings():

    # Put all filenames from the working directory into a list.
    oldNames = list(os.listdir())

    # Determine the number of columns and rows.
    reThing = re.compile('\d{3}.\d{3}')
    coordinates = reThing.findall(str(oldNames[-1]))
    coordinates = list(coordinates[0])
    cols = "".join(coordinates[0:3])
    rows = "".join(coordinates[4:7])

    # Removes leading zeros and add 1 to obtain the actual usable numbers.
    cols = int(cols.lstrip('0')) + 1
    rows = int(rows.lstrip('0')) + 1

    # Put the filenames into sub-lists (with the correct montage order) into a new list.
    thing = []
    for i in range(0, rows + 1):
        thing.append(oldNames[-i:0:-rows])

    # For some reason the previous loop skips the 000_000 file. The next row adds it to the list.
    thing[rows].append(oldNames[0])

    # Reverse the order of the sub-lists to get everything into the correct montage order.
    thing.reverse()

    niceThing = []

    # Put the sub-lists into a normal list.
    for i in thing:
        for x in i:
            niceThing.append(x)

    newNames = list(x for x in range(0, len(oldNames)))

    # Rename the files using the numbers in the newNames list.
    for i in range(0, len(niceThing)):
        os.rename(str(niceThing[i]), str(newNames[i]) + '.tif')

    with open('grid_size.txt', 'w') as f:
        f.write('The grid has ' + str(cols) + ' columns and ' + str(rows) + ' rows.')

from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    os.chdir(filename)
    doThings()


root = Tk()
root.title('Grid sort')
root.geometry('310x260')
L = Label(root, wraplength = 300, text = 'Press the button to select the folder that contains the images you want to sort. The program will change the names of the image files to a sequence of numbers, which ImageJ will then load in the correct order for its montage tool. The correct size of the montage will be saved in a text file in the same folder as the images. The process is IRREVERSIBLE, only use it on files you have backed up. There will be no notification on completion.')
L.config(font =('Calibri', 12))
button = Button(text='Select folder', command=browse_button)
button.place(relx = 0.5, rely = 0.9, anchor = CENTER)
L.pack()
mainloop()