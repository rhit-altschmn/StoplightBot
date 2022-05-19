print("GUI window test")

import tkinter
import time
from tkinter import ttk

def print_word():
    word = "You Lose"
    print(word)

def print_word_two():
    word_2 = "You Win"
    print(word_2)

def print_contents(entry_box):
    contents_of_entry_box = entry_box.get()

    if contents_of_entry_box == "Red":
        print("You Lose")
    if contents_of_entry_box == "Green":
        print("You Win")

def main():

    root = tkinter.Tk()
    root["background"] = "light blue"


    frame1 = tkinter.Frame(root, background="red", padx=100, pady=100)
    frame1.grid()

#This Is button 1 push, to say you lose
    print_stuff_button = ttk.Button(frame1, text="You Lose")
    print_stuff_button["command"] = lambda: print_word()
    print_stuff_button.grid()

# This Is button 2, push to say you win
    print_stuff_button = ttk.Button(frame1, text="You Win")
    print_stuff_button["command"] = lambda: print_word_two()
    print_stuff_button.grid()

# This Is button 3 , type 'Red' it says 'you lose', type 'Green' it says 'you win'
    print_stuff_button = ttk.Button(frame1, text="Level 3")
    print_stuff_button["command"] = lambda: print_contents(my_entry_box)
    print_stuff_button.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    root.mainloop()

main()


