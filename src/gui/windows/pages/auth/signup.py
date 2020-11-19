"""
    created at nov 18/2020 by Mmd4LIFE
    - signup page
"""

from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton
)
from PyQt5.QtCore import Qt

from gui.styles.pages.signup_styles import *


class SignUp(QWidget):

    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent=parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setContentsMargins(0, 0, 0, 0)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addStretch(0)
        self.main_layout.setAlignment(Qt.AlignHCenter)

        self.__init_ui__()

    def __init_ui__(self):
        self._add_textboxs_()
        self._add_btn_signup_()
        self._add_btn_register_account_()

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

    def _add_btn_signup_(self):
        btn_signup = QPushButton("sign up")
        btn_signup.setAccessibleName(btn_signup_style[0])
        btn_signup.setStyleSheet(btn_signup_style[1])

        def btn_register_clicked():
            username: str = self.username_edit_text.text()
            password: str = self.password_edit_text.text()

            from modules.data.data_context import User
            from datetime import datetime
            from ....components.message_box import MessageBox

            try:
                if username != "" and password != "":
                    User.create(
                        username=username,
                        password=password,
                        created_time=datetime.now()
                    )
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

        btn_signup.clicked.connect(btn_register_clicked)

        self.main_layout.addWidget(btn_signup)

    def _add_btn_register_account_(self):
        btn_goto_register_page = QPushButton("Register ?")
        btn_goto_register_page.setAccessibleName(btn_goto_register_page_style[0])
        btn_goto_register_page.setStyleSheet(btn_goto_register_page_style[1])
        btn_goto_register_page.setContentsMargins(0, 0, 0, 0)

        def change_page_to_register():
            self.set_visibility(False)
            self.signin_page.set_visibility(True)

        btn_goto_register_page.clicked.connect(change_page_to_register)

        self.main_layout.addWidget(btn_goto_register_page)

    def set_visibility(self, visible: bool):
        if visible:
            self.show()
        else:
            self.hide()

    def set_sign_in_page(self, signin: object):
        self.signin_page = signin
