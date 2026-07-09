import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)




arquivo_moradores = filedialog.askopenfilename(
    title="Selecione moradores.csv",
    filetypes=[("CSV", "*.csv")]
)

arquivo_domicilios = filedialog.askopenfilename(
    title="Selecione domicilios.csv",
    filetypes=[("CSV", "*.csv")]
)

moradores = pd.read_csv(arquivo_moradores, sep=";", decimal=",", encoding="utf-8-sig", low_memory=False)
domicilios = pd.read_csv(arquivo_domicilios, sep=",", encoding="utf-8-sig")
qtd_linhasm = len(moradores)
qtd_linhasd = len(domicilios)

RAsMenu = ["Água Quente", "Águas Claras", "Águas Lindas de Goiás", "Alexânia", "Área Rural",
"Arapoanga", "Arniqueira", "Brazlândia", "Candangolândia", "Ceilândia",
"Cidade Ocidental", "Cocalzinho de Goiás", "Cristalina", "Cruzeiro", "Fercal",
"Formosa", "Gama", "Guará", "Itapoã", "Jardim Botânico",
"Lago Norte", "Lago Sul", "Luziânia", "Novo Gama", "Núcleo Bandeirante",
"Padre Bernardo", "Paranoá", "Park Way", "Planaltina", "Planaltina de Goiás",
"Plano Piloto", "Recanto Das Emas", "Riacho Fundo", "Riacho Fundo II", "Samambaia",
"Santa Maria", "Santo Antônio do Descoberto", "SCIA", "São Sebastião", "SIA",
"Sobradinho", "Sobradinho II", "Sol Nascente / Pôr do Sol", "Sudoeste e Octogonal", "Taguatinga",
"Valparaíso de Goiás", "Varjão", "Vicente Pires"]

RAsNumeros = [5335, 5320, 5241, 5242, 5336,
5334, 5333, 5304, 5319, 5309,
5243, 5245, 5244, 5311, 5331,
5246, 5302, 5310, 5328, 5327,
5318, 5316, 5247, 5248, 5308,
5249, 5307, 5324, 5306, 5250,
5301, 5315, 5317, 5321, 5312,
5313, 5251, 5325, 5314, 5329,
5305, 5326, 5332, 5322, 5303,
5252, 5323, 5330]

meu_dicionario = dict(zip(RAsMenu, RAsNumeros))








def exportar():
    """Exporta para um arquivo os domicílios da região administrativa selecionada."""
    resultado = selecionado.get()

    if resultado not in meu_dicionario:
        showinfo("Aviso", "Selecione uma região.")
        return

    value = meu_dicionario[resultado]
    loc = domicilios[domicilios["localidade"] == value]

    arquivo = filedialog.asksaveasfilename(
        initialfile=f"{resultado}.csv",
        defaultextension=".csv",
        filetypes=[
            ("CSV", "*.csv"),
            ("Arquivo de texto", "*.txt")
        ]
    )

    if not arquivo:
        return

    if arquivo.endswith(".csv"):
        loc.to_csv(arquivo, index=False, sep=";", encoding="utf-8-sig")
    else:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(loc.to_string(index=False))

    showinfo("Sucesso", "Arquivo exportado com sucesso!")










def grafico():
    """Exibe uma janela com gráficos dos dados da região administrativa selecionada."""
    resultado = selecionado.get()
    value = meu_dicionario[resultado]
    loc = domicilios[domicilios["localidade"] == value]

    esp = [(loc["B01"] == 1).sum(), (loc["B01"] == 2).sum()]
    espp = [f"Permanente\n{esp[0]}", f"Improvisado\n{esp[1]}"]

    tipo = [(loc["B02"] == 1).sum(), (loc["B02"] == 2).sum(), (loc["B02"] == 3).sum()]
    tipop = [f"Casa\n{tipo[0]}", f"Apartamento\n{tipo[1]}", f"Cômodo\n{tipo[2]}"]

    sit = [(loc["B03"] == 1).sum(), (loc["B03"] == 2).sum(), (loc["B03"] == 3).sum(), (loc["B03"] == 4).sum(), (loc["B03"] == 5).sum(), (loc["B03"] == 88888).sum()]
    sitp = [f"Próprio\n(quitado)\n{sit[0]}", f"Próprio\n(pagando)\n{sit[1]}", f"Alugado\n{sit[2]}", f"Cedido\n(empregador)\n{sit[3]}", f"Cedido\n(outro)\n{sit[4]}", f"Não sabe\n{sit[5]}"]

    ben = [(loc["D15"] == 1).sum(), (loc["D15"] == 2).sum(), (loc["D15"] == 88888).sum()]
    benp = [f"Com benefício\n{ben[0]}", f"Sem benefício\n{ben[1]}", f"Não sabe\n{ben[2]}"]

    esg = [(loc["B14"] == 1).sum(), (loc["B14"] == 2).sum(), (loc["B14"] == 88888).sum()]
    esgp = [f"Sim\n{esg[0]}", f"Não\n{esg[1]}", f"Não sabe\n{esg[1]}"]

    def plot_graph(selection):
        """Atualiza o gráfico conforme a categoria escolhida pelo usuário."""
        ax.clear()

        if selection == "Benefício":
            x = benp
            y = ben
            ax.set_title(f"Domicílios que recebem benefícios ({resultado})\nTotal de domicílios: {sum(y)}")
        elif selection == "Situação":
            x = sitp
            y = sit
            ax.set_title(f"Situação dos domicílios ({resultado})\nTotal de domicílios: {sum(y)}")
        elif selection == "Espécie":
            x = espp
            y = esp
            ax.set_title(f"Espécie dos domicílios ({resultado})\nTotal de domicílios: {sum(y)}")
        elif selection == "Tipo":
            x = tipop
            y = tipo
            ax.set_title(f"Tipos de domicílios ({resultado})\nTotal de domicílios: {sum(y)}")
        elif selection == "Esgoto":
            x = esgp
            y = esg
            ax.set_title(f"Existe saneamento básico? ({resultado})\nTotal de domicílios: {sum(y)}")
        else:
            return

        graf = ax.bar(x, y, label=selection)
        total = sum(y)
        percentages = [v / total * 100 for v in y]
        ax.bar_label(graf, labels=[f"{p:.1f}%" for p in percentages], padding=3)
        ax.legend()
        ax.grid(axis="y", linestyle="--", alpha = 0.5)

        canvas.draw()

    janela2 = tk.Toplevel(janela)
    janela2.title(f"Gráfico ({resultado})")
    janela2.geometry("700x700")

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=janela2)
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    selected_option = tk.StringVar(value="Espécie")

    opcoes = ["Espécie", "Tipo", "Situação", "Benefício", "Esgoto"]
    for opt in opcoes:
        ttk.Radiobutton(
            janela2,
            text=opt,
            value=opt,
            variable=selected_option,
            command=lambda: plot_graph(selected_option.get())
        ).pack(anchor=tk.W, padx=10, pady=5)



    plot_graph(selected_option.get())











janela = tk.Tk()
janela.title("Trabalho de APC")
janela.geometry("320x280")
tk.Label(janela, text="Recorte D: infraestrutura e condições dos domicilios").pack(pady=1)
tk.Label(janela, text="Aluno: Emanuel Parreira Negrão Basso (252008772)").pack(pady=1)
tk.Label(janela, text=f"moradores: {qtd_linhasm} - domicilios: {qtd_linhasd}").pack(pady=1)
selecionado = tk.StringVar(value="Escolha a região")
option_menu = tk.OptionMenu(janela, selecionado, *meu_dicionario.keys())
option_menu.pack(pady=1)
btn_show = tk.Button(janela, text="Confirmar", command=grafico)
btn_show.pack(pady=1)
exp = btn_exportar = tk.Button(janela, text="Exportar dados", command=exportar)
exp.pack(pady=1)
janela.mainloop()
