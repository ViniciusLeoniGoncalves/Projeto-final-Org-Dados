import os
import pandas as pd
import streamlit as st
import plotgraphics as pg

st.title("Bem-vindo ao Galenus Análises")
st.subheader("Análise criada pelo grupo *Galenus Atrasadus*")

datapath = os.getcwd() + '/dataset/mobile_device_usage.csv'
if  os.path.exists(datapath):
    df = pd.read_csv(datapath)

    # Criar sidebar com botões para exibir os gráficos
    opt = st.sidebar.radio(
        "Veja as análises que temos prontas",
        options = ("Aparelhos x Sistema", "Eduardo", "Consumo x Modelo", "Idade x tempo de tela", "Gênero x tempo de tela", "faixa Etária x tempo de tela", "ver todos")
    )

    if opt == "Aparelhos x Sistema":
        st.write("Mostrando a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
        pg.so_distribuicao(df)
    if opt == ("Consumo x Modelo"):
        st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
        pg.consumo_modelo(df)
    if opt == ("Idade x tempo de tela"):
        st.write("Iremos mostrar o tempo médio de tela por idade:")
        pg.tela_idade(df)
    if opt == ("Gênero x tempo de tela"):
        st.write("Iremos mostrar o tempo médio de tela por gênero:")
        pg.tela_genero(df)
    if opt == ("faixa Etária x tempo de tela"):
        st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
        pg.tela_faixa_etaria(df)
    if opt == ("ver todos"):
        st.write("Mostrando a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
        pg.so_distribuicao(df)

    st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
    pg.consumo_modelo(df)

    st.write("Iremos mostrar o tempo médio de tela por idade:")
    pg.tela_idade(df)

    st.write("Iremos mostrar o tempo médio de tela por gênero:")
    pg.tela_genero(df)

    st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
    pg.tela_faixa_etaria(df)

    st.title("A partir daqui deu ruim:")
    st.text("não deu mais, plotei o gráfico")
else:
    st.markdown(f"## Arquivo não encontrado: {datapath}")
    st.markdown("### Certifique-se de estar no diretório principal do projeto e executar com: streamlit run analysis/main.py")