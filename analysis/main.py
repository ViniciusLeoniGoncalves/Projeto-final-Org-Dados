import os
import pandas as pd
import streamlit as st
import plotgraphics as pg

# Título e descrição do projeto


# Tratamento de caminho do arquivo
datapath = os.getcwd() + '/dataset/mobile_device_usage.csv'
if  os.path.exists(datapath):
    df = pd.read_csv(datapath)

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
        st.title("Trabalho Final - Análise e Visualização de Dados")
        st.subheader("Uso de dispositivos móveis e comportamento de usuário")
        st.markdown("""
            ### Instruções:
            - Use o menu lateral para escolher a análise que deseja visualizar.
            - Cada aba contém gráficos e insights específicos.
        """)
        st.write("### Dataset escolhido")
        st.dataframe(df)
        st.write(
            "Fonte: [Mobile Device Usage and User Behavior Dataset](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)"
        )
        df = df.drop(["User ID", "User Behavior Class"], axis = 1)
        st.write("### Dataset após limpeza")
        st.dataframe(df)
        st.markdown("""
            ### Trabalho desenvolvido por:
            - Eduardo Penedo - 120043223;
            - João Victor Borges - 121064604;
            - Vinicius Leoni - 121083446;
            - Vítor Ambrizzi - 121059455.
        """)
    # Exibir gráficos com base na aba selecionada
    elif opt == "Distribuição por sistema operacional":
        st.markdown("# Qual o modelo de celular mais popular entre os usuários?")
        st.write("Mostrando a distribuição de usuários de dispositivos móveis aparelhos por sistema operacional:")
        pg.so_distribuicao(df)
    elif opt == ("Média de consumo de bateria por dispositivo"):
        st.markdown("# Qual modelo de celular consome em média mais bateria?")
        st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
        pg.consumo_modelo(df)
    elif opt == ("Tempo de tela médio por idade"):
        st.markdown("# Qual idade passa mais tempo utilizando celular?")
        st.write("Olhando o tempo médio de tela por idade, percebemos que nesta análise as pessoas com **47 anos** possuem o tempo médio de uso mais elevado")
        pg.tela_idade(df)

        st.markdown("Também podemos ver que essa idade representa uma quantidade relevante da análise neste gráfico abaixo de pessoas por idade:")
        pg.quantidade_idade(df)
    elif opt == ("Tempo de tela médio por gênero"):
        st.markdown("# Quem passa mais tempo utilizando o celular; homens ou mulheres?")
        st.markdown("Observando o tempo médio de tela por gênero, podemos perceber que, por uma **pequeníssima** margem, homens tendem a ficar mais tempo ativamente no aparelho:")
        st.write("Iremos mostrar o tempo médio de tela por gênero:")
        pg.tela_genero(df)
    elif opt == ("Tempo de tela médio por faixa etária"):
        st.markdown("# Qual faixa entária passa mais tempo utilizando o celular?")
        st.markdown("Observamos já o tempo de tela por idade, mas essa informação pode ser muito granular.")
        st.markdown("Então observando o tempo de tela médio para cada **faixa etária**, podemos constatar que nesta análise que de forma geral, pessoas 50+ passam, em média, mais tempo com aparelho ativamente")
        st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
        pg.tela_faixa_etaria(df)

    elif opt == ("Ver todos"):

        st.markdown("# Qual o modelo de celular mais popular entre os usuários?")
        st.write("Mostrando a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
        pg.so_distribuicao(df)

        st.markdown("***")

        st.markdown("# Qual modelo de celular consome em média mais bateria?")
        st.write("Mostrando o consumo médio de bateria por modelo de dispositivo:")
        pg.consumo_modelo(df)

        st.markdown("***")

        st.markdown("# Qual idade passa mais tempo utilizando celular?")
        st.write("Olhando o tempo médio de tela por idade, percebemos que nesta análise as pessoas com **47 anos** possuem o tempo médio de uso mais elevado")
        pg.tela_idade(df)

        st.markdown("Também podemos ver que essa idade representa uma quantidade relevante da análise neste gráfico abaixo de pessoas por idade:")
        pg.quantidade_idade(df)
        
        st.markdown("***")

        st.markdown("# Quem passa mais tempo utilizando o celular; homens ou mulheres?")
        st.markdown("Observando o tempo médio de tela por gênero, podemos perceber que, por uma **pequeníssima** margem, homens tendem a ficar mais tempo ativamente no aparelho:")
        st.write("Iremos mostrar o tempo médio de tela por gênero:")
        pg.tela_genero(df)

        st.markdown("***")

        st.markdown("# Qual faixa entária passa mais tempo utilizando o celular?")
        st.markdown("Observamos já o tempo de tela por idade, mas essa informação pode ser muito granular.")
        st.markdown("Então observando o tempo de tela médio para cada **faixa etária**, podemos constatar que nesta análise que de forma geral, pessoas 50+ passam, em média, mais tempo com aparelho ativamente")
        st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
        pg.tela_faixa_etaria(df)
else:
    st.write("### Arquivo não encontrado!")
    st.write(f"O caminho '{datapath}' aparenta estar incorreto.")
    st.write("Certifique-se de estar no diretório principal do projeto e executar com: 'streamlit run analysis/main.py'")
