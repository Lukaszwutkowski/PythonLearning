from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="First Label", font=("Roboto", 24, "bold", "italic"))
#my_label.pack(side="top")
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=5)

my_label["text"] = "New Text"
my_label.config(text="New Text")



#Button

def button_clicked():
    #my_label.config(text="I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

button_2 = Button(text="New Button")
button_2.grid(column=2, row=0)

#Entry

input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)
window.mainloop()