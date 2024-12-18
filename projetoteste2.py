import streamlit as st
import pandas as pd

# Inicializa o estado da sessão
memoria = st.session_state

if "dicionario_gestao" not in memoria:
    memoria.dicionario_gestao = {"Despesas": {}, "Receitas": {}}

# Entrada de dados
despesa = st.text_input('Despesa')
valor_despesa = st.number_input('Valor da Despesa', min_value=0.0, step=0.01)
receita = st.text_input('Receita')
valor_receita = st.number_input('Valor da Receita', min_value=0.0, step=0.01)

# Adiciona despesas e receitas ao dicionário
if st.button('Adicionar Despesa'):
    if despesa:
        memoria.dicionario_gestao["Despesas"][despesa] = valor_despesa
if st.button('Adicionar Receita'):
    if receita:
        memoria.dicionario_gestao["Receitas"][receita] = valor_receita

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

# Gráficos usando Streamlit
st.subheader("Gráficos")

# Cria DataFrames para despesas e receitas
df_despesas = pd.DataFrame(memoria.dicionario_gestao["Despesas"].items(), columns=["Despesa", "Valor"]).set_index("Despesa")
df_receitas = pd.DataFrame(memoria.dicionario_gestao["Receitas"].items(), columns=["Receita", "Valor"]).set_index("Receita")

# Exibe gráficos de barras para despesas e receitas
st.bar_chart(df_despesas, use_container_width=True)
st.bar_chart(df_receitas, use_container_width=True)
