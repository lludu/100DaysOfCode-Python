from tkinter import *
# ---------- Documentation ---------- #
# -- https://docs.python.org/3/library/tkinter.html#the-packer
# -- http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# -- http://tcl.tk/man/tcl8.6/TkCmd/entry.htm



# ---------- Create the TK window ---------- #
window = Tk()
window.title("Mile to Km Converter")
# window.resizable(width=False,height=False)  # can the window be resized
window.iconbitmap('calc.ico') # change the default icons -> fontawesome svg converted to ico :D
window.configure(bg='whitesmoke', padx=20, pady=20)
window.wm_attributes('-transparentcolor','brown') # ALL "BROWN" colors will be transparent
# window.minsize(width=500, height=300)
# window.attributes("-alpha", 0.5) # Transparent window


# ---------- Center the TK window ---------- #
window_width = 300
window_height = 200
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def calculate():
    # 1 mile = 1.60934 km
    miles = int(miles_input.get())
    km = round((miles * 1.60934),2)
    converted_number.config(text=km)




miles_input = Entry(width="5", font=("Georgia", 16))
miles_input.grid(row=0, column=1)



miles_label = Label(text="Miles", font=("Georgia", 16), fg="#222", bg='whitesmoke')
miles_label.grid(row=0, column=2)
miles_label.config(padx=5, pady=5)

equal_label = Label(text="is equal to", font=("Georgia", 16), fg="#222", bg='whitesmoke')
equal_label.grid(row=1, column=0)
equal_label.config(padx=5, pady=5)

converted_number = Label(text="0", font=("Georgia", 16), fg="#222", bg='whitesmoke')
converted_number.grid(row=1, column=1)
converted_number.config(padx=5, pady=5)

km_label = Label(text="km", font=("Georgia", 16), fg="#222", bg='whitesmoke')
km_label.grid(row=1, column=2)
km_label.config(padx=5, pady=5)

calc_button = Button(text="Calculate", command=calculate, font=("Georgia", 10), fg="#222", bg='whitesmoke')
calc_button.grid(row=2, column=1)
calc_button.config(padx=5, pady=5)









window.mainloop()  # Keeps window on screen