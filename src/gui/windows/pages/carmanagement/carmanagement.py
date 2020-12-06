"""
    created at nov 19/2020 by Mmd4LIFE
    - car management page
"""

from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QHBoxLayout,
    QPushButton
)
from PyQt5.QtCore import Qt

from gui.styles.pages.carmanagement_styles import *

class CarManage(QWidget):

    def __init__(self, parent=None):
        super(CarManage, self).__init__(parent=parent)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setContentsMargins(0, 0, 0, 0)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 500, 200)
        self.main_layout.addStretch(0)
        self.main_layout.setAlignment(Qt.AlignHCenter)

        self.__init_ui__()

    def __init_ui__(self):
        self._add_btn_add_new_car_()
        self._add_btn_update_selected_()
        self._add_btn_delete_selected_()
        self.setLayout(self.main_layout)

    def _add_btn_add_new_car_(self):
        btn_add_new_car = QPushButton("Add New Car")
        btn_add_new_car.setAccessibleName(btn_add_new_car_style[0])
        btn_add_new_car.setStyleSheet(btn_add_new_car_style[1])

        self.main_layout.addWidget(btn_add_new_car)

    def _add_btn_update_selected_(self):
        btn_update_selected = QPushButton("Update Selected")
        btn_update_selected.setAccessibleName(btn_update_selected_styles[0])
        btn_update_selected.setStyleSheet(btn_update_selected_styles[1])

        self.main_layout.addWidget(btn_update_selected)

    def _add_btn_delete_selected_(self):
        btn_delete_selected = QPushButton("Delete Selected")
        btn_delete_selected.setAccessibleName(btn_delete_selected_styles[0])
        btn_delete_selected.setStyleSheet(btn_delete_selected_styles[1])

        self.main_layout.addWidget(btn_delete_selected)


