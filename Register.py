from tkinter import *
import sqlite3
import datetime
from tkinter import Tk, Label, PhotoImage
from tkinter import messagebox

window=Tk()
window.title("Registration Form")
window.geometry('720x550')
window.configure(bg='#333333')
window.resizable(False,False)
bg_image = PhotoImage(file="C:/Users/deanw/Documents/Register/background.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

import datetime
import sqlite3
from tkinter import messagebox

def passwordshow():
    openeye.config(file='C:/Users/deanw/Documents/Register/openeye.png')
    PasswordEntry.config(show='')
    eyeButton.config(command=passwordhide)

def passwordhide():
    openeye.config(file='C:/Users/deanw/Documents/Register/closedeye.png')
    PasswordEntry.config(show='*')
    eyeButton.config(command=passwordshow)

def login_page():
    window.destroy()
    import Login

def register():
    name_info = NameValue.get()
    email_info = EmailValue.get()
    phone_info = str(PhoneValue.get())
    dob_info = str(DOBValue.get())
    password_info = PasswordValue.get()
    
    if email_info=='' or name_info=='' or password_info=='' or dob_info=='' or phone_info=='':
        messagebox.showerror('Error!', 'all fields are required!')
    else:
        if checkValue.get() == 0:
            messagebox.showerror('Error!', 'Please agree to terms and conditions!')
        elif checkValue.get() == 1:
            # Check if the email already exists in the database
            if email_exists(email_info):
                messagebox.showerror('Error!', 'Email address already exists!')
            else:
                # Calculate the age from the date of birth
                if dob_info:
                    dob_year = int(dob_info[-4:])
                else:
                    dob_year = 0

                if dob_year:
                    current_year = datetime.datetime.now().year
                    age = current_year - dob_year
                else:
                    age = 0

                # Insert the user's information into the database
                conn = sqlite3.connect('register.db')
                cursor = conn.cursor()
                query = "INSERT INTO Register (name, email, phone, age, password) VALUES (?, ?, ?, ?, ?)"
                values = (name_info, email_info, phone_info, age, password_info)
                cursor.execute(query, values)
                conn.commit()
                conn.close()

                # Show a message box to indicate successful registration
                messagebox.showinfo('Registered!', 'Registration completed successfully!')

def email_exists(email):
    conn = sqlite3.connect('register.db')
    cursor = conn.cursor()
    query = "SELECT * FROM Register WHERE email = ?"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    conn.close()
    # If a result is returned, the email exists
    if result:
        return True
    else:
        return False

        conn.commit()
        conn.close()


Label(window,text="Registration Form", font="arial 25").pack(pady=50)
Label(window, text="Full Name",font=23).place(x=100, y=150)
Label(window, text="Email",font=23).place(x=100, y=200)
Label(window,text="Phone",font=23).place(x=100, y=250)
Label(window,text="Date Of Birth",font=23).place(x=100, y=300)
Label(window,text="Password",font=23).place(x=100, y=350)

#entery = databse
NameValue=StringVar()
EmailValue=StringVar()
PhoneValue=StringVar()
DOBValue=StringVar()
PasswordValue=StringVar()


nameEntry=Entry(window,textvariable=NameValue,width=30,bd=2,font=20)
emailEntry=Entry(window,textvariable=EmailValue,width=30,bd=2,font=20)
phoneEntry=Entry(window,textvariable=PhoneValue,width=30,bd=2,font=20)
dobValueEntry=Entry(window,textvariable=DOBValue,width=30,bd=2,font=20)
PasswordEntry=Entry(window,show='*',textvariable=PasswordValue,width=30,bd=2,font=20)
openeye=PhotoImage(file="C:/Users/deanw/Documents/Register/closedeye.png")
eyeButton=Button(window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=passwordshow)
eyeButton.place(x=480, y=350)


nameEntry.place(x=200, y=150)
emailEntry.place(x=200, y=200)
phoneEntry.place(x=200, y=250)
dobValueEntry.place(x=200, y=300)
PasswordEntry.place(x=200, y=350)

#Check button for if I want one?
checkValue=IntVar()
checkbtn=Checkbutton(text="I agree to the Terms & Conditions", variable=checkValue)
checkbtn.place(x=200, y=480)

#If they have made an account it will send them to the login area.
alreadyaccount=Entry(window, text="Login", font=('Open Sans', '9', 'bold'), bg='white')
alreadyaccount = Button(window, text="Have an account? Login!", font=('Open Sans', '9', 'bold'), bg='white', command=login_page)
alreadyaccount.place(x=200, y=450)

Button(text="Register", font=20, width=11, height=2, command=register).place(x=200, y=390)



window.mainloop()