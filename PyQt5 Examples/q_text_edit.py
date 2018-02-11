import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget,
                             QTextEdit, QHBoxLayout, QMessageBox, QFileDialog)
import os


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.save_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')

        self.save_btn.setShortcut('Ctrl+S')

        self.init_ui()

    def init_ui(self):

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.save_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        if filename[0] == '':
            return
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def clear_text(self):
        choice = QMessageBox.question(self, 'Message',
                                      "Are you sure to clear?", QMessageBox.Yes |
                                      QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            self.text.clear()
        else:
            pass

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
