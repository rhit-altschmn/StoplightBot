print("GUI window test")

import tkinter
from tkinter import ttk

def print_word():
    word = "You Lose"
    print(word)

def print_contents(entry_box):
    contents_of_entry_box = entry_box.get()

    if contents_of_entry_box == "Red":
        print("You Lose")
    else:
        print("You Win")

def main():

    root = tkinter.Tk()
    root["background"] = "light blue"

    frame1 = ttk.Frame(root, padding=100)
    frame1.grid()

#This Is button 1
    on_button = ttk.Button(frame1, text="Level 1")
    on_button.grid()

# This Is button 2
    print_stuff_button = ttk.Button(frame1, text="Level 2")
    print_stuff_button["command"] = lambda: print_word()
    print_stuff_button.grid()

# This Is button 3 , type 'Red' for it to say 'you lose' type anything else it will say you win
    print_stuff_button = ttk.Button(frame1, text="Level 3")
    print_stuff_button["command"] = lambda: print_contents(my_entry_box)
    print_stuff_button.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    root.mainloop()

main()


