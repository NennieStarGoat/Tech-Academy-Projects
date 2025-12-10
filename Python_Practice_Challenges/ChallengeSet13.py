import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgray')

        self.fname = StringVar()
        self.lname = StringVar()

        self.lblfname = Label(self.master, text='First Name', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lbllname = Label(self.master, text='Last Name', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lbldisplay = Label(self.master, text='', font=('Helvetica', 16), fg='black', bg='lightgray')

        self.txtfname = Entry(self.master, text=self.fname, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtlname = Entry(self.master, text=self.lname, font=('Helvetica', 16), fg='black', bg='lightblue')

        self.lblfname.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))
        self.lbllname.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))
        self.lbldisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))
        self.txtfname.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))
        self.txtlname.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))

        self.btnsubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnsubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        self.btncancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btncancel.grid(row=2, column=1, padx=(0, 90), pady=(30, 0), sticky=NE)

    def submit(self):
        fname = self.fname.get()
        lname = self.lname.get()
        self.lbldisplay.config(text='Hello {} {}!'.format(fname, lname))


    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
