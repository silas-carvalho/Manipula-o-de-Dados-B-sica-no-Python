# Manipulação de Dados Básica no Python

Este projeto explora a manipulação de dados usando Python, utilizando o Spyder como ambiente de desenvolvimento integrado (IDE), fornecido pela distribuição Anaconda. O projeto abrange desde a instalação de pacotes essenciais até a importação de bibliotecas e manipulação de dados com pandas e NumPy. Para demonstrar as técnicas, utilizamos a base de dados PISA, incluindo etapas práticas como a conversão de colunas para tipos numéricos e a remoção de valores ausentes.

# Instalação de Pacotes

Os pacotes necessários para a análise de dados foram instalados diretamente no ambiente do Spyder:
```bash
!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install plotly
```

# Importação de Bibliotecas

As bibliotecas fundamentais para operações matemáticas e manipulação de dados foram importadas:
```bash
import numpy as np
import pandas as pd
```

# Utilização da Base de Dados PISA

Os dados do programa PISA foram carregados em um DataFrame utilizando a função pd.read_csv:
```bash
pisa = pd.read_csv("dados/notas_pisa.csv", delimiter=",")
```

# Conversão de Colunas para Tipo Numérico

As colunas do DataFrame foram convertidas para tipos numéricos, com valores não conversíveis sendo substituídos por NaN:
Conversão das colunas de 2022
```bash
pisa['mathematics_2022'] = pd.to_numeric(pisa['mathematics_2022'], errors='coerce')
pisa['reading_2022'] = pd.to_numeric(pisa['reading_2022'], errors='coerce')
pisa['science_2022'] = pd.to_numeric(pisa['science_2022'], errors='coerce')
```

Conversão das colunas de 2018

```bash
pisa['mathematics_2018'] = pd.to_numeric(pisa['mathematics_2018'], errors='coerce')
pisa['reading_2018'] = pd.to_numeric(pisa['reading_2018'], errors='coerce')
pisa['science_2018'] = pd.to_numeric(pisa['science_2018'], errors='coerce')
```

# Remoção de Linhas com Valores Ausentes

As linhas contendo valores ausentes foram excluídas do DataFrame, gerando um novo DataFrame sem NaN:

```bash
pisa_na = pisa.dropna()
```









