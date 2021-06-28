from tkinter import *
from tkinter import messagebox  # For Alert Windows
from random import randint, choice, shuffle  # For Password Generator
import pyperclip  # to auto-copy passwords when generated
import json  # to save files in json file type


# ---------------------------- GLOBALS ------------------------------- #
DEFAULT_EMAIL = "lludu@live.com"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']
emojis = ['😀', '😅', '😭', '😈', '💩', '👋', '💪', '♠', '♣', '♥', '♦', '♚', '♛', '♜', '♝', '♞', '♟', '💯', '🐍',
          '🐉', '🐱', '🐶']

LOCK_ICON = "background.ico"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)

    # new_list = new_item for item in list
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_emojis = [choice(emojis) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers + password_emojis

    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD -------------------------------#

def save():

    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()

    new_data = {

        website: {"email": email, "password": password, }

    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n"
                                                              f"Email: {email}\n\nPassword:  {password}\n\n"
                                                              f"Is it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- FIND PASSWORD -------------------------------#

def find_password():

    website = website_input.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n\nPassword: {password}\n\n"
                                                       f" Press 'OK' to copy this password to clipboard")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

# GRID SYSTEM
# __________|____IMG____|__________ #
# __website_|___INPUT___|_SRCH_BTN_ #
# __email___|________INPUT_________ #
# __passw___|___INPUT___|__GEN_BTN_ #
# __________|______ADD_BTN_________ #


window = Tk()
window.title("Password Manager")
window.iconbitmap(LOCK_ICON)  # change the default icons -> fontawesome svg converted to ico :D
window.config(padx=50, pady=50)
window.resizable(width=False, height=False)  # can the window be resized

# ---------------------------- CANVAS IMAGE SWAP SETUP ------------------------------- #
pw_default = PhotoImage(file="background.png")
pw_search = PhotoImage(file="search.png")
pw_found = PhotoImage(file="found.png")


def img_default():
    canvas.itemconfig(image_id, image=pw_default)


def img_search():
    canvas.itemconfig(image_id, image=pw_search)
    canvas.after(1000, img_default)


def img_found():
    canvas.itemconfig(image_id, image=pw_found)
    canvas.after(750, img_default)


# ------------------WIDGETS SETUP----------------------#
canvas = Canvas(width=200, height=200, highlightthickness=0)
image_id = canvas.create_image(110, 100, image=pw_default)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# ----Input Fields---#
website_input = Entry(width="33")
website_input.grid(row=1, column=1, pady=3)
website_input.focus()

email_input = Entry(width="51")
email_input.grid(row=2, column=1, columnspan=2, pady=5)
# email_input.insert(0, DEFAULT_EMAIL)

password_input = Entry(width="33")
password_input.grid(row=3, column=1)

search_btn = Button(text="Search", command=find_password, width="15")
search_btn.grid(row=1, column=2)

gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width="43")
add_button.grid(row=4, column=1, columnspan=2, pady=5)


window.mainloop()
