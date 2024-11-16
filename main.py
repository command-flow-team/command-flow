import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from navigation_controller import NavigationController
from ccmd_manager import CcmdWidgets
from visuals import VisualApplier

import win32gui
import win32con
import win32api
import ctypes
from ctypes import wintypes

dwmapi = ctypes.windll.dwmapi
DWMWA_CAPTION_COLOR = 35

def set_title_bar_color(hwnd, color):
    color = wintypes.DWORD(color)
    hwnd = wintypes.HWND(hwnd)  # Ensure hwnd is a valid HWND type
    dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_CAPTION_COLOR, ctypes.byref(color), ctypes.sizeof(color))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlag(Qt.WindowTitleHint, False)
        self.setAttribute(Qt.WA_TranslucentBackground)
        hwnd = int(self.winId())
        title_bar_color = 0x00151515  # Format is 0x00BBGGRR
        set_title_bar_color(hwnd, title_bar_color)

        loadUi("cf-mainwindow.ui", self)
        self.mouse_dragging = False
        self.drag_position = QPoint()

        # Initialize visual styles and navigation
        self.vis = VisualApplier(self.home_button, self.cmd_button)
        self.vis.applyShadow(30, 0, 0, 0, 90, 7, 0, self.ccmd_side_bar)

        # Setup navigator and home page
        self.navigator = NavigationController(self.pageZone, self.vis, self.home_button, self.cmd_button)
        self.navigator.home_active()

        # Setup command widgets
        self.ccmd_manager = CcmdWidgets(self.ccmd_zone)

        # Connect buttons
        self.add_ccmd_button.clicked.connect(lambda: self.ccmd_manager.create_ccmd("test card", 993))
        self.home_button.clicked.connect(self.navigator.home_active)
        self.cmd_button.clicked.connect(self.navigator.cmd_active)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.minimize_window_animation)
        self.btn_maximize.clicked.connect(self.maximize_window)

    def get_hwnd(self):
        return int(self.winId())

    def minimize_window_animation(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(100)
        self.animation.setStartValue(1.0)  
        self.animation.setEndValue(0.0)   
        
        self.animation.finished.connect(self.showMinimized)
        self.animation.start()

    def showEvent(self, event):
        self.setWindowOpacity(1.0)
        super().showEvent(event)

    def maximize_window(self):
        if self.isMaximized():
            self.showNormal()  # Restores the window if it is maximized.
        else:
            self.showMaximized()  # Maximizes the window if it is not maximized.

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.title_bar.geometry().contains(event.pos()):
            self.mouse_dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.mouse_dragging:
            self.move(event.globalPos() - self.drag_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_dragging = False

# Launch the application
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()