import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataSheet/mobile_device_usage_dataset.csv')


def plot_graphic_aparelhos_sistema():
    # Contar ocorrências de cada sistema operacional
    os_counts = df["Operating System"].value_counts()

    #gráfico de pizza
    fig1, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        os_counts,
        labels=os_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=["#ffb3b3","#80b3ff","#b3ffb3","#ffb366","#c2b3ff"]
    )

    ax.axis('equal')  # Para deixar o gráfico circular
    plt.title("Distribuição por Sistema Operacional")
    st.pyplot(fig1) 



def plot_graphic_consumo_modelo():
    battery_drain_avg = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()

    #gráfico de barras
    fig2, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(battery_drain_avg['Device Model'], battery_drain_avg['Battery Drain (mAh/day)'], color=["#ffb3b3","#80b3ff","#b3ffb3","#ffb366","#c2b3ff"])

    plt.title("Média de Consumo de Bateria por Modelo de Dispositivo")
    plt.xlabel("Modelos de Dispositivo")
    plt.ylabel("Média de Consumo de Bateria (mAh/dia)")
    plt.xticks(rotation=45, ha="right")  # Rotaciona rótulos 
    plt.tight_layout()
    
    for i, bar in enumerate(bars):
        yval = bar.get_height()  # Obtém a altura (valor) da barra
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(battery_drain_avg['Battery Drain (mAh/day)'][i], 2), 
            ha='center', va='bottom', fontsize=10)  # Adiciona o texto com a média correspondente
    

    st.pyplot(fig2)


def plot_graphic_idade_tempoTela():
    #média de idade de pessoas por tempo de tela
    battery_drain_avg = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()

    #gráfico de barras
    fig3, ax = plt.subplots(figsize=(10, 6))
    ax.bar(battery_drain_avg['Age'], battery_drain_avg['Screen On Time (hours/day)'],color=["#80b3ff"])

    plt.title("Idade x Tempo de Tela")
    plt.xlabel("Idade")
    plt.ylabel("Tempo médio de tela ativa (horas/dia)")
    plt.tight_layout()
    
    st.pyplot(fig3)


def plot_graphic_genero_tempoTela():
    # Calcular a média do tempo de tela por gênero
    screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean()

    #gráfico de pizza
    fig4, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        screen_time_avg, 
        labels=["Feminino", "Masculino"], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=["#ffb3b3","#80b3ff","#b3ffb3","#ffb366","#c2b3ff"]
    )

    plt.title("Tempo médio de Tela por gênero")
    plt.tight_layout()

    st.pyplot(fig4)



def plot_graphic_faixaEtaria_tempoTela():
    # Filtro 1: Idade <= 10
    df_filtered_1 = df[df['Age'] <= 10]
    # Filtro 2: 10 < Idade <= 20
    df_filtered_2 = df[(df['Age'] > 10) & (df['Age'] <= 20)]
    # Filtro 2: 20 < Idade <= 30
    df_filtered_3 = df[(df['Age'] > 20) & (df['Age'] <= 30)]
    # Filtro 2: 30 < Idade <= 40
    df_filtered_4 = df[(df['Age'] > 30) & (df['Age'] <= 40)]
    # Filtro 2: 40 < Idade <= 50
    df_filtered_5 = df[(df['Age'] > 40) & (df['Age'] <= 50)]
    # Filtro 2: 50+
    df_filtered_6 = df[(df['Age'] > 50) ]
    # Calcular a média por 'Age' para cada filtro
    mean_filtered_1 = df_filtered_1['Screen On Time (hours/day)'].mean()
    mean_filtered_2 = df_filtered_2['Screen On Time (hours/day)'].mean()
    mean_filtered_3 = df_filtered_3['Screen On Time (hours/day)'].mean()
    mean_filtered_4 = df_filtered_4['Screen On Time (hours/day)'].mean()
    mean_filtered_5 = df_filtered_5['Screen On Time (hours/day)'].mean()
    mean_filtered_6 = df_filtered_6['Screen On Time (hours/day)'].mean()

    # Definir as faixas de idade e as médias para o gráfico
    x = ['[0-10]', '[10-20]','[20-30]','[30-40]','[40-50]','>50']
    y = [mean_filtered_1, mean_filtered_2, mean_filtered_3, mean_filtered_4, mean_filtered_5 , mean_filtered_6]
    fig5, ax = plt.subplots(figsize=(8, 8))
    # Criar o gráfico de barras
    bars=ax.bar(x, y, color=["#ffb3b3","#80b3ff","#b3ffb3","#ffb366","#c2b3ff"])
    # Adicionando título e legendas
    plt.title('Tempo de tela por faixa etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Tempo médio de tela ativa (horas/dia)')
    # Exibir o gráfico
    # Exibir os valores de cada barra
    for i, bar in enumerate(bars):
        yval = bar.get_height()  # Obtém a altura (valor) da barra
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(y[i], 2), 
                ha='center', va='bottom', fontsize=10)  # Adiciona o texto com a média correspondente
    
    st.pyplot(fig5)
