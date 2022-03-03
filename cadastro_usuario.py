import tkinter as tk
import psycopg2

janela = tk.Tk()

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost")
    print("connected")
except:
    print("I am unable to connect to the database")
cur = conn.cursor()


# cur.execute('''CREATE TABLE usuario (id serial PRIMARY KEY, nome char, telefone varchar, cpf varchar);''')
# conn.commit()


def inserir_usuario():  # Criar a função
    nome = entry_nome.get()  # Pega as informações que eu inseri
    telefone = entry_telefone.get()
    cpf = entry_cpf.get()
    cur.execute("INSERT INTO usuario(nome, telefone, cpf) VALUES (%s, %s, %s);", (nome, telefone, cpf))
    conn.commit()


janela.title('Cadastro de Usuários')
label_nome = tk.Label(text='Nome Usuário')
label_nome.grid(column=0, row=1, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_nome = tk.Entry()
entry_nome.grid(column=2, row=1, padx=10, pady=10, sticky='nswe', columnspan=2)
if entry_nome > 11:
    print('Digite o número novamente')
else:
    print('Cadastrado')

label_telefone = tk.Label(text='Telefone Usuário')
label_telefone.grid(column=0, row=2, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_telefone = tk.Entry()
entry_telefone.grid(column=2, row=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_cpf = tk.Label(text='CPF Usuário')
label_cpf.grid(column=0, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_cpf = tk.Entry()
entry_cpf.grid(column=3, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_cadastrar_usuario = tk.Button(text='Cadastrar', command=inserir_usuario)
botao_cadastrar_usuario.grid(column=0, row=4, padx=10, pady=10, sticky='nswe', columnspan=4)
janela.mainloop()
