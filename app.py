import requests
from tkinter import *


def pegar_cotacoes():  # Função que vai dar ação para algo, tipo ao clicar o botão vai fazer a ação de buscar a cotação
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)



janela = Tk()  # Inicio da Janela
janela.title('Teste')  # Titulo da Janela
texto_orientacao = Label(janela, text='Janela Teste')  # Por o Texto
texto_orientacao.grid(column=0, row=0)  # Por numa posição

botao = Button(janela, text='Clica aqui', command=pegar_cotacoes)
botao.grid(column=0, row=1)

texto_cotacao = Label(janela, text='')
texto_cotacao.grid(column=0, row=2)
janela.mainloop()  # Fim da janela
