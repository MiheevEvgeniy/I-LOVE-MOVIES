import os

from PyQt5.QtWidgets import QTableWidgetItem
import pyodbc


class Creating:
    def __init__(self):
        self.table = None
    def create_table(self,table):
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'\
                         r'DBQ=..\data\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cur = conn.cursor()
            # Selecting Name column from db
            cur.execute('SELECT Name FROM Films')
            row = 0
            col = 0
            # Adding name data in table
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
                    if row > self.table.rowCount():
                        self.table.setRowCount(row)
                        cell = QTableWidgetItem(str(element))
                        self.table.setItem(row-1, col, cell)
            # Selecting Mark column from db
            cur.execute('SELECT Mark FROM Films')
            col = 1
            row = 0
            # Adding mark data in table
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            # Selecting Status column from db
            cur.execute('SELECT Status FROM Films')
            col = 2
            row = 0
            # Adding status data in table
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            # Selecting Category column from db
            cur.execute('SELECT Category FROM Films')
            col = 3
            row = 0
            # Adding category data in table
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            # Selecting Time_pole column from db
            cur.execute('SELECT Time_pole FROM Films')
            col = 4
            row = 0
            # Adding time data in table
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            conn.commit()
        except Exception as ex:
            print("не дела в создании таблицы...")
            print(ex)
        table.show()
    def create_textline(self,name,x,y,size1,size2,font_size):
        # Pattern for creating text lines
        name.resize(size1, size2)
        f = name.font()
        f.setPixelSize(font_size)
        name.setFont(f)
        name.move(x, y)
    def create_button(self,btn,x,y,size1,size2, font):
        # Just a pattern for creating buttons
        btn.setDefault(True)
        btn.resize(size1, size2)
        f = btn.font()
        f.setPixelSize(font)
        btn.setFont(f)
        btn.move(x, y)
        btn.show()