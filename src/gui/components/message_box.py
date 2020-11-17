"""
    created at nov 18/2020 by Mmd4LIFE
    - message box for register
"""

from PyQt5.QtWidgets import QMessageBox


class MessageBox:

    def __init__(self, message: str, title: str):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle(title)
        self.msg.setInformativeText(message)

    def show(self):
        self.msg.exec_()
