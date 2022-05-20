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
        self.WIDTH = 1300
        self.HIGHT = 800
        # Main window
        self.setGeometry(350, 150, self.WIDTH, self.HIGHT)
        self.setWindowTitle("I.L.M. - I LOVE MOVIES v0.2")

        self.setWindowIcon(QIcon('ILF.ico'))
        self.setFixedSize(self.WIDTH, self.HIGHT)
        # Text lines
        self.txt1 = QLineEdit(self)
        self.txt1.setPlaceholderText("Название")

        self.txt2 = QComboBox(self)
        for num in range(100, 6, -5):
            if num%10==5:
                num=num/10
            else:
                num=int(num/10)
            self.txt2.addItem(str(num))

        self.txt3 = QComboBox(self)
        self.txt3.addItem("Завершено")
        self.txt3.addItem("Не завершено")

        self.txt4 = QComboBox(self)
        self.txt4.addItem("Фильм/Сериал")
        self.txt4.addItem("Книга")
        self.txt4.addItem("Игра")

        self.create_textline(self.txt1, 20, 30, 280, 40,25)
        self.create_textline(self.txt2, 20, 80, 280, 40,25)
        self.create_textline(self.txt3, 20, 130, 280, 40,25)
        self.create_textline(self.txt4, 20, 180, 280, 40, 25)

        txtval1 = self.txt1.text()
        txtval2 = self.txt2.currentText()
        txtval3 = self.txt3.currentText()
        self.txt = (txtval1, txtval2, txtval3)
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
        self.create_table(self.table, 20, 240)

        # Button
        self.btn1 = QPushButton("Добавить", self)
        self.create_button(self.btn1, 320, 30, 200, 40,20)
        self.btn1.clicked.connect(lambda: self.add_func())

        # Check boxes
        self.type_adding_btn= QCheckBox("Включить проверку поля",self)
        self.create_textline(self.type_adding_btn, 320, 80, 280, 40, 14)
        # Menu bar and progress bar
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.pbar.setGeometry(990, 710, 280, 45)
        self.menubar()
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
        # Search system
        self.srch_t = QLineEdit(self)
        self.srch_t.setPlaceholderText("Поиск")
        self.create_textline(self.srch_t, 550, 30, 230, 40, 20)

        self.srch_b = QPushButton(self)
        self.srch_b.setIcon(QIcon('search.svg'))
        self.create_button(self.srch_b, 800, 30, 40, 40, 20)
        self.srch_b.clicked.connect(lambda: self.search_func())

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

        self.search_terminal = QListWidget(self)
        self.create_textline(self.search_terminal, 850, 30, 435, 190, 14)

        self.filter_name = QCheckBox("Название", self.groupbox3)
        self.create_textline(self.filter_name, 30, 30, 280, 40, 14)

        self.filter_mark = QCheckBox("Оценка", self.groupbox3)
        self.create_textline(self.filter_mark, 30, 60, 280, 40, 14)

        self.filter_status = QCheckBox("Статус", self.groupbox3)
        self.create_textline(self.filter_status, 150, 0, 280, 40, 14)

        self.filter_category = QCheckBox("Категория", self.groupbox3)
        self.create_textline(self.filter_category, 150, 30, 280, 40, 14)

        self.filter_time = QCheckBox("Дата", self.groupbox3)
        self.create_textline(self.filter_time, 150, 60, 280, 40, 14)
    def menubar(self):

        exit_action = QAction(QIcon('exit.svg'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        save_action = QAction(QIcon('save.svg'), '&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save all data')
        save_action.triggered.connect(self.save_func)

        info_action = QAction(QIcon('info.svg'), '&Info', self)
        info_action.setShortcut('Ctrl+I')
        info_action.setStatusTip('Show information about program')
        info_action.triggered.connect(self.info_menu)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        file_menu.addAction(save_action)

        info_menu = menubar.addMenu('&Info')
        info_menu.addAction(info_action)
    def info_menu(self):
        self.reply = QDialog()
        self.reply.setFixedSize(380,380)
        vbox = QVBoxLayout()
        label_dialog = QLabel()
        self.reply.setWindowTitle("Information")
        self.reply.setWindowIcon(QIcon('Info.ico'))
        palette = QPalette()
        palette.setColor(QPalette.Button, Qt.yellow)

        label_dialog.setAutoFillBackground(True)
        label_dialog.setPalette(palette)
        label_dialog.setAlignment(Qt.AlignCenter)

        f = open('Info.txt','r')
        text=''
        for i in f:
            text+=i



        label_dialog.setText(text)
        vbox.addWidget(label_dialog)
        self.reply.setLayout(vbox)
        self.reply.exec()
    def add_func(self):
        if self.type_adding_btn.isChecked()==True:
            self.check_empty_pole()
        else:
            self.add_without_check()
    def create_button(self,btn,x,y,size1,size2, font):
        btn.setDefault(True)
        btn.resize(size1, size2)
        f = btn.font()
        f.setPixelSize(font)
        btn.setFont(f)
        btn.move(x, y)
        btn.show()
    def delete_func(self,txtval):
        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            row = self.table.rowCount()-1
            txtchange=int(txtval)
            cursor.execute('DELETE FROM Films WHERE id = ?', txtval)
            for i in range(txtchange+1,row+3):
                cursor.execute('UPDATE Films SET id = ? WHERE id = ?', (txtchange-1, txtchange))
                txtchange+=1
            conn.commit()
            print("норм все")
            try:
                for i in range(101):
                    # slowing down the loop
                    time.sleep(0.005)
                    # setting value to progress bar
                    self.pbar.setValue(i)
                self.pbar.setValue(0)
                self.table.removeRow(int(txtval) - 1)
            except Exception as ex:
                print("не дела...")
                print(ex)
        except Exception as ex:
            print("не дела...")
            print(ex)
    def list_del_group(self):
        self.list_l1 = QLabel(self.groupbox2)
        self.create_textline(self.list_l1, 10, 30, 80, 40,25)
        self.list_l1.setText("Строка")

        self.list_t1 = QLineEdit(self.groupbox2)
        self.create_textline(self.list_t1, 100, 30, 80, 40,25)

        self.list_t2 = QListWidget(self.groupbox2)
        self.create_textline(self.list_t2, 20, 150, 245, 115,14)

        self.list_b1 = QPushButton("+", self.groupbox2)
        self.create_button(self.list_b1, 200, 30, 40, 40,20)
        self.list_b1.clicked.connect(lambda: self.add_in_delList(self.list_t1.text()))

        self.list_b2 = QPushButton("Очистить", self.groupbox2)
        self.create_button(self.list_b2, 30, 85, 100, 45,20)
        self.list_b2.clicked.connect(lambda: self.clear_del_btn())

        self.list_nums=[]
        self.list_b3 = QPushButton("Удалить", self.groupbox2)
        self.create_button(self.list_b3, 150, 85, 100, 45,20)
        self.list_b3.clicked.connect(lambda: self.delete_list_of_rows())
    def check_empty_pole(self):
        txt1 = self.txt1.text()
        if txt1=="":
            self.reply = QDialog()
            vbox = QVBoxLayout()
            label_dialog = QLabel()
            self.reply.setWindowTitle("I.L.M.")
            self.reply.setWindowIcon(QIcon('ILF.ico'))
            palette = QPalette()
            palette.setColor(QPalette.Button, Qt.yellow)

            label_dialog.setAutoFillBackground(True)
            label_dialog.setPalette(palette)
            label_dialog.setText('Введены некорректные данные')
            label_dialog.setAlignment(Qt.AlignCenter)

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
                con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                             r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
                conn = pyodbc.connect(con_string)
                cursor = conn.cursor()
                for row in range(0, self.table.rowCount()):
                        Name=(self.table.item(row, 0).text())
                        Mark=(self.table.item(row, 1).text())
                        Status=(self.table.item(row, 2).text())
                        Category = (self.table.item(row, 3).text())
                        Time_pole = (self.table.item(row, 4).text())

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
        txtval1 = self.txt1.text()
        txtval2 = self.txt2.currentText()
        txtval3 = self.txt3.currentText()
        txtval4 = self.txt4.currentText()

        txt=(txtval1, txtval2, txtval3,txtval4)
        dt = datetime.datetime.now().replace(microsecond=0)
        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Films VALUES (?,?,?,?,?,?)',
                           self.table.rowCount()+1, txtval1,txtval2,txtval3,txtval4,dt)
            conn.commit()
            print("норм все")
            self.txt1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        col = 0
        for item in txt:
            cell = QTableWidgetItem(str(item))
            self.table.setItem(row, col, cell)
            col += 1
        self.table.setItem(row, 4, QTableWidgetItem(str(dt)))
    def create_table(self,table,x,y):
        table.setColumnCount(5)
        table.setRowCount(5)
        table.move(x, y)

        table.setColumnWidth(0, 380)
        table.setColumnWidth(1, 60)
        table.setColumnWidth(2, 150)
        table.setColumnWidth(3, 150)
        table.setColumnWidth(4, 190)

        table.setMinimumWidth(950)
        table.setMinimumHeight(self.HIGHT-250)
        table.setHorizontalHeaderLabels(["Название", "Оценка", "Статус","Категория","Дата добавления"])
        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cur = conn.cursor()
            cur.execute('SELECT Name FROM Films')
            row = 0
            col = 0
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
                    if row > self.table.rowCount():
                        self.table.setRowCount(row)
                        cell = QTableWidgetItem(str(element))
                        self.table.setItem(row-1, col, cell)

            cur.execute('SELECT Mark FROM Films')
            col = 1
            row = 0
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            cur.execute('SELECT Status FROM Films')
            col = 2
            row = 0
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            cur.execute('SELECT Category FROM Films')
            col = 3
            row = 0
            for Film in cur.fetchall():
                for element in Film:
                    cell = QTableWidgetItem(str(element))
                    self.table.setItem(row, col, cell)
                    row += 1
            cur.execute('SELECT Time_pole FROM Films')
            col = 4
            row = 0
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
    def clear_del_btn(self):
        self.list_nums=[]
        self.list_t2.clear()
    def create_textline(self,name,x,y,size1,size2,font_size):
        name.resize(size1, size2)
        f = name.font()
        f.setPixelSize(font_size)
        name.setFont(f)
        name.move(x, y)
    def closemenu(self):
        self.save_func()
        sys.exit(app.exec_())
    def closeEvent(self,event):
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
        self.ran_l1=QLabel(self.groupbox)
        self.create_textline(self.ran_l1, 10,30, 80, 40,25)
        self.ran_l1.setText("От")

        self.ran_l2 = QLabel(self.groupbox)
        self.create_textline(self.ran_l2, 140, 30, 80, 40,25)
        self.ran_l2.setText("До")

        self.ran_t1=QLineEdit(self.groupbox)
        self.create_textline(self.ran_t1, 50,30, 80, 40,25)

        self.ran_t2 = QLineEdit(self.groupbox)
        self.create_textline(self.ran_t2, 175, 30, 80, 40,25)

        self.ran_b1 = QPushButton("Запустить удаление", self.groupbox)
        self.create_button(self.ran_b1, 30, 85, 220, 45,20)
        self.ran_b1.clicked.connect(lambda: self.delete_range(self.ran_t1.text(),self.ran_t2.text()))
    def search_func(self):
        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                         r'DBQ=C:\Users\zheny\PycharmProjects\pythonProject\ILF.accdb;'
            conn = pyodbc.connect(con_string)
            cur = conn.cursor()
            cur.execute('SELECT Name FROM Films')
            self.search_terminal.clear()
            found = False
            for row in cur.fetchall():
                for k in row:
                    success = False
                    start = 0
                    srch_row = self.srch_t.text()
                    end = len(srch_row)
                    search=str(k).lower()
                    for i in range(0, len(search)):
                        for j in range(0, len(srch_row)):
                            if search[start:end] == srch_row.lower():
                                success = True
                                found=True
                            start += 1
                            end += 1
                        if success == True:
                            # print(search)
                            # cur.execute('SELECT Name, Mark, Status, Category, Time_pole FROM Films WHERE Name = ?',k)
                            filter_sys=[]
                            request=""
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
                            for i in filter_sys:
                                if i == filter_sys[len(filter_sys)-1]:
                                    request+=str(i)
                                else:
                                    request += str(i)+", "
                            if self.filter_name.isChecked()== True and self.filter_mark.isChecked()== True and\
                                self.filter_status.isChecked()== True and self.filter_category.isChecked() == True\
                                    and self.filter_time.isChecked()==True or self.groupbox3.isChecked()==False:
                                    request="Name, Mark, Status, Category, Time_pole"
                            if request=="":
                                break
                            fin_req="SELECT "+request+" FROM Films WHERE Name = ?"
                            cur.execute(fin_req, k)
                            for g in cur.fetchall():
                                item=""
                                for i in g:
                                    if i == g[len(filter_sys)-1]:
                                        item += str(i)
                                    else:
                                        item+=str(i) + ", "
                                self.search_terminal.addItem(item)
                            break
            if found==False:
                    self.search_terminal.addItem("Совпадений не найдено")


        except Exception as ex:
                print("не дела...")
                print(ex)
    def add_in_delList(self,num):
        try:
            equal=False
            if self.list_t1.text().isdigit()==True:
                for i in range(len(self.list_nums)):
                    if int(self.list_t1.text())==int(self.list_nums[i]):
                        equal=True
                    #print(self.list_t1.text(),self.list_nums[i],equal )
                if equal!=True:
                    self.list_t2.addItem(num)
                    self.list_nums.append(int(num))

            self.list_t1.clear()
        except Exception as ex:
            print("не дела...")
            print(ex)
    def delete_list_of_rows(self):
        try:
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

# постеры

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

