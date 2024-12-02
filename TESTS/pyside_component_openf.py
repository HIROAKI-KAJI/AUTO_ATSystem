import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog,QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "folder Open"
        self.setWindowTitle(self.title)

        # ボタンを使うことを宣言
        button = QPushButton(self)

        # ボタンに表示する文字
        button.setText("押してみよう！！")
        
        # ボタンを押したら実行させる処理
        # connectメソッド: 処理させるメソッド
        button.pressed.connect(self.CallbackButtonPressed)
        
        # ボタンを離したら実行させる処理（引数を指定する場合）
        # connectメソッド: 処理させるメソッド
        #button.released.connect(lambda: self.CallbackButtonReleased(90))

        
        self.setCentralWidget(button)

        self.resize(640,360)
    def CallbackButtonPressed(self):
        print("folder Dialog Opened")

        fileName = QFileDialog.getOpenFileName(self)

        print("選択したファイルは{}ですね".format(fileName))


def showimg():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    showimg()