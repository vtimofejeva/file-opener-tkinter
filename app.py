# https://www.youtube.com/watch?app=desktop&v=jE-SpRI3K5g&t=7m38s 
# Description: creates an App, where we can select multiple files on PC and then click to Run them all at the same time.
# steps:
# 1. import
# 2. define ROOT
# 3. create CANVAS
# 4. create FRAME
# 5. create BUTTONS
# 6. define what Buttons do - function addApp for the Run Apps button
# 7. define how to Run Apps - function runApps
# 8. enable the Saving of the selected files within the App, so when we re-open our app it has the previously selected files and we just need to click Run Apps:
#   8.1. at the end of the code: with open("save.txt", "w") as f:
#   8.2. at the beginning of the code: if os.path.isfile("save.txt"):
#   8.3. after the main loop: for app in apps:

import tkinter as tk # to create GUI
from tkinter import filedialog, Text # to create tabs and display text
import os # allows to run apps

root = tk.Tk() # as in html we have a body, so whatever is created needs to be attached to the root
# root.mainloop() # click Run now, and it will open an app GUI, but we will paste this at the very end of the code
apps = [] # for the function addApp, so we can append all files we are adding

# for the open("save.txt") to avoid having double commas if no file selected (see below):
if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        # generate an array:
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()] #strips any empty spaces between file pathes, but still returns noting in our App
        print(apps)
        # so we add extra loop at the end of the code - for app in apps

# define a function for the buttons - allows to save the file and specify how:
def addApp():
    for widget in frame.winfo_children(): # gives access to everythin that's attached to the frame, in this case labels (see below)
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*"))) # * means All, opens a directory search and has only two option to select a type of file - executable and All Files
    apps.append(filename)
    print(apps) # to test - Run > Open File > change type to All > select a file > see in Terminal the Path of the selected file
    # create a label/text within the app, that would show us the Path of the file:
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
        # but if we opened two files etc, the 1st opened Path would be duplicated again, so we need to implement For Widget In Frame at the beginning of the function

# looping over the apps and starting the file + don't forget to attach the command to the runApps button:
def runApps():
    for app in apps:
        os.startfile(app)
# so now we can open the PNG file

# to create canvas and attach it to the root:
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42") 
canvas.pack() # to actually attach/run

# to attach extra container within the canvas (so it will be a white rectangular on top of the teal background of the canvas):
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# add some buttons (can attach to the root or frame):
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps= tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

# whenever the app starts a first time, the Pathes will be saved as expecte:
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# to save the selection of files - whenever we close our app, it will create a save.txt and write there the files we selected
with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
# this has a bug though - if we don't select anything after clicking on Open App, the save.txt file will place comma anyway - See the beginning of the code where we load the file
