from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

class CommandDesk(QWidget):
    def __init__(self, label_text, description_text, status_text, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup main layout
        mainLayout = QVBoxLayout(self)

        # Horizontal layout for dot and texts
        titleLayout = QHBoxLayout()
        mainLayout.addLayout(titleLayout)

        # Dot label
        dotLabel = QLabel(self)
        dotLabel.setFixedSize(12, 12)
        dotLabel.setStyleSheet("background-color: #009B72; border-radius: 5px;")
        titleLayout.addWidget(dotLabel)
       

        # Vertical layout for text beside the dot
        textLayout = QVBoxLayout()
        titleLayout.addLayout(textLayout)

        # Title label
        titleLabel = QLabel(label_text, self)
        titleLabel.setStyleSheet("font: 600 38px \"Afacad Flux\"; color: white;")
        textLayout.addWidget(titleLabel)

        # Horizontal layout for description and status
        descLayout = QHBoxLayout()
        textLayout.addLayout(descLayout)

        # Status label
        statusLabel = QLabel(status_text, self)
        statusLabel.setStyleSheet("background-color: #009B72; font: 600 38px \"Afacad Flux\"; color: white;")
        statusLabel.setFixedWidth(170)
        statusLabel.setAlignment(Qt.AlignCenter)
        descLayout.addWidget(statusLabel)

        # Description label
        descLabel = QLabel(description_text, self)
        descLabel.setStyleSheet("font: 600 22px \"Afacad Flux\"; color: white;")
        descLayout.addWidget(descLabel)

        self.setStyleSheet("background: rgba(255, 255, 255, 0); border-radius: 10px;")
        self.setFixedHeight(115)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(255, 255, 255, 6))  # Semi-transparent black for background
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 20, 20)  # Rounded corners

    """ DOUBLE CLICK EVENT """
    def mouseDoubleClickEvent(self, event):
        # Signal or direct call to create a new desk
        print("Desk double-clicked!")  # Placeholder for action

class CDeskWidget:
    def __init__(self, workzone):
        self.layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)


        self.scroll_area.setStyleSheet('''
            QScrollBar:vertical {
                background: #141414;
                width: 15px;
                margin: 22px 0 22px 0;
                border-radius: 3px;
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
                border-radius: 3px;
            }

            QScrollBar::sub-line:vertical {
                background: #141414;
                height: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
                border-radius: 3px;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                width: 3px;
                height: 3px;
                background: #757575;
                border-radius: 3px;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }''')

        # Scroll area in the workzone
        workzone_layout = QVBoxLayout(workzone)
        workzone_layout.addWidget(self.scroll_area)

        
    def create_desk(self, desk_name, description, status):
        desk_layout = QHBoxLayout()

        # Hamburger menu to the left
        info_label = QLabel("☰")
        info_label.setFixedSize(40, 40)  # Adjust size as needed
        info_label.setStyleSheet("QLabel { background: rgba(255, 255, 255, 0); color: #757575; }")
        desk_layout.addWidget(info_label)

        # Create an instance of CommandDesk with label, description, and status
        ccmd_desk = CommandDesk(desk_name, description, status)
        desk_layout.addWidget(ccmd_desk)

        # Delete button to the right
        delete_desk_btn = QPushButton("D")
        delete_desk_btn.setFixedSize(50, 60)  # Adjust size as needed
        delete_desk_btn.setStyleSheet("QPushButton { background-color: #009B72; color: white; border-radius: 10px; }")
        delete_desk_btn.clicked.connect(self.printtest)
        desk_layout.addWidget(delete_desk_btn)

        self.layout.addLayout(desk_layout)

    def printtest(self):
        print("something happened!")