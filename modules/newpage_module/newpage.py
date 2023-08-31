from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QComboBox, QFormLayout, QPushButton, QVBoxLayout, QWidget, QAbstractItemView, QGridLayout, QLabel, QLineEdit, QHBoxLayout, QApplication
from PyQt5.QtGui import QIntValidator
from modules.newpage_module import newpage_functions as f
from general import general_functions as gf


class Subpage1(gf.Page):
    def __init__(self):
        super().__init__()

        # 1. Define page objects
        label = QLabel("<b>OPTIONS:</b>")
        self.lineoption1 = QLineEdit()
        self.lineoption1.setMinimumWidth(200)

        self.lineoption2 = QLineEdit(placeholderText='only int')
        self.lineoption2.setMinimumWidth(200)
        self.lineoption2.setValidator(QIntValidator())

        self.combo = QComboBox(self)
        self.combo.addItem("std")
        self.combo.addItem("max")
        self.combo.addItem("min")
        self.combo.addItem("avg")
        self.combo.addItem("median")

        self.checkbox = QCheckBox("")

        self.submit = QPushButton("Submit")

        # 2. Define page objects layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout3 = QFormLayout()
        layout3.setLabelAlignment(Qt.AlignLeft)
        layout3.setFormAlignment(Qt.AlignLeft)
        layout3.addRow(" - option 1:",self.lineoption1)
        layout3.addRow(" - option 2:",self.lineoption2)
        layout3.addRow(" - option 3",self.combo)
        layout3.addRow(" - option 4", self.checkbox)
        layout.addLayout(layout3)
        layout.addWidget(self.submit, alignment=Qt.AlignCenter)

        self.window = QVBoxLayout(self.container)
        self.window.addLayout(layout)
        self.window.addStretch()
    
  
class Subpage2(gf.Page):
    def __init__(self):
        super().__init__()

        # 1. Define page objects
        label = QLabel("File list")

        self.matrices_list = gf.DropFilesListWidget()
        self.matrices_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.add_file = QPushButton("Add file", self)
        self.add_folder = QPushButton("Add folder", self)
        self.remove = QPushButton("Remove selected", self)

        self.start_timepoint_label = QLabel('New start point:', self)
        self.start_timepoint = QLineEdit(self)

        self.end_timepoint_label = QLabel('New end point:', self)
        self.end_timepoint = QLineEdit(self)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.submit)

        # 2. Define page objects layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.matrices_list)
        layout3 = QHBoxLayout()
        layout3.addWidget(self.add_file)
        layout3.addWidget(self.add_folder)
        layout3.addWidget(self.remove)
        layout.addLayout(layout3)

        layout3 = QGridLayout()
        layout3.addWidget(self.start_timepoint_label, 0, 0)
        layout3.addWidget(self.start_timepoint, 0, 1)
        layout3.addWidget(self.end_timepoint_label, 0, 2)
        layout3.addWidget(self.end_timepoint, 0, 3)
        layout.addLayout(layout3)
        layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)
        self.window = QVBoxLayout(self.container)
        self.window.addLayout(layout)
        self.window.addStretch()
    
    def submit(self):
        # Read inputs and call functions in newpage_functions
        pass
    

class NewPage(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. Define page objects
        label = QLabel("<b>Example:</b> new page with a subdivision into other 2 subpages.")

        tabwizard = gf.TabWizard()
        tabwizard.addPage(Subpage1(), "Subpage1")
        tabwizard.addPage(Subpage2(), "Subpage2")
        
        # 2. Define page objects layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(tabwizard)
    
    