from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute(
    'CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL,password TEXT NOT NULL)')
db.commit()
db.close()


class user:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        find_user = ('SELCT * FROM user WHERE username=? and password=?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome"+self.username.get()
            self.head.configure(fg="White", bg="White",
                                font=("MV Boli", 30, "bold"))
            self.head.pack(fill=X)
            application = travel(root)
        else:
            ms.showerror('UserName is not in Database')

    def new_user(self):
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        find_user = ('SELCT * FROM user WHERE username=? and password=?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror("UserName is already taken")
        else:
            ms.showinfo('Account Created')
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [self.n_username.get(), self.n_password.get()])
        db.commit()

    def log(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()

    def crf(self):
        self.n_username.set("")
        self.n_password.set("")
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='Login Panel',
                          font=('Arial 20'), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=(
            '20'), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username,
              bd=5, font=("15")).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=(
            '20'), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password,
              bd=5, font=("15")).grid(row=1, column=1)
        Button(self.logf, text='Login', bd=1, font=("15"),
               padx=5, pady=5, command=self.login, bg="green")
        Button(self.logf, text='Create Account', bd=1, font=("15"), padx=5,
               pady=5, command=self.crf, bg="red").grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)

        Label(self.crf, text='Username: ', font=(
            '20'), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username,
              bd=5, font=("15")).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=(
            '20'), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password,
              bd=5, font=("15")).grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=1, font=("15"),
               padx=5, pady=5, command=self.new_user, bg="green")
        Button(self.crf, text='Go to Login', bd=1, font=("15"), padx=5,
               pady=5, command=self.log, bg="red").grid(row=2, column=1)
        self.crf.pack()


class travel:
    def __init__(self, root):
        self.root = root
        self.root.title("Cab Booking System")
        self.root.geometry(geometry)
        self.root.configure(background='black')
        self.root.resizable(width=False, height=False)

        DateOfOrder = StringVar()
        DateOfOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        journeyType = IntVar()
        carType = IntVar()

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        reset_counter = 0

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Mobile = StringVar()
        Telephone = StringVar()
        Email = StringVar()

        CabTax = StringVar()
        km = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        Receipt = StringVar()

        Standard = StringVar()
        FordGalaxy = StringVar()
        FordMondoe = StringVar()

        CabTax.set("0")
        km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        FordGalaxy.set("0")
        FordMondoe.set("0")

        # MainFrame
        MainFrame = Frame(self.root)
        MainFrame.pack(fill=BOTH, expand=TRUE)

        Tops = Frame(MainFrame, bd=10, bg="black", width=800, relief=RIDGE)
        Tops.pack(side=TOP, fill=BOTH)

        self.lblTitle = Label(Tops, font=('MV Boli', 30, 'bold'),
                              text='\t Cab Booking System', bg='black', fg='white', bd=10, anchor='w')
        self.lblTitle.grid()

        # Customer Frame Details
        customerDetailsFrame = LabelFrame(
            MainFrame, width=400, height=400, bg=20, pady=5, relief=RIDGE)
        customerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        FrameDetails = Frame(customerDetailsFrame, width=480,
                             height=300, bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)

        CustomerName = LabelFrame(FrameDetails, width=150, height=250, bd=10, font=(
            'arial', 12, 'bold'), text="Customer Info", relief=RIDGE)
        CustomerName.grid(row=0, column=0)

        Travel_Frame = LabelFrame(FrameDetails, bd=10, width=300, height=250, font=(
            'arial', 12, 'bold'), text="Booking Details", relief=RIDGE)
        Travel_Frame.grid(row=0, column=1)

        CostFrame = LabelFrame(FrameDetails, width=300,
                               height=150, bd=5, relief=FLAT)
        CostFrame.grid(row=1, column=1)

        # Image Frame
        Receipt_ButtonFrame = LabelFrame(
            customerDetailsFrame, bd=10, width=350, height=300, relief=SUNKEN)
        Receipt_ButtonFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        Receipt_ButtonFrame.picture = PhotoImage(
            file="./screenshots/thanku.png")
        Receipt_ButtonFrame.label = Label(
            Receipt_ButtonFrame, image=Receipt_ButtonFrame.picture)
        Receipt_ButtonFrame.label.pack()

        # Customer Information
        self.lblFirstName = Label(CustomerName, font=(
            'arial', 14, 'bold'), text="First Name", bd=7)
        self.lblFirstName.grid(row=0, column=0, sticky=W)
        self.txtFirstName = Entry(CustomerName, font=(
            'arial', 14, 'bold'), textvariable=Firstname, bd=7, insertwidth=2, justify=RIGHT)
        self.txtFirstName.grid(row=0, column=1)

        self.lblSurName = Label(CustomerName, font=(
            'arial', 14, 'bold'), text="Surname", bd=7)
        self.lblSurName.grid(row=1, column=0, sticky=W)
        self.txtSurName = Entry(CustomerName, font=(
            'arial', 14, 'bold'), textvariable=Surname, bd=7, insertwidth=2, justify=RIGHT)
        self.txtSurName.grid(row=1, column=1)

        self.lblAddress = Label(CustomerName, font=(
            'arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(CustomerName, font=(
            'arial', 14, 'bold'), textvariable=Address, bd=7, insertwidth=2, justify=RIGHT)
        self.txtAddress.grid(row=2, column=1)

        self.lblPostCode = Label(CustomerName, font=(
            'arial', 14, 'bold'), text="Post Code", bd=7)
        self.lblPostCode.grid(row=3, column=0, sticky=W)
        self.txtPostCode = Entry(CustomerName, font=(
            'arial', 14, 'bold'), textvariable=Postcode, bd=7, insertwidth=2, justify=RIGHT)
        self.txtPostCode.grid(row=3, column=1)

        self.lblMobile = Label(CustomerName, font=(
            'arial', 14, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=4, column=0, sticky=W)
        self.txtMobile = Entry(CustomerName, font=(
            'arial', 14, 'bold'), textvariable=Mobile, bd=7, insertwidth=2, justify=RIGHT)
        self.txtMobile.grid(row=4, column=1)

        self.lblEmail = Label(CustomerName, font=(
            'arial', 14, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=5, column=0, sticky=W)
        self.txtEmail = Entry(CustomerName, font=(
            'arial', 14, 'bold'), textvariable=Email, bd=7, insertwidth=2, justify=RIGHT)
        self.txtEmail.grid(row=5, column=1)

        # CabInfo
        self.lblpickup = Label(Travel_Frame, font=(
            'arial', 14, 'bold'), text='Pickup', bd=7)
        self.lblpickup.grid(row=0, column=0, sticky=W)

        self.cboPickup = ttk.Combobox(
            Travel_Frame, textvariable=var1, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboPickup['value']=('','Arcade Lane','The Fort','Cinema','Railway Station')
        self.cboPickup.current(0)


if __name__ == '__main__':
    root = Tk()
    w = 1150
    h = 650
    geometry = "%dx%d+%d+%d" % (w, h, 50, 0)
    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()
