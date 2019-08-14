import Tkinter


class Form():
    def __init__(self, conf):
        self.root = Tkinter.Tk()
        self.root.title('Parts Order to 106')
        self.root.geometry("400x200")

        # Frames
        frame_config = Tkinter.LabelFrame(self.root, text="Config")
        frame_config.grid(row=0, column=0, padx=5, pady=5, sticky=Tkinter.N)

        frame_text = Tkinter.LabelFrame(self.root, text="Status")
        frame_text.grid(row=0, column=1, padx=5, pady=5, sticky=Tkinter.NW)

        ftp_frame = Tkinter.LabelFrame(frame_config, text="ftp")
        ftp_frame.pack(fill=Tkinter.X , padx=5, pady=5)

        server_frame = Tkinter.LabelFrame(frame_config, text="Server")
        server_frame.pack(fill=Tkinter.X, padx=5, pady=5)

        # FTP Config
        label_ftp_host = Tkinter.Label(ftp_frame,text='Host')
        label_ftp_host.grid(row=0, column=0)

        entry_ftp_host = Tkinter.Entry(ftp_frame)
        entry_ftp_host.grid(row=0, column=1)
        entry_ftp_host.insert(Tkinter.END, conf.server)
        entry_ftp_host.configure(state='readonly')

        label_ftp_user = Tkinter.Label(ftp_frame,text='User')
        label_ftp_user.grid(row=1, column=0)

        entry_ftp_user = Tkinter.Entry(ftp_frame)
        entry_ftp_user.insert(Tkinter.END, conf.user)
        entry_ftp_user.grid(row=1, column=1)
        entry_ftp_user.configure(state='readonly')

        label_ftp_pass = Tkinter.Label(ftp_frame,text='Pass')
        label_ftp_pass.grid(row=2, column=0)

        entry_ftp_pass = Tkinter.Entry(ftp_frame)
        entry_ftp_pass.insert(Tkinter.END, conf.passwd)
        entry_ftp_pass.grid(row=2, column=1)
        entry_ftp_pass.configure(state='readonly')

        # Folder/File in server
        label_server_output = Tkinter.Label(server_frame,text='Output folder')
        label_server_output.grid(row=0, column=0)

        entry_server_output = Tkinter.Entry(server_frame)
        entry_server_output.insert(Tkinter.END, conf.output_folder)
        entry_server_output.grid(row=0, column=1)
        entry_server_output.configure(state='readonly')

        label_server_db_file = Tkinter.Label(server_frame,text='DB File')
        label_server_db_file.grid(row=1, column=0)

        entry_server_db_file = Tkinter.Entry(server_frame)
        entry_server_db_file.insert(Tkinter.END, conf.db_file)
        entry_server_db_file.grid(row=1, column=1)
        entry_server_db_file.configure(state='readonly')

        # Status Text
        self.text_status = Tkinter.Text(frame_text, width=20, height=10)
        self.text_status.pack(padx=5, pady=5)

        self.index=0

        # Test Button
        button_test = Tkinter.Button(frame_text,text='Test',command=self.button_test_clicked)
        button_test.pack(padx=5, pady=5)

    def button_test_clicked(self):
        self.text_status.insert("1.0", 'Button Clicked!\n')

    def do_mainloop(self):
        self.root.mainloop()

    def append_status(self, text):
        self.index = 1 + self.index
        self.text_status.insert("1.0", str(self.index) + ':' + text + '\n')
