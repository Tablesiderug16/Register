Introduction:
This is a Python script for a simple registration form using Tkinter and SQLite3. 
The registration form collects user information such as name, email, phone, date of birth, and password. 
The user’s information is then stored in a SQLite3 database. Which can be extracted when the login function is in use if data has already been stored.

Dependencies:
Python 3.x
Tkinter module
sqlite3 module
datetime module


Instructions for Use:
Run the Python script in a Python environment or IDE. (virtual stuido) 
The user is required to input their name, email, phone, date of birth, and password in the respective fields.
The user must check the “I agree to the Terms & Conditions” checkbox before submitting their information.
Click the “Register” button to submit the user’s information to the database.
A message box will appear to indicate successful registration or errors.
If the user has an existing account, they can click on the “Have an account? Login!” button to go to the login page.


Note:
Make sure that the background.png, openeye.png, and closedeye.png files are stored in the correct location (C:/Users/user/Documents/filename) as specified in the script.
The script checks whether the email address already exists in the database before inserting a new record.
The age of the user is calculated based on the date of birth entered by the user.
