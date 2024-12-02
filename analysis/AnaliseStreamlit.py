import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Bem-vindo ao site Galenus Analysis")

# Ler o CSV
df = pd.read_csv('../dataSheet/mobile_device_usage_dataset.csv')

# Verificar se a coluna "Operating System" existe
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
    st.text("Mostraremos a distribuição de aparelhos por Sistema Operacional (Android ou iOS):")
    plt.title("Distribuição por Sistema Operacional")
    st.pyplot(fig1) 

else:
    print("A coluna 'Operating System' não foi encontrada no arquivo.")


st.write("Iremos mostrar a média de consumo de bateria por modelo de dispositivo:")


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

st.write("Iremos mostrar a média de idade de pessoas por tempo de tela:")

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

st.write("Iremos mostrar a média de tempo de tela por gênero:")

# Calcular a média do tempo de tela por gênero
battery_drain_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()

# Criar gráfico de barras
fig4, ax = plt.subplots(figsize=(10, 6))
ax.bar(battery_drain_avg['Gender'], battery_drain_avg['Screen On Time (hours/day)'], color='skyblue')

# Personalizar o gráfico
plt.title("Gênero x Tempo de Tela")
plt.xlabel("Gênero")
plt.ylabel("Tela Ligada (Hora/dia)")
plt.tight_layout()  # Ajusta o layout para evitar sobreposições

# Mostrar o gráfico
st.pyplot(fig4)

st.write("Média de tempo de tela por idade:")
st.title("A partir daqui deu ruim:")
"""

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
x = ['(0-10]', '(10-20]','(20-30]','(30-40]','(40-50]','>50']
y = [mean_filtered_1, mean_filtered_2, mean_filtered_3, mean_filtered_4, mean_filtered_5 , mean_filtered_6]

# Criar o gráfico de barras
fig5 = plt.bar(x, y, color=['blue', 'green'])

# Adicionando título e legendas
plt.title('Average Screen On Time by Age with Different Filters')
plt.xlabel('Age')
plt.ylabel('Average Screen On Time (hours/day)')

# Exibir o gráfico
st.pyplot(fig5)"""