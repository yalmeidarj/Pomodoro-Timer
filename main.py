from tkinter import *
import math

window = Tk()
window.title("Pomodoro App")

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
work_min = 25
short_break_min = 5
long_break_min = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    '''Resets checkmarks to empty list, sets reps to "0", config timer_label to "Timer".'''
    global reps
    reps = 0
    window.after_cancel(timer)
    checkmark.clear()
    check_mark.config(text=f"{''.join(checkmark)}", font=(FONT_NAME, 25), bg=GREEN, fg=PINK)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_count, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0
checkmark = []


def start_timer():
    '''Starts count_down function with proper parameter based on # of reps.'''
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_min * 60)
        timer_label.config(text="Long Break", font=(FONT_NAME, 30, "bold"), bg=GREEN, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min * 60)
        timer_label.config(text="Break", font=(FONT_NAME, 30, "bold"), bg=GREEN, fg=RED)
    else:
        count_down(work_min * 60)
        timer_label.config(text="Work Time", font=(FONT_NAME, 30, "bold"), bg=GREEN, fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    '''Starts countdown based on parameter.'''
    count * 60
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f'0{secs}'
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_count, text=f'{mins}:{secs}')
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark.append("🗸")
            check_mark.config(text=f"{''.join(checkmark)}", font=(FONT_NAME, 25), bg=GREEN, fg=PINK)
            check_mark.grid(column=1, row=4)
            print("checkmark printed")

# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
window.config(padx=100, pady=50, bg=GREEN)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=tomato_img)

timer_count = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=GREEN, fg=RED)
timer_label.grid(column=1, row=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label()

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

window.mainloop()
