import sys
import resources
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QSizePolicy


class VisualApplier:
    def __init__(self, home_button, cmd_button):
        self.home_button = home_button
        self.cmd_button = cmd_button

    """ APPLY SHADOWS FOR WIDGETS """
    def applyShadow(self, blur, r, g, b, alpha, dx, dy, cwidget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blur)
        shadow.setColor(QColor(r, g, b, alpha))
        shadow.setOffset(dx, dy)
        cwidget.setGraphicsEffect(shadow)


    """ UPDATING ICONS IN APP """
    def active_tab_icons_update(self, active_tab):

        """ Updates icons through changing their stylesheets, based
         on the active tab. """
        if active_tab == "home_page":
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
        elif active_tab == "cmd_page":
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
        