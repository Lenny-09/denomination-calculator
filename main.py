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


window.mainloop()