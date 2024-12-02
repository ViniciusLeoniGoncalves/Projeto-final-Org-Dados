import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotgraphics as pg

st.title("Bem-vindo ao site Galenus Análises")
st.subheader("Análise criada pelo grupo *Galenus Atrasadus*")

# Ler o CSV
df = pd.read_csv('../dataset/mobile_device_usage.csv')
df.describe()

#criar sidebar com botões para exibir os gráficos
opt=st.sidebar.radio("Veja as análises que temos prontas", options=("Aparelhos x Sistema","Eduardo","Consumo x Modelo","Idade x tempo de tela","Gênero x tempo de tela", "faixa Etária x tempo de tela", "ver todos"))

if opt=="Aparelhos x Sistema":
    st.write("Mostrando a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
    pg.plot_graphic_aparelhos_sistema()
if opt==("Consumo x Modelo"):
    st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
    pg.plot_graphic_consumo_modelo()
if opt==("Idade x tempo de tela"):
    st.write("Iremos mostrar o tempo médio de tela por idade:")
    pg.plot_graphic_idade_tempoTela()
if opt==("Gênero x tempo de tela"):
    st.write("Iremos mostrar o tempo médio de tela por gênero:")
    pg.plot_graphic_genero_tempoTela()
if opt==("faixa Etária x tempo de tela"):
    st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
    pg.plot_graphic_faixaEtaria_tempoTela()


if opt==("ver todos"):
    st.write("Mostrando a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
    pg.plot_graphic_aparelhos_sistema()

    st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
    pg.plot_graphic_consumo_modelo()

    st.write("Iremos mostrar o tempo médio de tela por idade:")
    pg.plot_graphic_idade_tempoTela()

    st.write("Iremos mostrar o tempo médio de tela por gênero:")
    pg.plot_graphic_genero_tempoTela()

    st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
    pg.plot_graphic_faixaEtaria_tempoTela()  




