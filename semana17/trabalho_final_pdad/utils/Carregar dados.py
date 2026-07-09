arquivo_moradores = filedialog.askopenfilename(title="Selecione moradores.csv", filetypes=[("CSV", "*.csv")]) # Abre uma janela para o usuário selecionar o arquivo de moradores

arquivo_domicilios = filedialog.askopenfilename(title="Selecione domicilios.csv", filetypes=[("CSV", "*.csv")]) # Abre uma janela para selecionar o arquivo de domicílios

# Lê os arquivos CSV utilizando o pandas
moradores = pd.read_csv(arquivo_moradores, sep=";", decimal=",", encoding="utf-8-sig", low_memory=False)
domicilios = pd.read_csv(arquivo_domicilios, sep=",", encoding="utf-8-sig")

#Conta a quantidade de linhas dentro de cada data frame
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

meu_dicionario = dict(zip(RAsMenu, RAsNumeros)) # Pega as duas listas anteriores e cria um dicionário com elas
