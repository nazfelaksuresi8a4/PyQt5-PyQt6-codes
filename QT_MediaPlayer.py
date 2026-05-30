import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QFileDialog
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl


class MediaPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.resize(800, 600)

        self.player = QMediaPlayer()

        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)

        self.open_btn = QPushButton("Dosya Aç")
        self.play_btn = QPushButton("Oynat")
        self.pause_btn = QPushButton("Duraklat")

        self.open_btn.clicked.connect(self.open_file)
        self.play_btn.clicked.connect(self.player.play)
        self.pause_btn.clicked.connect(self.player.pause)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.open_btn)
        layout.addWidget(self.play_btn)
        layout.addWidget(self.pause_btn)

        self.setLayout(layout)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Medya Dosyası Seç",
            "",
            "Video Dosyaları (*.mp4 *.avi *.mkv);;Tüm Dosyalar (*)"
        )

        if file_name:
            media = QMediaContent(QUrl.fromLocalFile(file_name))
            self.player.setMedia(media)


app = QApplication(sys.argv)
window = MediaPlayer()
window.show()
sys.exit(app.exec_())
