import os
import pandas as pd
import streamlit as st
import plotgraphics as pg

# Título e descrição do projeto
st.title("Bem-vindo ao Galenus Análises")
st.subheader("Análise criada pelo grupo *Galenus Atrasadus*")

# Tratamento de caminho do arquivo
datapath = os.getcwd() + '/dataset/mobile_device_usage.csv'
if  os.path.exists(datapath):
    # Leitura e limpeza do dataset
    df = pd.read_csv(datapath)
    df = df.drop(["User ID", "User Behavior Class"], axis = 1)

    # Sidebar com as opções
    opt = st.sidebar.radio(
        "Navegue pelas análises disponíveis",
        options = (
            "Home",
            "Distribuição por sistema operacional",
            "Média de consumo de bateria por dispositivo", 
            "Tempo de tela médio por idade",
            "Tempo de tela médio por gênero",
            "Tempo de tela médio por faixa etária",
            "Ver todos"
        )
    )

    # Conteúdo
    # Página inicial
    if opt == "Home":
        st.write("# Uso de dispositivos móveis e comportamento de usuário")
        st.write("## Dataset Utilizado")
        st.dataframe(df)
        st.write(
            "Fonte do Dataset: [Mobile Device Usage and User Behavior Dataset](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)"
        )
        st.markdown(
            """
            ### Instruções:
            - Use o menu lateral para escolher a análise que deseja visualizar.
            - Cada aba contém gráficos e insights específicos.
            """
        )
    # Exibir gráficos com base na aba selecionada
    elif opt == "Distribuição por sistema operacional":
        st.write("Mostrando a distribuição de usuários de dispositivos móveis aparelhos por sistema operacional:")
        pg.so_distribuicao(df)
    elif opt == ("Média de consumo de bateria por dispositivo"):
        st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
        pg.consumo_modelo(df)
    elif opt == ("Tempo de tela médio por idade"):
        st.write("Iremos mostrar o tempo médio de tela por idade:")
        pg.tela_idade(df)
    elif opt == ("Tempo de tela médio por gênero"):
        st.write("Iremos mostrar o tempo médio de tela por gênero:")
        pg.tela_genero(df)
    elif opt == ("Tempo de tela médio por faixa etária"):
        st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
        pg.tela_faixa_etaria(df)
    elif opt == ("Ver todos"):
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
else:
    st.markdown(f"## Arquivo não encontrado: {datapath}")
    st.markdown("### Certifique-se de estar no diretório principal do projeto e executar com: streamlit run analysis/main.py")
