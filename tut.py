import time
import datetime
import sys
import configparser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel, QLineEdit, QProgressBar,
                             QPushButton, QVBoxLayout, QAction,
                             QTableWidget, QTableWidgetItem,
                             QMainWindow, QApplication, QComboBox,
                             QListWidget,QGroupBox, QCheckBox,
                             QMessageBox)
import pyodbc
from PyQt5.QtWidgets import qApp
from PyQt5.QtGui import QIcon, QPalette
import tkinter

class Creating():
    def __init__(self):
        self.table = None
    def create_table(self,table):
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\User\Desktop\pythonProject\ILF.accdb;'
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
            print("не дела...")
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
class UI(object):
    def init_UI(self, MW):
        # Main window
        self.cr = Creating()
        root = tkinter.Tk()


        self.WIDTH = root.winfo_screenwidth() - 240
        self.HEIGHT = root.winfo_screenheight() - 200
        self.center_w = root.winfo_reqwidth()
        self.center_h = root.winfo_reqheight()
        MW.setGeometry(self.center_w - 100, self.center_h - 100, self.WIDTH, self.HEIGHT)
        MW.setWindowTitle("I.L.M. - I LOVE MOVIES v0.3")
        MW.setWindowIcon(QIcon('ILF.ico'))
        MW.setFixedSize(self.WIDTH, self.HEIGHT)

        # Main lines (Name, Mark, Status, Category)
        # Name
        self.txt1 = QLineEdit(self)
        self.cr.create_textline(self.txt1, 20, 30, 200, 30, 16)
        # Mark
        self.txt2 = QComboBox(MW)
        for num in range(100, 6, -5):
            if num % 10 == 5:
                num = num / 10
            else:
                num = int(num / 10)
            self.txt2.addItem(str(num))
        self.cr.create_textline(self.txt2, 20, 65, 200, 30, 16)

        # Status
        self.txt3 = QComboBox(MW)
        self.cr.create_textline(self.txt3, 20, 100, 200, 30, 16)

        # Category
        self.txt4 = QComboBox(MW)
        self.cr.create_textline(self.txt4, 20, 135, 200, 30, 16)

        # Range deleting group
        self.groupbox = QGroupBox(MW)
        self.groupbox.setCheckable(True)
        self.groupbox.move(830, 30)
        self.groupbox.autoFillBackground()
        Ran_m1 = '''
                                         QGroupBox {
                                             background-color: white;
                                             spacing: 5px;
                                             font-size:12px;
                                             min-width: 280px;
                                             min-height:50px;
                                             border: 2px solid gray;
                                             border-radius: 5px;
                                         }
                                         QGroupBox::title {
                                             margin-top:1px;
                                             border: 2px solid gray;
                                         }
                                         '''
        self.groupbox.setStyleSheet(Ran_m1)

        # One by one deleting group
        self.groupbox2 = QGroupBox(MW)
        self.groupbox2.setCheckable(True)
        self.groupbox2.move(830, 90)
        self.groupbox2.autoFillBackground()
        List_m2 = '''
                                                 QGroupBox {
                                                     background-color: white;
                                                     spacing: 5px;
                                                     font-size:12px;
                                                     min-width: 280px;
                                                     min-height:140px;
                                                     border: 2px solid gray;
                                                     border-radius: 5px;
                                                 }
                                                 QGroupBox::title {
                                                     margin-top:1px;
                                                     border: 2px solid gray;
                                                 }
                                                 '''
        self.groupbox2.setStyleSheet(List_m2)

        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(5)
        self.table.move(20, 240)

        L = (self.WIDTH - 35)
        LENGTH_Name = L * 0.45
        LENGTH_Mark = L * 0.1
        LENGTH_Status = L * 0.15
        LENGTH_Category = L * 0.15
        LENGTH_Date = L * 0.12

        self.table.setColumnWidth(0, int(LENGTH_Name))
        self.table.setColumnWidth(1, int(LENGTH_Mark))
        self.table.setColumnWidth(2, int(LENGTH_Status))
        self.table.setColumnWidth(3, int(LENGTH_Category))
        self.table.setColumnWidth(4, int(LENGTH_Date))

        self.table.setMinimumWidth(L)
        self.table.setMinimumHeight(self.HEIGHT - 250)

        # Button
        self.btn1 = QPushButton(MW)
        self.cr.create_button(self.btn1, 40, 175, 160, 30, 16)


        # Check boxes
        self.type_adding_btn = QCheckBox(MW)
        self.cr.create_textline(self.type_adding_btn, 40, 205, 200, 30, 12)

        # Progress bar
        self.pbar = QProgressBar(MW)
        self.pbar.setValue(0)
        self.pbar.setGeometry(480, 225, 335, 10)
        pbar_style = """
                        QProgressBar {
                                border: 2px solid grey;
                                border-radius: 5px;
                                text-align: center;
                                font-size: 10px;
                        }
                        QProgressBar::chunk {
                                background-color: #CD96CD;
                                width: 10px;
                                margin: 0.5px;
                        }
                """
        self.pbar.setStyleSheet(pbar_style)
        MW.setStyleSheet("""
                            QMainWindow {
                                background-image: url(background.jpg);  
                            }
                        """)
        # Terminal for searching results
        self.search_terminal = QListWidget(MW)
        self.cr.create_textline(self.search_terminal, 480, 30, 335, 190, 14)
class Options(UI):
    def __init__(self, parent=None):
        super(Options, self).__init__(parent)
        self.count_found_data = None
        self.search_terminal = None
        self.config = None
        self.ran_b1 = None
        self.ran_l2 = None
        self.ran_t1 = None
        self.ran_l1 = None
        self.list_b3 = None
        self.list_b2 = None
        self.list_l1 = None
        self.found_data_value = None
        self.found_data = None
        self.srch_t = None
        self.filter_time = None
        self.filter_category = None
        self.filter_status = None
        self.filter_mark = None
        self.filter_name = None
        self.groupbox3 = None
    def change_language(self, type):
        if type == "English":
            self.txt1.setPlaceholderText("Name")
            self.lan_setting = "Change language"
            self.num_x_lan = 15
            self.Current_lan = "English"
            self.font_setting = "Change font size"
            self.num_x_font = 20
            self.num_x2_font = 70

            self.txt3.clear()
            self.txt3.addItem("Finished")
            self.txt3.addItem("Not finished")

            self.txt4.clear()
            self.txt4.addItem("Film/Series")
            self.txt4.addItem("Book")
            self.txt4.addItem("Game")

            self.groupbox.setTitle("Turn on range deleting")
            self.groupbox2.setTitle("Turn on list deleting")
            self.groupbox3.setTitle("Filters")

            self.filter_name.setText("Name")
            self.filter_mark.setText("Mark")
            self.filter_status.setText("Status")
            self.filter_category.setText("Category")
            self.filter_time.setText("Date")

            self.table.setHorizontalHeaderLabels(["Name", "Mark", "Status", "Category", "Date"])

            self.btn1.setText("Add")

            self.type_adding_btn.setText("Turn on checking pole")

            self.srch_t.setPlaceholderText("Search")

            self.found_data.setText(f"Coincidences found: ")
            self.cr.create_textline(self.found_data_value, 420, 190, 250, 50, 20)

            self.list_l1.setText("Line")
            self.cr.create_textline(self.list_l1, 30, 15, 80, 40, 16)
            self.list_b2.setText("Clear")
            self.list_b3.setText("Start")

            self.ran_l1.setText("From")
            self.cr.create_textline(self.ran_t1, 50, 25, 50, 20, 14)
            self.ran_l2.setText("To")
            self.ran_b1.setText("Start\ndeleting")

            self.config.set("application", "language", "eng")

            self.exit_word = "Exit"
            self.exit_sentence = "Exit with saving?"
        if type == "Русский":
            self.lan_setting = "Сменить язык"
            self.num_x_lan = 30
            self.Current_lan = "Русский"
            self.font_setting = "Изменить размер\n   шрифта"
            self.num_x_font = 15
            self.num_x2_font = 75

            self.txt1.setPlaceholderText("Название")

            self.txt3.clear()
            self.txt3.addItem("Завершено")
            self.txt3.addItem("Не завершено")

            self.txt4.clear()
            self.txt4.addItem("Фильм/Сериал")
            self.txt4.addItem("Книга")
            self.txt4.addItem("Игра")

            self.groupbox.setTitle("Включить удаление диапазона")
            self.groupbox2.setTitle("Включить удаление по списку")
            self.groupbox3.setTitle("Фильтры")

            self.filter_name.setText("Название")
            self.filter_mark.setText("Оценка")
            self.filter_status.setText("Статус")
            self.filter_category.setText("Категория")
            self.filter_time.setText("Дата")

            self.table.setHorizontalHeaderLabels(["Название", "Оценка", "Статус", "Категория", "Дата"])

            self.btn1.setText("Добавить")

            self.type_adding_btn.setText("Включить проверку поля")

            self.srch_t.setPlaceholderText("Поиск")

            self.found_data.setText(f"Совпадений найдено: ")
            self.cr.create_textline(self.found_data_value, 440, 190, 250, 50, 20)

            self.list_l1.setText("Строка")
            self.cr.create_textline(self.list_l1, 15, 15, 70, 40, 16)
            self.list_b2.setText("Очистить")
            self.list_b3.setText("Старт")

            self.ran_l1.setText("От")
            self.cr.create_textline(self.ran_t1, 40, 25, 60, 20, 14)
            self.ran_l2.setText("До")
            self.ran_b1.setText("Запустить\nудаление")

            self.exit_word = "Выход"
            self.exit_sentence= "Выйти с сохранением данных?"
            self.config.set("application", "language", "rus")
    def search(self):
        try:
            # Connection to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\User\Desktop\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cur = conn.cursor()
            # Selecting data from db
            cur.execute('SELECT Name FROM Films')
            self.search_terminal.clear()
            # Loop for searching in row
            for row in cur.fetchall():
                # Loop for searching in list of data from row
                for k in row:
                    success = False
                    start = 0
                    srch_row = self.srch_t.text()
                    end = len(srch_row)
                    search=str(k).lower()
                    # Comparing parts of data from row with your request data
                    for i in range(0, len(search)):
                        for j in range(0, len(srch_row)):
                            if search[start:end] == srch_row.lower():
                                success = True
                            start += 1
                            end += 1
                        # If found then check filters
                        if success == True:
                            filter_sys=[]
                            request=""
                            # Filters checking
                            if self.filter_name.isChecked()==True:
                                filter_sys.append("Name")
                            if self.filter_mark.isChecked()==True:
                                filter_sys.append("Mark")
                            if self.filter_status.isChecked()==True:
                                filter_sys.append("Status")
                            if self.filter_category.isChecked()==True:
                                filter_sys.append("Category")
                            if self.filter_time.isChecked()==True:
                                filter_sys.append("Time_pole")
                            # Making part of request for db by filters
                            for i in filter_sys:
                                if i == filter_sys[len(filter_sys)-1]:
                                    request+=str(i)
                                else:
                                    request += str(i)+", "
                            # If all filters if on or off then add every filter
                            if self.filter_name.isChecked()== True and self.filter_mark.isChecked()== True and\
                                self.filter_status.isChecked()== True and self.filter_category.isChecked() == True\
                                    and self.filter_time.isChecked()==True or self.groupbox3.isChecked()==False:
                                    request="Name, Mark, Status, Category, Time_pole"
                            if request=="":
                                break
                            # Making request for db
                            fin_req="SELECT "+request+" FROM Films WHERE Name = ?"
                            cur.execute(fin_req, k)
                            # Adding found data in list
                            for g in cur.fetchall():
                                item=""
                                for i in g:
                                    if i == g[len(filter_sys)-1]:
                                        item += str(i)
                                    else:
                                        item+=str(i) + ", "

                                self.search_terminal.addItem(item)
                                self.count_found_data += 1

                            break
            # If nothing found then print it in list

            self.found_data_value.setText(f"{self.count_found_data}")
            self.count_found_data = 0
        except Exception as ex:
                print("не дела...")
                print(ex)
class Deleting(UI):
    def __init__(self):
        self.list_nums = None
    def delete(self,txtval):
        # This function deleting data from db
        try:
            # Loading db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\User\Desktop\pythonProject\ILF.accdb;'
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
class Systems(UI):
    def __init__(self, parent=None):
        super(Systems, self).__init__(parent)
        self.font_setting = None
        self.num_x2_font = None
        self.num_x_font = None
        self.Current_lan = None
        self.lan_setting = None
        self.num_x_lan = None
    def searching_sys(self):
        # Search line
        self.srch_t = QLineEdit(self)
        self.cr.create_textline(self.srch_t, 230, 30, 200, 30, 16)

        # Search button
        self.srch_b = QPushButton(self)
        self.srch_b.setIcon(QIcon('search.svg'))
        self.cr.create_button(self.srch_b, 440, 30, 30, 30, 16)


        # Filters
        self.groupbox3 = QGroupBox(self)
        self.groupbox3.setCheckable(True)
        self.groupbox3.move(230, 70)
        self.groupbox3.autoFillBackground()
        Ran_m3 = '''
                                                         QGroupBox {
                                                             background-color: white;
                                                             spacing: 5px;
                                                             font-size:12px;
                                                             min-width: 220px;
                                                             min-height:120px;
                                                             border: 2px solid gray;
                                                             border-radius: 5px;
                                                         }
                                                         QGroupBox::title {
                                                             margin-top:1px;
                                                             border: 2px solid gray;
                                                         }
                                                         '''
        self.groupbox3.setStyleSheet(Ran_m3)

        self.found_data = QLabel(self)
        self.count_found_data = 0
        self.cr.create_textline(self.found_data, 230, 190, 250, 50, 20)

        self.found_data_value = QLabel(self)
        self.cr.create_textline(self.found_data_value, 440, 190, 250, 50, 20)
        self.found_data_value.setText(f"{self.count_found_data}")

        # Filter "Name"
        self.filter_name = QCheckBox(self.groupbox3)
        self.cr.create_textline(self.filter_name, 10, 20, 280, 40, 12)

        # Filter "Mark"
        self.filter_mark = QCheckBox(self.groupbox3)
        self.cr.create_textline(self.filter_mark, 10, 50, 280, 40, 12)

        # Filter "Status"
        self.filter_status = QCheckBox(self.groupbox3)
        self.cr.create_textline(self.filter_status, 10, 80, 280, 40, 12)

        # Filter "Category"
        self.filter_category = QCheckBox(self.groupbox3)
        self.cr.create_textline(self.filter_category, 100, 20, 280, 40, 12)

        # Filter "Date"
        self.filter_time = QCheckBox(self.groupbox3)
        self.cr.create_textline(self.filter_time, 100, 50, 280, 40, 12)
    def menu_bar(self):
        # Function for creating menu bar
        # Exit action
        self.exit_action = QAction(QIcon('exit.svg'), '&Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Exit application')

        # Save action
        self.save_action = QAction(QIcon('save.svg'), '&Save', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save all data')

        # Info action
        self.info_action = QAction(QIcon('info.svg'), '&Info', self)
        self.info_action.setShortcut('Ctrl+I')
        self.info_action.setStatusTip('Show information about program')

        # Settings action
        self.settings_action = QAction(QIcon('settings.svg'), '&Settings', self)
        self.settings_action.setShortcut('Ctrl+E')
        self.settings_action.setStatusTip('Program settings')

        # Menu bar and adding actions on it
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('&File')
        self.file_menu.addAction(self.exit_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.settings_action)

        self.info_menu = self.menubar.addMenu('&Info')
        self.info_menu.addAction(self.info_action)
    def settings_menu(self):
        # Settings window for menu bar
        self.st_menu = QDialog()
        self.st_menu.setFixedSize(800, 400)
        self.st_menu.setWindowTitle("Settings")
        self.st_menu.setWindowIcon(QIcon('settings.svg'))
        self.st_menu.setWindowModality(Qt.ApplicationModal)

        self.lbl = QLabel(self.st_menu)
        self.cr.create_textline(self.lbl, 30, 30, 200, 30, 16)
        self.cr.create_textline(self.lbl, self.num_x_lan, 30, 200, 30, 16)
        self.lbl.setText(self.lan_setting)

        self.lan = QComboBox(self.st_menu)
        self.cr.create_textline(self.lan, 150, 30, 100, 30, 16)
        self.lan.addItem("Русский")
        self.lan.addItem("English")
        self.lan.setCurrentText(self.Current_lan)

        self.lbl1 = QLabel(self.st_menu)
        self.cr.create_textline(self.lbl1, self.num_x_font, self.num_x2_font, 200, 45, 16)
        self.lbl1.setText(self.font_setting)

        self.new_font = QLineEdit(self.st_menu)
        self.cr.create_textline(self.new_font, 150, 75, 40, 30, 16)

        def chan_lag():
            self.change_language(self.lan.currentText())
            self.cr.create_textline(self.lbl, self.num_x_lan, 30, 200, 30, 16)
            self.lbl.setText(self.lan_setting)
            self.lbl1.setText(self.font_setting)
        self.lan.currentTextChanged.connect(lambda: chan_lag())

        self.st_menu.exec_()
    def info_win(self):
        # Info window for menu bar
        self.reply = QDialog()
        self.reply.setFixedSize(380, 380)

        vbox = QVBoxLayout()
        label_dialog = QLabel()

        self.reply.setWindowTitle("Information")
        self.reply.setWindowIcon(QIcon('info.svg'))
        self.reply.setWindowModality(Qt.ApplicationModal)

        palette = QPalette()
        palette.setColor(QPalette.Button, Qt.yellow)

        # Setting window style
        label_dialog.setAutoFillBackground(True)
        label_dialog.setPalette(palette)
        label_dialog.setAlignment(Qt.AlignCenter)

        # Taking rows from file
        f = open('Info.txt', 'r')
        text = ''
        for i in f:
            text += i
        # Adding this rows
        label_dialog.setText(text)

        vbox.addWidget(label_dialog)
        self.reply.setLayout(vbox)
        self.reply.exec()
    def range_group(self):
        # This function is for creating objects in the group 1 (range deleting)
        # Label "From"
        self.ran_l1 = QLabel(self.groupbox)
        self.cr.create_textline(self.ran_l1, 10, 20, 80, 30, 16)
        # Label "To"
        self.ran_l2 = QLabel(self.groupbox)
        self.cr.create_textline(self.ran_l2, 110, 20, 80, 30, 16)
        # Text line for "From" data
        self.ran_t1 = QLineEdit(self.groupbox)
        self.cr.create_textline(self.ran_t1, 40, 25, 60, 20, 14)
        # Text line for "To" data
        self.ran_t2 = QLineEdit(self.groupbox)
        self.cr.create_textline(self.ran_t2, 140, 25, 60, 20, 14)
        # Start deleting button
        self.ran_b1 = QPushButton(self.groupbox)
        self.cr.create_button(self.ran_b1, 210, 10, 60, 35, 10)
    def list_del_group(self):
        # This function is for creating objects in the group 2 (deleting one by one)

        # Label and text line where you have to enter data for deleting
        self.list_l1 = QLabel(self.groupbox2)
        self.cr.create_textline(self.list_l1, 10, 15, 80, 40, 16)

        self.list_t1 = QLineEdit(self.groupbox2)
        self.cr.create_textline(self.list_t1, 75, 27, 80, 20, 14)

        # Add deleting data button
        self.list_b1 = QPushButton(self.groupbox2)
        self.cr.create_button(self.list_b1, 170, 27, 20, 20, 14)
        self.list_b1.setText("+")

        # Clear list with deleting data
        self.list_b2 = QPushButton(self.groupbox2)
        self.cr.create_button(self.list_b2, 210, 10, 60, 20, 10)

        # Delete button
        self.list_nums = []
        self.list_b3 = QPushButton(self.groupbox2)
        self.cr.create_button(self.list_b3, 210, 35, 60, 20, 10)


        # Space where shows data for deleting
        self.list_t2 = QListWidget(self.groupbox2)
        self.cr.create_textline(self.list_t2, 20, 60, 245, 70, 14)
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
                self.reply.setWindowIcon(QIcon('ILF.ico'))
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
                         r'DBQ=C:\Users\User\Desktop\pythonProject\ILF.accdb;'
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
class Saving(UI):
    def __init__(self, parent=None):
        super(Saving, self).__init__(parent)
        self.filter_category = None
        self.filter_status = None
        self.filter_time = None
        self.filter_mark = None
        self.filter_name = None
        self.config = None
        self.groupbox3 = None
    def save_func(self):
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\User\Desktop\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            for row in range(0, self.table.rowCount()):
                # Taking data from rows in table
                Name = (self.table.item(row, 0).text())
                Mark = (self.table.item(row, 1).text())
                Status = (self.table.item(row, 2).text())
                Category = (self.table.item(row, 3).text())
                Time_pole = (self.table.item(row, 4).text())
                # Saving it in db
                cursor.execute('UPDATE Films SET Name = ? WHERE id = ?', (Name, row + 1))
                cursor.execute('UPDATE Films SET Mark = ? WHERE id = ?', (Mark, row + 1))
                cursor.execute('UPDATE Films SET Status = ? WHERE id = ?', (Status, row + 1))
                cursor.execute('UPDATE Films SET Category = ? WHERE id = ?', (Category, row + 1))
                cursor.execute('UPDATE Films SET Time_pole = ? WHERE id = ?', (Time_pole, row + 1))
            conn.commit()
            print("норм все сохранилось")
            self.txt1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)
    def save_settings(self):
        if self.groupbox3.isChecked()==True:
            self.config.set("application", "filters_is_on", "0")
        else:
            self.config.set("application", "filters_is_on", "1")

        if self.groupbox2.isChecked()==True:
            self.config.set("application", "list_del_is_on", "0")
        else:
            self.config.set("application", "list_del_is_on", "1")

        if self.groupbox.isChecked()==True:
            self.config.set("application", "range_del_is_on", "0")
        else:
            self.config.set("application", "range_del_is_on", "1")

        if self.filter_name.isChecked()==True:
            self.config.set("application", "filter_name", "0")
        else:
            self.config.set("application", "filter_name", "1")

        if self.filter_mark.isChecked()==True:
            self.config.set("application", "filter_mark", "0")
        else:
            self.config.set("application", "filter_mark", "1")

        if self.filter_status.isChecked()==True:
            self.config.set("application", "filter_status", "0")
        else:
            self.config.set("application", "filter_status", "1")

        if self.filter_category.isChecked()==True:
            self.config.set("application", "filter_category", "0")
        else:
            self.config.set("application", "filter_category", "1")

        if self.filter_time.isChecked()==True:
            self.config.set("application", "filter_date", "0")
        else:
            self.config.set("application", "filter_date", "1")

        if self.type_adding_btn.isChecked()==True:
            self.config.set("application", "check_add_func", "0")
        else:
            self.config.set("application", "check_add_func", "1")
        with open('config.ini', 'w') as configfile:  # save
            self.config.write(configfile)
class Loading(UI):
    def __init__(self, parent=None):
        self.groupbox3 = None
        self.filter_time = None
        self.filter_category = None
        self.filter_status = None
        self.filter_mark = None
        self.filter_name = None
        self.config = None
    def load_settings(self):
        if self.config["application"]["filter_name"] == '1':
            self.filter_name.setChecked(False)
        else:
            self.filter_name.setChecked(True)

        if self.config["application"]["filter_mark"] == '1':
            self.filter_mark.setChecked(False)
        else:
            self.filter_mark.setChecked(True)

        if self.config["application"]["filter_status"] == '1':
            self.filter_status.setChecked(False)
        else:
            self.filter_status.setChecked(True)

        if self.config["application"]["filter_category"] == '1':
            self.filter_category.setChecked(False)
        else:
            self.filter_category.setChecked(True)

        if self.config["application"]["filter_date"] == '1':
            self.filter_time.setChecked(False)
        else:
            self.filter_time.setChecked(True)

        if self.config["application"]["check_add_func"] == '1':
            self.type_adding_btn.setChecked(False)
        else:
            self.type_adding_btn.setChecked(True)

        if self.config["application"]["filters_is_on"] == '1':
            self.groupbox3.setChecked(False)
        else:
            self.groupbox3.setChecked(True)

        if self.config["application"]["list_del_is_on"] == '1':
            self.groupbox2.setChecked(False)
        else:
            self.groupbox2.setChecked(True)

        if self.config["application"]["range_del_is_on"] == '1':
            self.groupbox.setChecked(False)
        else:
            self.groupbox.setChecked(True)
class App(QMainWindow,Options,Systems,Saving,Loading,Adding,Deleting,Creating):
    def __init__(self):
        super().__init__()
        self.init_UI(self)
        self.btn1.clicked.connect(lambda: self.add_func())

        self.range_group()
        self.ran_b1.clicked.connect(lambda: self.range(self.ran_t1.text(), self.ran_t2.text()))

        self.list_del_group()
        self.list_b3.clicked.connect(lambda: self.list())
        self.list_b2.clicked.connect(lambda: (self.list_nums.clear(), self.list_t2.clear()))
        self.list_b1.clicked.connect(lambda: self.add_in_delList(self.list_t1.text()))

        self.create_table(self.table)

        self.menu_bar()
        self.exit_action.triggered.connect(qApp.quit)
        self.save_action.triggered.connect(self.save_func)
        self.settings_action.triggered.connect(self.settings_menu)
        self.info_action.triggered.connect(self.info_win)

        self.searching_sys()
        self.srch_b.clicked.connect(lambda: self.search())

        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.load_settings()
        def chan_lag():
            self.change_language(self.lan.currentText())
            self.cr.create_textline(self.lbl, self.num_x_lan, 30, 200, 30, 16)
            self.lbl.setText(self.lan_setting)
            self.lbl1.setText(self.font_setting)

        if self.config["application"]["language"] == 'rus':
            self.Current_lan = "Русский"
            self.change_language(self.Current_lan)

        if self.config["application"]["language"] == 'eng':
            self.Current_lan = "English"
            self.change_language(self.Current_lan)
    def closeEvent(self,event):
        # Program Closing window
        close = QMessageBox.question(self,
                                               self.exit_word,
                                               self.exit_sentence,
                                               QMessageBox.Yes | QMessageBox.Cancel)

        if close == QMessageBox.Yes:
            self.save_settings()
            self.save_func()
            event.accept()
        if close == QMessageBox.Cancel:
            event.ignore()

# постеры или описание
# разделить программу на файлы

# сделать переключение между таблицами разных категорий
# доделать поле для выхода
# установить фон для терминала системы поиска

# в настройках знак вопроса (иконка) - дать функционал
# сделать смену языка ******
# в русской версии сделать окно выхода тоже на русском (выбор - да, отмена)

# окно для настроек(глобальных) и разбить на группы(основное, вид и т.д.):
"""
1) включение/выключение очистки полей в месте удаления данных
2) выбор языка -------------
3) отключение предупреждения при выходе
4) установка цвета закрузочной полосы
5) смена стилей приложения
6) изменение размера шрифта в разных областях программы (или на все)------------
7) перевести информацию из таблицы в отдельный файл (txt, excel)
8) Темная тема (вкл/выкл)
"""


# сделать apk и попробовать удалить бд
# ЗАДЕЛ НА БУДУЩЕЕ!! КОРОЧ, СОЗДАТЬ ОТДЕЛЬНОЕ ОКНО С НАСТРОЙКАМИ
# ВНЕШНЕГО ВИДА!!!!!!! ЦВЕТА, КАРТИНКИ ФОНА И Т.Д. ООААООАОАОАОАОАО
# КОРОЧ, ЕЩЕ ОДНА КРУТАЯ ИДЕЯ!!!!!!! МОЖНО СОЗДАВАТЬ СТИИИИИИЛЛИИИИ!!! ОАОАОАОАОАОАОА

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    APPLICATION = App()
    APPLICATION.show()
    sys.exit(app.exec_())

