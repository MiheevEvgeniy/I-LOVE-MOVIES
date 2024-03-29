
from creating import *
import tkinter
from PyQt5.QtWidgets import (QLineEdit, QProgressBar,
                             QPushButton, QTableWidget, QComboBox,
                             QListWidget, QGroupBox, QCheckBox)
from PyQt5.QtGui import QIcon


class UI(object):
    def __init__(self):
        self.program_path = None

    def init_UI(self, MW):
        # Main window
        self.cr = Creating()
        root = tkinter.Tk()

        self.WIDTH = 1120
        self.HEIGHT =600
        self.center_w = int(root.winfo_reqwidth()*1.5)
        self.center_h = int(root.winfo_reqheight()*1.5)
        MW.setGeometry(self.center_w, self.center_h, self.WIDTH, self.HEIGHT)
        MW.setWindowTitle("I.L.M. - I LOVE MOVIES v0.4")
        MW.setWindowIcon(QIcon(self.program_path +"\\textures\\ILF.ico"))
        MW.setFixedSize(self.WIDTH, self.HEIGHT)

        # Main lines (Name, Rate, Status, Category)
        # Name
        self.txt1 = QLineEdit(self)
        self.cr.create_textline(self.txt1, 20, 30, 200, 30, 16)

        # Rate
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
        self.table.setRowCount(0)
        self.table.move(20, 240)

        L = (self.WIDTH - 35)
        LENGTH_Name = L * 0.45
        LENGTH_Rate = L * 0.1
        LENGTH_Status = L * 0.15
        LENGTH_Category = L * 0.15
        LENGTH_Date = L * 0.12

        self.table.setColumnWidth(0, int(LENGTH_Name))
        self.table.setColumnWidth(1, int(LENGTH_Rate))
        self.table.setColumnWidth(2, int(LENGTH_Status))
        self.table.setColumnWidth(3, int(LENGTH_Category))
        self.table.setColumnWidth(4, int(LENGTH_Date))

        self.table.setMinimumWidth(L)
        self.table.setMinimumHeight(self.HEIGHT - 250)

        self.borderStyle = "QTableWidget::item {border: 1px outset gray;}"
        self.cellsStyle = "QTableWidget{background-color: white;}"
        self.headStyle = "QHeaderView::section{background-color: white}"
        self.table.setStyleSheet(self.borderStyle + self.cellsStyle+ self.headStyle)

        # Button
        self.btn1 = QPushButton(MW)
        self.cr.create_button(self.btn1, 40, 175, 160, 30, 16)

        # Check boxes
        self.type_adding_btn = QCheckBox(MW)
        self.cr.create_textline(self.type_adding_btn, 25, 205, 200, 30, 14)

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

        background = (self.program_path + "\\textures\\background.jpg").replace('\\', '/')
        MW.setStyleSheet("""
                            QMainWindow {
                                background-image: url(""" + background + """);  
                            }
                        """)
        # Terminal for searching results
        self.search_terminal = QListWidget(MW)
        self.cr.create_textline(self.search_terminal, 480, 30, 335, 190, 14)
