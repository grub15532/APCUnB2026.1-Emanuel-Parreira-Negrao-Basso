def gerar_relatorio():
    resultado = selecionado.get()

    if resultado not in meu_dicionario:
        showinfo("Aviso", "Selecione uma região.")
        return

    value = meu_dicionario[resultado]
    loc = domicilios[domicilios["localidade"] == value]

    # Estatísticas
    esp = [(loc["B01"] == 1).sum(), (loc["B01"] == 2).sum()]
    tipo = [(loc["B02"] == 1).sum(), (loc["B02"] == 2).sum(), (loc["B02"] == 3).sum()]
    sit = [
        (loc["B03"] == 1).sum(),
        (loc["B03"] == 2).sum(),
        (loc["B03"] == 3).sum(),
        (loc["B03"] == 4).sum(),
        (loc["B03"] == 5).sum(),
        (loc["B03"] == 88888).sum()
    ]
    ben = [(loc["D15"] == 1).sum(), (loc["D15"] == 2).sum(), (loc["D15"] == 88888).sum()]
    esg = [(loc["B14"] == 1).sum(), (loc["B14"] == 2).sum(), (loc["B14"] == 88888).sum()]

    # Solicita ao usuário onde salvar o relatório
    arquivo = filedialog.asksaveasfilename(
        initialfile=f"Relatorio_{resultado}.txt",
        defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt")]
    )

    if not arquivo:
        return

    # Escreve o relatório em um arquivo de texto
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE INFRAESTRUTURA DOS DOMICÍLIOS\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Região Administrativa: {resultado}\n")
        f.write(f"Código da região: {value}\n")
        f.write(f"Total de domicílios da região: {len(loc)}\n\n")

        f.write("ESPÉCIE DO DOMICÍLIO\n")
        f.write(f"  Permanente: {esp[0]}\n")
        f.write(f"  Improvisado: {esp[1]}\n\n")

        f.write("TIPO DO DOMICÍLIO\n")
        f.write(f"  Casa: {tipo[0]}\n")
        f.write(f"  Apartamento: {tipo[1]}\n")
        f.write(f"  Cômodo: {tipo[2]}\n\n")

        f.write("SITUAÇÃO DO DOMICÍLIO\n")
        f.write(f"  Próprio (quitado): {sit[0]}\n")
        f.write(f"  Próprio (pagando): {sit[1]}\n")
        f.write(f"  Alugado: {sit[2]}\n")
        f.write(f"  Cedido pelo empregador: {sit[3]}\n")
        f.write(f"  Cedido por outra pessoa: {sit[4]}\n")
        f.write(f"  Não sabe: {sit[5]}\n\n")

        f.write("BENEFÍCIO SOCIAL\n")
        f.write(f"  Recebem benefício: {ben[0]}\n")
        f.write(f"  Não recebem: {ben[1]}\n")
        f.write(f"  Não sabe: {ben[2]}\n\n")

        f.write("ESGOTAMENTO SANITÁRIO\n")
        f.write(f"  Possui: {esg[0]}\n")
        f.write(f"  Não possui: {esg[1]}\n")
        f.write(f"  Não sabe: {esg[2]}\n")

    showinfo("Sucesso", "Relatório gerado com sucesso!")