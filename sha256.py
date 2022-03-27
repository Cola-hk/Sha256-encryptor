import hashlib
from tkinter import *
import pyperclip as balls

app = Tk()
app.title("Sha256 encryptor (auto clipboard)")
app.geometry('450x100')
app.resizable(False,False)

def encryption():
    input_string = string.get()
    print_label = Label(app,text=(hashlib.sha256(input_string.encode('utf-8')).hexdigest()),padx=30)
    hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    print_label.place(x=0,y=65)
    balls.copy(hash)

string = Entry(app)
string.pack(pady=5)

search_button = Button(app,text="Encrypt!",command=encryption)
search_button.pack(pady=5)

app.mainloop()