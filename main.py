import sys
import resources
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from navigation_controller import NavigationController
from ccmd_mng import ccmd_widgets


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi("command-flow-main-window.ui", self)
        self.ccmd_zone.setStyleSheet('''border-radius: 7px; background-color: #2C3037;''')

        # Set up NavigationController
        self.navigator = NavigationController(self.pageZone)
        self.navigator.go_to_default()

        # Initialize ccmd_widgets and connect button
        self.ccmd_manager = ccmd_widgets(self.ccmd_zone)
        self.add_ccmd_button.clicked.connect(lambda: self.ccmd_manager.create_ccmd("test card", 993))

        # Button connections
        self.home_button.clicked.connect(self.navigator.go_to_home)
        self.cmd_button.clicked.connect(self.navigator.go_to_command)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        # Initialize variables for dragging (Title bar)
        self.mouse_dragging = False
        self.drag_position = QPoint()

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


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.setFixedWidth(800)
main_window.setFixedHeight(600)

app.exec_()