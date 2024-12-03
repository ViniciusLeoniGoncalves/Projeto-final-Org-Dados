import matplotlib.pyplot as plt
import streamlit as st
from pandas import isna

plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.rcParams.update({'font.size': 15})

def so_distribuicao(df):
    # Contar ocorrências de cada sistema operacional
    os_counts = df["Operating System"].value_counts()

    fig, ax = plt.subplots(figsize = (10, 6))
    ax.pie( # Configura o gráfico de pizza
        os_counts.values,
        labels = os_counts.index,
        autopct = '%1.2f%%',
        startangle = 90,
        colors = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff']
    )

    # Personalizar o gráfico
    ax.axis('equal')    # Corrige o formato para um círculo
    plt.title("Distribuição de usuários por sistema operacional")

    st.pyplot(fig)

def consumo_modelo(df):
    # Calcular a média do consumo de bateria por modelo
    battery_drain_avg = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()

    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(  # Configura o grafico de barras
        battery_drain_avg['Device Model'], 
        battery_drain_avg['Battery Drain (mAh/day)'], 
        color = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width = 0.6
    )

    # Personalizar o gráfico
    plt.title("Média de consumo de bateria por dispositivo")
    plt.xlabel("Dispositivos")
    plt.ylabel("Média de consumo de bateria (mAh/dia)")
    ax.set_ylim([min(battery_drain_avg['Battery Drain (mAh/day)']) - 50, max(battery_drain_avg['Battery Drain (mAh/day)']) + 50])   # Ajusta o intervalo do eixo y
    plt.xticks(rotation = 30) # Rotaciona os rótulos para melhor visualização
    plt.tight_layout()  # Ajusta o layout para evitar sobreposições

    # Adiciona o valor acima da barra
    for i, bar in enumerate(bars):
        yval = bar.get_height() # Obtém a altura (valor) da barra
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # Posição horizontal do texto (centro da barra)
            yval + 0.1,     # Posição vertical (logo acima da barra)
            round(battery_drain_avg['Battery Drain (mAh/day)'][i], 2),  # Texto a ser exibido (valor arredondado)
            ha = 'center',  # Alinha o texto horizontalmente ao centro
            va = 'bottom',  # Alinha o texto verticalmente à parte inferior do texto
            fontsize = 15   # Define o tamanho da fonte do texto
        )

    st.pyplot(fig)

def tela_idade(df):
    # Calcular a média de idade de pessoas por tempo de tela
    age_screen_time_avg = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()

    fig, ax = plt.subplots(figsize = (10, 6))
    ax.bar( # Configura o grafico de barras
        age_screen_time_avg['Age'],
        age_screen_time_avg['Screen On Time (hours/day)'],
        color =  ['#18c0c4'],
        width = 0.6
    )

    # Personalizar o gráfico
    plt.title("Tempo de tela médio por idade")
    plt.xlabel("Idade")
    plt.ylabel("Tempo de tela médio (horas/dia)")
    ax.set_xlim([min(age_screen_time_avg['Age']) - 1, max(age_screen_time_avg['Age']) + 1]) # Ajusta o intervalo do eixo x
    ax.set_ylim([min(age_screen_time_avg['Screen On Time (hours/day)']) - 0.5, max(age_screen_time_avg['Screen On Time (hours/day)']) + 0.5])   # Ajusta o intervalo do eixo y
    plt.tight_layout()  # Ajusta o layout para evitar sobreposições

    st.pyplot(fig)

def quantidade_idade(df):
    # Calcular a quantidade de pessoas por idade
    age_count = df['Age'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize = (10, 6))
    ax.bar( # Configura o grafico de barras
        age_count.index,
        age_count.values,
        color = ['#18c0c4'],
        width = 0.6
    )

    # Personaliza o gráfico
    plt.title("Contagem de pessoas por idade")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade de pessoas")
    ax.set_xlim([min(age_count.index) - 1, max(age_count.index) + 1])   # Ajusta o intervalo do eixo x
    plt.tight_layout()

    st.pyplot(fig)

def tela_genero(df):
    # Calcular a média do tempo de tela por gênero
    df['Gender'] = df['Gender'].replace({'Female': 'Feminino', 'Male': 'Masculino'})
    gender_screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()

    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar( # Configura o grafico de barras
        gender_screen_time_avg['Gender'],
        gender_screen_time_avg['Screen On Time (hours/day)'],
        color = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width = 0.6,
    )

    plt.title("Tempo de tela médio por gênero", fontsize = 15)
    plt.xlabel("Gênero", fontsize = 15)
    plt.ylabel("Tela Ligada (Hora/dia)", fontsize = 15)
    ax.set_ylim([min(gender_screen_time_avg['Screen On Time (hours/day)']) - 0.05, max(gender_screen_time_avg['Screen On Time (hours/day)']) + 0.05])   # Ajusta o intervalo do eixo y
    plt.tight_layout()  

     # Adiciona o valor acima da barra
    for i, bar in enumerate(bars):
        yval = bar.get_height() # altura (valor) da barra
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            yval + 0.001,     # Posição acima da barra
            round(gender_screen_time_avg['Screen On Time (hours/day)'][i], 2), # Texto a ser exibido (valor arredondado)
            ha = 'center',  # Alinha o texto 
            va = 'bottom',  # Alinha o texto verticalmente à parte inferior do texto
            fontsize = 15   # Define o tamanho da fonte do texto
        )

    st.pyplot(fig)

def filtros_faixa_etaria(df):
    # Configuração dos filtros de idade
    filtros = [
        df[df['Age'] <= 20],
        df[(df['Age'] > 20) & (df['Age'] <= 30)],
        df[(df['Age'] > 30) & (df['Age'] <= 40)],
        df[(df['Age'] > 40) & (df['Age'] <= 50)],
        df[(df['Age'] > 50)]
    ]

    return filtros

labels_faixa_etaria = ['[0 - 20]', '[21 - 30]', '[31 - 40]', '[41 - 50]', '[ 50+ ]']

def tela_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Calcular a média do tempo de tela para cada filtro de idade
    medias = [filtro['Screen On Time (hours/day)'].mean() for filtro in filtros]
    medias = [0 if isna(val) else val for val in medias]  # Substitui NaN por 0

    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar( # Configura o grafico de barras
        labels_faixa_etaria,
        medias,
        color =  ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width = 0.6
    )

    # Personalizar o gráfico
    plt.title('Tempo de tela médio por faixa etária')
    plt.xlabel('Faixa etária')
    plt.ylabel('Tempo de tela médio (horas/dia)')
    ax.set_ylim([min(medias) - 0.1, max(medias) + 0.1])   # Ajusta o intervalo do eixo y

    # Adiciona o valor acima da barra
    for i, bar in enumerate(bars):
        yval = bar.get_height() # Obtém a altura (valor) da barra
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # Posição horizontal do texto (centro da barra)
            yval + 0.01,     # Posição vertical (logo acima da barra)
            round(medias[i], 2), # Texto a ser exibido (valor arredondado) 
            ha = 'center',  # Alinha o texto horizontalmente ao centro
            va = 'bottom',  # Alinha o texto verticalmente à parte inferior do texto
            fontsize =15   # Define o tamanho da fonte do texto
        )  # Adiciona o texto com a média correspondente
    
    st.pyplot(fig)

def usuarios_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Contagem de usuários por faixa etária
    contagem = [len(filtro) for filtro in filtros]
    contagem = [0 if isna(val) else val for val in contagem]  # Substitui NaN por 0

    fig, ax = plt.subplots(figsize = (10, 6))
    wedeges, texts, autotexts = ax.pie( # Configura o gráfico de pizza
        contagem,
        autopct = '%1.2f%%',
        startangle = 90,
        colors = ["#ffb3b3","#80b3ff","#b3ffb3","#ffb366","#c2b3ff"]
    )

    # Personalizar o gráfico
    ax.axis('equal')    # Corrige o formato para um círculo
    # Adicionar a legenda fora do gráfico
    ax.legend(
        wedeges,    # Referência às fatias do gráfico
        labels_faixa_etaria,          # Texto da legenda
        title = "Faixas Etárias",
        loc = "center left",            # Localização da legenda
        bbox_to_anchor=(1, 0, 0.5, 1)   # Ajusta a posição da legenda (fora do gráfico)
    )
    plt.title("Distribuição de usuários por faixa etária")

    st.pyplot(fig)

def usuarios_genero(df):
    # Configuração dos filtros de gênero
    filtros = [
        df[df['Gender'] == "Male"],
        df[df['Gender'] == "Female"]
    ]
    labels_genero = ["Masculino", "Feminino"]

    # Contagem de usuários por gênero
    contagem = [len(filtro) for filtro in filtros]
    contagem = [0 if isna(val) else val for val in contagem]  # Substitui NaN por 0

    fig, ax = plt.subplots(figsize = (10, 6))

    ax.pie( # Configura o gráfico de pizza
        contagem,
        labels = labels_genero,
        autopct = '%1.2f%%',
        startangle = 90,
        colors = ["#66b3ff", "#ff9999"]
    )

    # Personalizar o gráfico
    ax.axis('equal')    # Corrige o formato para um círculo
    plt.title("Distribuição de usuários por gênero")

    st.pyplot(fig)

def aplicativos_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Calcular a média do tempo de tela para cada filtro de idade
    medias = [filtro['Number of Apps Installed'].mean() for filtro in filtros]
    medias = [0 if isna(val) else val for val in medias]  # Substitui NaN por 0

    fig, ax = plt.subplots(figsize = (10, 6))
    ax.bar( # Configura o grafico de barras
        labels_faixa_etaria,
        medias,
        color = ["#ffb3b3","#80b3ff","#b3ffb3","#ffb366","#c2b3ff"],
        width = 0.6
    )

    # Personalizar o gráfico
    plt.title('Média de aplicativos instalados por faixa etária')
    plt.xlabel('Faixa etária')
    plt.ylabel('Aplicativos instalados')
    ax.set_ylim([min(medias) - 1, max(medias) + 1])   # Ajusta o intervalo do eixo y

    st.pyplot(fig)
