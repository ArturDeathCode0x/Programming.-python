
from tkinter import *
from tkinter import ttk, messagebox

# ======================================================
# MODEL
# ======================================================
class SistemaModel:
    def __init__(self):
        self.dados = []

    def adicionar(self, nome, idade):
        self.dados.append({
            "nome": nome,
            "idade": idade
        })

    def listar(self):
        return self.dados

    def remover(self, index):
        del self.dados[index]


# ======================================================
# CONTROLLER
# ======================================================
class SistemaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def adicionar_usuario(self):
        nome = self.view.entrada_nome.get()
        idade = self.view.entrada_idade.get()

        if nome == "" or idade == "":
            messagebox.showwarning("ERRO", "Preencha todos os campos")
            return

        self.model.adicionar(nome, idade)
        self.view.atualizar_tabela(self.model.listar())

        self.view.entrada_nome.delete(0, END)
        self.view.entrada_idade.delete(0, END)

        messagebox.showinfo("SUCESSO", "Usuário cadastrado")

    def remover_usuario(self):
        item = self.view.tabela.selection()

        if not item:
            messagebox.showwarning("ERRO", "Selecione um usuário")
            return

        index = self.view.tabela.index(item)

        self.model.remover(index)
        self.view.atualizar_tabela(self.model.listar())

        messagebox.showinfo("REMOVIDO", "Usuário removido")

    def sair(self):
        self.view.app.destroy()


# ======================================================
# VIEW
# ======================================================
class SistemaView:
    def __init__(self, app):
        self.app = app

        self.app.title("Mini Sistema Tkinter")
        self.app.geometry("900x500")
        self.app.configure(bg="#0f172a")

        # RESPONSIVO
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        self.frame = Frame(app, bg="#0f172a")
        self.frame.grid(sticky="nsew")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        titulo = Label(
            self.frame,
            text="SISTEMA DE CADASTRO",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # NOME
        Label(
            self.frame,
            text="Nome",
            font=("Arial", 14),
            bg="#0f172a",
            fg="white"
        ).grid(row=1, column=0, sticky="w", padx=20)

        self.entrada_nome = Entry(
            self.frame,
            font=("Arial", 14)
        )
        self.entrada_nome.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # IDADE
        Label(
            self.frame,
            text="Idade",
            font=("Arial", 14),
            bg="#0f172a",
            fg="white"
        ).grid(row=1, column=1, sticky="w", padx=20)

        self.entrada_idade = Entry(
            self.frame,
            font=("Arial", 14)
        )
        self.entrada_idade.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # BOTÕES
        self.btn_adicionar = Button(
            self.frame,
            text="Adicionar",
            font=("Arial", 12, "bold"),
            bg="#22c55e",
            fg="white",
            height=2
        )
        self.btn_adicionar.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_remover = Button(
            self.frame,
            text="Remover",
            font=("Arial", 12, "bold"),
            bg="#ef4444",
            fg="white",
            height=2
        )
        self.btn_remover.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        # TABELA
        self.tabela = ttk.Treeview(
            self.frame,
            columns=("Nome", "Idade"),
            show="headings"
        )

        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Idade", text="Idade")

        self.tabela.column("Nome", anchor="center")
        self.tabela.column("Idade", anchor="center")

        self.tabela.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.frame.grid_rowconfigure(4, weight=1)

        # BOTÃO SAIR
        self.btn_sair = Button(
            self.frame,
            text="Sair",
            font=("Arial", 12, "bold"),
            bg="#3b82f6",
            fg="white",
            height=2
        )
        self.btn_sair.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    def atualizar_tabela(self, dados):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for pessoa in dados:
            self.tabela.insert(
                "",
                END,
                values=(pessoa["nome"], pessoa["idade"])
            )


# ==================================