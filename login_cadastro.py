import tkinter as tk

def cadastrar():
    janela2 = tk.Toplevel()
    janela2.geometry('200x200')
    janela2.title('Cadastro')
    label_nome = tk.Label(janela2, text='Nome')
    label_nome.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
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
    botao_confirmar = tk.Button(janela2, text='Confirmar', command='')
    botao_confirmar.grid(column=1, row=3, padx=10, pady=10, sticky='nswe')


def logar():
    janela3 = tk.Toplevel()
    janela3.geometry('200x200')
    janela3.title('login')
    label_nome = tk.Label(janela3, text='Nome')
    label_nome.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
    entry_nome = tk.Entry(janela3)
    entry_nome.grid(column=1, row=0, padx=10, pady=10, sticky='nswe')
    label_cpf = tk.Label(janela3, text='CPF')
    label_cpf.grid(column=0, row=2, padx=10, pady=10, sticky='nswe')
    entry_cpf = tk.Entry(janela3)
    entry_cpf.grid(column=1, row=2, padx=10, pady=10, sticky='nswe')
    botao_voltar = tk.Button(janela3, text='Voltar', command=janela3.destroy)
    botao_voltar.grid(column=0, row=3, padx=10, pady=10, sticky='nswe')
    botao_logar = tk.Button(janela3, text='Logar', command='')
    botao_logar.grid(column=1, row=3, padx=10, pady=10, sticky='nswe')


janela = tk.Tk()
janela.geometry('200x200')
janela.title('APP')
botao1 = tk.Button(janela, text='Cadastro', command=cadastrar)
botao1.grid(column=0, row=2, padx=10, pady=10, sticky='nswe')
botao2 = tk.Button(janela, text='Login', command=logar)
botao2.grid(column=1, row=2, padx=10, pady=10, sticky='nswe')
janela.mainloop()
