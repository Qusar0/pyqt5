import sys
from PyQt5.QtCore import pyqtSignal, QObject, QFile, QTextStream
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QWidget,
                             QApplication, QLCDNumber, QSlider,
                             QVBoxLayout, QMainWindow, QInputDialog,
                             QFrame, QColorDialog, QFontDialog, QSizePolicy,
                             QLabel, QAction, QFileDialog, QTextEdit,
                             )
from PyQt5.QtGui import QColor, QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        saveFile = QAction(QIcon('save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.save_file)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        self.current_file = None

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.current_file = fname
        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def save_file(self):
        if self.current_file:
            self._save_to_file(self.current_file)

    def _save_to_file(self, file_name):
        file = QFile(file_name)
        if not file.open(QFile.WriteOnly | QFile.Text):
            return
        
        text_stream = QTextStream(file)
        text_stream << self.textEdit.toPlainText()
        file.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())