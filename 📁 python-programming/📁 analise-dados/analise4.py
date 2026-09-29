from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd

# =========================================
# JANELA
# =========================================
app = Tk()
app.title("Sistema com Pandas")
app.geometry("700x500")

# =========================================
# DATAFRAME
# =========================================
dados = pd.DataFrame(columns=["Nome", "Idade"])

# =========================================
# FUNÇÃO ADICIONAR
# =========================================
def adicionar():

    global dados

    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if nome == "" or idade == "":
        messagebox.showwarning(
            "ERRO",
            "Preencha os campos"
        )
        return

    novo = pd.DataFrame({
        "Nome": [nome],
        "Idade": [idade]
    })

    dados = pd.concat(
        [dados, novo],
        ignore_index=True
    )

    atualizar_tabela()

    entrada_nome.delete(0, END)
    entrada_idade.delete(0, END)

# =========================================
# FUNÇÃO ATUALIZAR TABELA
# =========================================
def atualizar_tabela():

    for item in tabela.get_children():
        tabela.delete(item)

    for _, linha in dados.iterrows():

        tabela.insert(
            "",
            END,
            values=(
                linha["Nome"],
                linha["Idade"]
            )
        )

# =========================================
# SALVAR EXCEL
# =========================================
def salvar_excel():

    dados.to_excel(
        "usuarios.xlsx",
        index=False
    )

    messagebox.showinfo(
        "SUCESSO",
        "Arquivo salvo"
    )

# =========================================
# INPUTS
# =========================================
Label(app, text="Nome").pack()

entrada_nome = Entry(app, font=("Arial", 14))
entrada_nome.pack(fill="x", padx=20)

Label(app, text="Idade").pack()

entrada_idade = Entry(app, font=("Arial", 14))
entrada_idade.pack(fill="x", padx=20)

# =========================================
# BOTÕES
# =========================================
Button(
    app,
    text="Adicionar",
    command=adicionar
).pack(pady=10)

Button(
    app,
    text="Salvar Excel",
    command=salvar_excel
).pack()

# =========================================
# TABELA
# =========================================
tabela = ttk.Treeview(
    app,
    columns=("Nome", "Idade"),
    show="headings"
)

tabela.heading("Nome", text="Nome")
tabela.heading("Idade", text="Idade")

tabela.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

app.mainloop()