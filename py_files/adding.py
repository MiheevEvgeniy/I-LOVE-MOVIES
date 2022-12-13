import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel, QVBoxLayout)
import datetime
from PyQt5.QtGui import QPalette
from ui import *


class Adding(UI):
    def __init__(self):
        self.list_t2 = None
        self.list_nums = None
        self.list_t1 = None
    def add_func(self):
        #This function is for checkbox for add button
        if self.type_adding_btn.isChecked()==True:
            txt1 = self.txt1.text()
            if txt1 == "":
                # Creating window and setting some parameters
                self.reply = QDialog()
                vbox = QVBoxLayout()
                label_dialog = QLabel()
                self.reply.setWindowTitle("I.L.M.")
                self.reply.setWindowIcon(QIcon(os.path.abspath("..\\textures\\ILF.ico")))
                palette = QPalette()
                palette.setColor(QPalette.Button, Qt.yellow)

                # Window with info about error
                label_dialog.setAutoFillBackground(True)
                label_dialog.setPalette(palette)
                label_dialog.setText('Введены некорректные данные')
                label_dialog.setAlignment(Qt.AlignCenter)

                # OK button
                button_ok = QPushButton(self.reply)
                button_ok.setText("Ок")
                button_ok.clicked.connect(self.reply.close)

                layout = QHBoxLayout()
                layout.addWidget(button_ok)
                vbox.addWidget(label_dialog)
                vbox.addSpacing(10)
                vbox.addLayout(layout)
                self.reply.setLayout(vbox)
                self.reply.exec()
                pass
        else:
            self.add_without_check(self.txt1.text(), self.txt2.currentText(),
                                   self.txt3.currentText(), self.txt4.currentText(), self.table, self.txt1)
    def add_without_check(self, txtval1, txtval2, txtval3, txtval4, table, txt1):

        # Making list from it and saving current time
        txt = (txtval1, txtval2, txtval3, txtval4)
        dt = datetime.datetime.now().replace(microsecond=0)
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=..\data\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            # Adding data in db
            cursor.execute('INSERT INTO Films VALUES (?,?,?,?,?,?)',
                           table.rowCount() + 1, txtval1, txtval2, txtval3, txtval4, dt)
            conn.commit()
            print("норм все")
            txt1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)
        # Adding new line in table
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        # Adding data in new row
        for item in txt:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1
        table.setItem(row, 4, QTableWidgetItem(str(dt)))
    def add_in_delList(self,num):
        # Checking if data was added or is not number
        try:
            equal=False
            if self.list_t1.text().isdigit()==True:
                for i in range(len(self.list_nums)):
                    if int(self.list_t1.text())==int(self.list_nums[i]):
                        equal=True
                if equal!=True:
                    self.list_t2.addItem(num)
                    self.list_nums.append(int(num))

            self.list_t1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)