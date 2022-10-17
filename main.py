from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    timer_label.config(text="Pomodoro", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = 10  # WORK_MIN * 60
    short_break_sec = 3  # SHORT_BREAK_MIN * 60
    long_break_sec = 5  # LONG_BREAK_MIN * 60

    global timer_label
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Counting down in minutes and seconds
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global checkmark
        if reps % 8 == 0:
            checkmark = ""
        elif reps % 2 == 0:
            checkmark += "✔︎"
        checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


# Tomato timer image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Timer label
timer_label = Label(text="Pomodoro", font=(FONT_NAME, 64, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

# Start button
start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=1, row=3)

# Reset button
reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=3, row=3)

# Checkmarks
checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)


window.mainloop()
