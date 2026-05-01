# Código para ler um arquivo Excel usando a biblioteca pandas
import pandas as pd

# Definindo o caminho do arquivo Excel
caminho = "C:\\teste_git\\dados\\não_processados\\tabela_vendas_ZePequeno.xlsx"

# Lendo o arquivo Excel e armazenando em um DataFrame
#zp = pd.read_excel(caminho, sheet_name='Planilha1')
zp = pd.read_excel(caminho)

print(zp)

print(zp.columns) # Exibe as colunas do DataFrame

print(zp.head()) # Exibe as primeiras linhas do DataFrame

print(zp.info()) # Exibe informações sobre o DataFrame, como tipos de dados e valores nulos

#print(zp.describe()) # Exibe estatísticas descritivas para colunas numéricas
