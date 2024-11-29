import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ler o CSV
df = pd.read_csv('../dataSheet/mobile_device_usage_dataset.csv')


def plot_graphic_aparelhos_sistema():
    if "Operating System" in df.columns:
        # Contar ocorrências de cada sistema operacional
        os_counts = df["Operating System"].value_counts()

        # Criar gráfico de pizza
        fig1, ax = plt.subplots(figsize=(6,6))
        ax.pie(
            os_counts,
            labels=os_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
        )
        ax.axis('equal')  # Para deixar o gráfico circular
        plt.title("Distribuição por Sistema Operacional")
        st.pyplot(fig1) 

    else:
        print("A coluna 'Operating System' não foi encontrada no arquivo.")

def plot_graphic_consumo_modelo():
    
    # Calcular a média do consumo de bateria por modelo
    battery_drain_avg = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()

    # Criar gráfico de barras
    fig2, ax = plt.subplots(figsize=(10, 6))
    ax.bar(battery_drain_avg['Device Model'], battery_drain_avg['Battery Drain (mAh/day)'], color='skyblue')

    # Personalizar o gráfico
    plt.title("Média de Consumo de Bateria por Modelo de Dispositivo")
    plt.xlabel("Modelos de Dispositivo")
    plt.ylabel("Média de Consumo de Bateria (mAh/dia)")
    plt.xticks(rotation=45, ha="right")  # Rotaciona os rótulos para melhor visualização
    plt.tight_layout()  # Ajusta o layout para evitar sobreposições

    # Mostrar o gráfico
    st.pyplot(fig2)

def plot_graphic_idade_tempoTela():
    # Calcular a média de idade de pessoas por tempo de tela
    battery_drain_avg = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()

    # Criar gráfico de barras
    fig3, ax = plt.subplots(figsize=(10, 6))
    ax.bar(battery_drain_avg['Age'], battery_drain_avg['Screen On Time (hours/day)'], color='skyblue')

    # Personalizar o gráfico
    plt.title("Idade x Tempo de Tela")
    plt.xlabel("Idade")
    plt.ylabel("Tela Ligada (Hora/dia)")
    plt.tight_layout()  # Ajusta o layout para evitar sobreposições
    # Mostrar o gráfico
    st.pyplot(fig3)