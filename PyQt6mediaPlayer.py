import sys
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class MedyaOynatici(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Medya Oynatıcı")
        self.setGeometry(100, 100, 800, 600)

        # Medya oynatıcı ve video alanı tanımlama
        self.medya_oynatici = QMediaPlayer()
        self.video_alani = QVideoWidget()

        # Arayüz elemanları oluşturma
        self.buton_dosya_ac = QPushButton("Dosya Aç")
        self.buton_dosya_ac.clicked.connect(self.dosya_ac)

        self.buton_oynat = QPushButton()
        self.buton_oynat.setEnabled(False)
        # PyQt6'da standart ikonlara erişim QStyle.StandardPixmap ile yapılır
        self.buton_oynat.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.buton_oynat.clicked.connect(self.oynat_duraklat)

        self.ilerleme_cubugu = QSlider(Qt.Orientation.Horizontal)
        self.ilerleme_cubugu.setRange(0, 0)
        self.ilerleme_cubugu.sliderMoved.connect(self.konum_ayarla)

        # Düzen (Layout) yönetimi
        yatay_duzen = QHBoxLayout()
        yatay_duzen.setContentsMargins(0, 0, 0, 0)
        yatay_duzen.addWidget(self.buton_dosya_ac)
        yatay_duzen.addWidget(self.buton_oynat)
        yatay_duzen.addWidget(self.ilerleme_cubugu)

        dikey_duzen = QVBoxLayout()
        dikey_duzen.addWidget(self.video_alani)
        dikey_duzen.addLayout(yatay_duzen)

        merkezi_widget = QWidget()
        merkezi_widget.setLayout(dikey_duzen)
        self.setCentralWidget(merkezi_widget)

        # Sinyal ve slot bağlantıları
        self.medya_oynatici.setVideoOutput(self.video_alani)
        self.medya_oynatici.playbackStateChanged.connect(self.durum_degisti)
        self.medya_oynatici.positionChanged.connect(self.konum_degisti)
        self.medya_oynatici.durationChanged.connect(self.sure_degisti)

    def dosya_ac(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(
            self, "Medya Dosyası Seç", "", "Videolar (*.mp4 *.avi *.wmv);;Ses Dosyaları (*.mp3)"
        )
        if dosya_adi:
            # PyQt6'da QMediaContent kaldırıldı, doğrudan QUrl.fromLocalFile kullanılır
            self.medya_oynatici.setSource(QUrl.fromLocalFile(dosya_adi))
            self.buton_oynat.setEnabled(True)
            self.medya_oynatici.play()

    def oynat_duraklat(self):
        if self.medya_oynatici.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.medya_oynatici.pause()
        else:
            self.medya_oynatici.play()

    def durum_degisti(self, durum):
        if durum == QMediaPlayer.PlaybackState.PlayingState:
            self.buton_oynat.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.buton_oynat.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))

    def konum_degisti(self, konum):
        self.ilerleme_cubugu.setValue(konum)

    def sure_degisti(self, sure):
        self.ilerleme_cubugu.setRange(0, sure)

    def konum_ayarla(self, konum):
        self.medya_oynatici.setPosition(konum)

if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    oynatici = MedyaOynatici()
    oynatici.show()
    sys.exit(uygulama.exec_())
