from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    print("Clicked.")
    new_text = input.get()
    my_label.config(text=new_text)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

button = Button(text="Click Me !", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

new_button = Button(text="New Button")
# new_button.pack()
new_button.grid(row=0, column=2)

input = Entry(width=10)
# input.pack()
input.grid(row=2, column=3)


window.mainloop()