from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QLabel, QVBoxLayout, QAction, QSlider)
from PyQt5.QtGui import QPalette, QColor
from ui import *


class Systems(UI):
    def __init__(self):
        super(Systems, self).__init__()
        self.clr_x = None
        self.color_setting = None
        self.clr_text = None
        self.color_conf = None
        self.ed_col_pl = None
        self.blue = None
        self.green = None
        self.red = None
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
        self.st_menu.setFixedSize(800, 400)
        self.st_menu.setWindowTitle("Settings")
        self.st_menu.setWindowIcon(QIcon('..\\textures\\settings.svg'))
        self.st_menu.setWindowModality(Qt.ApplicationModal)

        self.lbl = QLabel(self.st_menu)
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

        self.color_lbl  = QLabel(self.st_menu)
        self.cr.create_textline(self.color_lbl, 20, 125, 200, 30, 16)
        self.color_lbl.setText(self.color_setting)

        self.color_btn = QPushButton(self.st_menu)
        self.cr.create_button(self.color_btn, self.clr_x, 120, 110, 30, 16)
        self.color_btn.setText(self.clr_text)
        self.color_btn.clicked.connect((lambda: pick_color_menu()))

        self.elements = QComboBox(self.st_menu)
        self.cr.create_textline(self.elements, self.clr_x+150, 120, 150, 30, 16)
        self.elements.addItem("Table borders")
        self.elements.addItem("Table cells")
        self.elements.addItem("Font")
        self.elements.addItem("Poles")
        self.elements.addItem("Menu bar")

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
                color_plate = QPushButton(self.pcm)
                self.cr.create_button(color_plate, x, y, 25, 25, 12)

                color_plate.setPalette(pal)
                self.color_plates.append(color_plate)
                if i == 9:
                    x = 10
                    y += 40
                else:
                    x += 30


            self.save_color_plate = QPushButton(self.pcm)
            self.cr.create_button(self.save_color_plate, 10, 80, 300, 30, 16)
            self.save_color_plate.setText(self.ed_col_pl)
            self.save_color_plate.clicked.connect(lambda: self.save_color(self.red_txt.text(),
                                                                       self.green_txt.text(),
                                                                       self.blue_txt.text()))

            self.load_colors()

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
            self.lbl1.setText(self.font_setting)
            self.cr.create_textline(self.lbl1, self.num_x_font, self.num_x2_font, 200, 45, 16)
            self.color_lbl.setText(self.color_setting)
            self.color_btn.setText(self.clr_text)
            self.cr.create_textline(self.color_btn, self.clr_x, 120, 100, 30, 16)

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