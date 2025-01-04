# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 07:58:47 2025

#Aluno: Silas Carvalho

#Escola e curso: MBA em Data Science e Analytics USP ESALQ

# Prof. Dr. Wilson Tarantin Junior
"""

# Manipulação de Dados Básica no Python

# Instalar pacotes para análise de dados

# Instalar pacotes diretamente no ambiente do notebook é uma maneira conveniente de configurar \
# seu ambiente de trabalho para análise de dados sem precisar sair e usar o terminal separadamente.

## Descrição:

# pandas: Uma ferramenta poderosa para manipulação e análise de dados. \
# numpy: Essencial para operações numéricas. \
# matplotlib: Ideal para criar gráficos e plots estáticos. \
# seaborn: Fornece gráficos estatísticos atraentes. \
# plotly: Perfeito para criar gráficos interativos e dinâmicos.

#%% Comandos de instalação
# Para executar a célula de código, pressione Shift + Enter enquanto estiver dentro da célula.

!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install plotly

#%%

## Importar bibliotecas essenciais para análise de dados

# NumPy é uma biblioteca para operações matemáticas e numéricas. \
# A apelidamos de 'np' para facilitar a leitura e escrita do código. \
# pandas é uma biblioteca poderosa para manipulação e análise de dados. \
# A apelidamos de 'pd' para tornar o código mais claro e conciso.

#%% Importar bibliotecas
# Para executar a célula de código, pressione Shift + Enter enquanto estiver dentro da célula.

import numpy as np
import pandas as pd

#%%

## Vamos utilizar a base de dados PISA

# pd.read_csv: Esta função é usada para ler um arquivo CSV e convertê-lo em um DataFrame pandas. \
# "notas_pisa.csv": Este é o nome do arquivo CSV que está sendo lido. \
# delimiter=",": Este parâmetro especifica que o delimitador no arquivo CSV é uma vírgula.

#%% Ler o arquivo CSV
# Esse comando lê um arquivo CSV chamado "notas_pisa.csv" e o carrega em um DataFrame pandas chamado pisa. \
# Fonte pisa https://pisadataexplorer.oecd.org/ide/idepisa/dataset.aspx \
# Para executar a célula de código, pressione Shift + Enter enquanto estiver dentro da célula.

pisa = pd.read_csv("dados/notas_pisa.csv", delimiter=",")

#%% Conversão de Colunas para Tipo Numérico

# Os seguintes comandos convertem as colunas especificadas do DataFrame 'pisa' para um tipo numérico. 
# Valores que não podem ser convertidos são substituídos por NaN (Not a Number). 
# Para executar cada célula de código, pressione Shift + Enter enquanto estiver dentro da célula.

# Converter colunas de 2022

pisa['mathematics_2022'] = pd.to_numeric(pisa['mathematics_2022'], errors='coerce')
pisa['reading_2022'] = pd.to_numeric(pisa['reading_2022'], errors='coerce')
pisa['science_2022'] = pd.to_numeric(pisa['science_2022'], errors='coerce')

#%%

# Converter colunas de 2018

pisa['mathematics_2018'] = pd.to_numeric(pisa['mathematics_2018'], errors='coerce')
pisa['reading_2018'] = pd.to_numeric(pisa['reading_2018'], errors='coerce')
pisa['science_2018'] = pd.to_numeric(pisa['science_2018'], errors='coerce')

#%%

# O comando pisa_na = pisa.dropna() remove todas as linhas do DataFrame 'pisa' \
# que contêm valores ausentes (NaN) e cria um novo DataFrame chamado 'pisa_na' \
# com as linhas restantes.

pisa_na = pisa.dropna()
#%%