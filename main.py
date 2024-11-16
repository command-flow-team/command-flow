import sys
import resources
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation, QSize, QEasingCurve
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
from PyQt5.QtWidgets import QSizePolicy

dwmapi = ctypes.windll.dwmapi
DWMWA_CAPTION_COLOR = 35

def set_title_bar_color(hwnd, color):
    color = wintypes.DWORD(color)
    hwnd = wintypes.HWND(hwnd)  # Ensure hwnd is a valid HWND type
    dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_CAPTION_COLOR, ctypes.byref(color), ctypes.sizeof(color))

class MainWindow(QMainWindow):
    def __init__(self):

        """ LOAD UI FILE, SET UP VARIABLES FOR DRAGGING, 
        SET UP CUSTOM SIDE-BAR """
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


        """ SET UP METHODS FROM VISUALS.PY """
        self.vis = VisualApplier(self.home_button, self.cmd_button)
        self.vis.applyShadow(30, 0, 0, 0, 90, 7, 0, self.ccmd_side_bar)

        """ SET UP NAVIGATOR, PUSH DEFAULT PAGE WITH LAUNCH 
        (CURRENTLY HOME PAGE)"""
        self.navigator = NavigationController(self.pageZone, self.vis, self.home_button, self.cmd_button)
        self.navigator.home_active()

        """ FIX ME
        Initialize ccmd_widgets and connect button """
        self.ccmd_manager = CcmdWidgets(self.ccmd_zone)

        """ BUTTONS CONNECTIONS """
        self.add_ccmd_button.clicked.connect(lambda: self.ccmd_manager.create_ccmd("test card", 993))
        self.home_button.clicked.connect(self.navigator.home_active)
        self.cmd_button.clicked.connect(self.navigator.cmd_active)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.minimize_window_animation)
        self.btn_maximize.clicked.connect(self.maximize_window)

    def get_hwnd(self):
        # Convert PyQt5 window ID to Win32 window handle
        return int(self.winId())

    def minimize_window_animation(self):
        hwnd = self.get_hwnd()
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(75)  # Duration of the animation
        self.animation.setStartValue(1.0)  # Start with full opacity
        self.animation.setEndValue(0.0)    # Fade to transparent
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.minimize_window)  # Once the animation is done, hide the window
        self.animation.start()

        

    def minimize_window(self):
        self.showMinimized()
        self.setWindowOpacity(1)

        
        
    def maximize_window(self):
        hwnd = self.get_hwnd()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    
    """ SET UP METHODS FOR DRAGGING, CURRENTLY ONLY TITLE BAR SUPPORTED """
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


""" ESSENTIALS FOR LAUNCHING THE APPLICATION """
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()


app.exec_()