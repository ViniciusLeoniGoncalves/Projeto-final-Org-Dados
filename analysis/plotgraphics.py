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
    ax.set_ylim([1400, 1600])   # Ajusta o intervalo do eixo y
    plt.xticks(rotation=30) # Rotaciona os rótulos para melhor visualização
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
            fontsize =15   # Define o tamanho da fonte do texto
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
    ax.set_xlim([17, 60])   # Ajusta o intervalo do eixo x
    ax.set_ylim([4, 7])   # Ajusta o intervalo do eixo y
    plt.tight_layout()  # Ajusta o layout para evitar sobreposições

    st.pyplot(fig)

def tela_genero(df):
    # Calcular a média do tempo de tela por gênero
    df['Gender'] = df['Gender'].replace({'Female': 'Feminino', 'Male': 'Masculino'})
    gender_screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()

    fig, ax = plt.subplots(figsize = (10, 6),)
    bars = ax.bar( # Configura o grafico de barras
        gender_screen_time_avg['Gender'],
        gender_screen_time_avg['Screen On Time (hours/day)'],
        color = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width = 0.6,
        
    )

    plt.title("Tempo de tela médio por gênero",fontsize =15)
    plt.xlabel("Gênero",fontsize =15)
    plt.ylabel("Tela Ligada (Hora/dia)", fontsize=15)
    ax.set_ylim([5.2, 5.3])   
    plt.tight_layout()  

     # Adiciona o valor acima da barra
    for i, bar in enumerate(bars):
        yval = bar.get_height() # altura (valor) da barra
        ax.text(
            bar.get_x() + bar.get_width() / 2,  
            yval + 0.001,     # Posição acima da barra
            round(gender_screen_time_avg['Screen On Time (hours/day)'][i], 2), 
            ha = 'center',  # Alinha o texto 
            va = 'bottom',  
            fontsize =15   
        )  

    st.pyplot(fig)

def tela_faixa_etaria(df):
    # Configuração dos filtros de idade
    df_filtered_1 = df[df['Age'] <= 20]
    df_filtered_2 = df[(df['Age'] > 20) & (df['Age'] <= 30)]
    df_filtered_3 = df[(df['Age'] > 30) & (df['Age'] <= 40)]
    df_filtered_4 = df[(df['Age'] > 40) & (df['Age'] <= 50)]
    df_filtered_5 = df[(df['Age'] > 50)]

    # Calcular a média do tempo de tela para cada filtro de idade
    mean_filtered_1 = df_filtered_1['Screen On Time (hours/day)'].mean()
    mean_filtered_2 = df_filtered_2['Screen On Time (hours/day)'].mean()
    mean_filtered_3 = df_filtered_3['Screen On Time (hours/day)'].mean()
    mean_filtered_4 = df_filtered_4['Screen On Time (hours/day)'].mean()
    mean_filtered_5 = df_filtered_5['Screen On Time (hours/day)'].mean()

    # Definição dos eixos do gráfico
    x = ['[0 - 20]', '[21 - 30]', '[31 - 40]', '[41 - 50]', '50+']
    y = [
        mean_filtered_1,
        mean_filtered_2,
        mean_filtered_3,
        mean_filtered_4,
        mean_filtered_5
    ]
    y = [0 if isna(val) else val for val in y]   # Substitui NaN por 0

    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar( # Configura o grafico de barras
        x,
        y,
        color =  ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width = 0.6
    )

    # Personalizar o gráfico
    plt.title('Tempo de tela médio por faixa etária')
    plt.xlabel('Faixa etária')
    plt.ylabel('Tempo de tela médio (horas/dia)')
    ax.set_ylim([min(y) - 0.1, max(y) + 0.1])   # Ajusta o intervalo do eixo y

    # Adiciona o valor acima da barra
    for i, bar in enumerate(bars):
        yval = bar.get_height() # Obtém a altura (valor) da barra
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # Posição horizontal do texto (centro da barra)
            yval + 0.01,     # Posição vertical (logo acima da barra)
            round(y[i], 2), # Texto a ser exibido (valor arredondado) 
            ha = 'center',  # Alinha o texto horizontalmente ao centro
            va = 'bottom',  # Alinha o texto verticalmente à parte inferior do texto
            fontsize =15   # Define o tamanho da fonte do texto
        )  # Adiciona o texto com a média correspondente
    
    st.pyplot(fig)
    

def quantidade_idade(df):
    # Calcular a quantidade de pessoas por idade
    age_count = df['Age'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize = (10, 6))
    ax.bar( # Configura o grafico de barras
        age_count.index,
        age_count.values,
        color =  ['#18c0c4'],
        width = 0.6
    )

    # Personaliza o gráfico
    plt.title("Contagem de pessoas por Idade")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade de pessoas")
    ax.set_xlim([17, 60])   # Ajusta o intervalo do eixo x
    plt.tight_layout()

    st.pyplot(fig)