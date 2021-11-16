from tkinter import *
from PIL import Image, ImageTk
from speech_recognition import *

root = Tk()
root.geometry("290x392")
root.maxsize(290, 392)
root.minsize(290, 392)
root.title("Calculator by Shivam")
root.wm_iconbitmap("calculator.ico")
root.configure(bg="black")


def click(event):
    global sc_value
    text = event.widget.cget("text")
    if text == "=":
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        else:
            value = eval(screen.get())
        sc_value.set(value)
        screen.update()
    elif text == "C":
        sc_value.set("")
        screen.update()
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()


def audio(event):
    global sc_value
    speech = Recognizer()
    sc_value.set("")
    screen.update()
    sc_value.set("speak now")
    screen.update()
    with Microphone() as source:
        audio = speech.listen(source)
        try:
            text = speech.recognize_google(audio)
            sc_value.set(text)
            screen.update()
            if 'x' in text:
                text = text.replace('x', '*')
            print(text)
            value = eval(text)
            sc_value.set(value)
            screen.update()

        except:
            sc_value.set("sorry")
            screen.update()

sc_value = StringVar()
sc_value.set("")
screen = Entry(root, textvariable=sc_value, font="lucida 30 bold",
               borderwidth=5, bg="black", fg="light grey", relief=SUNKEN)
screen.pack(fill=X, padx=5, pady=5, ipadx=5, ipady=1)

list1 = ['7', '8', '9']
list2 = ['4', '5', '6']
list3 = ['1', '2', '3']

f0 = Frame(root, bg="black")
b = Button(f0, text="C", font="lucida 20 bold", padx=10, borderwidth=5, pady=1, bg="light green")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

image = Image.open("mic.png")
resize = image.resize((55, 49), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)
b = Button(f0, image=photo, font="lucida 20 bold", padx=7, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", audio)

b = Button(f0, text="%", font="lucida 20 bold", padx=7, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
b = Button(f0, text="/", font="lucida 20 bold", padx=14, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
f0.pack()

f1 = Frame(root, bg="black")
for i in list1:
    b = Button(f1, text=i, font="lucida 20 bold", padx=12, borderwidth=5, pady=1, bg="light grey")
    b.pack(side=LEFT, padx=1, pady=1)
    b.bind("<Button-1>", click)
b = Button(f1, text='*', font="lucida 20 bold", padx=12, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
f1.pack()

f2 = Frame(root, bg="black")
for i in list2:
    b = Button(f2, text=i, font="lucida 20 bold", padx=12, borderwidth=5, pady=1, bg="light grey")
    b.pack(side=LEFT, padx=1, pady=1)
    b.bind("<Button-1>", click)
b = Button(f2, text='-', font="lucida 20 bold", padx=13, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
f2.pack()

f3 = Frame(root, bg="black")
for i in list3:
    b = Button(f3, text=i, font="lucida 20 bold", padx=12, borderwidth=5, pady=1, bg="light grey")
    b.pack(side=LEFT, padx=1, pady=1)
    b.bind("<Button-1>", click)
b = Button(f3, text='+', font="lucida 20 bold", padx=9, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
f3.pack()

f4 = Frame(root, bg="black")
b = Button(f4, text="0", font="lucida 20 bold", padx=47, borderwidth=5, pady=1, bg="light grey")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
b = Button(f4, text=".", font="lucida 20 bold", padx=16, borderwidth=5, pady=1, bg="light grey")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
b = Button(f4, text="=", font="lucida 20 bold", padx=9, borderwidth=5, pady=1, bg="orange")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)
f4.pack()

root.mainloop()
