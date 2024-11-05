from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtCore import Qt

class CommandCard(QWidget):
    def __init__(self, label_text, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        layout = QVBoxLayout()
        
        self.label = QLabel(label_text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px;")  # Increase font size for better readability
        layout.addWidget(self.label)
        
        self.number_label = QLabel(str(number))
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet("font-size: 14px;")  # Increase font size
        layout.addWidget(self.number_label)
        
        self.setLayout(layout)
        
        self.setStyleSheet("background-color: lightblue; border: 1px solid gray; padding: 15px;")  # Increase padding
        self.setFixedSize(150, 100)  # Adjust size as needed (width, height)

class ccmd_widgets:
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

        # scroll area in the workzone
        workzone_layout = QVBoxLayout(workzone)
        workzone_layout.addWidget(self.scroll_area)

    def create_ccmd(self, label_text, number):
        # Create an instance of CommandCard with label and number
        command_card = CommandCard(label_text, number)
        self.layout.addWidget(command_card)