import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QListWidgetItem, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout,
                             QHBoxLayout, QStackedWidget, QComboBox,
                             QLabel)

from PyQt5.QtWidgets import QApplication


class MyWindow(QStackedWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        first_page_widget = QWidget(self)
        btn1 = QPushButton('Soy de la pag 1', first_page_widget)
        btn1.clicked.connect(lambda: self.setCurrentIndex(1))

        second_page_widget = QWidget(self)
        btn2 = QPushButton('Soy de la pag 2', second_page_widget)
        btn2.clicked.connect(lambda: self.setCurrentIndex(2))

        self.third_page_widget = QWidget(self)
        self.third_page_widget.label = QLabel('Holi soy de la 3', self.third_page_widget)

        self.addWidget(first_page_widget)
        self.addWidget(second_page_widget)
        self.addWidget(self.third_page_widget)

        self.setCurrentIndex(0)

        # self.pageComboBox = QComboBox(self)
        # self.pageComboBox.addItem('Page1')
        # self.pageComboBox.addItem('Page2')
        # self.pageComboBox.addItem('Page3')
        # self.pageComboBox.activated.connect(self.setCurrentIndex)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName('Progra - Pop')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())
