import streamlit as st
import pandas as pd
#testar o sidebar

st.title("Estatisticas dos jogadores na copa de 2026")

caminho = r"C:\Users\joao.assuncao\Downloads\fifa_world_cup_2026_player_performance.csv"
df = pd.read_csv(caminho)

st.write("Que jogador deseja analizar?")
name = st.text_input("Qual" ,max_chars=20  ,key ="Nome_Jogador" , width=300,placeholder="Nome do jogador")

if name:
    pesquisa = df["player_name"].str.contains(name, case=False)
    jogador = df[pesquisa]

    if not jogador.empty:
        st.write("###Estatistica do ${name}")
        st.dataframe(df["player_name"], on_select="rerun")
    else:
        st.write("Jogador não encontrado")



