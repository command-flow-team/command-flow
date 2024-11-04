from PyQt5.QtWidgets import QLabel, QVBoxLayout

class ccmd_widgets:
    def __init__(self):
        self.layout = None

    def create_ccmd(self, workzone):
        # Check if layout exists, if not, create a QVBoxLayout for workzone
        if not self.layout:
            self.layout = QVBoxLayout(workzone)
            workzone.setLayout(self.layout)
        
        # Create and add a new command card (QLabel) to the layout
        new_ccmd = QLabel("New card")
        new_ccmd.setStyleSheet("font: 700 italic 14pt \"Munson\"; color: white;")
        self.layout.addWidget(new_ccmd)