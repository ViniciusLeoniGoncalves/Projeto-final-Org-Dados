import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotgraphics as pg

st.title("Bem-vindo ao site Galenus Análises")
st.subheader("Análise criada pelo grupo *Galenus Atrasadus*")

# Ler o CSV
df = pd.read_csv('../dataSheet/mobile_device_usage_dataset.csv')
opt=st.sidebar.radio("Veja as análises que temos prontas", options=("Aparelhos x Sistema","Eduardo","Consumo x Modelo","Idade x tempo de tela","Gênero x tempo de tela", "faixa Etária x tempo de tela"))
# Verificar se a coluna "Operating System" existe
if opt=="Aparelhos x Sistema":
    st.write("Mostrando a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
    pg.plot_graphic_aparelhos_sistema()

if opt==("Consumo x Modelo"):
    st.write("Mostrando a média de consumo de bateria por modelo de dispositivo:")
    pg.plot_graphic_consumo_modelo()
if opt==("Idade x tempo de tela"):
    st.write("Iremos mostrar a média de idade de pessoas por tempo de tela:")
    pg.plot_graphic_idade_tempoTela()
if opt==("Gênero x tempo de tela"):
    st.write("Iremos mostrar a média de tempo de tela por gênero:")
    pg.plot_graphic_genero_tempoTela()
if opt==("faixa Etária x tempo de tela"):
    st.write("Iremos mostrar o tempo de tela médio para cada faixa etária")
    pg.plot_graphic_faixaEtaria_tempoTela()

st.write("Média de tempo de tela por idade:")
st.title("A partir daqui deu ruim:")
st.text("não deu mais, plotei o gráfico")
#st.write("Iremos mostrar o tempo de tela médio para cada faixa etária")
#pg.plot_graphic_faixaEtaria_tempoTela()



