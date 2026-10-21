from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window = Tk()
window.title('denomination counter')
window.configure(bg = 'lightblue')
window.geometry('650x400')

upload = Image.open('ksh.jpeg')
upload = upload.resize((300,280))
image = ImageTk.PhotoImage(upload)
label = Label(window,image = image)
label.place(x = 180,y = 10)
label2 = Label(window,text = 'welcome to the denomination counter application',bg = 'lightblue')
label2.place(x = 180,y = 280)

def msg():
    msgbox = messagebox.showinfo('alert!','do you want to calculate the denomination count?')
    if msgbox == 'ok':
        topwin()

button1 = Button(window,text = "let's get started",command = msg)
button1.place(x = 250,y = 300)

def topwin():
    top = Toplevel()
    top.title('denominations calculator')
    top.geometry('600x350')
    top.configure(bg = 'lightblue')
    label = Label(top,text = 'enter total amount')
    label.place(x = 230,y = 30)
    entry = Entry(top)
    entry.place(x = 200,y = 50)


    lbl1 = Label(top,text = '1000')
    lbl1.place(x = 180,y = 110)
    entry1 = Entry(top)
    entry1.place(x = 230,y = 110)

    lbl2 = Label(top,text = '500')
    lbl2.place(x = 180,y = 140)
    entry2 = Entry(top)
    entry2.place(x = 230,y = 140)

    lbl3 = Label(top,text = '200')
    lbl3.place(x = 180,y = 170)
    entry3 = Entry(top)
    entry3.place(x = 230,y = 170)

    lbl4 = Label(top,text = '100')
    lbl4.place(x = 180,y = 200)
    entry4 = Entry(top)
    entry4.place(x = 230,y = 200)

    lbl5 = Label(top,text = '50')
    lbl5.place(x = 180,y = 230)
    entry5 = Entry(top)
    entry5.place(x = 230,y = 230)

    def calculate():
        amount = int(entry.get())
        note1000 = amount // 1000
        amount %= 1000
        note500 = amount // 500
        amount %= 500
        note200 = amount // 200
        amount %= 200
        note100 = amount // 100
        amount %= 100
        note50 = amount // 50
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END)
        entry5.delete(0,END)

        entry1.insert(END,str(note1000))
        entry2.insert(END,str(note500))
        entry3.insert(END,str(note200))
        entry4.insert(END,str(note100))
        entry5.insert(END,str(note50))

    button = Button(top,text = 'calculate',command = calculate,background = 'lightblue')
    button.place(x = 240,y = 80)

window.mainloop()