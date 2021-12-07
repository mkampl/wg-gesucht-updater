#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore 
from datetime import datetime

from wggesuchtupdate import refresh_wg_gesucht

class WG_Gesucht_Updater(QWidget):
    def __init__(self,parent = None):
        super(WG_Gesucht_Updater,self).__init__(parent)
        self.layout = QHBoxLayout()

        self.l_form = QFormLayout()
        self.e_id = QLineEdit("Offer ID")
        self.l_form.addRow("ID", self.e_id)
        self.e_user = QLineEdit("my user")
        self.l_form.addRow("user", self.e_user)
        self.e_pw = QLineEdit("my pw")
        self.l_form.addRow("pw", self.e_pw)


        self.b_Update   = QPushButton('Update')
        self.b_Update.clicked.connect(self.btnUpdate)
        self.l_form.addRow(self.b_Update)


        self.b_Close   = QPushButton('Close')
        self.b_Close.clicked.connect(self.btnClose)
        self.l_form.addRow(self.b_Close)


        self.layout.addLayout(self.l_form)
        self.setLayout(self.layout)
        self.setWindowTitle("WG Gesucht - Updater")


    def btnUpdate(self):
        print("Update Button pressed")
        self.b_Update.setEnabled(False)
        refresh_wg_gesucht(self.e_id.text(),self.e_user.text(),self.e_pw.text())
        now = datetime.now()
        current_time = now.strftime("%d.%m.%Y - %H:%M:%S")
        print("Updated at =", current_time)
        self.b_Update.setEnabled(True)

    def btnClose(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WG_Gesucht_Updater()
    ex.show()
    sys.exit(app.exec_())
