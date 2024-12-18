import streamlit as st

memoria = st.session_state

if "dicionario_gestao" not in memoria:
    memoria.dicionario_gestao = {}

despesa = st.text_input('Despesas')
valor = st.number_input('Valor')
receita = st.number_input('Receita')

if st.button('ADD'):
    memoria.dicionario_gestao[despesa] = valor

st.table(memoria.dicionario_gestao)

soma = sum(memoria.dicionario_gestao.values())
st.write(f'Total de despesas: R${soma}')
#if memoria.dicionario_gestao:
#     memoria.dicionario_gestao[despesa] = Valor
     #st.write(f' Despesas: {soma}')

if receita >= soma:
    st.write('Suas despesas cabe dentro da sua receita !')
elif receita < soma:
     calc =  receita - soma
     st.write (f'Voce ainda tem uma divida de R$ {calc} , sua receita não foi o suficiente')   

if st.button('Limpar Histórico'):
    memoria.dicionario_gestao.clear()
    st.write('Histórico limpo!')        


