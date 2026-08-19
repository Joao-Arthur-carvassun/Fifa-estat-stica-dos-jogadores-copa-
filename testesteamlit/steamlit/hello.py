import streamlit as st
import pandas as pd
import numpy as np


datas = {
    "Name": ["Alice", "Bob", "Charlie"], # coluna 1
    "Age": [25, 30, 35], #coluna 2
    "City": ["New York", "London", "Paris"] #coluna 3
}

df = pd.DataFrame(datas)
#DataFrame pega os dados 

st.line_chart(df,x="Name",y="City",color="#1316CF")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({ # cria uma tabel estatica
    'first column': [1, 2, 3, 4]
}))

st.dataframe()#tabela interativa

st.text("Texte de uma tabela datafrema por enquanto com on_selected = off")

dataframe = {
    "0" : 33,
    "1":44,
    "2":55
}

st.dataframe(dataframe,on_select="rerun")

