# -*- coding: utf-8 -*-
"""

    Creator: Yaroslav Kikel
    Finished: 19th May 2019 year 

"""
import sys
import sqlite3
#import help

from notes import *
from PyQt5 import QtCore, QtGui, QtWidgets

#help.create_db()
#help.write_none_values_db()

def read_db(textEditId):
    con = sqlite3.connect('saves/saves.db')
    cur = con.cursor()

    query = 'SELECT body FROM notes WHERE id =' + str(textEditId)

    cur.execute(query)
    text = cur.fetchall()
    new_text = []

    for elem in text:
        new_text.append(elem[0])
    text = ''.join(new_text)
    del(new_text)

    cur.close()
    con.close()

    return text

def update_db(textEditId, value):
    con = sqlite3.connect('saves/saves.db')
    cur = con.cursor()

    query = 'UPDATE notes SET body = ' + "'" + str(value) + "'" + ' WHERE id = ' + str(textEditId)

    cur.execute(query)
    con.commit()

    cur.close()
    con.close()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.pushButton.clicked.connect(self.MyFunction)
        
        #write elements from db
        self.ui.textEdit.setText(str(read_db(1)))
        self.ui.textEdit_2.setText(str(read_db(2)))
        self.ui.textEdit_3.setText(str(read_db(3)))
        self.ui.textEdit_4.setText(str(read_db(4)))
                 
    def MyFunction(self):
        #save elements into db
        elem1 = self.ui.textEdit.toPlainText()
        elem2 = self.ui.textEdit_2.toPlainText()
        elem3 = self.ui.textEdit_3.toPlainText()
        elem4 = self.ui.textEdit_4.toPlainText()

        update_db(1, elem1)
        update_db(2, elem2)
        update_db(3, elem3)
        update_db(4, elem4)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())