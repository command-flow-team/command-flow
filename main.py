import sys
import resources
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from navigation_controller import NavigationController
from ccmd_mng import CcmdWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        loadUi("command-flow-main-window.ui", self)
        
        # Initialize variables for dragging (Title bar)
        self.mouse_dragging = False
        self.drag_position = QPoint()

        # Set up NavigationController, push default page with launch
        self.navigator = NavigationController(self.pageZone)
        self.navigator.go_to_default()
        self.home_active()

        # Initialize ccmd_widgets and connect button
        self.ccmd_manager = CcmdWidgets(self.ccmd_zone)

        # Button connections
        self.add_ccmd_button.clicked.connect(lambda: self.ccmd_manager.create_ccmd("test card", 993))
        self.home_button.clicked.connect(self.home_active)
        self.cmd_button.clicked.connect(self.cmd_active)
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 90))
        shadow.setOffset(7, 0)
        self.ccmd_side_bar.setGraphicsEffect(shadow)


    # Active page methods
    def home_active(self):
        self.navigator.go_to_home()
        self.icons_update("home")
    
    def cmd_active(self):
        self.navigator.go_to_command()
        self.icons_update("cmd")

    def icons_update(self, active_tab):
        """Updates the stylesheets of sidebar icons based on the active page"""
        if active_tab == "home":
            self.home_button.setStyleSheet("""
                QPushButton 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/home-icon-qt.png);
                    background-repeat: no-repeat;

                }
                QPushButton:hover 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/home-icon-qt-hover.png);
                    background-repeat: no-repeat;
                }
                QPushButton:pressed {
                    border-radius: 0px;
                    border-image: url(:/icons/home-icon-qt-pressed.png);
                    background-repeat: no-repeat;
                }
            """)
            self.cmd_button.setStyleSheet("""
                QPushButton 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/command-icon-qt-inactive.png);
                    width: 32px;
                    height: 32px;
                    background-repeat: no-repeat;

                }
                QPushButton:hover 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/command-icon-qt-inactive-hover.png);
                    background-repeat: no-repeat;
                }
                QPushButton:pressed {
                    border-radius: 0px;
                    border-image: url(:/icons/command-icon-qt-pressed.png);
                    background-repeat: no-repeat;
                }
            """)
        elif active_tab == "cmd":
            self.home_button.setStyleSheet("""
                QPushButton 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/home-icon-qt-inactive.png);
                    background-repeat: no-repeat;

                }
                QPushButton:hover 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/home-icon-qt-inactive-hover.png);
                    background-repeat: no-repeat;
                }
                QPushButton:pressed {
                    border-radius: 0px;
                    border-image: url(:/icons/home-icon-qt-pressed.png);
                    background-repeat: no-repeat;
                }
            """)
            self.cmd_button.setStyleSheet("""
                QPushButton 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/command-icon-qt.png);
                    background-repeat: no-repeat;

                }
                QPushButton:hover 
                {
                    border-radius: 0px;
                    border-image: url(:/icons/command-icon-qt-hover.png);
                    background-repeat: no-repeat;
                }
                QPushButton:pressed {
                    border-radius: 0px;
                    border-image: url(:/icons/command-icon-qt-pressed.png);
                    background-repeat: no-repeat;
                }
            """)

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