import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.title('Sistema de Recomendação - Análise Exploratória')

st.header('Carregando e Pré-processando os Dados')

df = pd.read_csv('supermarket_sales.csv')
df['ID da Fatura 2'] = range(len(df))
df['Data'] = pd.to_datetime(df['Data'])

st.write(df.head())

st.header('Análise Descritiva')

st.write('Descrição:')
st.write(df.describe())

st.write('Dimensões:')
st.write('Linhas:', df.shape[0])
st.write('Colunas:', df.shape[1])

st.write('Tipos de Dados:')
st.write(df.dtypes)

st.write('Valores Nulos:')  
st.write(df.isna().sum())

st.header('Análise Univariada')

columns = ['Preço Unitário', 'Total', 'Avaliação', 'Lucro Bruto']

for col in columns:

  plt.figure()
  sns.histplot(df[col], kde=True)
  
  (mu, sigma) = stats.norm.fit(df[col])
  
  st.write(f'{col}: mu = {mu:.2f}, sigma = {sigma:.2f}')
  
  skew = df[col].skew()
  kurtosis = df[col].kurtosis()
  
  st.write(f'{col}: Assimetria: {skew:.2f}')
  st.write(f'{col}: Curtose: {kurtosis:.2f}')
  
  x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
  y = stats.norm.pdf(x, mu, sigma)
  plt.plot(x, y)

  plt.title(f'Distribuição de {col}')
  st.pyplot(plt)
  
  fig = plt.figure()
  stats.probplot(df[col], plot=plt)
  st.pyplot(fig)

st.header('Análise Bivariada')

st.subheader('Preço Unitário por Linha de Produto')

fig, ax = plt.subplots()
sns.boxplot(x='Linha de Produto', y='Preço Unitário', data=df, ax=ax)
sns.stripplot(x='Linha de Produto', y='Preço Unitário', data=df, ax=ax, 
              jitter=True, color='black', size=3)
st.pyplot(fig)

st.subheader('Vendas Totais por Tipo de Cliente, Pagamento e Gênero')

g = sns.FacetGrid(df, col='Pagamento', row='Tipo de Cliente', hue='Gênero')
g.map(sns.barplot, 'Linha de Produto', 'Total')
g.add_legend(title='Gênero')

for ax in g.axes.flat: 
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45) 

st.pyplot(g.fig)

st.header('Análise Temporal')

st.subheader('Densidade de Transações no Horário de Funcionamento')

df_hours = df[(df['Hora'].dt.hour >= 10) & (df['Hora'].dt.hour < 20)]
df_hours['MinutesParaAbertura'] = df_hours['Hora'].apply(lambda x: (x.hour - 10)*60 + x.minute)

fig, ax = plt.subplots()
sns.histplot(data=df_hours, x='MinutesParaAbertura', bins=60, kde=True, ax=ax)

st.pyplot(fig)

st.subheader('Vendas Semanais por Cidade')

df_weekly = df.groupby([df['Cidade'], pd.Grouper(key='Data', freq='W')])['Total'].sum().reset_index() 

fig, ax = plt.subplots()
sns.lineplot(data=df_weekly, x='Data', y='Total', hue='Cidade', ax=ax)

st.pyplot(fig)