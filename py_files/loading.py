from PyQt5.QtGui import QPalette, QColor

from ui import *


class Loading(UI):
    def __init__(self):
        self.color_plates = None
        self.color_conf = None
        self.groupbox3 = None
        self.filter_time = None
        self.filter_category = None
        self.filter_status = None
        self.filter_Rate = None
        self.filter_name = None
        self.config = None

    def load_colors(self):
        for i in range(1, 21):
            try:
                hex_color = (self.color_conf["user_colors"]["col" + str(i)])[1:]
                hex_tuple = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                red = hex_tuple[0]
                green = hex_tuple[1]
                blue = hex_tuple[2]
                
                pal = QPalette()
                pal.setColor(QPalette.Button, QColor(red, green, blue))
                self.color_plates[i-1].setPalette(pal)
            except Exception as e:
                print(e)

    def load_styles(self):
            borderStyle = "QTableWidget::item {border: 1px outset " + self.color_conf["user_colors"]["table_borders"] \
                          + ";}"
            cellsStyle = "QTableWidget{background-color: " + self.color_conf["user_colors"]["table_cells"] + ";}"
            headStyle = "QHeaderView::section{background-color: " + self.color_conf["user_colors"]["table_head"] + ";}"
            self.table.setStyleSheet(borderStyle + cellsStyle + headStyle)



            pbar_style = """
                                                    QProgressBar {
                                                            border: 2px solid gray; 
                                                            border-radius: 5px;
                                                            text-align: center;
                                                            font-size: 10px;
                                                    }
                                                    QProgressBar::chunk {
                                                            background-color: """ + self.color_conf["user_colors"][
                "progress_bar"] + ";""""
                                                            width: 10px;
                                                            margin: 0.5px;
                                                    }
                                            """
            self.pbar.setStyleSheet(pbar_style)

            newColor = "QMenuBar{background-color: " + self.color_conf["user_colors"]["menu_bar"] + ";}"
            self.menubar.setStyleSheet(newColor)

    def load_settings(self):
        if self.config["application"]["filter_name"] == '1':
            self.filter_name.setChecked(False)
        else:
            self.filter_name.setChecked(True)

        if self.config["application"]["filter_Rate"] == '1':
            self.filter_Rate.setChecked(False)
        else:
            self.filter_Rate.setChecked(True)

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