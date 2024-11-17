import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

from navigation_controller import NavigationController
from ccmd_manager import CcmdWidgets
from visuals import VisualApplier

import ctypes
from ctypes import wintypes


""" SET UP CONSTANTS """
dwmapi = ctypes.windll.dwmapi
DWMWA_CAPTION_COLOR = 35
WM_SYSCOMMAND = 0x0112
SC_MINIMIZE = 0xF020

""" CHANGE TITLE-BAR COLOR """
def set_title_bar_color(hwnd, color):
    color = wintypes.DWORD(color)
    hwnd = wintypes.HWND(hwnd)  # Ensure hwnd is a valid HWND type
    dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_CAPTION_COLOR, ctypes.byref(color), ctypes.sizeof(color))


class MainWindow(QMainWindow):
    def __init__(self):

        """ LOAD UI FILE, SET UP TITLE-BAR """
        super(MainWindow, self).__init__()
        hwnd = int(self.winId())
        title_bar_color = 0x00151515  # Format is 0x00BBGGRR
        set_title_bar_color(hwnd, title_bar_color)

        loadUi("cf-mainwindow.ui", self)

        """ SET UP METHODS FROM VISUALS.PY """
        self.vis = VisualApplier(self.home_button, self.cmd_button)
        self.vis.applyShadow(30, 0, 0, 0, 90, 7, 0, self.ccmd_side_bar)

        """ SET UP NAVIGATOR, PUSH DEFAULT PAGE WITH LAUNCH 
        (CURRENTLY HOME PAGE)"""
        self.navigator = NavigationController(self.pageZone, self.vis, self.home_button, self.cmd_button)
        self.navigator.home_active()

        """ SET UP COMMAND WIDGETS """
        self.ccmd_manager = CcmdWidgets(self.ccmd_zone)

        """ BUTTONS CONNECTIONS """
        self.add_ccmd_button.clicked.connect(lambda: self.ccmd_manager.create_ccmd("test card", 993))
        self.home_button.clicked.connect(self.navigator.home_active)
        self.cmd_button.clicked.connect(self.navigator.cmd_active)


# Launch the application
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.setWindowTitle("command-flow")
main_window.setWindowIcon(QIcon(":/icons/home-icon-qt.png"))
main_window.show()
app.exec_()