import sys
import resources
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from navigation_controller import NavigationController
from ccmd_manager import CcmdWidgets
from visuals import VisualApplier


class MainWindow(QMainWindow):
    def __init__(self):

        """ LOAD UI FILE, SET UP VARIABLES FOR DRAGGING, 
        SET UP CUSTOM SIDE-BAR """
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi("command-flow-main-window.ui", self)
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
        self.btn_minimize.clicked.connect(self.showMinimized)

    
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
main_window.setFixedWidth(800)
main_window.setFixedHeight(600)

app.exec_()