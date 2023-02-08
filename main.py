# This project is done according to the points from 
# https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Random-Number-Generator.md
# by SerjSX 

import customtkinter
from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import sys
from PIL import  Image

root = customtkinter.CTk()
root.title("Python Number Generator Project")
root.geometry("600x400")

# This is to identify if it is already displayed on the window.
display_frame = None

# Grabs the directory name
path = sys.path[0]

copy_img = customtkinter.CTkImage(light_image=Image.open(path + "/copy.png"),
                                    size=(25,25))

negmin_var = StringVar()
negmax_var = StringVar()
def checkbox_event(type):
    if type == "min" and negmin_var.get() == "on":
        if not minimum_input.get().startswith("-"):
            # First it grabs whatever is in the input with adding - at the beginning
            negativised = "-" + minimum_input.get()

            # Then it deletes whatever is in the input
            minimum_input.delete(0, END)

            # It adds in the input the negativised number
            minimum_input.insert(0, negativised)
    elif type == "min" and negmin_var.get() == "off":
        # First it retrieves and splits the number in the input with -
        split = minimum_input.get().split("-")

        # It deletes whatever is in the input
        minimum_input.delete(0, END)

        # It inserts the 1 from the split which is whatever number there is after the - sign
        minimum_input.insert(0, split[1])
    elif type == "max" and negmax_var.get() == "on":
        if not maximum_input.get().startswith("-"):
            negativised = "-" + maximum_input.get()
            maximum_input.delete(0, END)
            maximum_input.insert(0, negativised)
    elif type == "max" and negmax_var.get() == "off":
        split = maximum_input.get().split("-")
        maximum_input.delete(0, END)
        maximum_input.insert(0, split[1])


def generate():
    # Logging the start and end strictly according to the user input
    try:
        start = float(minimum_input.get())
    except:
        messagebox.showerror("Error", "An error occured during transforming the minimum to integer. Value is set to 0 by default.")
        start = 0
        minimum_input.delete(0, END)
        minimum_input.insert(0, 0)

    try:
        end = float(maximum_input.get())
    except:
        messagebox.showerror("Error", "An error occured during transforming the maximum to integer. Value is set to 0 by default.")
        end = 0
        maximum_input.delete(0, END)
        maximum_input.insert(0, 0)

    # The following is done for identifying if user input is an integer or a float.
    # This is done by converting the float to string, splitting with ., and if the number
    # after . is 0 then it can be safely converted to an integer, or else it'll stay as a float.
    splitted_start = str(start).split(".")
    splitted_end = str(end).split(".")
    float_ping = True

    # If the splitted ind1 is 0, then it can be safely converted to an integer
    # Also ping float_ping to False
    if splitted_start[1] == "0":
        start = int(minimum_input.get())
        float_ping = False
    if splitted_end[1] == "0":
        end = int(maximum_input.get())
        float_ping = False

    # If start/end starts with -, then it's negative so set the variable to on. If not, set it to off.
    if str(start).startswith("-"):
        negmin_var.set("on")
    else:
        negmin_var.set("off")
        
    if str(end).startswith("-"):
        negmax_var.set("on")
    else:
        negmin_var.set("off")

    opposite = False

    # If end is less than start, then toggle opposite
    if end < start:
        print("Opposite true")
        opposite = True

    # If opposite false then just normall randomize from start to end
    if opposite == False:

        # We do the following to show correct negative checkboxes
        if str(start).startswith("-"):
            negmin_var.set("on")
            print("Opposite start on")
        else:
            negmin_var.set("off")
            print("Opposite start off")
        
        if str(end).startswith("-"):
            negmax_var.set("on")
            print("Opposite end on")
        else:
            negmax_var.set("off")
            print("Opposite end off")

        # If start and end are both negative, then trigger both of them to on
        if str(start).startswith("-") and str(end).startswith("-"):
            negmin_var.set("on")
            negmax_var.set("on")
            print("Opposite both on")

        # If both values are 0, -0, or the same, then throw an error message. Or else proceed
        # with randomizing.
        if minimum_input.get() == '0' and maximum_input.get() == '0':
            print(start,end)
            messagebox.showerror("Error", "You cannot put both values 0.")
            return
        elif minimum_input.get() == '-0' and maximum_input.get() == '-0':
            print(start,end)
            messagebox.showerror("Error", "You cannot put both values -0.")
            return
        elif minimum_input.get() == maximum_input.get() and maximum_input.get() == minimum_input.get():
            print(start,end)
            messagebox.showerror("Error", "You cannot generate a number with the same number.")
            return
        else:
            # If float_ping is False, then use randrange to find a random number. This does it normal integer.
            if float_ping == False:
                result = random.randrange(start, end)
            
            # If it's True then use uniform which considers it as a float.
            else:
                result = random.uniform(start, end)
    # If opposite is true then switch their places
    else:
        # Replace the input displays as well
        minimum_input.delete(0, END)
        minimum_input.insert(0, end)
        maximum_input.delete(0, END)
        maximum_input.insert(0, start)

        # We do the opposite here because we are switching the places
        if str(start).startswith("-"):
            negmax_var.set("on")
            print("Opposite start on")
        else:
            negmax_var.set("off")
            print("Opposite start off")
        
        if str(end).startswith("-"):
            negmin_var.set("on")
            print("Opposite end on")
        else:
            negmin_var.set("off")
            print("Opposite end off")

        if str(start).startswith("-") and str(end).startswith("-"):
            negmin_var.set("on")
            negmax_var.set("on")
            print("Opposite both on")

        # If both values are 0, -0, or the same, then throw an error message. Or else proceed
        # with randomizing.
        if minimum_input.get() == '0' and maximum_input.get() == '0':
            print(start,end)
            messagebox.showerror("Error", "You cannot put both values 0.")
            return
        elif minimum_input.get() == '-0' and maximum_input.get() == '-0':
            print(start,end)
            messagebox.showerror("Error", "You cannot put both values -0.")
            return
        elif minimum_input.get() == maximum_input.get() and maximum_input.get() == minimum_input.get():
            print(start,end)
            messagebox.showerror("Error", "You cannot generate a number with the same number.")
            return
        else:
            if float_ping == False:
                result = random.randrange(end, start)
            else:
                result = random.uniform(end, start)
    display(result)


# The function to display the result
def display(num):
    # Globalizing what's necessary 
    global define_frame
    global display_frame

    # If display_frame is not None, then most probably there is another frame already.
    # So we destroy the old one before creating a new one.
    if display_frame != None:
        display_frame.destroy()

    # Below are mostly for the GUI
    display_frame = customtkinter.CTkFrame(define_frame)
    display_frame.pack(pady=10)

    # This is what displays the result
    result = customtkinter.CTkLabel(display_frame, text=num, font=customtkinter.CTkFont(size=20, weight="bold"))
    result.pack(side=LEFT, padx=10)

    # This button is used for copying the result with pyperclip
    copy_button = customtkinter.CTkButton(display_frame, image=copy_img, text="", width=20,
                                        corner_radius=0, command=lambda: pyperclip.copy(num))
    copy_button.pack(side=LEFT)


# All below are mainly for the GUI
title = customtkinter.CTkLabel(root, text="Welcome to Python Number Generator Project", font=customtkinter.CTkFont(size=20, weight="bold"))
title.pack(pady=30)

define_frame = customtkinter.CTkFrame(root)
define_frame.pack()

define_text = customtkinter.CTkLabel(define_frame, text="Define a minimum and a maximum range", font=customtkinter.CTkFont(size=16, weight="bold"))
define_text.pack(pady=10)

maxmin_frame = customtkinter.CTkFrame(define_frame, fg_color = "transparent")
maxmin_frame.pack()

minimum_frame = customtkinter.CTkFrame(maxmin_frame)
minimum_frame.pack(side=LEFT, padx=10)
minimum_text = customtkinter.CTkLabel(minimum_frame, text="Type the minimum amount")
minimum_text.pack(pady=10, padx=10)
minimum_input = customtkinter.CTkEntry(minimum_frame)
minimum_input.pack(pady=5)

negmin_checkbox = customtkinter.CTkCheckBox(master=minimum_frame, text="Negative", command=lambda: checkbox_event("min"),
                                     variable=negmin_var, onvalue="on", offvalue="off")
negmin_checkbox.pack(padx=10, pady=10)

maximum_frame = customtkinter.CTkFrame(maxmin_frame)
maximum_frame.pack(side=LEFT, padx=10)
maximum_text = customtkinter.CTkLabel(maximum_frame, text="Type the maximum amount")
maximum_text.pack(pady=10, padx=10)
maximum_input = customtkinter.CTkEntry(maximum_frame)
maximum_input.pack(pady=5)

negmax_checkbox = customtkinter.CTkCheckBox(master=maximum_frame, text="Negative", command=lambda: checkbox_event("max"),
                                     variable=negmax_var, onvalue="on", offvalue="off")
negmax_checkbox.pack(padx=10, pady=10)

generate_button = customtkinter.CTkButton(root, text="Generate", command=generate)
generate_button.pack(pady=10)

root.mainloop()