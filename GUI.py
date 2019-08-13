import Tkinter as Tk

class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.pack(expand=1, fill=Tk.BOTH, anchor=Tk.NW)
        self.create_widgets()

    def create_widgets(self):
        self.label = Tk.Label(self, text='INPUT file')
        self.entry = Tk.Entry(self, width=40)
        self.button = Tk.Button(self, text='Open')
        self.check = Tk.Checkbutton(self, text='test')
        self.text = Tk.Text(self)

        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.button.grid(column=2, row=0)
        self.check.grid(column=0, row=1)
        self.text.grid(column=0, columnspan=3, row=2)

root = Tk.Tk()
app = Application(master=root)
app.mainloop()