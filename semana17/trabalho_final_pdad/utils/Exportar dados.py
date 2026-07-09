def exportar():
    """Exporta para um arquivo os domicílios da região administrativa selecionada."""
    resultado = selecionado.get() # Obtém a região escolhida pelo usuário

    # Verifica se uma região foi selecionada
    if resultado not in meu_dicionario:
        showinfo("Aviso", "Selecione uma região.")
        return

    value = meu_dicionario[resultado] # Obtém o código correspondente à região
    loc = domicilios[domicilios["localidade"] == value] # Filtra apenas os domicílios dessa região

    arquivo = filedialog.asksaveasfilename(initialfile=f"{resultado}.csv", defaultextension=".csv", filetypes=[("CSV", "*.csv"), ("Arquivo de texto", "*.txt")])

    if not arquivo:
        return

    # Exporta em CSV ou TXT dependendo da extensão escolhida
    if arquivo.endswith(".csv"):
        loc.to_csv(arquivo, index=False, sep=";", encoding="utf-8-sig")
    else:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(loc.to_string(index=False))

    showinfo("Sucesso", "Arquivo exportado com sucesso!")
