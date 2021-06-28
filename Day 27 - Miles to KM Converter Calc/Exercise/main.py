from tkinter import *
# ---------- Documentation ---------- #
# -- https://docs.python.org/3/library/tkinter.html#the-packer
# -- http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# -- http://tcl.tk/man/tcl8.6/TkCmd/entry.htm



# ---------- Create the TK window ---------- #
window = Tk()
window.title("My First GUI Program")
# window.resizable(width=False,height=False)  # can the window be resized
window.iconbitmap('pied-piper-square-brands.ico') # change the default icons -> fontawesome svg converted to ico :D
window.configure(bg='#222', padx=20, pady=20)
window.wm_attributes('-transparentcolor','brown') # ALL "BROWN" colors will be transparent
# window.minsize(width=500, height=300)
# window.attributes("-alpha", 0.5) # Transparent window


# ---------- Center the TK window ---------- #
window_width = 800
window_height = 500
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# ---------- Create a background image ---------- #
background_image=PhotoImage(file="wallpaper.png")
background_label = Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



# ---------- Create a Label ---------- #
my_label = Label(text="I am a Label", font=("Georgia", 24, "bold"), fg="#06823A")
# my_label.pack() # places in center of screen

my_label["text"] = "New Text"  # you can change the default value this way
my_label.config(text="Pied Piper") # you can change the default value this way
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# ---------- Create a Button ---------- #
def button_clicked():
    my_label.config(text=entry.get())
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# ---------- Create a Button ---------- #
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)



# ---------- Create a Entry Field ---------- #
entry = Entry(width="30")
entry.insert(END, string="Some text to begin with.")
entry.grid(column=4, row=3)
entry.get()













window.mainloop()  # Keeps window on screen