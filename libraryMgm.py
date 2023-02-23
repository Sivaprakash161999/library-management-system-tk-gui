from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import bgcolor
from PIL import Image
from PIL import ImageTk
from tkcalendar import *
import smtplib
import sqlite3
import time
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date

# main window
root = Tk()
root.title("Library Management System")
root.iconbitmap("aa.ico")
root.geometry("900x500+50+100")
root.resizable(0, 0)

### Database connections
#make connection for 'admin' database
db = sqlite3.connect('admin.db')
#make connection for StoreBooks database
dbstore = sqlite3.connect('StoreBooks.db')
#make connection for StudentsData database
dbstudents = sqlite3.connect('StudentsData.db')

class main:

    def cur(self):
        self.fm3 = Frame(root, bg='#fff', width=900, height=390)
        self.fm3.place(x=0, y=110)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            if int(h) >= 12 and int(m) >= 0:
                self.lb7_hr.config(text="PM")

            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)

            self.lb1_hr.after(200, clock)

        self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb1_hr.place(x=607, y=0, width=60, height=30)

        self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb3_hr.place(x=677, y=0, width=60, height=30)

        self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#581845', fg='white')
        self.lb5_hr.place(x=747, y=0, width=60, height=30)

        self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#581845', fg='white')
        self.lb7_hr.place(x=817, y=0, width=60, height=30)

        clock()

        #right side image
        self.canvas8 = Canvas(self.fm3, bg='black', width=400, height=300)
        self.canvas8.place(x=475, y=40)
        self.photo9 = PhotoImage(file="afterlogin1.png")
        self.canvas8.create_image(0, 0, image=self.photo9, anchor=NW)

        self.develop = Label(self.fm3, text='Developed By - Sivaprakash', bg='#fff', fg='#d7837f',
                                        font=('Candara', 12, 'bold'))

        self.develop.place(x=700, y=350)

        #AddButton
        self.bt1 = Button(self.fm3, text='  Add Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.addbook, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt1.place(x=40, y=40)
        self.logo = PhotoImage(file='bt1.png')
        self.bt1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1,1)
        self.bt1.config(image=self.small_logo)

        #IssueButton
        self.bt2 = Button(self.fm3, text='  Issue Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.issuebook, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt2.place(x=250, y=40)
        self.log = PhotoImage(file='bt2.png')
        self.bt2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1,1)
        self.bt2.config(image=self.small_log)

        #EditButton
        self.bt3 = Button(self.fm3, text='  Edit Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.edit, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt3.place(x=40, y=120)
        self.logb = PhotoImage(file='bt3.png')
        self.bt3.config(image=self.logb, compound=LEFT)
        self.small_logb = self.logb.subsample(1,1)
        self.bt3.config(image=self.small_logb)

        #ReturnButton
        self.bt4 = Button(self.fm3, text='  Return Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.returnbook, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt4.place(x=250, y=120)
        self.log4 = PhotoImage(file='bt4.png')
        self.bt4.config(image=self.log4, compound=LEFT)
        self.small_log4 = self.log4.subsample(1,1)
        self.bt4.config(image=self.small_log4)

        #DeleteButton
        self.bt5 = Button(self.fm3, text='  Delete Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.delete, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt5.place(x=40, y=200)
        self.log5 = PhotoImage(file='bt5.png')
        self.bt5.config(image=self.log5, compound=LEFT)
        self.small_log5 = self.log5.subsample(1,1)
        self.bt5.config(image=self.small_log5)

        #ShowButton
        self.bt6 = Button(self.fm3, text='  Show Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.show, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt6.place(x=40, y=280)
        self.log6 = PhotoImage(file='bt6.png')
        self.bt6.config(image=self.log6, compound=LEFT)
        self.small_log6 = self.log6.subsample(1,1)
        self.bt6.config(image=self.small_log6)

        #SearchButton
        self.bt7 = Button(self.fm3, text='  Search Books', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                            height=0, bd=7, relief='flat', command=self.search, cursor='hand2',
                            activebackground='black', activeforeground='#581845')
        self.bt7.place(x=250, y=200)
        self.log7 = PhotoImage(file='bt7.png')
        self.bt7.config(image=self.log7, compound=LEFT)
        self.small_log7 = self.log7.subsample(1,1)
        self.bt7.config(image=self.small_log7)

        #ExitButton
        try:
            self.bt8 = Button(self.fm3, text='  Log Out', fg='#fff', bg='#581854', font=('Candara', 15, 'bold'), width=170,
                                height=0, bd=7, relief='flat', command=self.code, cursor='hand2',
                                activebackground='black', activeforeground='#581845')
            self.bt8.place(x=250, y=280)
            self.log8 = PhotoImage(file='bt8.png')
            self.bt8.config(image=self.log8, compound=LEFT)
            self.small_log8 = self.log8.subsample(1,1)
            self.bt8.config(image=self.small_log8)
        except:
            self.bt9 = ttk.Button(self.fm3, text='Name', bg='#a40000', font=('Candara', 15, 'bold'), width=150,
                                height=0)
            self.bt9.place(x=40, y=350)
            self.log9 = PhotoImage(file='bt8.png')
            self.bt9.config(image=self.log9, compound=LEFT)
            self.small_log9 = self.log9.subsample(1,1)
            self.bt9.config(image=self.small_log9)

    def addbook(self):
        pass

    def issuebook(self):
        pass

    def edit(self):
        pass

    def returnbook(self):
        pass

    def delete(self):
        pass

    def show(self):
        pass

    def show(self):
        pass

    def search(self):
        pass

    def login(self):
        self.var1 = self.e1.get()
        self.var2 = self.e2.get()

        cursor = db.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='" + self.var1 + "' and Password='" + self.var2 + "'")
        db.commit()
        self.ab = cursor.fetchone()

        if self.ab != None:
            self.under_fm = Frame(root, height=500, width=900, bg='#fff')
            self.under_fm.place(x=0, y=0)

            self.fm2 = Frame(root, bg="#012727", height=80, width=900)
            self.fm2.place(x=0, y=0)

            self.lbb = Label(self.fm2, bg='#012727')
            self.lbb.place(x=15, y=5)
            self.ig = PhotoImage(file='library.png')
            self.lbb.config(image=self.ig)

            self.lb3 = Label(self.fm2, text='DASHBOARD', fg='White', bg='#012727', font=('times new roman', 30, 'bold'))
            self.lb3.place(x=325, y=17)

            #Name of the logged in admin
            self.name = Label(root, text="Name : ", bg='#fff', fg="black", font=("Calibri", 12, 'bold'))
            self.name.place(x=5, y=83)
            self.name1 = Label(root, text=self.ab[0], bg='#fff', fg="black", font=("Calibri", 12, 'bold'))
            self.name1.place(x=60, y=83)

            #Display Date
            self.today = date.today()
            self.dat = Label(root, text='Date : ', bg='#fff', fg='black', font=('Calibri', 12, 'bold'))
            self.dat.place(x=750, y=83)
            self.dat2 = Label(root, text=self.today, bg='#fff', fg='black', font=('Calibri', 12, 'bold'))
            self.dat2.place(x=800, y=83)

            #For Head Part
            self.cur()
        else:
            messagebox.showerror('Library System:', 'Your ID or Password is invalid!')




    def mouseClick(self, event):
        self.rog = Tk()
        self.rog.title("Change Password")
        self.rog.geometry("400x300+300+210")
        self.rog.iconbitmap("pass.ico")
        self.rog.resizable(0, 0)
        self.rog.configure(bg='#000')

        self.framerog = Frame(self.rog, width=160, height=30, bg="#d6ed17")
        self.framerog.place(x=95, y=15)

        self.label = Label(self.framerog, text="SET NEW PASSWORD", bg="#d6ed17", fg="#606060", font=('calibri', 12, 'bold'))
        self.label.place(x=5, y=4)

        #User ID
        self.user = Label(self.rog, text='User ID', bg='#000', fg='white', font=('Times New Roman', 11, 'bold'))
        self.user.place(x=40, y=95)

        #New Password
        self.user = Label(self.rog, text='New Password', bg='#000', fg='white', font=('Times New Roman', 11, 'bold'))
        self.user.place(x=40, y=170)

        self.ef1 = Entry(self.rog, width=24, font=('Calibri', 8, 'bold'), bd=4, relief='groove')
        self.ef1.place(x=170, y=95)

        self.ef2 = Entry(self.rog, width=24, font=('Calibri', 8, 'bold'), bd=4, relief='groove')
        self.ef2.place(x=170, y=170)

        #Submit Button
        self.btn1 = Button(self.rog, text='SUBMIT', fg='#606060', bg='#d6ed17', width=8, font=('Calibri', 12, 'bold'),
                    activebackground='black', activeforeground='#d6ed17', bd=3, relief='flat',
                    cursor='hand2', command=self.chan_pas)
        self.btn1.place(x=40, y=240)


    def chan_pas(self):
        self.a = self.ef1.get()
        self.b = self.ef2.get()

        # conn = sqlite3.connect('admin.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM 'UserLogin' WHERE UserID='"+self.a+"'")
        db.commit()
        self.data = cursor.fetchone()

        if self.data != None:
            cursor = db.cursor()
            cursor.execute("Update UserLogin SET PASSWORD='" + self.b + "' WHERE UserID='" + self.a + "'")
            db.commit()
            messagebox.showinfo("SUCCESSFUL", "Your Password is changed")
            self.rog.destroy()

        else:
            messagebox.showerror("ERROR", "UserID doesn't exist")
            self.rog.destroy()

        self.rog.mainloop()

    def mainclear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def code(self):
        self.fm = Frame(root, height = 500, width = 900, bg = 'white')
        self.fm.place(x = 0, y = 0)

        self.canvas = Canvas(self.fm, height = 500, width = 900, bg = '#000000')
        self.canvas.place(x = 0, y = 0)

        self.photo = ImageTk.PhotoImage(file = r"main_bg.jpg")
        self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        self.fm1 = Frame(self.canvas, height=260, width=300, bg='#000000', bd=3, relief='sunken')
        self.fm1.place(x=300, y=120)

        #UserID Label
        self.b1 = Label(self.fm1, text='User ID', bg='black', font=('Arial', 10, 'bold'), fg='white')
        self.b1.place(x=20, y=42)

        self.e1 = Entry(self.fm1, width=22, font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.e1.place(x=100, y=40)

        #Password Label
        self.lb2 = Label(self.fm1, text='Password', bg='black', font=('Arial', 10, 'bold'), fg='white')
        self.lb2.place(x = 20, y = 102)

        self.e2 = Entry(self.fm1, width=22, show='*', font=('arial', 9, 'bold'), bd=4, relief='groove')
        self.e2.place(x = 100, y = 100)

        #Login Button
        self.btn1 = Button(self.fm1, text='  Login', fg='black', bg='yellow', width=100, font=('Arial', 11, 'bold'),
                    activebackground='black', activeforeground='yellow', command=self.login, bd=3, relief='flat', cursor='hand2')
        self.btn1.place(x=25, y=160)
        self.logo = PhotoImage(file=r"login.png")
        self.btn1.config(image=self.logo, compound=LEFT)
        # self.small_logo = self.logo.subsample(1, 1)
        # self.btn1.config(image=self.small_logo)

        #Clear Button
        self.btn2=Button(self.fm1, text='  Clear', fg='black', bg='yellow', width=100, font=('Arial', 11, 'bold'),
                    activebackground='black', activeforeground='yellow', command=self.mainclear, bd=3, relief='flat', cursor='hand2')
        self.btn2.place(x=155, y=160)
        self.log = PhotoImage(file=r"clear.png")
        self.btn2.config(image=self.log, compound=LEFT)
        # self.small_log = self.log.subsample(1, 1)
        # self.btn2.config(image=self.small_log)

        #Forgot Password Clickable Label
        self.forgot = Label(self.fm1, text='Forgot Password?', fg='White', bg='#000000', activeforeground='black',
                    font=('cursive', 9, 'bold'))
        self.forgot.place(x=80, y=220)
        self.forgot.bind("<Button>", self.mouseClick)

        root.mainloop()

#object for calling the function
obj = main()
obj.code()
