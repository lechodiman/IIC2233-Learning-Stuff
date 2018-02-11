import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QSlider, QCheckBox
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.l_1 = QLabel(self)
        self.l_1.setText('Look at me')
        self.b = QPushButton(QtGui.QIcon('pythonlogo.png'), 'Clear', self)
        self.b_2 = QPushButton('Print', self)
        self.s_1 = QSlider(Qt.Horizontal)
        self.s_1.setMinimum(1)
        self.s_1.setMaximum(99)
        self.s_1.setValue(25)
        self.s_1.setTickInterval(10)
        self.s_1.setTickPosition(QSlider.TicksBelow)
        self.cbx = QCheckBox('Do you like dogs?')
        self.btn_3 = QPushButton('Click me')

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l_1)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)
        v_box.addWidget(self.b_2)
        v_box.addLayout(h_box)
        v_box.addWidget(self.s_1)
        v_box.addWidget(self.btn_3)
        v_box.addWidget(self.cbx)
        self.setLayout(v_box)

        self.setWindowTitle('PyQt Lesson 2')

        self.b.clicked.connect(lambda: self.btn_click_2(self.b, 'Hello from clear button'))
        self.b_2.clicked.connect(lambda: self.btn_click_2(self.b_2, 'Hello from print button'))
        self.s_1.valueChanged.connect(self.v_change)
        self.btn_3.clicked.connect(lambda: self.btn_click_3(self.cbx.isChecked(), self.l_1))

        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        self.l_1.setText('I have been clicked')

    def btn_click_2(self, btn, string):
        if btn.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v_change(self):
        my_value = str(self.s_1.value())
        self.le.setText(my_value)

    def btn_click_3(self, check, label):
        if check:
            label.setText('I guess you like dogs!')
        else:
            label.setText('Dog hater then')


if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = MyWindow()
        sys.exit(app.exec_())

run()
