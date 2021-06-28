from tkinter import *
# ---------- Documentation ---------- #
# -- https://docs.python.org/3/library/tkinter.html#the-packer
# -- http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# -- http://tcl.tk/man/tcl8.6/TkCmd/entry.htm



# ---------- Create the TK window ---------- #
window = Tk()
window.title("Mile to Km Converter")
window.resizable(width=False,height=False)  # can the window be resized
window.iconbitmap('calc.ico') # change the default icons -> fontawesome svg converted to ico :D
window.configure(bg='whitesmoke', padx=20, pady=20)
window.wm_attributes('-transparentcolor','brown') # ALL "BROWN" colors will be transparent
# window.minsize(width=500, height=300)
# window.attributes("-alpha", 0.5) # Transparent window


# ---------- Center the TK window ---------- #
window_width = 300
window_height = 150
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def calculate():
    # --------------LIST BOX PICKER-------------------#
    # if listbox.get(listbox.curselection()) == "Miles":
    #     miles = float(distance_input.get())
    #     km = round((miles * 1.60934), 2)
    #     dist_label.config(text="Km")
    #     converted_number.config(text=km)
    # elif listbox.get(listbox.curselection()) == "Km":
    #     km = float(distance_input.get())
    #     miles = round((km / 1.60934), 2)
    #     converted_number.config(text=miles)
    #     dist_label.config(text="Miles")
    # else:
    #     converted_number.config(text="0")

    # --------------RADIO BUTTON PICKER-------------------#
    if radio_state.get() == 1:
        miles = float(distance_input.get())
        km = round((miles * 1.60934), 2)
        dist_label.config(text="Km")
        print(f'{miles} miles is {km} km')
        converted_number.config(text=km)
    elif radio_state.get() == 2:
        km = float(distance_input.get())
        miles = round((km / 1.60934), 2)
        converted_number.config(text=miles)
        print(f'{km} km is {miles} miles')
        dist_label.config(text="Miles")
    # pass


dist_label = Label(text="", font=("Georgia", 16), fg="#222", bg='whitesmoke')
dist_label.grid(row=1, column=2)
dist_label.config(padx=5, pady=5)

distance_input = Entry(width="5", font=("Georgia", 16))
distance_input.grid(row=0, column=0)


equal_label = Label(text="is equal to", font=("Georgia", 16), fg="#222", bg='whitesmoke')
equal_label.grid(row=1, column=0)
equal_label.config(padx=5, pady=5)

converted_number = Label(text="0", font=("Georgia", 16), fg="#222", bg='whitesmoke')
converted_number.grid(row=1, column=1)
converted_number.config(padx=5, pady=5)



calc_button = Button(text="Calculate", command=calculate, font=("Georgia", 10), fg="#222", bg='whitesmoke')
calc_button.grid(row=2, column=1)
calc_button.config(padx=5, pady=5)


# listbox = Listbox(height=2)
# listbox.grid(row=0, column=2)
# distances = ["Miles", "Km"]
# for item in distances:
#     listbox.insert(distances.index(item), item)
# listbox.bind("<<ListboxSelect>>")

#Radiobutton
def radio_used():
    if radio_state.get() == 1:
        print("Miles")
    else:
        print("Km")
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Km", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=0, column=1)
radiobutton2.grid(row=0, column=2)







window.mainloop()  # Keeps window on screen