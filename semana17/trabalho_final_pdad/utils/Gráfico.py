def grafico():
    """Exibe uma janela com gráficos dos dados da região administrativa selecionada."""
    resultado = selecionado.get()
    value = meu_dicionario[resultado]
    loc = domicilios[domicilios["localidade"] == value] # Filtra os dados da região selecionada

    # Conta quantos domicílios são permanentes e improvisados
    esp = [(loc["B01"] == 1).sum(), (loc["B01"] == 2).sum()]
    espp = [f"Permanente\n{esp[0]}", f"Improvisado\n{esp[1]}"]

    # Conta os tipos de domicílio
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
        ax.clear() # Limpa o gráfico anterior antes de desenhar um novo

        # Atualiza o gráfica com os dados de acordo com o radio button selecionado
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

        graf = ax.bar(x, y, label=selection) # Desenha o gráfico de barras
        total = sum(y)
        percentages = [v / total * 100 for v in y] # Calcula a porcentagem de cada categoria
        ax.bar_label(graf, labels=[f"{p:.1f}%" for p in percentages], padding=3) # Exibe as porcentagens acima das barras
        ax.legend()
        ax.grid(axis="y", linestyle="--", alpha = 0.5)
        canvas.draw() # Atualiza o gráfico na janela

    janela2 = tk.Toplevel(janela)
    janela2.title(f"Gráfico ({resultado})")
    janela2.geometry("700x700")

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=janela2)
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    selected_option = tk.StringVar(value="Espécie")

    opcoes = ["Espécie", "Tipo", "Situação", "Benefício", "Esgoto"]

    # Cria uma lista de botões para cada variável dentro da lista "opcoes"
    for opt in opcoes:
        ttk.Radiobutton(janela2, text=opt, value=opt, variable=selected_option, command=lambda: plot_graph(selected_option.get())).pack(anchor=tk.W, padx=10, pady=5)
    plot_graph(selected_option.get())
