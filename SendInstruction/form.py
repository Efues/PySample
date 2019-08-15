# -*- coding: utf-8 -*-
import os
import codecs
import Tkinter
import datetime
import sqlite3
from contextlib import closing

class Form():
    def __init__(self, conf):
        self.conf = conf

        self.root = Tkinter.Tk()
        self.root.title('Parts Order to 106')
        self.root.geometry("400x200")
#        self.root.attributes("-fullscreen", True)
        self.setup_controllers()

    def setup_controllers(self):
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
        entry_ftp_host.insert(Tkinter.END, self.conf.server)
        entry_ftp_host.configure(state='readonly')

        label_ftp_user = Tkinter.Label(ftp_frame,text='User')
        label_ftp_user.grid(row=1, column=0)

        entry_ftp_user = Tkinter.Entry(ftp_frame)
        entry_ftp_user.insert(Tkinter.END, self.conf.user)
        entry_ftp_user.grid(row=1, column=1)
        entry_ftp_user.configure(state='readonly')

        label_ftp_pass = Tkinter.Label(ftp_frame,text='Pass')
        label_ftp_pass.grid(row=2, column=0)

        entry_ftp_pass = Tkinter.Entry(ftp_frame)
        entry_ftp_pass.insert(Tkinter.END, self.conf.passwd)
        entry_ftp_pass.grid(row=2, column=1)
        entry_ftp_pass.configure(state='readonly')

        # Folder/File in server
        label_server_output = Tkinter.Label(server_frame,text='Output folder')
        label_server_output.grid(row=0, column=0)

        entry_server_output = Tkinter.Entry(server_frame)
        entry_server_output.insert(Tkinter.END, self.conf.output_folder)
        entry_server_output.grid(row=0, column=1)
        entry_server_output.configure(state='readonly')

        label_server_db_file = Tkinter.Label(server_frame,text='DB File')
        label_server_db_file.grid(row=1, column=0)

        entry_server_db_file = Tkinter.Entry(server_frame)
        entry_server_db_file.insert(Tkinter.END, self.conf.db_file)
        entry_server_db_file.grid(row=1, column=1)
        entry_server_db_file.configure(state='readonly')

        # Status Text
        self.text_status = Tkinter.Text(frame_text, width=20, height=9)
        self.text_status.grid(row=0, column=0,columnspan=2,padx=5, pady=5)
        self.index=0

        # serial device
        self.serial=None

        # Test Button
        button_test = Tkinter.Button(frame_text,text='Test',command=self.button_test_clicked)
        button_test.grid(row=1, column=0,padx=5, pady=5)

        # close Button
        button_close = Tkinter.Button(frame_text, text='Close', command=self.button_close_clicked)
        button_close.grid(row=1, column=1,padx=5, pady=5)

    def button_test_clicked(self):
#        self.main('JAMA501195000001021100021041011102112071210412406127041410214201144061520440205515015160151908520045210652606523105220640102200596622620000000001wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww001')
#        self.main('JAMA501195000001021100021041011102112071210412406127041410214201144061520440205515015160151908520045210652606523105220640102201107270140000000001wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww001')
        self.main('JAMA501195000001021100021041011102112071210412406127041410214201144061520440205515015160151908520045210652606523105220640102201107270140000000001wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww002')

    def run(self):
        self.root.after(100, self.loop)
        self.root.mainloop()

    def button_close_clicked(self):
        self.root.quit()

    def append_status(self, text):
        self.index = 1 + self.index
        self.text_status.insert("1.0", str(self.index) + ':' + text + '\n')

    def loop(self):
        if self.serial is not None:
            line = self.serial.readline()
            if line != "":
                self.main(line)

        # repeat again in 0.1 second
        self.root.after(100, self.loop)

    def main(self, qrline):
        item_no = None
        try:
            print('In main...')
            print(qrline)

            # todo check DB File and Output folder existance

            # Get PartsNoFrom SQLien
            item_no_and_seller_id = self.parse_qrline(qrline);
            item_no = item_no_and_seller_id[0]
            print(item_no_and_seller_id)

            # Get record from DB
            record = self.select(item_no_and_seller_id);
            print(record)

            # Write to file
            file_path = self.write_file(record);

            # Send file


            # Delete file
#            os.remove(file_path)

        except Exception as e:
            self.append_status('Failed:'+  item_no)
            print(e.message)

    def parse_qrline(self, qrline):
        qr_pre_fix = "JAMA50119500000102110002104101110211207121041240612704141021420114406152044020551501516015190852004521065260652310522064010220"
        qr_digit_count=221
        item_no_count=10
        seller_id_count=3

        if len(qrline) is not qr_digit_count:
            raise Exception('invalid qr : digit count is' + len(qrline))
        if(qrline.find(qr_pre_fix) is not 0):
            raise Exception('invalid qr : prefix error')

        item_no = qrline[len(qr_pre_fix):len(qr_pre_fix)+item_no_count]
        seller_id = qrline[qr_digit_count - seller_id_count:qr_digit_count]

        # check if string is numerical value
        item_no_tmp = int(item_no)
        seller_id_tmp = int(seller_id)

        # change format to item no in DB
        item_no = item_no[0:6] + "-" + item_no[6:item_no_count]
        return [item_no, seller_id_tmp]

    def select(self, item_no_and_seller_id):
        with closing(sqlite3.connect(self.conf.local_db_file_path)) as conn:
            c = conn.cursor()
            select_sql = 'select * from items'
            for row in c.execute(select_sql):
                if( row[0] == item_no_and_seller_id[0] and row[5] is None):
                    return row
                if( row[0] == item_no_and_seller_id[0] and row[5] == item_no_and_seller_id[1]):
                    return row
        raise Exception('cannot find in DB')

    def write_file(self, record):
        now = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        item_no = record[0]
        item_no = item_no[0:len(item_no)]
        item_no_without_minus = item_no.replace('-', '')
        item_name = record[1]
        quantity = int(record[2]) * int(record[3])
        location = record[4]
        seller_name = record[6]
        file_name = now + '_User_BHT_Pa_----_br_br_br_' + item_no_without_minus + '-_'+str(quantity) + '_Yet_0_Instruction.csv'
        content = item_no + '*,1,' + location + ',[' + item_name + '],1,' + str(quantity) + u',[ﾊﾟﾚｯﾄ],Yet,0,'
        if (seller_name is not None):
            content = item_no + '*,1,' + location + ',[' + item_name + '(' + seller_name + ')],1,' + str(quantity) + u',[ﾊﾟﾚｯﾄ],Yet,0,'
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write(content)
        return file_name
