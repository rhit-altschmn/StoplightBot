print("GUI window test")

import tkinter
from tkinter import ttk


def main():

    root = tkinter.Tk()
    root["background"] = "light blue"

    frame1 = ttk.Frame(root, padding=100)
    frame1.grid()

    on_button = ttk.Button(frame1, text="Turn ON")
    on_button.grid()


    root.mainloop()

main()


