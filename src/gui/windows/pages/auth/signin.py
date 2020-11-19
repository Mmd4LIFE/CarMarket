"""
    created at nov 18/2020 by Mmd4LIFE
    - signin page
"""

from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton
)
from PyQt5.QtCore import Qt

from gui.styles.pages.signin_styles import *

from functools import partial


class SingIn(QWidget):

    def __init__(self, parent=None):
        super(SingIn, self).__init__(parent=parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setContentsMargins(0, 0, 0, 0)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addStretch(0)
        self.main_layout.setAlignment(Qt.AlignHCenter)

        self.__init_ui__()

    def __init_ui__(self):
        self._add_textboxs_()
        self._add_forgot_password_()
        self._add_btn_login_()
        self._add_btn_create_account_()
        self.setLayout(self.main_layout)

    def _add_textboxs_(self):

        self.username_edit_text = QLineEdit()
        self.username_edit_text.setPlaceholderText("Enter UserName")
        self.username_edit_text.setAccessibleName(q_edit_text_style[0])
        self.username_edit_text.setStyleSheet(q_edit_text_style[1])

        self.main_layout.addWidget(self.username_edit_text)

        self.password_edit_text = QLineEdit()
        self.password_edit_text.setPlaceholderText("Enter Password")
        self.password_edit_text.setAccessibleName(q_edit_text_style[0])
        self.password_edit_text.setStyleSheet(q_edit_text_style[1])

        self.main_layout.addWidget(self.password_edit_text)

    def _add_forgot_password_(self):
        btn_forgot_password = QPushButton("Forgot password?")
        btn_forgot_password.setAccessibleName(btn_forgot_password_style[0])
        btn_forgot_password.setStyleSheet(btn_forgot_password_style[1])

        self.main_layout.addWidget(btn_forgot_password)

    def _add_btn_login_(self):
        btn_login = QPushButton("Login")
        btn_login.setAccessibleName(btn_login_style[0])
        btn_login.setStyleSheet(btn_login_style[1])

        def btn_login_clicked():
            username: str = self.username_edit_text.text()
            password: str = self.password_edit_text.text()

            from modules.data.data_context import User
            from gui.components.message_box import MessageBox

            try:
                if username != "" and password != "":
                    user = User.select().where(
                        (User.username == username) & (User.password == password)
                    )
                    if len(user) > 0:
                        MessageBox(
                            title="Sucess",
                            message="Welcome " + username
                        ).show()
                    else:
                        MessageBox(
                            title="Not Sucess",
                            message="UnAuthorized"
                        ).show()
                else:
                    MessageBox(
                    title="Error",
                    message=str("please fill both of username and password")
                ).show()

            except Exception as error:
                MessageBox(
                    title="Error",
                    message=str(error)
                ).show()

        btn_login.clicked.connect(btn_login_clicked)
        self.main_layout.addWidget(btn_login)

    def _add_btn_create_account_(self):
        btn_create_account = QPushButton("Create new account ?")
        btn_create_account.setAccessibleName(btn_create_account_style[0])
        btn_create_account.setStyleSheet(btn_create_account_style[1])
        btn_create_account.setContentsMargins(0, 0, 0, 0)

        def clicked_create_account():
            self.set_visibility(False)
            self.signup_page.set_visibility(True)

        btn_create_account.clicked.connect(clicked_create_account)

        self.main_layout.addWidget(btn_create_account)

    def set_visibility(self, visible: bool):
        if visible:
            self.show()
        else:
            self.hide()

    def set_sign_up_page(self, signup: object):
        self.signup_page = signup
