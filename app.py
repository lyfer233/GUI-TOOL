import sys
from PyQt5.Qt import *
from layout import Ui_MainPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    Layout = Ui_MainPage()
    Layout.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())