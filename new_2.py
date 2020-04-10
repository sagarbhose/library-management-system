import sqlite3

conn = sqlite3.connect('record.db')
cursor = conn.cursor()


class admingui:
    def first(self):
        import Tkinter
        first = Tkinter.Tk()
        frame5=Frame(first)
        self.name_reg = Tkinter.Label(frame5, text="Enter your name", fg='black', font=font2)
        self.name_reg.grid(row=0, column=4, )
        self.name_reg_var = Tkinter.Entry(frame5)
        self.name_reg_var.grid(row=0, column=5)

        self.address_reg = Tkinter.Label(frame5, text="Enter your adderss", fg='black', font=font2)
        self.address_reg.grid(row=1, column=4)
        self.address_reg_var = Tkinter.Entry(frame5)
        self.address_reg_var.grid(row=1, column=5)

        self.phone_reg = Tkinter.Label(frame5, text="Enter your phone", fg='black', font=font2)
        self.phone_reg.grid(row=2, column=4)
        self.phone_reg_var = Tkinter.Entry(frame5)
        self.phone_reg_var.grid(row=2, column=5)

        self.age_reg = Tkinter.Label(frame5, text="Enter your age", fg='black', font=font2)
        self.age_reg.grid(row=3, column=4)
        self.age_reg_var = Tkinter.Entry(frame5)
        self.age_reg_var.grid(row=3, column=5)

        self.var_mobile = Tkinter.Label(frame5, text="Enter your mobile", fg='black', font=font2)
        self.var_mobile.grid(row=4, column=4)
        self.var_mobile = Tkinter.Entry(frame5)
        self.var_mobile.grid(row=4, column=5)

        self.username_reg = Tkinter.Label(frame5, text="Enter your username", fg='black', font=font2)
        self.username_reg.grid(row=5, column=4, )
        self.username_reg_var = Tkinter.Entry(frame5)
        self.username_reg_var.grid(row=5, column=5)

        self.password_reg = Tkinter.Label(frame5, text="Enter your password", fg='black', font=font2)
        self.password_reg.grid(row=6, column=4)
        self.password_reg_var = Tkinter.Entry(frame5)
        self.password_reg_var.grid(row=6, column=5)

        submit1 = Tkinter.Button(frame5, text="SUBMIT", command=self.recordinfo1,bd=5)
        submit1.grid()
        frame5.grid()
        exit=Button(frame5,text="EXIT",command=first.destroy,bd=5)
        exit.grid(row=7,column=8)
        first.geometry("1600x1000")
        first.mainloop()


    def recordinfo1(self):
        self.name = self.name_reg_var.get()
        self.address = self.address_reg_var.get()
        self.age = self.age_reg_var.get()
        self.mobile = self.var_mobile.get()
        self.username = self.username_reg_var.get()
        self.password = self.password_reg_var.get()
        import sqlite3
        conn = sqlite3.connect('text.db')
        cursor = conn.cursor()
        check = 'SELECT count(name) FROM sqlite_master WHERE type="table" AND name="INFODATA"'
        cursor.execute(check)
        if cursor.fetchone()[0] == 1:
            insert = "INSERT INTO INFODATA(NAME,ADDRESS,AGE,MOBILE,USERNAME,PASSWORD) VALUES(?,?,?,?,?,?);"
            cursor.execute(insert, (self.name, self.address, self.age, self.mobile, self.username, self.password))
            conn.commit()
            import tkMessageBox
            s=tkMessageBox.askokcancel("RECORDED","DATA RECORDED SUCESSFULLY")




        else:
            table = "CREATE TABLE INFODATA(NAME TEXT,ADDRESS TEXT,AGE INT,MOBILE INT,USERNAME TEXT,PASSWORD TEXT)"
            cursor.execute(table)
            import tkMessageBox
            s1 = tkMessageBox.askokcancel("NOT RECORDED", "PLZ DO IT AGAIN")


    def recordissu(self):
        cursor = conn.cursor()
        check = 'SELECT count(name) FROM sqlite_master WHERE type="table" AND name="RECORDS"'
        cursor.execute(check)
        if cursor.fetchone()[0] == 1:
            self.bookname = self.bookname_issu.get()
            self.studentid = self.studentid_issu.get()
            import datetime
            today = datetime.date.today()
            finaldate = datetime.datetime.now().date() + datetime.timedelta(days=1)
            insert = "INSERT INTO RECORDS(ID,bookname,today,finaldate) VALUES(?,?,?,?);"
            cursor.execute(insert, (self.studentid, self.bookname, today, finaldate))
            conn.commit()
            import tkMessageBox
            q=tkMessageBox.askokcancel("CONGRAGULATION","BOOK ISSUED SUCESSFULLY")
        else:
            create = " CREATE TABLE RECORDS(ID PRIMARYKEY ,bookname VARCHAR,today VARCHAR,finaldate VARCHAR)"
            cursor.execute(create)
            import  tkMessageBox
            q1=tkMessageBox.askokcancel("ERROR","PLEASE TRY AGAIN")

    def second(self):
        import Tkinter
        second = Tkinter.Tk()
        frame6=Frame(second)
        frame6.grid()
        self.l0 = Tkinter.Label(frame6, text="*****WELCOME PLZ FILLED DETAILED*****")
        self.l0.grid(row=0, column=2)

        self.l1 = Tkinter.Label(frame6, text="ENTER BOOK NAME")
        self.l1.grid(row=1, column=1)
        self.bookname_issu = Tkinter.Entry(frame6)
        self.bookname_issu.grid(row=1, column=2)

        self.l3 = Tkinter.Label(frame6, text="ENTER STUDENT ID")
        self.l3.grid(row=3, column=1)
        self.studentid_issu = Tkinter.Entry(frame6)
        self.studentid_issu.grid(row=3, column=2)

        submit2 = Tkinter.Button(frame6, text="SUBMIT", command=self.recordissu,bd=5)
        submit2.grid(row=7, column=5)
        exit = Button(frame6, text="EXIT", command=second.destroy, bd=5)
        exit.grid(row=7, column=8)
        second.geometry("1600x1000")
        second.mainloop()

    def checking(self):
        self.new_ID = self.id_issu.get()
        verify = 'SELECT * FROM RECORDS WHERE ID=?'
        cursor.execute(verify, [(self.new_ID)])
        reslut = []
        reslut = cursor.fetchone()
        a = reslut[2]
        import datetime
        c = datetime.datetime.now().date()
        z = str(c)
        for i in reslut:
            print(i)
        if (z > a):
            import tkMessageBox
            z=tkMessageBox.askokcancel("RENEVAL","PLEASE RENEW YOUR BOOK SIR")
        else:
            import tkMessageBox
            z1=tkMessageBox.askokcancel("SERVICE","ENJOY YOUR BOOK SIR")


    def third(self):
        import Tkinter
        third = Tkinter.Tk()
        frame7=Frame(third)
        frame7.grid()
        self.l0 = Tkinter.Label(frame7, text="*****WELCOME PLZ FILLED DETAILED*****")
        self.l0.grid(row=0, column=2)
        self.l2 = Tkinter.Label(frame7, text="ENTER BOOK id")
        self.l2.grid(row=2, column=1)
        self.id_issu = Tkinter.Entry(frame7)
        self.id_issu.grid(row=2, column=2)
        submit3 = Tkinter.Button(frame7, text="SUBMIT", command=self.checking,bd=5)
        submit3.grid(row=7, column=5)
        exit = Button(frame7, text="EXIT", command=third.destroy, bd=5)
        exit.grid(row=7, column=8)
        third.geometry("1600x1000")
        third.mainloop()

    def four(self):
        import Tkinter
        win3 = Tkinter.Tk()
        self.l0 = Tkinter.Label(win3, text="*****WELCOME PLZ FILLED DETAILED*****")
        self.l0.grid(row=0, column=2)

        self.l1 = Tkinter.Label(win3, text="ENTER BOOK NAME")
        self.l1.grid(row=1, column=1)
        self.bookname_issu = Tkinter.Entry(win3)
        self.bookname_issu.grid(row=1, column=2)

        self.l2 = Tkinter.Label(win3, text="ENTER BOOK id")
        self.l2.grid(row=2, column=1)
        self.id_issu = Tkinter.Entry(win3)
        self.id_issu.grid(row=2, column=2)

        self.l3 = Tkinter.Label(win3, text="ENTER STUDENT ID")
        self.l3.grid(row=3, column=1)
        self.studentid_issu = Tkinter.Entry(win3)
        self.studentid_issu.grid(row=3, column=2)
        win.mainloop()
class my:
    def adminlogin(self):
        import Tkinter
        self.winq = Tk()
        frame3 = Frame(self.winq)
        frame3.pack()
        A1 = Tkinter.Label(frame3, text="ENTER USERNAME", font=font2)
        A1.grid()
        self.inp_username1 = Tkinter.Entry(frame3)
        self.inp_username1.grid(row=0, column=1)
        A2 = Tkinter.Label(frame3, text="ENTER PASSWORD", font=font2)
        A2.grid()
        self.inp_password = Tkinter.Entry(frame3)
        self.inp_password.grid(row=1, column=1)
        btnn1 = Tkinter.Button(frame3, text="submit", bg="white", command=self.assign, bd=5)
        btnn1.grid(row=2, column=1)
        self.winq.geometry("1600x1000")

    def assign(self):
        self.user1 = self.inp_username1.get()
        self.pass1 = self.inp_password.get()
        self.verify()

    def verify(self):
        import Tkinter
        import tkMessageBox
        if self.user1 == "admin" and self.pass1 == "password":
            self.adminmainframework()

        else:
            l_1 = tkMessageBox.askokcancel("invalid username or password", "plz enter valid username or password")
            if l_1 == "true":
                self.winq.destroy()

    def adminmainframework(self):
        import Tkinter
        calladmin = admingui()
        self.winq.destroy()
        root = Tkinter.Tk()
        frame4 = Frame(root)
        frame4.pack(side=TOP)
        lab1 = Tkinter.Button(frame4, text="1.REGISTER A NEW STUDENT", command=calladmin.first, font=font2)
        lab1.grid(row=0, column=0)
        lab2 = Tkinter.Button(frame4, text="2.ISSUING NEW BOOK", command=calladmin.second, font=font2)
        lab2.grid(row=2, column=0)
        lab3 = Tkinter.Button(frame4, text="3.CHECKING ISSUED BOOK STATUS", command=calladmin.third, font=font2)
        lab3.grid(row=3, column=0)
        lab4 = Tkinter.Button(frame4, text="4.RESSUING BOOK", command=calladmin.four, font=font2)
        lab4.grid(row=4, column=0)
        exit1 = Button(frame4, text="EXIT", command=root.destroy, bd=5)
        exit1.grid()
        root.geometry("1600x1000")
        root.mainloop()


from Tkinter import *
from tkFont import Font

callmy = my()
calladmin = admingui()
win = Tk()
frame1 = Frame(win)
frame2 = Frame(win)
frame2.pack()
font1 = Font(family="Times New Roman", size=39, weight="bold", slant="italic", underline=1)
font2 = Font(family="Nakula", size=16, weight="bold")
frame1.pack()
mainlabel = Label(frame2, text="WELCOME TO LIBRARY MANAGEMENT SYSTEM", font=font1)
mainlabel.pack()
l1 = Label(frame1, text="1.ADMIN", fg="black", bg="yellow", font=font2)
l1.grid(row=0, column=0)
btn1 = Button(frame1, text="ENTER", bg="white", command=callmy.adminlogin, bd=5)
btn1.grid(row=0, column=1)
l2 = Label(frame1, text="2.LIBRARAIN", fg="black", bg="yellow", font=font2)
l2.grid(row=1, column=0)
btn2 = Button(frame1, text="ENTER", bg="white", bd=5)
btn2.grid(row=1, column=1)
win.geometry("1600x1000")
win.mainloop()
