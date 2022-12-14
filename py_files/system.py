from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QLabel, QVBoxLayout, QAction, QSlider, QFileDialog, QMessageBox)
from PyQt5.QtGui import QPalette, QColor
from ui import *
import adding
import pandas as pd


class Systems(UI):
    def __init__(self):
        super(Systems, self).__init__()
        self.color_setting = None
        self.clr_text = None
        self.color_conf = None
        self.ed_col_pl = None
        self.blue = None
        self.green = None
        self.red = None
        self.num_x2_font = None
        self.num_x_font = None
        self.Current_lan = None
        self.lan_setting = None
        self.num_x_lan = None
        self.txtCreate = None
        self.xlsCreate = None
        self.txtLoadText = None
        self.xlsLoadText = None
        self.films=None
        self.books = None
        self.games = None
        self.finish = None
        self.reset = None
        self.table_borders_text = None
        self.table_cells_text = None
        self.table_head = None
        self.menubar_text = None
        self.progress_bar = None
        self.hex_txt = None

    def searching_sys(self):
        # Search line
        self.srch_t = QLineEdit(self)
        self.cr.create_textline(self.srch_t, 230, 30, 200, 30, 16)

        # Search button
        self.srch_b = QPushButton(self)
        self.srch_b.setIcon(QIcon('..\\textures\\search.svg'))
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
        self.exit_action = QAction(QIcon('..\\textures\\exit.svg'), '&Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Exit application')

        # Save action
        self.save_action = QAction(QIcon('..\\textures\\save.svg'), '&Save', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save all data')

        # Info action
        self.info_action = QAction(QIcon('..\\textures\\info.svg'), '&Info', self)
        self.info_action.setShortcut('Ctrl+I')
        self.info_action.setStatusTip('Show information about program')

        # Settings action
        self.settings_action = QAction(QIcon('..\\textures\\settings.svg'), '&Settings', self)
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
        self.st_menu.setFixedSize(540, 300)
        self.st_menu.setWindowTitle("Settings")
        self.st_menu.setWindowIcon(QIcon('..\\textures\\settings.svg'))
        self.st_menu.setWindowModality(Qt.ApplicationModal)

        self.colorAndLaguage = QGroupBox(self.st_menu)
        self.colorAndLaguage.move(20, 20)
        self.colorAndLaguage.autoFillBackground()

        self.lbl = QLabel(self.colorAndLaguage)
        self.cr.create_textline(self.lbl, self.num_x_lan, 30, 200, 30, 16)
        self.lbl.setText(self.lan_setting)

        self.lan = QComboBox(self.colorAndLaguage)
        self.cr.create_textline(self.lan, 150, 30, 100, 30, 16)
        self.lan.addItem("Русский")
        self.lan.addItem("English")
        self.lan.setCurrentText(self.Current_lan)

        def finishChoosingColor(element, color):

            if element == self.menubar_text:
                newColor = "QMenuBar{background-color: " + color + ";}"
                self.menubar.setStyleSheet(newColor)
            if element == self.table_borders_text:
                self.borderStyle = "QTableWidget::item {border: 1px outset " + color + ";}"
                self.table.setStyleSheet(self.borderStyle + self.cellsStyle + self.headStyle)
            if element == self.table_cells_text:
                self.cellsStyle = "QTableWidget{background-color: " + color + ";}"
                self.table.setStyleSheet(self.borderStyle + self.cellsStyle + self.headStyle)
            if element == self.table_head:
                self.headStyle = "QHeaderView::section{background-color: " + color + ";}"
                self.table.setStyleSheet(self.borderStyle + self.cellsStyle + self.headStyle)
            if element == self.progress_bar:
                newColor = """
                    QProgressBar {
                            border: 2px solid gray;
                            border-radius: 5px;
                            text-align: center;
                            font-size: 10px;
                    }
                    QProgressBar::chunk {
                            background-color: """ + color + """;
                            width: 10px;
                            margin: 0.5px;
                    }
                """
                self.pbar.setStyleSheet(newColor)

        self.color_lbl  = QLabel(self.colorAndLaguage)
        self.cr.create_textline(self.color_lbl, 30, 80, 200, 40, 16)
        self.color_lbl.setText(self.color_setting)

        self.elements = QComboBox(self.colorAndLaguage)
        self.cr.create_textline(self.elements, 40, 125, 170, 30, 16)
        self.elements.addItem(self.table_borders_text)
        self.elements.addItem(self.table_cells_text)
        self.elements.addItem(self.table_head)
        self.elements.addItem(self.menubar_text)
        self.elements.addItem(self.progress_bar)

        self.color_btn = QPushButton(self.colorAndLaguage)
        self.cr.create_button(self.color_btn, 40, 170, 110, 30, 16)
        self.color_btn.setText(self.clr_text)
        self.color_btn.clicked.connect((lambda: pick_color_menu()))

        self.resetTheme = QPushButton(self.colorAndLaguage)
        self.cr.create_button(self.resetTheme, 40, 210, 160, 30, 16)
        self.resetTheme.setText(self.reset)
        self.resetTheme.clicked.connect(lambda: setResetTheme())

        def setResetTheme():
            finishChoosingColor(self.table_borders_text, "gray")
            finishChoosingColor(self.table_cells_text, "white")
            finishChoosingColor(self.table_head, "white")
            finishChoosingColor(self.menubar_text, "white")
            finishChoosingColor(self.progress_bar, "white")

        self.loadAndUploads = QGroupBox(self.st_menu)
        self.loadAndUploads.move(310, 20)
        self.loadAndUploads.autoFillBackground()

        # Load to txt
        self.txtUpload = QPushButton(self.loadAndUploads)
        self.cr.create_button(self.txtUpload, 30, 30, 130, 30, 16)
        self.txtUpload.setText(self.txtCreate)
        self.txtUpload.clicked.connect((lambda: uploadTxt()))

        # Load to xls
        self.xlsUpload = QPushButton(self.loadAndUploads)
        self.cr.create_button(self.xlsUpload, 30, 80, 140, 30, 16)
        self.xlsUpload.setText(self.xlsCreate)
        self.xlsUpload.clicked.connect((lambda: uploadXls()))

        # Load from txt
        self.txtLoad = QPushButton(self.loadAndUploads)
        self.cr.create_button(self.txtLoad, 30, 130, 130, 30, 16)
        self.txtLoad.setText(self.txtLoadText)
        self.txtLoad.clicked.connect((lambda:  readTxt()))

        # Load from xls
        self.xlsLoad = QPushButton(self.loadAndUploads)
        self.cr.create_button(self.xlsLoad, 30, 180, 140, 30, 16)
        self.xlsLoad.setText(self.xlsLoadText)
        self.xlsLoad.clicked.connect((lambda: readXls()))

        def readXls():
            try:
                dir_ = QFileDialog.getOpenFileName(None, 'Select a file:', 'C:\\')
                if (dir_[0][-4:]) == ".xls" or (dir_[0][-4:]) == ".xlsx":
                    data = pd.read_excel(dir_[0], engine="openpyxl")
                    for i in range(0,data[self.filter_name.text()].size):
                        Name = data[self.filter_name.text()][i]
                        Status = data[self.filter_status.text()][i]
                        Mark = data[self.filter_mark.text()][i]
                        Category = data[self.filter_category.text()][i]
                        adding.Adding.add_without_check(adding.Adding(), Name, Mark, Status, Category, self.table, self.txt1)
                QMessageBox.about(self.st_menu, "Результат загрузки", "Данные загружены")
            except Exception as ex:
                QMessageBox.about(self.st_menu, "Результат загрузки", "Ошибка загрузки")
                print(ex)
        def uploadXls():
            try:
                dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\',
                                                              QFileDialog.ShowDirsOnly)
                path = dir_+'/My ILM list.xls'
                Name = []
                Mark = []
                Status = []
                Category = []
                for row in range(0, self.table.rowCount()):
                    # Taking data from rows in table
                    Name.append((self.table.item(row, 0).text()))
                    Mark.append((self.table.item(row, 1).text()))
                    Status.append(self.table.item(row, 2).text())
                    Category.append(self.table.item(row, 3).text())
                data = pd.DataFrame(data = {self.filter_category.text(): Category,
                                     self.filter_name.text(): Name,
                                     self.filter_mark.text(): Mark,
                                     self.filter_status.text(): Status})
                data.to_excel(path, engine='xlsxwriter')
                QMessageBox.about(self.st_menu, "Результат выгрузки", "Данные выгружены")
            except Exception as ex:
                QMessageBox.about(self.st_menu, "Результат выгрузки", "Ошибка выгрузки")
                print(ex)

        def uploadTxt():
            try:
                dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\',
                                                              QFileDialog.ShowDirsOnly)
                file = open(dir_+'/My ILM list.txt','w')
                maxLineLen = 70
                for row in range(0, self.table.rowCount()):
                    # Taking data from rows in table
                    Name = (self.table.item(row, 0).text())
                    Mark = (self.table.item(row, 1).text())
                    Status = (self.table.item(row, 2).text())
                    Category = (self.table.item(row, 3).text())
                    line = Category + ": " + Name + " (" + Status + " " + Mark + "/10)\n"
                    lineLen = len(line)
                    if lineLen != maxLineLen:
                        line =  Category+ ": " +Name + ("-"*(maxLineLen-lineLen))+ " (" + Status + " " + Mark + "/10)\n"
                    file.write(line)
                QMessageBox.about(self.st_menu, "Результат выгрузки", "Данные выгружены")
                file.close()
            except Exception as ex:
                QMessageBox.about(self.st_menu, "Результат выгрузки", "Ошибка выгрузки")
                print(ex)
        def readTxt():
            try:
                dir_ = QFileDialog.getOpenFileName(None, 'Select a file:', 'C:\\')
                if (dir_[0][-4:]) == ".txt":
                    with open(dir_[0], 'r', encoding="utf-8") as f:

                        for file in f:
                            isCategory = True
                            isName = False
                            isStatus = False
                            isMark = False
                            Name = ""
                            Status = ""
                            Mark = ""
                            Category = ""

                            for i in file:
                                if i == ":" and isCategory:
                                    isCategory = False
                                    isName = True
                                    continue
                                if i == "(" and isName:
                                    isName = False
                                    isStatus = True
                                    continue
                                if not (isName) and isStatus and i == " ":
                                    isStatus = False
                                    isMark = True
                                    continue
                                if not (isStatus) and isMark and i == "/":
                                    break
                                if isCategory:
                                    Category+=i
                                elif isName:
                                    Name+=i
                                elif isStatus:
                                    Status+=i
                                elif isMark:
                                    Mark+=i

                            adding.Adding.add_without_check(adding.Adding(), Name, Mark, Status, Category, self.table, self.txt1)
                    QMessageBox.about(self.st_menu, "Результат загрузки", "Данные загружены")
                    f.close()

            except Exception as ex:
                QMessageBox.about(self.st_menu, "Результат загрузки", "Ошибка загрузки")
                print(ex)
        def pick_color_menu():
            # Info window for menu bar
            self.pcm = QDialog()
            self.pcm.setFixedSize(600, 300)
            self.pcm.setWindowTitle("Color picker")
            self.pcm.setWindowModality(Qt.ApplicationModal)

            # --------------SLIDER-RED--------------

            self.slider_red = QSlider(Qt.Vertical, self.pcm)
            self.slider_red.move(325, 10)
            self.slider_red.setMinimumHeight(220)
            self.slider_red.setMinimum(0)
            self.slider_red.setMaximum(255)
            self.slider_red.setValue(0)
            self.slider_red.setTickPosition(QSlider.NoTicks)
            self.slider_red.setTickInterval(1)
            self.slider_red.valueChanged.connect(lambda: color_set(self.slider_red.value(),
                                                                   self.slider_green.value(),
                                                                   self.slider_blue.value()))

            # --------------SLIDER-GREEN--------------

            self.slider_green = QSlider(Qt.Vertical, self.pcm)
            self.slider_green.move(355, 10)
            self.slider_green.setMinimumHeight(220)
            self.slider_green.setMinimum(0)
            self.slider_green.setMaximum(255)
            self.slider_green.setValue(0)
            self.slider_green.setTickPosition(QSlider.NoTicks)
            self.slider_green.setTickInterval(1)
            self.slider_green.valueChanged.connect(lambda: color_set(self.slider_red.value(),
                                                                     self.slider_green.value(),
                                                                     self.slider_blue.value()))

            # --------------SLIDER-BLUE--------------

            self.slider_blue = QSlider(Qt.Vertical, self.pcm)
            self.slider_blue.move(385, 10)
            self.slider_blue.setMinimumHeight(220)
            self.slider_blue.setMinimum(0)
            self.slider_blue.setMaximum(255)
            self.slider_blue.setValue(0)
            self.slider_blue.setTickPosition(QSlider.NoTicks)
            self.slider_blue.setTickInterval(1)
            self.slider_blue.valueChanged.connect(lambda: color_set(self.slider_red.value(),
                                                                    self.slider_green.value(),
                                                                    self.slider_blue.value()))
            # --------------SEE-COLOR--------------

            self.color_menu = QLineEdit(self.pcm)
            self.color_menu.setDisabled(True)
            pal = QPalette()
            pal.setColor(QPalette.Base, QColor(255, 255, 255).toRgb())
            self.color_menu.setPalette(pal)
            self.cr.create_textline(self.color_menu, 420, 10, 170, 150, 16)
            # --------------RED--------------
            self.lbl_red = QLabel(self.pcm)
            self.cr.create_textline(self.lbl_red, 420, 165, 100, 20, 12)
            self.lbl_red.setText(self.red)

            self.red_txt = QLineEdit(self.pcm)
            self.cr.create_textline(self.red_txt, 480, 165, 100, 20, 12)
            self.red_txt.setText("255")

            # --------------GREEN--------------

            self.lbl_green = QLabel(self.pcm)
            self.cr.create_textline(self.lbl_green, 420, 195, 100, 20, 12)
            self.lbl_green.setText(self.green)

            self.green_txt = QLineEdit(self.pcm)
            self.cr.create_textline(self.green_txt, 480, 195, 100, 20, 12)
            self.green_txt.setText("255")

            # --------------BLUE--------------

            self.lbl_blue = QLabel(self.pcm)
            self.cr.create_textline(self.lbl_blue, 420, 225, 100, 20, 12)
            self.lbl_blue.setText(self.blue)

            self.blue_txt = QLineEdit(self.pcm)
            self.cr.create_textline(self.blue_txt, 480, 225, 100, 20, 12)
            self.blue_txt.setText("255")

            self.red_txt.textEdited.connect(lambda: text_color_edited(self.red_txt.text(),
                                                                      self.green_txt.text(),
                                                                      self.blue_txt.text()))
            self.green_txt.textEdited.connect(lambda: text_color_edited(self.red_txt.text(),
                                                                        self.green_txt.text(),
                                                                        self.blue_txt.text()))
            self.blue_txt.textEdited.connect(lambda: text_color_edited(self.red_txt.text(),
                                                                       self.green_txt.text(),
                                                                       self.blue_txt.text()))
            # ------------------HEX----------------------
            self.hex_code = QLabel(self.pcm)
            self.cr.create_textline(self.hex_code, 420, 255, 100, 20, 12)
            self.hex_code.setText("HEX CODE")

            self.hex_txt = QLineEdit(self.pcm)
            self.cr.create_textline(self.hex_txt, 480, 255, 100, 20, 12)
            self.hex_txt.setText("#ffffff")
            # --------------YOUR-COLORS----------------
            self.color_plates = []
            x = 10
            y = 10
            pal = QPalette()
            pal.setColor(QPalette.Button, QColor(255, 255, 255).toRgb())

            for i in range(20):
                self.color_plates.append(QPushButton(self.pcm))
                self.color_plates[i].setPalette(pal)
                self.color_plates[i].clicked.connect(lambda state, index=i, obj = self.color_plates[i]: miniColorBtn(index))
                self.cr.create_button(self.color_plates[i], x, y, 25, 25, 12)
                print(i)
                print(self.color_plates[i])
                print("---------------")

                if i == 9:
                    x = 10
                    y += 40
                else:
                    x += 30
            def miniColorBtn(index):
                try:
                    hex_color = (self.color_conf["user_colors"]["col" + str(index + 1)])[1:]
                    hex_tuple = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
                    red = hex_tuple[0]
                    green = hex_tuple[1]
                    blue = hex_tuple[2]

                    color = QColor(red, green, blue)

                    pallet = QPalette()
                    pallet.setColor(QPalette.Base, QColor(color.toRgb()))
                    self.color_menu.setPalette(pallet)

                    self.red_txt.setText(str(red))
                    self.green_txt.setText(str(green))
                    self.blue_txt.setText(str(blue))

                    self.slider_red.setValue(red)
                    self.slider_green.setValue(green)
                    self.slider_blue.setValue(blue)

                    self.hex_txt.setText("#" + hex_color)
                except Exception as e:
                    print(e)

            self.save_color_plate = QPushButton(self.pcm)
            self.cr.create_button(self.save_color_plate, 10, 80, 300, 30, 16)
            self.save_color_plate.setText(self.ed_col_pl)
            self.save_color_plate.clicked.connect(lambda: self.save_color(self.red_txt.text(),
                                                                       self.green_txt.text(),
                                                                       self.blue_txt.text()))

            self.load_colors()

            self.chooseColor = QPushButton(self.pcm)
            self.cr.create_button(self.chooseColor, 10, 150, 300, 30, 16)
            self.chooseColor.setText(self.finish)
            self.chooseColor.clicked.connect(lambda: finishChoosingColor(self.elements.currentText(), self.hex_txt.text()))




            self.pcm.show()


            def text_color_edited(red, green, blue):
                if str(red).isdigit() == False:
                    red = 0
                if str(green).isdigit() == False:
                    green = 0
                if str(blue).isdigit() == False:
                    blue = 0

                self.slider_red.setValue(int(red))
                self.slider_green.setValue(int(green))
                self.slider_blue.setValue(int(blue))
                color_set(red, green, blue)

            def color_set(red, green, blue):
                red,green,blue=int(red),int(green),int(blue)
                if str(red).isdigit() == True \
                        and str(green).isdigit() == True \
                        and str(blue).isdigit() == True:
                    if red > 255:
                        red = 255
                    if green > 255:
                        green = 255
                    if blue > 255:
                        blue = 255

                    self.red_txt.setText(str(red))
                    self.green_txt.setText(str(green))
                    self.blue_txt.setText(str(blue))


                    pal = QPalette()
                    pal.setColor(QPalette.Base, QColor(red, green, blue).toRgb())
                    self.color_menu.setPalette(pal)

                    hex_row="#"
                    if len((str(hex(red))[2:])) <2:
                        hex_row+="0"+str(hex(red))[2:]
                    else:
                        hex_row +=str(hex(red))[2:]

                    if len(str(hex(green))[2:]) <2:
                        hex_row+="0"+str(hex(green))[2:]
                    else:
                        hex_row +=str(hex(green))[2:]

                    if len(str(hex(blue))[2:]) <2:
                        hex_row+="0"+str(hex(blue))[2:]
                    else:
                        hex_row +=str(hex(blue))[2:]
                    self.hex_txt.setText(hex_row)
                else:
                    if str(red).isdigit() == False:
                        red = 0
                    if str(green).isdigit() == False:
                        green = 0
                    if str(blue).isdigit() == False:
                        blue = 0
                    color_set(red, green, blue)

        def chan_lag():
            self.change_language(self.lan.currentText())
            self.cr.create_textline(self.lbl, self.num_x_lan, 30, 200, 30, 16)
            self.lbl.setText(self.lan_setting)
            self.xlsUpload.setText(self.xlsCreate)
            self.txtUpload.setText(self.txtCreate)
            self.txtLoad.setText(self.txtLoadText)
            self.xlsLoad.setText(self.xlsLoadText)
            self.color_lbl.setText(self.color_setting)
            self.color_btn.setText(self.clr_text)

            self.elements.clear()
            self.elements.addItem(self.table_borders_text)
            self.elements.addItem(self.table_cells_text)
            self.elements.addItem(self.table_head)
            self.elements.addItem(self.menubar_text)
            self.elements.addItem(self.progress_bar)

            self.resetTheme.setText(self.reset)

        self.lan.currentTextChanged.connect(lambda: chan_lag())

        self.st_menu.exec_()

    def info_win(self):
        # Info window for menu bar
        self.reply = QDialog()
        self.reply.setFixedSize(380, 380)

        vbox = QVBoxLayout()
        label_dialog = QLabel()

        self.reply.setWindowTitle("Information")
        self.reply.setWindowIcon(QIcon('..\\textures\\info.svg'))
        self.reply.setWindowModality(Qt.ApplicationModal)

        palette = QPalette()
        palette.setColor(QPalette.Button, Qt.yellow)

        # Setting window style
        label_dialog.setAutoFillBackground(True)
        label_dialog.setPalette(palette)
        label_dialog.setAlignment(Qt.AlignCenter)

        # Taking rows from file
        f = open(os.path.abspath("..\\data\\Info.txt"), 'r')
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