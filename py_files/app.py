import os
import sys, configparser
from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox, qApp)
from options import *
from system import *
from saving import *
from loading import *
from adding import *
from deleting import *
from distutils.dir_util import copy_tree


class App(QMainWindow, Options, Systems, Saving, Loading, Adding, Deleting, Creating):
    def __init__(self):
        super().__init__()

        self.program_path = os.path.dirname(os.path.realpath(__file__))

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
        self.color_conf = configparser.ConfigParser()
        self.config.read(os.path.abspath(self.program_path + '\\data\\config.ini'))
        self.color_conf.read(os.path.abspath(self.program_path + '\\data\\color_data.ini'))
        self.load_settings()
        self.load_styles()

        if self.config["application"]["language"] == 'rus':
            self.Current_lan = "Русский"
            self.change_language(self.Current_lan)

        if self.config["application"]["language"] == 'eng':
            self.Current_lan = "English"
            self.change_language(self.Current_lan)

    def closeEvent(self, event):
        # Program Closing window
        close = QMessageBox.question(self,
                                     self.exit_word,
                                     self.exit_sentence,
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if close == QMessageBox.Yes:
            self.save_settings()
            self.save_func()
            event.accept()
        if close == QMessageBox.No:
            event.accept()
        if close == QMessageBox.Cancel:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    APPLICATION = App()
    APPLICATION.show()
    sys.exit(app.exec_())
