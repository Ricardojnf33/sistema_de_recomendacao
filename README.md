# Sistema de Recomendação para Dados de Supermercado

## Descrição do Projeto

Este projeto consiste em um sistema de recomendação construído com Python e Streamlit para fornecer insights sobre os dados de vendas de um supermercado. O sistema realiza uma análise exploratória abrangente dos dados e poderia ser expandido para incluir diferentes modelos de recomendação.

# Conjunto de Dados

O conjunto de dados `supermarket_sales.csv` contém transações de vendas de um supermercado localizado em 3 diferentes cidades. Ele inclui informações como:

- Data e hora da transação
- Cidade
- Cliente tipo (Membro vs Normal)
- Gênero do cliente
- Produto linha (Alimentos, Bebidas, Detergente, etc)
- Quantidade vendida de cada produto
- Preço unitário
- Taxas e impostos
- Lucro total
- Pagamento (Dinheiro, Cartão, Vale)
- Classificação dada pelo cliente

## Bibliotecas Utilizadas

- `streamlit` - Para construir o webapp
- `pandas` - Para análise de dados
- `matplotlib` e `seaborn` - Para visualizações
- `scipy` - Para estatísticas e distribuições

## Análise de Dados

A análise de dados realizada inclui:

- **Análise Descritiva**: Estatísticas resumidas do conjunto de dados e verificação de dados ausentes
- **Análise Univariada**: Histograma, estatísticas e distribuição normal de variáveis numéricas chave
- **Análise Bivariada**: Boxplot de preço por produto, gráficos de barras agrupados de vendas
- **Análise Temporal**: Densidade de transações ao longo do dia, tendência semanal por cidade

## Modelos Potenciais

O sistema poderia ser estendido para incluir modelos de recomendação como:

- Filtragem Colaborativa
- Sistema de Recomendação Baseado em Conteúdo
- Classificação por Associação
- Deep Learning com Embedding

A análise exploratória realizada fornece uma base sólida para selecionar os modelos mais apropriados.

## Como Usar

O aplicativo Streamlit pode ser executado localmente com:

`streamlit run app.py`

Para implantação na nuvem, o Streamlit Cloud oferece implantação rápida. Basta conectar o repositório do GitHub e implantar com um clique.

## Contribuindo

Pull requests são bem-vindos! Sinta-se à vontade para contribuir com este projeto abrindo um problema ou enviando um PR para resolver um problema ou adicionar uma nova funcionalidade.




















