import time
from ui import *


class Deleting(UI):
    def __init__(self):
        self.list_nums = None
    def delete(self,txtval):
        # This function deleting data from db
        try:
            # Loading db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=..\data\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            # Taking count of rows and deleting data from text line
            row = self.table.rowCount()-1
            txtchange=int(txtval)
            # Deleting from db
            cursor.execute('DELETE FROM Films WHERE id = ?', txtval)
            # Repairing numbering
            for i in range(txtchange+1,row+3):
                cursor.execute('UPDATE Films SET id = ? WHERE id = ?', (txtchange-1, txtchange))
                txtchange+=1
            conn.commit()
            print("норм все")
            # Deleting data from table
            try:
                for i in range(101):
                    # Slowing down the loop
                    time.sleep(0.005)
                    # Setting value to progress bar
                    self.pbar.setValue(i)
                # Remove row from table and clearing progress bar
                self.pbar.setValue(0)
                self.table.removeRow(int(txtval) - 1)
            except Exception as ex:
                print("не дела...")
                print(ex)
        except Exception as ex:
            print("не дела...")
            print(ex)
    def list(self):
        try:
            # deleting one by one func
            change=0
            self.list_nums.sort()
            for i in range(len(self.list_nums)):
                self.delete(self.list_nums[i]-change)
                change+=1
        except Exception as ex:
            print("не дела...")
            print(ex)
    def range(self, start, end):
        try:
            # Deleting range func
            for i in range(int(start), int(end)+1):
                self.delete(start)
                time.sleep(0.005)
        except Exception as ex:
            print("не дела...")
            print(ex)