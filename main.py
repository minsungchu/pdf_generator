import sys
from PyPDF2 import PdfFileReader
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from pathlib import Path


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # TEST PdfFileReader
        pdf_path = "e:/SW/progit_v2.1.1.pdf"  # PDF 경로 및 파일 이름 설정
        pdf = PdfFileReader(str(pdf_path))
        pageTest = pdf.getNumPages()
        print("Pages of progit.pdf is " + str(pageTest))
        pageInfo = pdf.documentInfo
        print(pageInfo)
        print(pageInfo.title)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())