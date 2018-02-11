from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QGraphicsView, QGraphicsScene, QPushButton, QGraphicsTextItem, QLineEdit, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(400, 300)
        # self.list_w = QListWidget(self)
        # for i in range(10):
        #     self.list_w.addItem('Item {}'.format(i + 1))

        # item = QListWidgetItem(self.list_w)
        # item.setText('Holi')
        # icon = QIcon(QPixmap('pythonlogo.png'))
        # item.setIcon(icon)

        # self.chat_view = ChatWindow(self)
        # self.chat_view.show()

        v_box = QVBoxLayout()
        for i in range(10):
            btn = QPushButton('Wenaza la calabza')
            v_box.addWidget(btn)

        # container widget
        self.widget = QWidget()
        # layout of container widwet
        layout = QVBoxLayout(self)
        for i in range(20):
            label = QLabel('test')
            layout.addWidget(label)
        self.widget.setLayout(layout)

        # scroll area properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(self.widget)

        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        self.setLayout(v_layout)


class ChatWindow(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 350, 250)
        self.setScene(self.scene)
        self.text = QGraphicsTextItem('Holi')
        self.scene.addItem(self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
