import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Breve descrição do aplicativo
st.subheader("_Minha Planilha_ de :blue[Receitas] e :red[Despesas] :sunglasses:")

st.write("Este é um app simples de gestão financeira.")


# Inicializa o estado da sessão
memoria = st.session_state

if "dicionario_gestao" not in memoria:
    memoria.dicionario_gestao = {"Despesas": {}, "Receitas": {}}

# Barra lateral para inserção de dados
st.sidebar.header("Adicionar Nova Transação")

# Entrada de dados na barra lateral
tipo_transacao = st.sidebar.selectbox('Tipo de Transação', ['Despesa', 'Receita'])
nome = st.sidebar.text_input('Nome')
valor = st.sidebar.number_input('Valor', min_value=0.0, step=0.01)

# Adiciona transações ao dicionário
if st.sidebar.button('Adicionar'):
    if tipo_transacao == 'Despesa' and nome:
        memoria.dicionario_gestao["Despesas"][nome] = valor
    elif tipo_transacao == 'Receita' and nome:
        memoria.dicionario_gestao["Receitas"][nome] = valor

# Exibe as tabelas de despesas e receitas
st.subheader("Despesas")
st.table(pd.DataFrame(memoria.dicionario_gestao["Despesas"].items(), columns=["Despesa", "Valor"]))

st.subheader("Receitas")
st.table(pd.DataFrame(memoria.dicionario_gestao["Receitas"].items(), columns=["Receita", "Valor"]))

# Calcula os totais de despesas e receitas
total_despesas = sum(memoria.dicionario_gestao["Despesas"].values())
total_receitas = sum(memoria.dicionario_gestao["Receitas"].values())

# Exibe os totais
st.write(f'Total de Despesas: R${total_despesas}')
st.write(f'Total de Receitas: R${total_receitas}')

# Verifica se a receita cobre as despesas
if total_receitas >= total_despesas:
    st.success('Suas despesas cabem dentro da sua receita!')
else:
    calc = total_receitas - total_despesas
    st.error(f'Você ainda tem uma dívida de R$ {calc:.2f}, sua receita não foi suficiente.')

# Limpa o histórico
if st.button('Limpar Histórico'):
    memoria.dicionario_gestao = {"Despesas": {}, "Receitas": {}}
    st.write('Histórico limpo!')

# Seleção de gráfico na barra lateral
st.sidebar.header("Visualização de Gráficos")
opcao_grafico = st.sidebar.selectbox('Selecionar Gráfico', ['Despesas', 'Receitas'])

# Gráficos usando matplotlib e Streamlit
st.subheader("Gráficos")

# Cria DataFrames para despesas e receitas
df_despesas = pd.DataFrame(memoria.dicionario_gestao["Despesas"].items(), columns=["Despesa", "Valor"]).set_index("Despesa")
df_receitas = pd.DataFrame(memoria.dicionario_gestao["Receitas"].items(), columns=["Receita", "Valor"]).set_index("Receita")

# Exibe o gráfico selecionado
if opcao_grafico == 'Despesas':
    fig, ax = plt.subplots()
    ax.bar(df_despesas.index, df_despesas['Valor'], color='red')
    ax.set_title('Despesas')
    ax.set_ylabel('Valor (R$)')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
elif opcao_grafico == 'Receitas':
    fig, ax = plt.subplots()
    ax.bar(df_receitas.index, df_receitas['Valor'], color='green')
    ax.set_title('Receitas')
    ax.set_ylabel('Valor (R$)')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
