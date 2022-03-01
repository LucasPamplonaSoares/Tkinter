import tkinter as tk
from tkinter import ttk
# import datetime as dt
import psycopg2

tipo_lista = ['Caixa', 'Unidade', 'Kg']
lista_produto = []
janela = tk.Tk()

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost")
    print("connected")
except:
    print("I am unable to connect to the database")
cur = conn.cursor()


def criarTabela():
        cur.execute("CREATE TABLE estoque (id serial PRIMARY KEY, descricao char, tipo_unidade char, quantidade integer);")


def inserir_produto():  # Criar a função
    descricao = entry_descricao.get()  # Pega as informações que eu inseri
    tipo = combobox_selecionar.get()
    quantidade = entry_quantidade.get()
    cur.execute("INSERT INTO estoque(descricao, tipo_unidade, quantidade) VALUES (%s, %s, %s);", (descricao, tipo, quantidade))
    conn.commit()



janela.title('Estoque Mercearia Luz')  # Titulo da janela

label_descricao = tk.Label(text='Descrição do Produto')
label_descricao.grid(column=0, row=1, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()  # Entrada de dados
entry_descricao.grid(column=0, row=2, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text='Tipo da Unidade')
label_tipo_unidade.grid(column=0, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar = ttk.Combobox(values=tipo_lista)
combobox_selecionar.grid(column=2, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text='Quantidade do Produto')
label_quantidade.grid(column=0, row=4, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(column=2, row=4, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_cadastrar_produto = tk.Button(text='Cadastrar', command=inserir_produto)
botao_cadastrar_produto.grid(column=0, row=5, padx=10, pady=10, sticky='nswe', columnspan=4)


janela.mainloop()
