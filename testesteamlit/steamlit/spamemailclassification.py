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
    jogador = df[pesquisa]# retorna o dados com as linhas encontradas

    if not jogador.empty:
        evento = st.dataframe(jogador["player_name"], on_select="rerun",height="auto",width ="content",selection_mode='single-row')
        print(evento)
        #{'selection': {'rows': [0, 1, 3], 'columns': [], 'cells': []}} [0, 1, 3] dicionario que guarda arreys

        linha_selecionada = evento.selection["rows"]#selection chava padrão
        print(linha_selecionada)

        if linha_selecionada:   
            indice_linha = linha_selecionada[0]
            col1,col2,col3 = st.columns(3)

            col1.metric("Gols",jogador.iloc[indice_linha]["goals"])
            col2.metric("Assists",jogador.iloc[indice_linha]["assists"])
            col3.metric("Precisão de passes (%)",jogador.iloc[indice_linha]["total_passes"])

    else:
        st.write("Jogador não encontrado")
