from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

WORK_BROWN = "#e59b4c"
CYAN_RELAX = "#20b8c1"
PURPLE_BREAK = "#913fdb"
DARK_MODE = "#222"
LIGHT_MODE = "Whitesmoke"


FONT_NAME = "Georgia"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ✓ Checkmark symbol
# GRID SYSTEM
# _____|TITLE|_____ #
# _____|_IMG_|_____ #
# START|_____|RESET #
# _____|CHECK|_____ #
# _____|_____|_____ #


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=WORK_BROWN)
    check_marks.config(text="")
    REPS = 0
    to_work()




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down(2 * 60) #  5 minute timer
    global REPS
    REPS += 1
    short_breaks = [2,4,6]

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS == 8:  #  REPS % 8 == 0
        count_down(long_break_sec)
        to_long_break()
        timer_label.config(text="Break", fg=PURPLE_BREAK)
        pop_window()
        print(REPS)

    elif REPS in short_breaks:  #  REPS % 2 == 0
        count_down(short_break_sec)
        to_relax()
        timer_label.config(text="Relax", fg=CYAN_RELAX)
        pop_window()
        print(REPS)

    else: #  REPS % 2 != 0
        count_down(work_sec)
        to_work()
        timer_label.config(text="Work", fg=WORK_BROWN)
        pop_window()
        print(REPS)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = count // 60 # Floor Division instead of using math.floor
    count_sec = count % 60 # Seconds after we divide by 60 for the minutes

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"


    # if len(str(count_min)) == 1:
    #     count_min = str(count_min)
    #     count_min = count_min.zfill(2)

    # if len(str(count_sec)) == 1:
    #     count_sec = str(count_sec)
    #     count_sec = count_sec.zfill(2)


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count -1)  # change first *arg to speed test

    elif REPS == 8:
        reset_timer()
        pop_window()
        timer_label.config(text="Done!", fg=WORK_BROWN)



    else:
        start_timer()
        check = ""
        for _ in range(REPS // 2):
            check += "✓"
        check_marks.config(text=check)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=DARK_MODE)
window.resizable(width=False,height=False)  # can the window be resized
window.iconbitmap('stopwatch.ico') # change the default icons -> fontawesome svg converted to ico :D

def pop_window():
    window.lift()
    window.attributes('-topmost',True)
    window.after_idle(window.attributes,'-topmost',False)

canvas = Canvas(width=210, height=210, bg=DARK_MODE, highlightthickness=0)


# ---------------------------- CANVAS IMAGE SWAP SETUP ------------------------------- #
work = PhotoImage(file="work.png")
relax = PhotoImage(file="relax.png")
long_break = PhotoImage(file="break.png")


def to_work():
    # change image on canvas
    canvas.itemconfig(image_id, image=work)
    check_marks.config(fg=WORK_BROWN)
    dark_mode()

def to_relax():
    # change image on canvas
    canvas.itemconfig(image_id, image=relax)
    check_marks.config(fg=CYAN_RELAX)
    light_mode()

def to_long_break():
    # change image on canvas
    canvas.itemconfig(image_id, image=long_break)
    check_marks.config(fg=PURPLE_BREAK)
    light_mode()

image_id = canvas.create_image(105, 105, image=work)


# ---------------------------- DARK/LIGHT MODE SETUP ------------------------------- #

def dark_mode():
    window.config(bg=DARK_MODE)
    canvas.itemconfig(timer_text, fill=LIGHT_MODE)
    canvas.config(bg=DARK_MODE)
    timer_label.config(bg=DARK_MODE)
    check_marks.config(bg=DARK_MODE)


def light_mode():
    window.config(bg=LIGHT_MODE)
    canvas.itemconfig(timer_text, fill=DARK_MODE)
    canvas.config(bg=LIGHT_MODE)
    timer_label.config(bg=LIGHT_MODE)
    check_marks.config(bg=LIGHT_MODE)




# ---------------------------- WIDGETS SETUP ------------------------------- #
timer_text = canvas.create_text(105, 105, text="00:00", fill=LIGHT_MODE, font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=WORK_BROWN, bg=DARK_MODE)
timer_label.grid(row=0, column=1)

start_btn = Button(text="Start", command=start_timer, font=(FONT_NAME, 10), fg=DARK_MODE, bg=LIGHT_MODE, highlightthickness=0)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 10), fg=DARK_MODE, bg=LIGHT_MODE, highlightthickness=0)
reset_btn.grid(row=2, column=2)

check_marks = Label(font=(FONT_NAME, 20, "bold"), fg=WORK_BROWN, bg=DARK_MODE)
check_marks.grid(row=3, column=1)







window.mainloop()  # Keeps window on screen