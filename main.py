from tkinter import *


def calculate_speed():
    all_text = input_text.get("1.0", "end-1c")
    print(all_text)
    words_per_minute = all_text.split(" ")
    output_label = Label(window, text=f"Your typing speed is {len(words_per_minute)} wps", padx=10, pady=10)
    print(len(words_per_minute))
    text_counter = 0
    for i in range(len(words_per_minute)):
        if text_list[i] == words_per_minute[i]:
            text_counter += 1
    wrong_words = len(words_per_minute)-text_counter
    output_label_desc = Label(window, text=f"Out of the words you typed, {wrong_words} words are typo", padx=10, pady=10)
    output_label.pack(padx=20, pady=20)
    output_label_desc.pack()


def start_calculating():
    input_text.delete(1.0,END)
    display = Label(window, text='Start typing, calculation started', padx=5, pady=5)
    display.pack()
    delay = window.after(10000, calculate_speed)


text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n "
        "when an unknown printer took a galley of type and scrambled it to make a type\n "
        "specimen book. It has survived not only five centuries, but also the leap into\n "
        "electronic typesetting, remaining essentially unchanged.")

text_list = text.split(" ")

delay = None
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Typing speed calculator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Label
l = Label(window, text='Press "Start" to start calculating your typing speed', padx=10, pady=10)
l.config(font=("Courier", 14))

paragraph = Label(window, text=text, padx=10, pady=10)
paragraph.config(font=("Courier", 10))

# Input Text
input_text = Text(window, height=7,
                  width=75,
                  bg="light yellow")

# Button
start_button = Button(window, height=2,
                      width=20,
                      text="Start",
                      command=start_calculating)

output_label_desc = Label(window, padx=10, pady=10)

l.pack(padx=15, pady=15)
paragraph.pack()
input_text.pack(padx=10, pady=10)
start_button.pack(padx=5, pady=5)

window.mainloop()