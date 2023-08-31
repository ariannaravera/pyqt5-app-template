import os
import logging
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QWidget, QTabWidget, QLineEdit, QScrollArea, QListWidget, QMessageBox



class QLineEditHandler(logging.Handler):
    """
    logging handler to send message to QLineEdit.

    Examples
    --------
    label=QLineEdit()
    handler=QLineEditHandler(label)
    logging.getLogger().addHandler(handler)
    """

    def __init__(self, qlabel):
        logging.Handler.__init__(self)
        self.label = qlabel

    def emit(self, record):
        msg = self.format(record)
        self.label.setText(msg)
        # to focus on the beginning of the text if too long
        self.label.setCursorPosition(0)
        # force repainting to update message even when busy
        self.label.repaint()


class QMessageBoxErrorHandler(logging.Handler):
    """
    Logging handler to send message to QMessageBox.critical

    Examples
    --------
    handler= QMessageBoxErrorHandler(self)
    handler.setLevel(logging.ERROR)
    logging.getLogger().addHandler(handler)    
    """

    def __init__(self, parent):
        logging.Handler.__init__(self)
        self.parent = parent

    def emit(self, record):
        msg = self.format(record)
        QMessageBox.critical(self.parent, 'Error', msg)


class DropFilesListWidget(QListWidget):
    """
    A QListWidget with drop support for files and folders. If a folder is dropped, all files contained in the folder are added.
    """

    def __init__(self, parent=None, filetypes=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.filetypes = filetypes

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            if url.isLocalFile():
                if os.path.isfile(url.toLocalFile()):
                    filename = url.toLocalFile()
                    if len(self.findItems(filename, Qt.MatchExactly)) == 0 and (self.filetypes is None or os.path.splitext(filename)[1] in self.filetypes):
                        self.addItem(filename)
                if os.path.isdir(url.toLocalFile()):
                    d = url.toLocalFile()
                    # keep only files (not folders)
                    filenames = [os.path.join(d, f)
                                 for f in os.listdir(d)]
                    if not self.filetypes is None:
                        # keep only allowed filetypes
                        filenames = [f for f in filenames
                                     if os.path.splitext(f)[1] in self.filetypes]
                    # keep only existing files (not folders)
                    filenames = [f for f in filenames
                                 if os.path.isfile(f)]
                    # do not add if already in the list
                    filenames = [f for f in filenames
                                 if len(self.findItems(f, Qt.MatchExactly)) == 0]
                    self.addItems(filenames)


class DropFileLineEdit(QLineEdit):
    """
    A QLineEdit with drop support for files.
    """

    def __init__(self, parent=None, filetypes=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.filetypes = filetypes

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            if url.isLocalFile():
                if os.path.isfile(url.toLocalFile()):
                    filename = url.toLocalFile()
                    if self.filetypes is None or os.path.splitext(filename)[1] in self.filetypes:
                        self.setText(filename)


class DropFolderLineEdit(QLineEdit):
    """
    A QLineEdit with drop support for folder.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            if url.isLocalFile():
                if os.path.isdir(url.toLocalFile()):
                    self.setText(url.toLocalFile())


class TabWizard(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabBar().installEventFilter(self)

    def addPage(self, page, title):
        if not isinstance(page, Page):
            raise TypeError(f"{page} must be Page object")
        self.addTab(page, title)
        page.completeChanged.connect(self.nextPage)
    
    def addHomePage(self, page):
        tab_index = self.addTab(page, '')
        self.setTabIcon(tab_index, QIcon('support_files/home.svg'))
        self.setIconSize(QSize(12,12))
        page.completeChanged.connect(self.nextPage)

    def nextPage(self):
        next_index = self.currentIndex() + 1
        if next_index < self.count():
            self.setCurrentIndex(next_index)


class Page(QWidget):
    completeChanged = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.container = QWidget()
        lay = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.container)
        scroll.setBackgroundRole(QPalette.Base)
        scroll.setFrameShape(QFrame.NoFrame)
        lay.addWidget(scroll)

    
class IgnoreDuplicate(logging.Filter):
    """
    logging filter to ignore duplicate messages.
    """

    def __init__(self, message=None):
        logging.Filter.__init__(self)
        self.last = None
        self.message = message

    def filter(self, record):
        current = (record.module, record.levelno, record.msg)
        if self.message is None or self.message == record.msg:
            # add other fields if you need more granular comparison, depends on your app
            if self.last is None or current != self.last:
                self.last = current
                return True
            return False
        self.last = current
        return True