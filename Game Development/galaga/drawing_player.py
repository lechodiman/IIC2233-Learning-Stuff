from PyQt5.QtWidgets import (QWidget, QFrame, QApplication, QMainWindow,
                             QGraphicsScene, QGraphicsRectItem,
                             QGraphicsView, QGraphicsItem, QGraphicsTextItem, QGraphicsPixmapItem)
import sys
from PyQt5.QtCore import Qt, QTimer, QObject, QUrl
from PyQt5.QtGui import QFont, QPixmap, QImage, QBrush
import random
from PyQt5 import QtMultimedia as M


class MyView(QWidget):
    def __init__(self):
        super().__init__()
        self.game_init()

    def game_init(self):
        self.scene = QGraphicsScene(parent=self)
        self.player = QGraphicsRectItem()
        self.player.setRect(0, 0, 100, 100)

        # add the item to the scene
        self.scene.addItem(self.player)
        self.view = QGraphicsView(self.scene, parent=self)

        # add a view, widget(invisible)
        self.show()


class Player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap('./imgs/DurrrSpaceShip.png').scaled(80, 80, Qt.KeepAspectRatio))
        self.bulletsound = M.QMediaPlayer()
        media = M.QMediaContent(QUrl("./sounds/bullet.mp3"))
        self.bulletsound.setMedia(media)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            if self.pos().x() > 0:
                self.setPos(self.x() - 10, self.y())
        elif event.key() == Qt.Key_Right:
            if self.pos().x() + 100 < 800:
                self.setPos(self.x() + 10, self.y())
        elif event.key() == Qt.Key_Space:
            bullet = Bullet()
            bullet.setPos(self.x(), self.y())
            self.scene().addItem(bullet)

            # play bulletsound
            if self.bulletsound.state() == M.QMediaPlayer.PlayingState:
                self.bulletsound.setPosition(0)
            elif self.bulletsound.state() == M.QMediaPlayer.StoppedState:
                self.bulletsound.play()

    def spawn(self):
        # create an enemy
        enemy = Enemy()
        self.scene().addItem(enemy)


class Enemy(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        # set random position
        self.setPos(random.random() * 700, 0)

        self.setPixmap(QPixmap('./imgs/monster1.png').scaled(100, 100, Qt.KeepAspectRatio))
        self.setTransformOriginPoint(50, 50)
        self.setRotation(180)

        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        # move enemy down
        self.setPos(self.x(), self.y() + 5)
        if (self.pos().y()) > 600:
            # decrease health
            health.decrease()
            # remove from the scene first
            self.scene().removeItem(self)
            # delete this instance to save memory
            del self


class Bullet(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap('./imgs/bullet.png'))
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)

    def move(self):
        # if bullet collides with enemy, destroy both
        self.colliding_items = self.collidingItems()
        for i in self.colliding_items:
            if isinstance(i, Enemy):
                # increase score
                score.increase()
                # remove them both
                self.scene().removeItem(i)
                self.scene().removeItem(self)
                del i
                del self
                return
        # move bullet up
        self.setPos(self.x(), self.y() - 10)
        if (self.pos().y() + self.pixmap().height()) < 0:
            # remove from the scene first
            self.scene().removeItem(self)
            # delete this instance to save memory
            del self


class Score(QGraphicsTextItem):
    def __init__(self):
        super().__init__()
        self.score = 0

        # draw the text
        self.setPlainText('Score: {}'.format(self.score))
        self.setDefaultTextColor(Qt.blue)
        self.setFont(QFont('times', 16))

    def getScore(self):
        return self.score

    def increase(self):
        self.score += 1
        self.setPlainText('Score: {}'.format(self.score))


class Health(QGraphicsTextItem):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.setPos(self.x(), self.y() + 25)
        self.setPlainText('Health: {}'.format(self.health))
        self.setDefaultTextColor(Qt.red)
        self.setFont(QFont('times', 16))

    def decrease(self):
        self.health -= 1
        self.setPlainText('Health: {}'.format(self.health))

    def getHealth(self):
        return self.health


if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)

        scene = QGraphicsScene()

        # adding scene background
        scene.setBackgroundBrush(QBrush(QImage('./imgs/background.png')))

        player = Player()

        # add the item to the scene
        scene.addItem(player)

        # make player focusable
        player.setFlag(QGraphicsItem.ItemIsFocusable)
        player.setFocus()

        # add a view, widget(invisible)
        view = QGraphicsView(scene)
        view.setFixedSize(800, 600)
        # horizontal and vertical scroll bar has benn disabled
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scene.setSceneRect(0, 0, 800, 600)
        player.setPos(view.width() / 2 - player.pixmap().width() / 2, view.height() - player.pixmap().height())
        view.show()

        global score
        score = Score()
        scene.addItem(score)

        global health
        health = Health()
        scene.addItem(health)

        # spawn enemies
        timer = QTimer()

        def spawn():
            enemy = Enemy()
            scene.addItem(enemy)
        timer.timeout.connect(spawn)
        timer.start(1000)

        # play background music
        url = QUrl.fromLocalFile("./sounds/intro.ogg")
        media = M.QMediaContent(url)
        playlist = M.QMediaPlaylist()
        playlist.addMedia(media)
        playlist.setPlaybackMode(M.QMediaPlaylist.Loop)
        music = M.QMediaPlayer()
        music.setPlaylist(playlist)
        music.setVolume(10)
        music.play()
        # media = M.QMediaContent(url)
        # music = M.QMediaPlayer()
        # music.setMedia(media)
        # music.setVolume(20)
        # music.play()

        sys.exit(app.exec_())

run()
