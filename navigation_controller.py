from PyQt5.QtWidgets import QStackedWidget


class NavigationController:
    def __init__(self, stacked_widget: QStackedWidget):
        self.stacked_widget = stacked_widget

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_command(self):
        self.stacked_widget.setCurrentIndex(1)
