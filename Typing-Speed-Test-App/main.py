import random
from tkinter import *
from english_words import english_words_lower_set


# Functions
def start_timer():
    global run
    get_words()
    if run == 0:
        countdown(60)
        run += 1


def countdown(count):
    global timer
    timer_label.config(text=f"Time: {count}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        input_field.config(state="disabled")
        update_wpm()


def get_words():
    global word_list
    # Get a list of random words
    words = list(english_words_lower_set)
    for word_label in WORD_LABELS:
        word = random.choice(words)
        word_label.config(text=word, fg=BLACK)
        word_list.append(word_label.cget("text"))


def verify_word(event):
    global word_count, correct_word, incorrect_word
    word = input_field.get()
    if " " in word:
        word = word.split()[0]
    input_field.icursor(0)
    input_field.delete(0, 'end')
    current_word = WORD_LABELS[word_count]
    if current_word.cget("text") == word:
        current_word.config(fg=GREEN)
        correct_word += 1
    else:
        current_word.config(fg=RED)
        incorrect_word += 1
    word_count += 1
    if word_count == 10:
        word_count = 0
        get_words()


def update_wpm():
    wpm = correct_word + incorrect_word
    wpm_label.config(text=f"WPM: {wpm:.2f}")


def restart():
    global run, timer, word_list, word_count, correct_word, incorrect_word
    run = 0
    timer = None
    word_list = []
    word_count = 0
    correct_word = 0
    incorrect_word = 0
    input_field.delete(0, 'end')
    start_timer()


# Constants
timer = None
run = 0
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Courier"
word_list = []
word_count = 0
correct_word = 0
incorrect_word = 0


# GUI using tkinter
window = Tk()

title_label = Label(text="Welcome To Typerrr!", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 45))
title_label.grid(row=1, column=0, columnspan=5)

# Word labels
word_label_1 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_1.grid(row=2, column=0, padx=5, pady=35)

word_label_2 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_2.grid(row=2, column=1)

word_label_3 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_3.grid(row=2, column=2)

word_label_4 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_4.grid(row=2, column=3)

word_label_5 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_5.grid(row=2, column=4)

word_label_6 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_6.grid(row=3, column=0, padx=5)

word_label_7 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_7.grid(row=3, column=1)

word_label_8 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_8.grid(row=3, column=2)

word_label_9 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_9.grid(row=3, column=3)

word_label_10 = Label(text="", bg=YELLOW, font=(FONT_NAME, 20))
word_label_10.grid(row=3, column=4)

WORD_LABELS = [word_label_1, word_label_2, word_label_3, word_label_4, word_label_5,
               word_label_6, word_label_7, word_label_8, word_label_9, word_label_10]

input_field = Entry(width=52, font=(FONT_NAME, 20))
input_field.grid(row=4, column=0, columnspan=5, pady=35)
input_field.bind("<space>", verify_word)

start_button = Button(text="Start", bg=GREEN, font=(FONT_NAME, 20), command=start_timer)
start_button.grid(row=5, column=0, pady=25)

restart_button = Button(text="Restart", bg=GREEN, font=(FONT_NAME, 20), command=restart)
restart_button.grid(row=5, column=1, pady=25)

wpm_label = Label(text="WPM: -", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 25))
wpm_label.grid(row=5, column=3)

timer_label = Label(text="Time: 60", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 25))
timer_label.grid(row=5, column=4)

# Screen configurations
window.title("Typing Speed Test App")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("+270+100")
window.resizable(False, False)

window.mainloop()




