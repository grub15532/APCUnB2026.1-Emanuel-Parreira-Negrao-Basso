def grafico():
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

    def plot_graph(selection):
        ax.clear()

        if selection == "Benefício":
            x = benp
            y = ben
            ax.set_title(f"Domicílios que recebem benefícios ({resultado})")
        elif selection == "Situação":
            x = sitp
            y = sit
            ax.set_title(f"Situação dos domicílios ({resultado})")
        elif selection == "Espécie":
            x = espp
            y = esp
            ax.set_title(f"Espécie dos domicílios ({resultado})")
        elif selection == "Tipo":
            x = tipop
            y = tipo
            ax.set_title(f"Tipos de domicílios ({resultado})")
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

    opcoes = ["Espécie", "Tipo", "Situação", "Benefício"]
    for opt in opcoes:
        ttk.Radiobutton(
            janela2,
            text=opt,
            value=opt,
            variable=selected_option,
            command=lambda: plot_graph(selected_option.get())
        ).pack(anchor=tk.W, padx=10, pady=5)



    plot_graph(selected_option.get())