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
                self.reply.setWindowIcon(QIcon('C:\\Users\\User\\Desktop\\pythonProject\\textures\\ILF.ico'))
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
            self.add_without_check()
    def add_without_check(self):
        # Taking data from text lines (Name, Mark and etc)
        txtval1 = self.txt1.text()
        txtval2 = self.txt2.currentText()
        txtval3 = self.txt3.currentText()
        txtval4 = self.txt4.currentText()

        # Making list from it and saving current time
        txt = (txtval1, txtval2, txtval3, txtval4)
        dt = datetime.datetime.now().replace(microsecond=0)
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\User\Desktop\pythonProject\data\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            # Adding data in db
            cursor.execute('INSERT INTO Films VALUES (?,?,?,?,?,?)',
                           self.table.rowCount() + 1, txtval1, txtval2, txtval3, txtval4, dt)
            conn.commit()
            print("норм все")
            self.txt1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)
        # Adding new line in table
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        col = 0
        # Adding data in new row
        for item in txt:
            cell = QTableWidgetItem(str(item))
            self.table.setItem(row, col, cell)
            col += 1
        self.table.setItem(row, 4, QTableWidgetItem(str(dt)))
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