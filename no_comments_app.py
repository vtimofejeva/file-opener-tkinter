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

import tkinter as tk
from tkinter import filedialog, Text 
import os 

root = tk.Tk()
apps = [] 

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]
        print(apps)

def addApp():
    for widget in frame.winfo_children(): 
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*"))) 
    apps.append(filename)
    print(apps) 
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=300, width=700, bg="white") 
canvas.pack()

frame = tk.Frame(root, bg="#263D42")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(frame, text="Open File", padx=10, pady=5, fg="black", bg="white", command=addApp)
openFile.pack()

deleteFile = tk.Button(root, text="Delete File", padx=10, pady=5, fg="black", bg="white")
deleteFile.pack()

runApps = tk.Button(frame, text="Run Apps", padx=10, pady=5, fg="black", bg="white", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
