from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QGroupBox
from PyQt5.QtCore import Qt
import napari

class Napari(QWidget):
    def __init__(self):
        super().__init__()
        # 1. Define page objects
        self.button = QPushButton("Open", self)
        self.button.clicked.connect(self.open_napari)
        
        # 2. Define page objects layout
        layout = QVBoxLayout()
        groupbox = QGroupBox("Open napari to visualize image(s) and/or mask(s)")
        layout2 = QVBoxLayout()
        layout2.addWidget(self.button, alignment=Qt.AlignCenter)
        groupbox.setLayout(layout2)
        layout.addWidget(groupbox)
        self.setLayout(layout)


    def open_napari(self):
        """
        Open an empty napari window
        """
        viewer = napari.Viewer()
        viewer.show(block=True)