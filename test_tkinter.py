import tkinter as tk
import os

root = tk.Tk()
root.title("Testing Tkinter Options")

def button_clicked():
    print("Button Clicked!")

canvas = tk.Canvas(root, height=500, width=500, bg="blue")
canvas.pack()

top_frame = tk.Frame(root, bg="gray")
top_frame.place(relwidth=1, relheight=0.05)

test_button = tk.Button(top_frame,
                   text="Test Click", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=2,
                   pady=1,
                   width=7,
                   wraplength=100)
test_button.pack(padx=5, pady=1, side="left")



root.mainloop()