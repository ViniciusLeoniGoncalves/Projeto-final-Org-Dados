import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotgraphics as pg

st.title("Bem-vindo ao site Galenus Análises")
st.subheader("Análise criada pelo grupo *Galenus Atrasadus*")

# Ler o CSV
df = pd.read_csv('../dataSheet/mobile_device_usage_dataset.csv')
opt=st.sidebar.radio("Veja as análises que temos prontas", options=("Aparelhos x Sistema","Eduardo","Consumo x Modelo","Idade x tempo de tela"))
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