"""
    created at nov 18/2020 by Mmd4LIFE
    - start app from this class
"""

from gui.windows.mainwindow import MainWindow

from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import QApplication


class StartUp:

    def __init__(self):
        self.app = QApplication(sys_argv)
        self.gui_main = MainWindow()

    def start_app(self):
        self.gui_main.execute_app()
        sys_exit(self.app.exec_())

