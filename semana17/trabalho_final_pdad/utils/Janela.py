janela = tk.Tk() # Cria a janela principal da aplicação
janela.title("Trabalho de APC")
janela.geometry("600x600")
tk.Label(janela, text="Recorte D: infraestrutura e condições dos domicilios").pack(pady=1)
tk.Label(janela, text="Aluno: Emanuel Parreira Negrão Basso (252008772)").pack(pady=1)
tk.Label(janela, text=f"moradores: {qtd_linhasm} - domicilios: {qtd_linhasd}").pack(pady=1)
selecionado = tk.StringVar(value="Escolha a região") # Variável que armazena a região escolhida no menu
option_menu = tk.OptionMenu(janela, selecionado, *meu_dicionario.keys()) # Cria o menu suspenso com todas as regiões administrativas
option_menu.pack(pady=1)
btn_show = tk.Button(janela, text="Confirmar", command=grafico) # Botão que abre a janela dos gráficos
btn_show.pack(pady=1)
exp = btn_exportar = tk.Button(janela, text="Exportar dados", command=exportar) # Botão para exportar os dados filtrados
exp.pack(pady=1)
btn_relatorio = tk.Button(janela, text="Gerar relatório", command=gerar_relatorio).pack(pady=1) # Botão que gera um relatório em formato TXT
janela.mainloop() # Inicia o loop principal da interface gráfica
