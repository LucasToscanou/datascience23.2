# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:56:25 2023

@author: Lucas
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import PolynomialFeatures


arquivo = pd.read_csv('C://Users//Lucas//Desktop//Intro Ciencia de Dados//spotify-2023.csv', index_col=None, header=0, decimal=',', encoding='latin1')


Corr01 = arquivo[["bpm",'danceability_%']]

Corr01.plot(kind = 'scatter', x = 'bpm', y = 'danceability_%',title = 'BPM x Dançabilidade')



# =============================================================================
# REGRESSAO LINEAR
# =============================================================================

# Crie um gráfico de dispersão com o seaborn
sns.scatterplot(data=Corr01, x='bpm', y='danceability_%')

# Crie a linha de regressão usando o seaborn
sns.regplot(data=Corr01, x='bpm', y='danceability_%', scatter=False, color='red', line_kws={"linewidth": 2})

# Adicione rótulos e título ao gráfico
plt.xlabel('bpm')
plt.ylabel('danceability_%')
plt.title('Gráfico de Dispersão com Linha de Regressão')

# Exiba o gráfico
plt.show()

# =============================================================================
# REGRESSAO POLINOMIAL
# =============================================================================

# Criar um DataFrame para a regressão polinomial
X = Corr01[['bpm']]
y = Corr01['danceability_%']

# Transformar a variável independente em um polinômio de segundo grau
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Ajustar um modelo de regressão linear aos dados transformados
regressor = LinearRegression()
regressor.fit(X_poly, y)

# Prever os valores usando o modelo ajustado
y_pred = regressor.predict(X_poly)

# Criar o gráfico de dispersão usando seaborn
sns.scatterplot(data=Corr01, x='bpm', y='danceability_%', label='Dados reais')

# Plotar a regressão polinomial
sns.lineplot(x=X['bpm'], y=y_pred, color='red', label='Regressão Quadrática')

plt.xlabel('bpm')
plt.ylabel('danceability_%')
plt.title('Regressão Quadrática entre bpm e danceability_%')
plt.legend()
plt.show()













