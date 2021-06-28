# -------------------- Modules -------------------- #
import requests
# API Requests Documentation # https://docs.python-requests.org/en/master/
from tkinter import *



def get_quote():
    pass
    # -------------------- Request Data from the API -------------------- #
    response = requests.get(url="https://api.kanye.rest/")
    # print(response.status_code) # Shows the status code i.e. 200 / 404
    response.raise_for_status()  # Shows raised exception for errors

    # -------------------- Getting Data from the API -------------------- #
    data = response.json()  # Actual json data from the api
    # print(data)
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()