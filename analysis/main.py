import os
import pandas as pd
import streamlit as st
import plotgraphics as pg

# Título e descrição do projeto
st.title("Trabalho Final - Análise e Visualização de Dados")
st.subheader("Uso de dispositivos móveis e comportamento de usuário")

# Tratamento de caminho do arquivo
datapath = os.getcwd() + '/dataset/mobile_device_usage.csv'
if  os.path.exists(datapath):
    df = pd.read_csv(datapath)

    # Sidebar com as opções
    opt = st.sidebar.radio(
        "Navegue pelas análises disponíveis",
        options = (
            "Página inicial",
            "Distribuição por sistema operacional",
            "Média de consumo de bateria por dispositivo",
            "Tempo de tela médio por idade",
            "Tempo de tela médio por gênero",
            "Tempo de tela médio por faixa etária",
            "Distribuição de usuários por faixa etária",
            "Distribuição de usuários por gênero",
            "Média de aplicativos instalados por faixa etária",
            "Ver todos"
        )
    )

    # Conteúdo
    # Página inicial
    if opt == "Página inicial":
        st.markdown("""
            ### Instruções:
            - Use o menu lateral para escolher a análise que deseja visualizar.
            - Cada aba contém gráficos e insights específicos.
            - O menu lateral pode ser acessado a qualquer momento.
            - Ao final de toda página você pode ser direcionado para a página inicial.
        """)
        st.write("### Dataset escolhido")
        st.dataframe(df)
        st.write(
            "Fonte: [Mobile Device Usage and User Behavior Dataset](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset)"
        )

        # Limpeza
        df = df.drop(["User ID", "User Behavior Class"], axis = 1)
        st.write("""
            Após realizar o entendimento do dataset, ficou claro que não existiam
            valores nulos, e que a única limpeza necessária seria a das colunas
            "User ID" e "User Behavior Class", desnecessárias para a análise.
        """)

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
        st.write("Observando contagem de sistemas operacionais em nossa base de dados, é possível afirmar com certeza que os aparelhos celulares dos usuários utilizam **predominantemente** o Android. Veja a proporção:")
        pg.so_distribuicao(df)
    elif opt == ("Média de consumo de bateria por dispositivo"):
        st.markdown("# Qual modelo de celular consome em média mais bateria?")
        st.write("Ao observar o consumo médio de bateria por modelo de celular, podemos constatar por uma margem significativa que o **Iphone 12** é o aparelho que mais consome bateria, em média. Vejamos o gráfico:")
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
    elif opt == ("Distribuição de usuários por faixa etária"):
        st.markdown("# Qual a faixa etária mais predominante?")
        st.markdown("Podemos observar no gráfico abaixo que os usuários na faixa de **[21-30] e [31-40]** predominam em nossa base de dados.")
        pg.usuarios_faixa_etaria(df)
    elif opt == ("Distribuição de usuários por gênero"):
        st.markdown("# A base de dados tem mais usuários homens ou mulheres?")
        st.markdown("Observando o gráfico abaixo, podemos ver que a proporção é bem próxima, mas ainda assim existem **mais usuários masculinos**")
        pg.usuarios_genero(df)
    elif opt == ("Média de aplicativos instalados por faixa etária"):
        st.markdown("# Qual faixa etária guarda mais aplicativos?")
        st.markdown("Observando o gráfico abaixo, podemos ver que os usuários na **faixa de [21-30]** tem mais aplicativos instalados")
        pg.aplicativos_faixa_etaria(df)
    elif opt == ("Ver todos"):

        st.markdown("# Qual o modelo de celular mais popular entre os usuários?")
        st.write("Observando contagem de sistemas operacionais em nossa base de dados, é possível afirmar com certeza que os aparelhos celulares dos usuários utilizam **predominantemente** o Android. Veja a proporção:")
        pg.so_distribuicao(df)

    
        st.markdown("# Qual modelo de celular consome em média mais bateria?")
        st.write("Ao observar o consumo médio de bateria por modelo de celular, podemos constatar por uma margem significativa que o **Iphone 12** é o aparelho que mais consome bateria, em média. Vejamos o gráfico:")
        pg.consumo_modelo(df)
    

        st.markdown("# Qual idade passa mais tempo utilizando celular?")
        st.write("Olhando o tempo médio de tela por idade, percebemos que nesta análise as pessoas com **47 anos** possuem o tempo médio de uso mais elevado")
        pg.tela_idade(df)

        st.markdown("Também podemos ver que essa idade representa uma quantidade relevante da análise neste gráfico abaixo de pessoas por idade:")
        pg.quantidade_idade(df)

    
        st.markdown("# Quem passa mais tempo utilizando o celular; homens ou mulheres?")
        st.markdown("Observando o tempo médio de tela por gênero, podemos perceber que, por uma **pequeníssima** margem, homens tendem a ficar mais tempo ativamente no aparelho:")
        st.write("Iremos mostrar o tempo médio de tela por gênero:")
        pg.tela_genero(df)
    

        st.markdown("# Qual faixa entária passa mais tempo utilizando o celular?")
        st.markdown("Observamos já o tempo de tela por idade, mas essa informação pode ser muito granular.")
        st.markdown("Então observando o tempo de tela médio para cada **faixa etária**, podemos constatar que nesta análise que de forma geral, pessoas 50+ passam, em média, mais tempo com aparelho ativamente")
        st.markdown("Iremos mostrar o tempo de tela médio para cada **faixa etária**")
        pg.tela_faixa_etaria(df)
    

        st.markdown("# Qual a faixa etária mais predominante?")
        st.markdown("Podemos observar no gráfico abaixo que os usuários na faixa de **[21-30] e [31-40]** predominam em nossa base de dados.")
        pg.usuarios_faixa_etaria(df)
    

              

        st.markdown("# Qual faixa etária guarda mais aplicativos?")
        st.markdown("Observando o gráfico abaixo, podemos ver que os usuários na **faixa de [21-30]** tem mais aplicativos instalados")
        pg.aplicativos_faixa_etaria(df)

        
else:
    st.write("### Arquivo não encontrado!")
    st.write(f"O caminho '{datapath}' aparenta estar incorreto.")
    st.write("Certifique-se de estar no diretório principal do projeto e executar com: 'streamlit run analysis/main.py'")
