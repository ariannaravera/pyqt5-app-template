#!/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2023, Arianna Ravera <ariannaravera22@gmail.com>
# All rights reserved.

import sys
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFormLayout

from modules.newpage_module import newpage
from modules.segmentation_module import segmentation
from modules.napari_module import napari
from general import general_functions as gf


class Home(gf.Page):
    def __init__(self, page_description):
        super().__init__()
        self.window = QFormLayout(self.container)
        self.title = QLabel('<b>HOME</b>', self)
        self.title.setFont(QFont('Arial', 18))
        self.title.setAlignment(Qt.AlignCenter)
        self.window.addRow(self.title)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.window.addRow(self.line)

        self.text = QLabel(page_description, self)
        self.text.setWordWrap(True)
        self.window.addRow(self.text)

        
class NewPageName(gf.Page):
    def __init__(self):
        super().__init__()
        self.window = QVBoxLayout(self.container)
        self.window.addWidget(newpage.NewPage())
        self.window.addStretch()
   

class Segmentation(gf.Page):
    def __init__(self):
        super().__init__()
        self.window = QVBoxLayout(self.container)
        self.window.addWidget(segmentation.Segmentation())
        self.window.addStretch()


class Napari(gf.Page):
    def __init__(self):
        super().__init__()
        self.window = QVBoxLayout(self.container)
        self.window.addWidget(napari.Napari())
        self.window.addStretch()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        window = QVBoxLayout(self)

        title = "App Name"
        self.setWindowTitle(title)

        self.image = QLabel()
        pixmap = QPixmap("./support_files/icon.png")
        pixmap = pixmap.scaledToWidth(50)
        self.image.setPixmap(pixmap)
        self.image.setAlignment(Qt.AlignCenter)
        window.addWidget(self.image)
        tabwizard = gf.TabWizard()
        window.addWidget(tabwizard)

        page_description = "This is a template"
        
        tabwizard.addHomePage(Home(page_description))
        tabwizard.addPage(NewPageName(), "NewPageName")
        tabwizard.addPage(Napari(), "Napari")
        tabwizard.addPage(Segmentation(), "Segmentation")

        layout = QHBoxLayout()
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(QApplication.quit)
        self.quit_button.setStyleSheet("background: darkred;")
        layout.addWidget(self.quit_button, alignment=Qt.AlignRight)
        window.addLayout(layout)

        # Setup logging
        logging.basicConfig(level=logging.INFO, format="%(asctime)s (%(name)s) [%(levelname)s] %(message)s", handlers=[logging.StreamHandler(sys.stdout)])

        # Add a handler to output errors to QMessageBox
        self.qmessagebox_handler = gf.QMessageBoxErrorHandler(self)
        self.qmessagebox_handler.setFormatter(logging.Formatter('%(message)s'))
        self.qmessagebox_handler.setLevel(logging.ERROR)
        logging.getLogger().addHandler(self.qmessagebox_handler)

    def __del__(self):
        # Remove handler to avoid problems after self and self.status_line are destroyed
        logging.getLogger().removeHandler(self.qlabel_handler)
        logging.getLogger().removeHandler(self.qmessagebox_handler)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    #w.resize(900,800)
    sys.exit(app.exec_())
