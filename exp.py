import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DialogDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DialogDemo, self).__init__(parent)
        # Установить заголовок и начальный размер основного интерфейса
        self.setWindowTitle("Пример диалога")
        self.resize(350,300)

        # Создайте кнопку, обратите внимание, что self in () имеет важное значение, используется для загрузки некоторых настроек его свойств
        self.btn=QPushButton(self)
        #Set: текст, позиция перемещения, функция слота ссылки
        self.btn.setText("Всплывающее диалоговое окно")
        self.btn.move(50,50)
        self.btn.clicked.connect(self.showdialog)

    def showdialog(self):
        # Создать объект QDialog
        dialog=QDialog()
        # Создать кнопку для вновь созданного объекта диалога
        btn=QPushButton('ok',dialog)
        # Переместить кнопку, установить заголовок диалога
        btn.move(50,50)
        dialog.setWindowTitle("Dialog")
        # Установите для свойства окна значение ApplicationModal, пользователь может закрыть основной интерфейс только после закрытия всплывающего окна.
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=DialogDemo()
    demo.show()
    sys.exit(app.exec_())