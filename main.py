from PyQt5 import QtWidgets
from PyQt5 import uic
import sqlite3


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.coffee)

    def coffee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        self.res = cur.execute('''SELECT * FROM cofe''').fetchall()
        for i in self.res:
            self.listWidget.addItem(str(i))
        con.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())
