import tkinter
from tkinter import messagebox
import sqlite3
from tkinter import ttk

window=tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')
window.resizable(False,False)

def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    else:
        try:
            conn = sqlite3.connect('register.db')
            cursor = conn.cursor()
        except:
            messagebox.showerror('Error!', 'Connection not established!')
            return
        query = 'SELECT * FROM Register WHERE email=? AND password=?'
        cursor.execute(query, (username_entry.get(), password_entry.get()))
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error!', 'Invalid username or password')
        else:
            messagebox.showinfo('Success', 'Login successful!')



def Create_account():
    window.destroy()
    import Register


frame = tkinter.Label()

login_label=tkinter.Label(frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 30,))
username_Label=tkinter.Label(frame, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry=tkinter.Entry(frame, font=("Arial, 16"))
password_entry=tkinter.Entry(frame, show="*", font=("Arial, 16"))
password_label=tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button=tkinter.Button(frame, text="Login", bg='#FF3399', fg="#FFFFFF", font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news")
username_Label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=5)
login_button.grid(row=3, column=0, columnspan=2)

alreadyaccount=tkinter.Label(frame, text="Dont have an account?", font=('Open Sans', '9', 'bold'), bg='white')
alreadyaccount = tkinter.Button(frame, text="Dont have an account?", font=('Open Sans', '9', 'bold'), bg='white', command=Create_account)
alreadyaccount.grid(row=11, column=0, columnspan=2)
frame.pack()

#Check button for if I want one?
# checkValue=IntVar
# checkbtn=Checkbutton(text="Remeber Me?", variable=checkValue)
# checkbtn.place(x=200, y=350)


window.mainloop()
 
