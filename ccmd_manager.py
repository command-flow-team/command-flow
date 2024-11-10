from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt

class CommandCard(QWidget):
    def __init__(self, label_text, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # set up layout for different cards
        layout = QVBoxLayout()
        
        # test ccmd label set up
        self.label = QLabel(label_text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px;")  # Increase font size for better readability
        layout.addWidget(self.label)
        
        # test ccmd number set up
        self.number_label = QLabel(str(number))
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet("font-size: 12px;")  # Increase font size
        layout.addWidget(self.number_label)
        
        self.setLayout(layout)
        
        self.setStyleSheet("background-color: #151515; padding: 15px; color: white; font: 600 24pt \"Afacad Flux\";")  # Increase padding
        self.setFixedSize(140, 200)  # Adjust size as needed (width, height)

class CcmdWidgets:
    def __init__(self, workzone):
        # main layout
        self.layout = QVBoxLayout()
        
        # configure a scroll area for scrolling through cards
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # widget to hold the layout and set it as the scroll area's widget
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setStyleSheet('''
            QScrollBar:vertical {
                background: #141414;
                width: 15px;
                margin: 22px 0 22px 0;
            }
            QScrollBar::handle:vertical {
                background: #757575;
                min-height: 20px;
                border-radius: 3px;
            }
            QScrollBar::add-line:vertical {
                background: #141414;
                height: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                background: #141414;
                height: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                width: 3px;
                height: 3px;
                background: #757575;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }''')

        # scroll area in the workzone
        workzone_layout = QVBoxLayout(workzone)
        workzone_layout.addWidget(self.scroll_area)

    def create_ccmd(self, label_text, number):
        # create an instance of CommandCard with label and number
        command_card = CommandCard(label_text, number)
        self.layout.addWidget(command_card)