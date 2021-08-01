from tkinter import *
from tkinter.messagebox import showinfo
from config.get_start import NavegarColaborar
from time import sleep


app = Tk()
app.title("Login Colaborar")
app.geometry("500x200")
app.maxsize(width=450, height=200)
app.minsize(width=450, height=200)
app.config(bg="white")
txt_titulo = Label(app, text="Colaborar EAD")
txt_titulo.config(font=('Arial Black', 18), bg="white")
txt_titulo.place(width=350, height=25, relx=0.1, rely=0.1)

txt_username = Label(app, text="Nome de Usuário", bg="white")
txt_username.place(width=120, relx=0.05, rely=0.3)

inpt_username = Entry(app)
inpt_username.place(width=240, relx=0.35, rely=0.3)

txt_password = Label(app, text="Senha de Usuário", bg="white")
txt_password.place(width=120, relx=0.05, rely=0.5)

inpt_password = Entry(app, show="*")
inpt_password.place(width=240, relx=0.35, rely=0.5)

btn_login = Button(app, text="Logar", command=lambda: clicou_logar())
btn_login.place(relx=0.72, rely=0.70, width=70)

def clicou_logar():
    usuario = inpt_username.get().strip()
    senha = inpt_password.get().strip()
    colaborar = NavegarColaborar('https://www.colaboraread.com.br/', usuario, senha)
    txt_username.config(fg="black")
    txt_password.config(fg="black")
    app.title("Aguarde...")
    app.update()
    sleep(2)
    if colaborar.start_login():
        txt_username.destroy()
        txt_password.destroy()
        inpt_password.destroy()
        inpt_username.destroy()
        btn_login.destroy()
        txt_titulo.destroy()

        txt_criando_tabela = Label(app, text="Aguarde enquanto o PDF com a tabela é gerado...", bg="white")
        txt_criando_tabela.place(relx=0.1, rely=0.4)
        app.update()

        colaborar.app = app
        colaborar.get_all_colaborar_info()
        colaborar.transformar_html()
        colaborar.close_page()

        txt_criando_tabela.destroy()
        txt_tudo_pronto = Label(app, text="Tudo Pronto!", font=('helvetica', 20), bg="white")
        txt_tudo_pronto.place(relx=0.3, rely=0.1)
        txt_msg_pronto = Label(app, text="Acesse o arquivo gerado chamado: 'arquivo.pdf'", bg="white")
        txt_msg_pronto.place(relx=0.15, rely=0.4)
        btn_fechar = Button(app, text="Fechar", command=lambda: fechar_programa())
        btn_fechar.place(relx=0.4, rely=0.65)
        app.update()

    else:
        txt_username.config(fg="red")
        txt_password.config(fg="red")
        app.title("Dados Incorretos")
        app.update()

def fechar_programa():
    app.destroy()

app.mainloop()