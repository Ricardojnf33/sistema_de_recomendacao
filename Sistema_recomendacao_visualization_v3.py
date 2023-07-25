# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Definindo o título da aplicação
st.title('Sistema de Recomendação - Análise Exploratória')

# Criando um cabeçalho para indicar o carregamento e pré-processamento dos dados
st.header('Carregando e Pré-processando os Dados')

# Carregando o arquivo CSV contendo os dados e armazenando no DataFrame 'df'
df = pd.read_csv('notebooks/supermarket_sales.csv')

# Verificando e tratando valores faltantes (se houver)
df = df.dropna()

# Convertendo a coluna 'Data' para o tipo de dados datetime
df['Data'] = pd.to_datetime(df['Data'])

# Adicionando uma coluna 'ID da Fatura' que contém um número sequencial para cada registro do DataFrame
df['ID da Fatura'] = range(len(df))

# Exibindo as primeiras linhas do DataFrame para uma visualização inicial
st.write(df.head())

# Criando um cabeçalho para a seção de análise descritiva
st.header('Análise Descritiva')

# Exibindo a descrição estatística do DataFrame
st.write('Descrição:')
st.write(df.describe())

# Exibindo o número de linhas e colunas do DataFrame
st.write('Dimensões:')
st.write('Linhas:', df.shape[0])
st.write('Colunas:', df.shape[1])

# Exibindo os tipos de dados presentes no DataFrame
st.write('Tipos de Dados:')
st.write(df.dtypes)

# Exibindo o número de valores nulos em cada coluna do DataFrame
st.write('Valores Nulos:')
st.write(df.isna().sum())

# Criando um cabeçalho para a seção de análise univariada
st.header('Análise Univariada')

# Lista de colunas numéricas que serão analisadas
columns = ['Preço Unitário', 'Total', 'Avaliação', 'Lucro Bruto']

# Para cada coluna, serão criados gráficos de histograma, estatísticas de distribuição,
# gráfico de densidade e gráfico de probabilidade normal
for col in columns:
    plt.figure()
    sns.histplot(df[col], kde=True)

    # Ajustando uma distribuição normal aos dados e calculando a média (mu) e desvio padrão (sigma)
    (mu, sigma) = stats.norm.fit(df[col])

    # Exibindo os parâmetros da distribuição normal
    st.write(f'{col}: mu = {mu:.2f}, sigma = {sigma:.2f}')

    # Calculando a assimetria e a curtose dos dados
    skew = df[col].skew()
    kurtosis = df[col].kurtosis()

    # Exibindo os valores de assimetria e curtose
    st.write(f'{col}: Assimetria: {skew:.2f}')
    st.write(f'{col}: Curtose: {kurtosis:.2f}')

    # Criando uma distribuição normal com base nos parâmetros mu e sigma
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)

    # Plotando a distribuição normal sobre o histograma
    plt.plot(x, y)

    plt.title(f'Distribuição de {col}')

    # Exibindo o gráfico usando a função st.pyplot() do Streamlit
    st.pyplot(plt)

    # Criando um gráfico de probabilidade normal (QQ plot) para avaliar a normalidade dos dados
    fig = plt.figure()
    stats.probplot(df[col], plot=plt)

    # Exibindo o gráfico de probabilidade normal
    st.pyplot(fig)

# Criando um cabeçalho para a seção de análise bivariada
st.header('Análise Bivariada')

# Subseção: Preço Unitário por Linha de Produto
st.subheader('Preço Unitário por Linha de Produto')

# Criando um boxplot e um stripplot para visualizar a distribuição do preço unitário por linha de produto
fig, ax = plt.subplots()
sns.boxplot(x='Linha de Produto', y='Preço Unitário', data=df, ax=ax)
sns.stripplot(x='Linha de Produto', y='Preço Unitário', data=df, ax=ax,
              jitter=True, color='black', size=3)

# Exibindo o gráfico usando a função st.pyplot() do Streamlit
st.pyplot(fig)

# Subseção: Vendas Totais por Tipo de Cliente, Pagamento e Gênero
st.subheader('Vendas Totais por Tipo de Cliente, Pagamento e Gênero')

# Criando um gráfico de barras faceted (por colunas e linhas) para comparar as vendas totais
# por tipo de cliente, tipo de pagamento e gênero
g = sns.FacetGrid(df, col='Pagamento', row='Tipo de Cliente', hue='Gênero')
g.map(sns.barplot, 'Linha de Produto', 'Total')
g.add_legend(title='Gênero')

# Rotacionando os rótulos do eixo x para melhor visualização
for ax in g.axes.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Exibindo o gráfico usando a função st.pyplot() do Streamlit
st.pyplot(g.fig)

# Criando um cabeçalho para a seção de análise temporal
st.header('Análise Temporal')

# Subseção: Densidade de Transações no Horário de Funcionamento
st.subheader('Densidade de Transações no Horário de Funcionamento')

# Filtrando as transações que ocorrem entre as 10h e 20h e calculando o tempo em minutos até a abertura da loja
df_hours = df[(df['Hora'].dt.hour >= 10) & (df['Hora'].dt.hour < 20)]
df_hours['MinutesParaAbertura'] = df_hours['Hora'].apply(lambda x: (x.hour - 10) * 60 + x.minute)

# Criando um histograma com a densidade de transações ao longo do horário de funcionamento
fig, ax = plt.subplots()
sns.histplot(data=df_hours, x='MinutesParaAbertura', bins=60, kde=True, ax=ax)

# Exibindo o gráfico usando a função st.pyplot() do Streamlit
st.pyplot(fig)

# Subseção: Vendas Semanais por Cidade
st.subheader('Vendas Semanais por Cidade')

# Agrupando as vendas por cidade e semana, e calculando o total de vendas em cada semana
df_weekly = df.groupby([df['Cidade'], pd.Grouper(key='Data', freq='W')])['Total'].sum().reset_index()

# Criando um gráfico de linhas para visualizar as vendas semanais por cidade
fig, ax = plt.subplots()
sns.lineplot(data=df_weekly, x='Data', y='Total', hue='Cidade', ax=ax)

# Exibindo o gráfico usando a função st.pyplot() do Streamlit
st.pyplot(fig)

# Rodapé da aplicação
st.footer('Powered by Cheetah Data Science')

