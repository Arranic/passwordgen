import os, random, string
from tkinter import *


# Password generation based on ascii letters, digits, and punctuation. 
def gen_password(password_length):
    initial_chars = string.ascii_letters + string.digits + string.punctuation
    characters = []
    for char in initial_chars:
        if char not in excluded_chars.get():
            characters += char
    else:
        print('Excluded characters: ' + excluded_chars.get())
    
    # Seed the password with a random seed
    random.seed = (os.urandom(1024))
    random_str = ''.join(random.choice(characters) for _ in range(password_length))
    return random_str

# This will update the length of the password we generate based on whatever input number is entered
def update_password():
    try:
        count_chars = int(pass_len.get())
    except ValueError:
        return
    
    password_box.config(state=NORMAL)
    password_box.delete(0, 'end')
    password_box.insert(0, gen_password(count_chars))
    password_box.config(state=NORMAL)
    
mainWindow = Tk()
mainWindow.title('Griffin Password Generator 2.0')
mainWindow.resizable(0,0)

frame = Frame(mainWindow)

frame.pack(side=TOP, pady=10, padx=10, fill=X, expand=1)
Label(frame, text="Password Length: ", anchor=E).grid(row=0, column=0, sticky=E)
default_value = 16
pass_len = Entry(frame)
pass_len.insert(0, default_value)
pass_len.grid(row=0, column=1)

Label(frame, text="Excluded Characters: ", anchor=E).grid(row=1, column=0, sticky=E)
default_exclusions = ''
excluded_chars = Entry(frame)
excluded_chars.insert(0, default_exclusions)
excluded_chars.grid(row=1, column=1)

butn = Button(frame, text="Generate Password")
butn['command'] = lambda: update_password()
butn.grid(row=0, column=2, rowspan=2, padx=10, ipadx=10)

Label(frame, text="Generated Password: ", anchor=E).grid(row=2, column=0, sticky=E)
password_box = Entry(frame)
password_box.grid(row=2, column=1)

update_password()

# Open main window
mainWindow.mainloop()