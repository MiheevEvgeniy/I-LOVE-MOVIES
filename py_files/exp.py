from PyQt5 import QtCore, QtWidgets


class SliderProxyStyle(QtWidgets.QProxyStyle):
    def pixelMetric(self, metric, option, widget):
        if metric == QtWidgets.QStyle.PM_SliderThickness:
            return 40
        elif metric == QtWidgets.QStyle.PM_SliderLength:
            return 40
        return super().pixelMetric(metric, option, widget)


class TestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)

        style = SliderProxyStyle(self.slider.style())
        self.slider.setStyle(style)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.slider)
        lay.addStretch()


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    w = TestWindow()
    w.show()
    app.exec_()