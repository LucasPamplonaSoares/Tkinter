import tkinter as tk
import psycopg2


try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost")
    print("connected")
except:
    print("I am unable to connect to the database")
cur = conn.cursor()

# cur.execute('''CREATE TABLE pessoa (id serial PRIMARY KEY, nome name, telefone varchar, cpf varchar);''')
# conn.commit()


def inserir():
    nome = entry_usuario.get()
    cpf = entry_cpf.get()
    cur.execute("INSERT INTO pessoa(nome,cpf) VALUES (%s, %s);", (nome, cpf))
    conn.commit()


def cadastro():
    janela2 = tk.Toplevel()
    janela2.title('Cadastro')
    label_nome = tk.Label(janela2, text='Nome')
    label_nome.grid(column=0, row=0, padx=10, pady=10)
    entry_nome = tk.Entry(janela2)
    entry_nome.grid(column=1, row=0, pady=10, padx=10, sticky='nswe')
    label_telefone = tk.Label(janela2, text='Telefone')
    label_telefone.grid(column=0, row=1, padx=10, pady=10, sticky='nswe')
    entry_telefone = tk.Entry(janela2)
    entry_telefone.grid(column=1, row=1, padx=10, pady=10, sticky='nswe')
    label_cpf = tk.Label(janela2, text='CPF')
    label_cpf.grid(column=0, row=2, padx=10, pady=10, sticky='nswe')
    entry_cpf = tk.Entry(janela2)
    entry_cpf.grid(column=1, row=2, padx=10, pady=10, sticky='nswe')
    botao_voltar = tk.Button(janela2, text='Volta', command=janela2.destroy)
    botao_voltar.grid(column=0, row=3, padx=10, pady=10, sticky='nswe')
    botao_confirmar = tk.Button(janela2, text='Cadastrar', command=inserir)
    botao_confirmar.grid(column=1, row=3, padx=10, pady=10, sticky='nswe')


janela = tk.Tk()
janela.title('Login')
label_usuario = tk.Label(janela, text='Usuario')
label_usuario.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
entry_usuario = tk.Entry(janela)
entry_usuario.grid(column=1, row=0, padx=10, pady=10, sticky='nswe')
label_cpf = tk.Label(janela, text='CPF')
label_cpf.grid(column=0, row=1, pady=10, padx=10, sticky='nswe')
entry_cpf = tk.Entry(janela)
entry_cpf.grid(column=1, row=1, padx=10, pady=10, sticky='nswe')
botao1 = tk.Button(janela, text='Cadastro', command=cadastro)
botao1.grid(column=0, row=2, padx=10, pady=10, sticky='nswe')
janela.mainloop()
