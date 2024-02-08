# ch 4.2.1 main.py
import sys 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit) #QPlainTextEdit 추가
from PyQt5.QtGui import QIcon # icon추가를 위한 라이브러리

class Calculator(QWidget) :

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() #텍스트 에딧 위젯 생성
        self.te1.setReadOnly(True) #텍스트 에딧 위제을 읽기만 가능하도록 수정
        self.btn1=QPushButton('Message', self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭시 핸들러 함수 연결

        vbox=QVBoxLayout() #수직 레이아웃 위제 생성
        vbox.addWidget(self.te1) # 빈 공간
        vbox.addWidget(self.btn1) #버튼 위치
        vbox.addStretch(1) #빈 공간

        self.setLayout(vbox) #빈 공간-버튼-빈공간 순으로 수직배치된 레이아웃 설정


        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) # 왼도우 아이콘 추가
        self.resize(256,256)
        self.show()

    def activateMessage(self): #버튼을 클릭할 때 동작하는 함수: 메시지 박스 출력
        QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText("Button clicked")
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    view=Calculator()
    sys.exit(app.exec_())
