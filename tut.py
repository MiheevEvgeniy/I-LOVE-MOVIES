import time
import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel, QLineEdit, QProgressBar,
                             QPushButton, QVBoxLayout, QAction, QTableWidget, QTableWidgetItem,
                             QMainWindow, QApplication, QComboBox,  QListWidget,QGroupBox, QCheckBox,QMessageBox)
import pyodbc
from PyQt5.QtWidgets import qApp
from PyQt5.QtGui import QIcon, QPalette


class WidgetGallery(QMainWindow):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        # Main window
        self.WIDTH = 1300
        self.HIGHT = 800
        self.setGeometry(350, 150, self.WIDTH, self.HIGHT)
        self.setWindowTitle("I.L.M. - I LOVE MOVIES v0.2")
        self.setWindowIcon(QIcon('ILF.ico'))
        self.setFixedSize(self.WIDTH, self.HIGHT)

        # Main lines (Name, Mark, Status, Category)
        # Name
        self.txt1 = QLineEdit(self)
        self.txt1.setPlaceholderText("Название")
        self.create_textline(self.txt1, 20, 30, 280, 40, 25)

        # Mark
        self.txt2 = QComboBox(self)
        for num in range(100, 6, -5):
            if num%10==5:
                num=num/10
            else:
                num=int(num/10)
            self.txt2.addItem(str(num))
        self.create_textline(self.txt2, 20, 80, 280, 40,25)

        #Status
        self.txt3 = QComboBox(self)
        self.txt3.addItem("Завершено")
        self.txt3.addItem("Не завершено")
        self.create_textline(self.txt3, 20, 130, 280, 40, 25)

        #Category
        self.txt4 = QComboBox(self)
        self.txt4.addItem("Фильм/Сериал")
        self.txt4.addItem("Книга")
        self.txt4.addItem("Игра")
        self.create_textline(self.txt4, 20, 180, 280, 40, 25)

        # Range deleting group
        self.groupbox = QGroupBox("Включить диапазон удаления", self)
        self.groupbox.setCheckable(True)
        self.groupbox.move(990, 240)
        self.groupbox.autoFillBackground()
        Ran_m1 = '''
                                 QGroupBox {
                                     background-color: white;
                                     spacing: 5px;
                                     font-size:12px;
                                     min-width: 280px;
                                     min-height:10em;
                                     border: 2px solid gray;
                                     border-radius: 5px;
                                 }
                                 QGroupBox::title {
                                     margin-top:1px;
                                     border: 2px solid gray;
                                 }
                                 '''
        self.groupbox.setStyleSheet(Ran_m1)
        self.Range_group()

        #One by one deleting group
        self.groupbox2 = QGroupBox("Включить удаление по списку", self)
        self.groupbox2.setCheckable(True)
        self.groupbox2.move(990, 410)
        self.groupbox2.autoFillBackground()
        List_m2 = '''
                                         QGroupBox {
                                             background-color: white;
                                             spacing: 5px;
                                             font-size:12px;
                                             min-width: 280px;
                                             min-height:20em;
                                             border: 2px solid gray;
                                             border-radius: 5px;
                                         }
                                         QGroupBox::title {
                                             margin-top:1px;
                                             border: 2px solid gray;
                                         }
                                         '''
        self.groupbox2.setStyleSheet(List_m2)
        self.list_del_group()

        # Table
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(5)
        self.table.move(20, 240)

        self.table.setColumnWidth(0, 380)
        self.table.setColumnWidth(1, 60)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 190)

        self.table.setMinimumWidth(950)
        self.table.setMinimumHeight(self.HIGHT-250)
        self.table.setHorizontalHeaderLabels(["Название", "Оценка", "Статус","Категория","Дата добавления"])

        self.create_table(self.table)

        # Button
        self.btn1 = QPushButton("Добавить", self)
        self.create_button(self.btn1, 320, 30, 200, 40,20)
        self.btn1.clicked.connect(lambda: self.add_func())

        # Check boxes
        self.type_adding_btn= QCheckBox("Включить проверку поля",self)
        self.create_textline(self.type_adding_btn, 320, 80, 280, 40, 14)

        # Progress bar
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.pbar.setGeometry(990, 710, 280, 45)
        pbar_style="""
                QProgressBar {
                        border: 2px solid grey;
                        border-radius: 5px;
                        text-align: center;
                        font-size: 25px;
                }
                QProgressBar::chunk {
                        background-color: #CD96CD;
                        width: 10px;
                        margin: 0.5px;
                }
        """
        self.pbar.setStyleSheet(pbar_style)
        self.setStyleSheet("""
                    QMainWindow {
                        background-image: url(background.jpg);  
                    }
                """)

        self.menubar()
        # Search system
        self.searching_sys()
    def searching_sys(self):
        # Search line
        self.srch_t = QLineEdit(self)
        self.srch_t.setPlaceholderText("Поиск")
        self.create_textline(self.srch_t, 550, 30, 230, 40, 20)

        # Search button
        self.srch_b = QPushButton(self)
        self.srch_b.setIcon(QIcon('search.svg'))
        self.create_button(self.srch_b, 800, 30, 40, 40, 20)
        self.srch_b.clicked.connect(lambda: self.search_func())

        # Filters
        self.groupbox3 = QGroupBox("Фильтры", self)
        self.groupbox3.setCheckable(True)
        self.groupbox3.setChecked(False)
        self.groupbox3.move(550, 80)
        self.groupbox3.autoFillBackground()
        Ran_m3 = '''
                                                         QGroupBox {
                                                             background-color: white;
                                                             spacing: 5px;
                                                             font-size:12px;
                                                             min-width: 285px;
                                                             min-height:100px;
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
        self.count_found_data=0
        self.create_textline(self.found_data, 550, 180, 250, 50, 20)
        self.found_data.setText(f"Совпадений найдено: {self.count_found_data}")

        # Filter "Name"
        self.filter_name = QCheckBox("Название", self.groupbox3)
        self.create_textline(self.filter_name, 30, 30, 280, 40, 14)

        # Filter "Mark"
        self.filter_mark = QCheckBox("Оценка", self.groupbox3)
        self.create_textline(self.filter_mark, 30, 60, 280, 40, 14)

        # Filter "Status"
        self.filter_status = QCheckBox("Статус", self.groupbox3)
        self.create_textline(self.filter_status, 150, 0, 280, 40, 14)

        # Filter "Category"
        self.filter_category = QCheckBox("Категория", self.groupbox3)
        self.create_textline(self.filter_category, 150, 30, 280, 40, 14)

        # Filter "Date"
        self.filter_time = QCheckBox("Дата", self.groupbox3)
        self.create_textline(self.filter_time, 150, 60, 280, 40, 14)

        # Terminal for searching results
        self.search_terminal = QListWidget(self)
        self.create_textline(self.search_terminal, 850, 30, 435, 190, 14)
    def menubar(self):
        # Function for creating menu bar
        # Exit action
        exit_action = QAction(QIcon('exit.svg'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        # Save action
        save_action = QAction(QIcon('save.svg'), '&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save all data')
        save_action.triggered.connect(self.save_func)

        # Info action
        info_action = QAction(QIcon('info.svg'), '&Info', self)
        info_action.setShortcut('Ctrl+I')
        info_action.setStatusTip('Show information about program')
        info_action.triggered.connect(self.info_menu)

        # Menu bar and adding actions on it
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        file_menu.addAction(save_action)

        info_menu = menubar.addMenu('&Info')
        info_menu.addAction(info_action)
    def info_menu(self):
        # Info window for menu bar
        self.reply = QDialog()
        self.reply.setFixedSize(380,380)

        vbox = QVBoxLayout()
        label_dialog = QLabel()

        self.reply.setWindowTitle("Information")
        self.reply.setWindowIcon(QIcon('Info.ico'))

        palette = QPalette()
        palette.setColor(QPalette.Button, Qt.yellow)

        # Setting window style
        label_dialog.setAutoFillBackground(True)
        label_dialog.setPalette(palette)
        label_dialog.setAlignment(Qt.AlignCenter)

        # Taking rows from file
        f = open('Info.txt','r')
        text=''
        for i in f:
            text+=i
        #Adding this rows
        label_dialog.setText(text)

        vbox.addWidget(label_dialog)
        self.reply.setLayout(vbox)
        self.reply.exec()
    def add_func(self):
        #This function is for checkbox for add button
        if self.type_adding_btn.isChecked()==True:
            self.check_empty_pole()
        else:
            self.add_without_check()
    def create_button(self,btn,x,y,size1,size2, font):
        # Just a pattern for creating buttons
        btn.setDefault(True)
        btn.resize(size1, size2)
        f = btn.font()
        f.setPixelSize(font)
        btn.setFont(f)
        btn.move(x, y)
        btn.show()
    def delete_func(self,txtval):
        # This function deleting data from db
        try:
            # Loading db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
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
    def list_del_group(self):
        # This function is for creating objects in the group 2 (deleting one by one)

        # Label and text line where you have to enter data for deleting
        self.list_l1 = QLabel(self.groupbox2)
        self.create_textline(self.list_l1, 10, 30, 80, 40,25)
        self.list_l1.setText("Строка")

        self.list_t1 = QLineEdit(self.groupbox2)
        self.create_textline(self.list_t1, 100, 30, 80, 40,25)

        # Space where shows data for deleting
        self.list_t2 = QListWidget(self.groupbox2)
        self.create_textline(self.list_t2, 20, 150, 245, 115,14)

        # Add deleting data button
        self.list_b1 = QPushButton("+", self.groupbox2)
        self.create_button(self.list_b1, 200, 30, 40, 40,20)
        self.list_b1.clicked.connect(lambda: self.add_in_delList(self.list_t1.text()))

        # Clear list with deleting data
        self.list_b2 = QPushButton("Очистить", self.groupbox2)
        self.create_button(self.list_b2, 30, 85, 100, 45,20)
        self.list_b2.clicked.connect(lambda: (self.list_nums.clear(), self.list_t2.clear()))

        # Delete button
        self.list_nums=[]
        self.list_b3 = QPushButton("Удалить", self.groupbox2)
        self.create_button(self.list_b3, 150, 85, 100, 45,20)
        self.list_b3.clicked.connect(lambda: self.delete_list_of_rows())
    def check_empty_pole(self):
        # Function for checking is Name pole empty or not
        txt1 = self.txt1.text()
        if txt1=="":
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
    def save_func(self):
            try:
                # Connecting to db
                con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                             r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
                conn = pyodbc.connect(con_string)
                cursor = conn.cursor()
                for row in range(0, self.table.rowCount()):
                        # Taking data from rows in table
                        Name=(self.table.item(row, 0).text())
                        Mark=(self.table.item(row, 1).text())
                        Status=(self.table.item(row, 2).text())
                        Category = (self.table.item(row, 3).text())
                        Time_pole = (self.table.item(row, 4).text())

                        # Saving it in db
                        cursor.execute('UPDATE Films SET Name = ? WHERE id = ?', (Name, row + 1 ))
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
    def add_without_check(self):
        # Taking data from text lines (Name, Mark and etc)
        txtval1 = self.txt1.text()
        txtval2 = self.txt2.currentText()
        txtval3 = self.txt3.currentText()
        txtval4 = self.txt4.currentText()

        # Making list from it and saving current time
        txt=(txtval1, txtval2, txtval3,txtval4)
        dt = datetime.datetime.now().replace(microsecond=0)
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            # Adding data in db
            cursor.execute('INSERT INTO Films VALUES (?,?,?,?,?,?)',
                           self.table.rowCount()+1, txtval1,txtval2,txtval3,txtval4,dt)
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
    def create_table(self,table):
        try:
            # Connecting to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
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
    def closeEvent(self,event):
        # Program Closing window
        close = QMessageBox.question(self,
                                               "Выход",
                                               "Выйти с сохранением данных?",
                                               QMessageBox.Yes | QMessageBox.Cancel)

        if close == QMessageBox.Yes:
            self.save_func()
            event.accept()
        if close == QMessageBox.Cancel:
            event.ignore()
    def Range_group(self):
        # This function is for creating objects in the group 1 (range deleting)
        # Label "From"
        self.ran_l1=QLabel(self.groupbox)
        self.create_textline(self.ran_l1, 10,30, 80, 40,25)
        self.ran_l1.setText("От")
        # Label "To"
        self.ran_l2 = QLabel(self.groupbox)
        self.create_textline(self.ran_l2, 140, 30, 80, 40,25)
        self.ran_l2.setText("До")
        # Text line for "From" data
        self.ran_t1=QLineEdit(self.groupbox)
        self.create_textline(self.ran_t1, 50,30, 80, 40,25)
        # Text line for "To" data
        self.ran_t2 = QLineEdit(self.groupbox)
        self.create_textline(self.ran_t2, 175, 30, 80, 40,25)
        # Start deleting button
        self.ran_b1 = QPushButton("Запустить удаление", self.groupbox)
        self.create_button(self.ran_b1, 30, 85, 220, 45,20)
        self.ran_b1.clicked.connect(lambda: self.delete_range(self.ran_t1.text(),self.ran_t2.text()))
    def search_func(self):
        try:
            # Connection to db
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cur = conn.cursor()
            # Selecting data from db
            cur.execute('SELECT Name FROM Films')
            self.search_terminal.clear()
            found = False
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
                                found=True
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

            self.found_data.setText(f"Совпадений найдено: {self.count_found_data}")
            self.count_found_data = 0
        except Exception as ex:
                print("не дела...")
                print(ex)
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
    def delete_list_of_rows(self):
        try:
            # deleting one by one func
            change=0
            self.list_nums.sort()
            for i in range(len(self.list_nums)):
                self.delete_func(self.list_nums[i]-change)
                change+=1
        except Exception as ex:
            print("не дела...")
            print(ex)
    def delete_range(self, start, end):
        try:
            # Deleting range func
            for i in range(int(start), int(end)+1):
                self.delete_func(start)
                time.sleep(0.005)
        except Exception as ex:
            print("не дела...")
            print(ex)

# поле удаления не цифра, а текст
# система поиска с указанием кол-ва совпадений
# сохранение настроек в бд
# предотвратить открытие кучи окон сразу

# постеры или описание
# разделить программу на классы

# сделать переключение между таблицами разных категорий

# сделать apk и попробовать удалить бд
# ЗАДЕЛ НА БУДУЩЕЕ!! КОРОЧ, СОЗДАТЬ ОТДЕЛЬНОЕ ОКНО С НАСТРОЙКАМИ
# ВНЕШНЕГО ВИДА!!!!!!! ЦВЕТА, КАРТИНКИ ФОНА И Т.Д. ООААООАОАОАОАОАО
# КОРОЧ, ЕЩЕ ОДНА КРУТАЯ ИДЕЯ!!!!!!! МОЖНО СОЗДАВАТЬ СТИИИИИИЛЛИИИИ!!! ОАОАОАОАОАОАОА

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gallery = WidgetGallery()

    gallery.show()
    sys.exit(app.exec_())

