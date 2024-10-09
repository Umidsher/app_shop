from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Sign in")

def registration():
    text = Label(text="Sign up to entry to the system!")
    text_log = Label(text="Login:")
    register_lodin = Entry()
    text_password1 = Label(text='Password:')
    register_password1 = Entry(show='*')
    text_password2 = Label(text='Confirm:')
    register_password2 = Entry(show='*')
    button_register = Button(text="Sign up!", command=lambda: save())
    text.pack()
    text_log.pack()
    register_lodin.pack()
    text_password1.pack()
    register_password1.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()

    def save():
        login_pass_save = {}
        login_pass_save[register_lodin.get()]=register_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text="Congratulations! You have signed up succesfully!")
    text_enter_login = Label(text="Login:")
    enter_login = Entry()
    text_enter_password = Label(text='Password:')
    enter_password = Entry(show='*')
    button_enter = Button(text="Sign in", command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Succesfully logged in!","Salomaat!")
            else:
                messagebox.showerror('UPS!', "Login or password was wrong!")

        else:
            messagebox.showerror('UPS!', "Login was wrong!")

registration()



root.mainloop()