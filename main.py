from tkinter import *
import math

import time
window = Tk()
window.title("Pomodoro App")

print("it's time")

# ---------------------------- CONSTANTS ------------------------------- #
OTHER_GREEN = "#C1DEAE"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
#GREENISH = "#C1DEAE"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
list_time = [WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN]

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0

def start_timer():
    global reps


    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", font=(FONT_NAME, 40, "bold"), bg=GREEN, fg=RED)
        check_mark.config(text="🗸", font=(FONT_NAME, 25), bg=GREEN, fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", font=(FONT_NAME, 40, "bold"), bg=GREEN, fg=RED)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work Time", font=(FONT_NAME, 40, "bold"), bg=GREEN, fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count * 60
    min = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f'0{secs}'
    if count > 0:
        window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_count, text=f'{min}:{secs}')
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text="🗸", font=(FONT_NAME, 25), bg= GREEN, fg= PINK)
            print("checkmark printed")

       # canvas.itemconfig(timer_count, text=f'{min}:{secs}')





# ---------------------------- UI SETUP ------------------------------- #


def say_something(thing):
    print(thing)

window.after(1000, say_something, "coe")

canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
window.config(padx=100, pady=50, bg=GREEN)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=tomato_img)
timer_count = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=GREEN, fg=RED)
timer_label.grid(column=1, row=0)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)
check_mark = Label()
check_mark.grid(column=1, row=4)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)


#count_down(25)

window.mainloop()
