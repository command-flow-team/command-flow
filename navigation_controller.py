from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtGui import QIcon
from visuals import VisualApplier
from PyQt5.QtWidgets import QSizePolicy

class NavigationController:

    default_page = 0
    home_page = 0
    cmd_page = 1

    def __init__(self, stacked_widget: QStackedWidget, vis, home_button, cmd_button):
        self.stacked_widget = stacked_widget
        self.vis = vis
        self.home_button = home_button
        self.cmd_button = cmd_button


    def cmd_active(self):
        self.stacked_widget.setCurrentIndex(self.cmd_page)
        self.vis.active_tab_icons_update("cmd_page")


    def home_active(self):
        self.stacked_widget.setCurrentIndex(self.home_page)
        self.vis.active_tab_icons_update("home_page")
