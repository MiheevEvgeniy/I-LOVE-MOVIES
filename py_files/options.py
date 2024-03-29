from ui import *
import pyodbc


class Options(UI):
    def __init__(self):
        super(Options, self).__init__()
        self.program_path = None
        self.count_found_data = None
        self.search_terminal = None
        self.config = None
        self.ran_b1 = None
        self.ran_l2 = None
        self.ran_t1 = None
        self.ran_l1 = None
        self.finish = None
        self.list_b3 = None
        self.list_b2 = None
        self.list_l1 = None
        self.found_data_value = None
        self.films = None
        self.books = None
        self.games = None
        self.found_data = None
        self.srch_t = None
        self.filter_time = None
        self.filter_category = None
        self.filter_status = None
        self.filter_Rate = None
        self.filter_name = None
        self.groupbox3 = None
        self.txtCreate = None
        self.xlsCreate = None
        self.txtLoadText = None
        self.xlsLoadText = None
    def change_language(self, type):
        if type == "English":
            self.txt1.setPlaceholderText("Name")
            self.lan_setting = "Change language"
            self.num_x_lan = 15
            self.Current_lan = "English"
            self.num_x_font = 20
            self.num_x2_font = 65
            self.finish = "Finish"

            self.txtCreate = "Upload to txt"
            self.xlsCreate = "Upload to excel"
            self.txtLoadText = "Load from txt"
            self.xlsLoadText = "Load from excel"

            self.red="Red"
            self.green = "Green"
            self.blue = "Blue"
            self.ed_col_pl="Save current color"
            self.clr_text = "Change color"
            self.color_setting = "Set element color:"

            self.txt3.clear()
            self.txt3.addItem("Finished")
            self.txt3.addItem("Not finished")

            self.films = "Film"
            self.series = "Series"
            self.books = "Book"
            self.games = "Game"
            self.txt4.clear()
            self.txt4.addItem(self.films)
            self.txt4.addItem(self.series)
            self.txt4.addItem(self.books)
            self.txt4.addItem(self.games)

            self.groupbox.setTitle("Turn on range deleting")
            self.groupbox2.setTitle("Turn on list deleting")
            self.groupbox3.setTitle("Filters")

            self.filter_name.setText("Name")
            self.filter_Rate.setText("Rate")
            self.filter_status.setText("Status")
            self.filter_category.setText("Category")
            self.filter_time.setText("Date")

            self.table.setHorizontalHeaderLabels(["Name", "Rate", "Status", "Category", "Date"])

            self.btn1.setText("Add")

            self.type_adding_btn.setText("Turn on checking pole")

            self.srch_t.setPlaceholderText("Search by name")
            self.reset = "Default theme"
            self.table_borders_text = "Table borders"

            self.found_data.setText(f"Coincidences found: ")
            self.cr.create_textline(self.found_data_value, 420, 190, 250, 50, 20)
            self.table_cells_text = "Table's background"
            self.table_head = "Table head"
            self.list_l1.setText("Line")
            self.cr.create_textline(self.list_l1, 30, 15, 80, 40, 16)
            self.list_b2.setText("Clear")
            self.list_b3.setText("Start")
            self.menubar_text = "Menu bar"
            self.progress_bar = "Progress bar"

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
            self.num_x_font = 12
            self.num_x2_font = 62
            self.finish = "Завершить"
            self.reset = "Тема по умолчанию"
            self.progress_bar = "Шкала прогресса"
            self.menubar_text = "Полоска конфигурации"

            self.table_borders_text = "Границы таблицы"
            self.table_head = "Заголовок таблицы"
            self.table_cells_text = "Фон таблицы"

            self.txtCreate = "Выгрузить в txt"
            self.xlsCreate = "Выгрузить в excel"
            self.txtLoadText = "Загрузить из txt"
            self.xlsLoadText = "Загрузить из excel"

            self.red = "Красный"
            self.green = "Зеленый"
            self.blue = "Синий"
            self.ed_col_pl = "Сохранить текущий цвет"
            self.clr_text = "Сменить цвет"
            self.color_setting = "Установить цвет элемента:"

            self.txt1.setPlaceholderText("Название")

            self.txt3.clear()
            self.txt3.addItem("Завершено")
            self.txt3.addItem("Не завершено")

            self.films = "Фильм"
            self.series = "Сериал"
            self.books = "Книга"
            self.games = "Игра"

            self.txt4.clear()
            self.txt4.addItem(self.films)
            self.txt4.addItem(self.series)
            self.txt4.addItem(self.books)
            self.txt4.addItem(self.games)

            self.groupbox.setTitle("Включить удаление диапазона")
            self.groupbox2.setTitle("Включить удаление по списку")
            self.groupbox3.setTitle("Фильтры")

            self.filter_name.setText("Название")
            self.filter_Rate.setText("Оценка")
            self.filter_status.setText("Статус")
            self.filter_category.setText("Категория")
            self.filter_time.setText("Дата")

            self.table.setHorizontalHeaderLabels(["Название", "Оценка", "Статус", "Категория", "Дата"])

            self.btn1.setText("Добавить")

            self.type_adding_btn.setText("Включить проверку поля")

            self.srch_t.setPlaceholderText("Поиск по названию")

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
                         r'DBQ='+self.program_path + '\data\ILF.accdb;'
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
                            if self.filter_Rate.isChecked()==True:
                                filter_sys.append("Rate")
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
                            if self.filter_name.isChecked()== True and self.filter_Rate.isChecked()== True and\
                                self.filter_status.isChecked()== True and self.filter_category.isChecked() == True\
                                    and self.filter_time.isChecked()==True or self.groupbox3.isChecked()==False:
                                    request="Name, Rate, Status, Category, Time_pole"
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
                print(ex)