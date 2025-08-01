from tkinter import *
from PIL import Image,ImageTk
from math import floor
# TODAY WE ARE GOING TO DESIGN POMODORO APPLICATION
NAVY = "#113F67"
BLACK = "#000000"
MINT = "#1DCD9F"
YELLOW = "#f7f5dd"
FONT_NAME = "Times New Roman"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# =================================TIMER MECHANISM========================================
def start_timer():
    global reps
    reps += 1
    work_hour = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="LONG BREAK")
        count_down(long_break)
    elif reps % 2 == 0:
        title_label.config(text="BREAK")
        count_down(short_break)
    else:
        title_label.config(text="PRACTICE WELL")
        count_down(work_hour)

# ================================COUNTDOWN MECHANISM====================================
def count_down(count):
    min_count = floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    if min_count < 10:
        min_count = f"0{min_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkbox.config(text=marks)


# ===========================================RESET BLOCK ================================
def reset_block():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="LET'S BEGIN")
    checkbox.config(text="")
#=========================================UI INTERFACE=================================
window = Tk()
window.title("Work Remainder")
window.config(padx=20, pady=20, bg=BLACK)

# LABELLING PART
title_label = Label(text="LET'S BEGIN", fg=MINT, bg=BLACK, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=3, row=0)

# RESIZING THE ORIGINAL IMAGE
original_image = Image.open("wukong.png")
resized_image = original_image.resize((800, 450))

image1 = ImageTk.PhotoImage(resized_image)
canvas = Canvas(width=800, height=450, bg=BLACK, highlightthickness=0)
canvas.create_image(0, 0, anchor="nw", image=image1)
timer_text = canvas.create_text(150, 112, text="00:00" ,fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(column=3, row=1)

# BUTTONS
start_button = Button(text="Start",fg=MINT, bg=BLACK, activebackground=BLACK, borderwidth=0,  highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=start_timer)
reset_button = Button(text="Reset", fg=MINT, bg=BLACK, activebackground=BLACK, borderwidth=0, highlightthickness=0, font=(FONT_NAME, 20, "bold"), command=reset_block)
canvas.create_window(660, 300, window=reset_button)
canvas.create_window(150, 300, window=start_button)

# CHECK BOXS
checkbox = Label( fg=MINT, bg=BLACK, font=("normal", 10, "bold"))
checkbox.grid(column=3, row=2)

window.mainloop()