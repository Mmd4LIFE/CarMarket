"""
    created at nov 19/2020 by Mmd4LIFE
    - main window for car market management
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QGridLayout,
    QApplication
)

from gui.styles.windows.managerwindow_styles import *


class ManagerWindow(QMainWindow):

    def __init__(self, parent=None):
        super(ManagerWindow, self).__init__(parent=parent)

        self.setWindowTitle("Manager page")
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            int((screen_size.width() - 800) / 2),
            int((screen_size.height() - 600) / 2),
            0, 0
        )

        self.setContentsMargins(0, 0, 0, 0)

        self.setAccessibleName(manager_window_style[0])
        self.setStyleSheet(manager_window_style[1])

    def __set_centeral_widget_config__(self):
        main_widget = QWidget(self)
        main_widget.setContentsMargins(0, 0, 0, 0)

        main_widget_layout = QGridLayout(main_widget)
        main_widget_layout.setContentsMargins(0, 0, 0, 0)







        




