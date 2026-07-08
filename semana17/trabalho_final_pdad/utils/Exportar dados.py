def exportar():
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
