import json
import requests

from dotenv import load_dotenv
import os

from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout,
QPushButton, QLineEdit, QSizePolicy, QComboBox, QLabel
)
from qdarktheme import load_stylesheet

load_dotenv()
TOKEN = os.getenv('token')

moedas = {'Iene':'JPY',
'Dolar':'USD',
'Euro':'EUR',
'Biticoin':'BTC',
'Remimbi':'CNY',
'Real':'BRL'}

# API = 'https://economia.awesomeapi.com.br/last/'


# url = "https://api.apilayer.com/fixer/convert?to=BRL&from=EUR&amount=5"

# payload = {}
# headers= {
#   "apikey": "seu token"
# }

# response = requests.request("GET", url, headers=headers, data = payload)

# status_code = response.status_code
# result = response.text


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Conversor de Moedas Feliz!!!')
        self.setFixedSize(550, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)


        self.input_1 = QLineEdit()
        self.input_2 = QLineEdit()
        self.input_2.setDisabled(True)
        self.input_1.setStyleSheet(
            '* {font-size: 16px; padding: 10px; margin: 0px 10px;}'
        )
        self.input_2.setStyleSheet(
            '* {font-size: 16px; padding: 10px; margin: 0px 10px; color: white;}'
        )

        self.label_De = QLabel('De:')
        self.label_Para = QLabel('Para:')
        self.label_De.setStyleSheet(
            '* {font-size: 16px; margin-left: 10px;}'
        )
        self.label_Para.setStyleSheet(
            '* {font-size: 16px; margin-left: 10px;}'
        )

        self.caixa_1 = QComboBox()
        self.caixa_1.setStyleSheet(
            '* {font-size: 16px; padding: 10px; margin: 10px;}'
        )

        self.caixa_2 = QComboBox()
        self.caixa_2.setStyleSheet(
            '* {font-size: 16px; padding: 10px; margin: 10px;}'
        )

        for valor in moedas.keys():
            self.caixa_1.addItem(valor)
            self.caixa_2.addItem(valor)

        self.button_converter = QPushButton('Converter')
        self.button_converter.setStyleSheet(
            '* {font-size: 30px; width: 300px;}'
        )

        # self.button_converter.clicked.connect(lambda : self.input_2.setText(self.caixa_1.currentText()))
        # event = lambda : self.input_2.setText(self.caixa_1.currentText())

        # self.caixa_1.currentIndexChanged.connect(event)
        # self.caixa_2.currentIndexChanged.connect(event)

        self.grid.addWidget(self.label_De)
        self.grid.addWidget(self.caixa_1)
        self.grid.addWidget(self.label_Para)
        self.grid.addWidget(self.caixa_2)
        self.grid.addWidget(self.input_1)
        self.grid.addWidget(self.input_2)
        self.grid.addWidget(self.button_converter)


        self.setCentralWidget(self.cw)

        
        try:
            self.button_converter.clicked.connect(lambda: self.input_2.setText(self.buscador()))
        except TypeError():
            pass

    def buscador(self) -> str:
        """Passa os valores para a API e pega o retorno"""
    

        # pega o valor das caixas de texto e input
        de = self.caixa_2.currentText()
        para = self.caixa_1.currentText()
        value = self.input_1.text()

        # Verifica se os valores das caixas são iguais
        if de == para:
            self.input_2.setText('[ERROR!], Os valores não podem ser iguais')
            raise TypeError()

        # Tenta converter o "value" em float
        try:
            value = float(value)
        except:
            self.input_2.setText('Valor invalido! O valor deve ser numerico!')
            raise TypeError()

        # Verifica se o "value" é diferente de 0
        if value == 0:
            self.input_2.setText('Valor invalido! 0 não pode ser convertido!')
            raise TypeError()

        url = f"https://api.apilayer.com/fixer/convert?to={moedas[de]}&from={moedas[para]}&amount={value}"

        payload = {}
        headers= {
                "apikey": TOKEN
            }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.text
        request = json.loads(result)
        request = f"{request['result']:.2f}"
        return str(request)
    

if __name__ == '__main__':

    app = QApplication()
    app.setStyleSheet(load_stylesheet())

    window = MyWindow()

    window.show()
    app.exec()