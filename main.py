from tkinter import *


class Root:
    """Инициализация приложения, открытие"""

    def init(self):
        self.root = Tk()
        self.root.title("Графический интерфейс чата")
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        '''Переменные'''

        self.message_send = ''

        '''Настройка поля для отправки сообщения'''
        self.entry = Entry(bd=1, width=40)
        self.entry.place(x=350, y=540)

        """Настойка кнопок"""
        self.b_send = Button(self.root, bd=0, width=80, height=80)
        self.b_send.place(x=620, y=490)

        self.b_zakr = Button(self.root, bd=0, command=lambda: print("Нажата кнопка закрепить!"), width=60, height=60)
        self.b_zakr.place(x=690, y=490)


class Send_mes_button(Root):  # В скобках вы указуете от какого класса наследовать (в данном случае о т Root)
    def __init__(self):
        self.init()
        self.b_send.config(command=self.send)

    def send(self):
        self.message_send = self.entry.get()
        print(self.message_send)


Send_mes_button().send()
Root().__init__()