
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # メインウィジェットの作成
        self.setWindowTitle("コンテナ形式GUI例")
        self.setGeometry(100, 100, 800, 600)

        # スタックウィジェット (ページ切り替え用コンテナ)
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # ページ1
        self.page1 = QWidget()
        layout1 = QVBoxLayout(self.page1)
        layout1.addWidget(QPushButton("ページ1"))
        
        # ページ2
        self.page2 = QWidget()
        layout2 = QVBoxLayout(self.page2)
        layout2.addWidget(QPushButton("ページ2"))

        # ページ3
        self.page3 = QWidget()
        layout3 = QVBoxLayout(self.page3)
        layout3.addWidget(QPushButton("ページ3"))

        # スタックにページを追加
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # ページ切り替えボタン
        self.switch_buttons = QHBoxLayout()
        btn1 = QPushButton("ページ1")
        btn2 = QPushButton("ページ2")
        btn3 = QPushButton("ページ3")

        btn1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        btn2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        btn3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        self.switch_buttons.addWidget(btn1)
        self.switch_buttons.addWidget(btn2)
        self.switch_buttons.addWidget(btn3)

        # 全体のレイアウト
        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.addLayout(self.switch_buttons)
        self.setMenuWidget(container)



if __name__ == "__main__":
    app = QApplication([])

    # メインウィンドウのインスタンスを作成し表示
    window = MainWindow()
    window.show()

    app.exec()

