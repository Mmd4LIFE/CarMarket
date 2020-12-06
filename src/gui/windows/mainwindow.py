"""
    created at nov 18/2020 by Mmd4LIFE
    - main window for authentication
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QGridLayout,
    QApplication, QLabel
)
from PyQt5.QtGui import QFont

from modules.data.data_context import AppContext
from gui.styles.windows.mainwindow_styles import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setWindowTitle("Auth page")
        self.setMinimumSize(350, 600)
        self.setMaximumSize(350, 600)

        screen_size = QApplication.desktop().geometry()
        self.setGeometry(
            int((screen_size.width() - 350) / 2),
            int((screen_size.height() - 600) / 2),
            0, 0
        )

        self.setContentsMargins(0, 0, 0, 0)

        self.setAccessibleName(main_window_style[0])
        self.setStyleSheet(main_window_style[1])

        self.__set_centeral_widget_config__()

    def __set_centeral_widget_config__(self):
        self.car_market_logo()
        main_widget = QWidget(self)
        main_widget.setContentsMargins(0, 0, 0, 0)

        main_widget_layout = QGridLayout(main_widget)
        main_widget_layout.setContentsMargins(0, 0, 0, 0)

        from .pages.auth.signin import SingIn
        from .pages.auth.signup import SignUp

        signin_page = SingIn(parent=self)
        signin_page.set_visibility(False)
        signup_page = SignUp(parent=self)
        signup_page.set_visibility(True)

        signin_page.set_sign_up_page(signup_page)
        signup_page.set_sign_in_page(signin_page)

        main_widget_layout.addWidget(signin_page)
        main_widget_layout.addWidget(signup_page)

        self.setCentralWidget(main_widget)

    #TODO -> set CarMarket Logo
    def car_market_logo(self):
        Logo = QLabel(self)
        Logo.setText("CarMarket")
        Logo.setFont(QFont('Times', 25))
        Logo.setAccessibleName(lable_car_market_logo_style[0])
        Logo.setStyleSheet(lable_car_market_logo_style[1])
    

    def execute_app(self):
        AppContext()

        self.show()


