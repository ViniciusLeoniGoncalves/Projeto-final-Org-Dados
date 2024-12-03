import matplotlib.pyplot as plt
import streamlit as st
from pandas import isna
import plotly.express as px
import plotly.graph_objects as go

plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.rcParams.update({'font.size': 15})
def so_distribuicao(df):

    # Contar ocorrências de cada sistema operacional
    os_counts = df["Operating System"].value_counts().reset_index()
    os_counts.columns = ["Operating System", "Count"]  # Certifique-se de usar os nomes corretos

    # Criar gráfico interativo com Plotly
    fig = px.pie(
        os_counts, 
        values="Count",  # Coluna com os valores
        names="Operating System",  # Coluna com os nomes
        title="Distribuição de usuários por sistema operacional",
        color_discrete_sequence=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width=600,  # Largura do gráfico
        height=600   # Altura do gráfico
    )
    # Mostrar gráfico no Streamlit
    st.plotly_chart(fig)

def consumo_modelo(df):
    # Calcular a média do consumo de bateria por modelo
    battery_drain_avg = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()

    # Calcular a média do consumo de bateria por modelo
    battery_drain_avg = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()

    # Criar gráfico interativo com Plotly
    fig = go.Figure()

    # Adicionar barras ao gráfico
    fig.add_trace(
        go.Bar(
            x=battery_drain_avg['Device Model'],
            y=battery_drain_avg['Battery Drain (mAh/day)'],
            marker_color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
            text=battery_drain_avg['Battery Drain (mAh/day)'].round(2),  # Valores exibidos acima das barras
            textposition='outside'  # Posição do texto
        )
    )

    # Personalizar layout
    fig.update_layout(
        title="Média de consumo de bateria por dispositivo",
        xaxis_title="Dispositivos",
        yaxis_title="Média de consumo de bateria (mAh/dia)",
        yaxis=dict(range=[1400, 1600]),  # Definir intervalo do eixo Y
        xaxis_tickangle=30,  # Rotacionar rótulos do eixo X
        template='plotly_white',  # Tema do gráfico
        margin=dict(t=50, b=50, l=50, r=50)
    )

    # Mostrar gráfico no Streamlit
    st.plotly_chart(fig)

def tela_idade(df):
    # Calcular a média de idade de pessoas por tempo de tela
    age_screen_time_avg = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()

    # Criar gráfico de barras interativo
    fig = go.Figure()

    # Adicionar barras ao gráfico
    fig.add_trace(
        go.Bar(
            x=age_screen_time_avg['Age'],
            y=age_screen_time_avg['Screen On Time (hours/day)'],
            marker_color='#18c0c4',  # Cor personalizada
        )
    )

    # Personalizar layout
    fig.update_layout(
        title="Tempo de tela médio por idade",
        xaxis=dict(
            title="Idade",
            range=[17, 60],  # Ajuste do intervalo do eixo X
            tickmode="linear"  # Garantir que as idades sejam exibidas como inteiros
        ),
        yaxis=dict(
            title="Tempo de tela médio (horas/dia)",
            range=[4, 7]  # Ajuste do intervalo do eixo Y
        ),
        template="plotly_dark",  # Tema do gráfico
        margin=dict(t=50, b=50, l=50, r=50)
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

def tela_genero(df):
    # Calcular a média do tempo de tela por gênero
    df['Gender'] = df['Gender'].replace({'Female': 'Feminino', 'Male': 'Masculino'})
    gender_screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()

    
    # Criação do gráfico interativo com Plotly
    fig = go.Figure(data=[go.Bar(
        x=gender_screen_time_avg['Gender'],
        y=gender_screen_time_avg['Screen On Time (hours/day)'],
        marker=dict(color=['#18c0c4', '#f62196']),
    )])

    # Adicionando título e rótulos
    fig.update_layout(
        title="Tempo de tela médio por gênero",
        xaxis_title="Gênero",
        yaxis_title="Tela Ligada (Hora/dia)",
        yaxis=dict(range=[5.2, 5.3]),  # Ajusta o intervalo do eixo Y
        font=dict(size=15),
    )

    # Adiciona os valores acima das barras
    for i, val in enumerate(gender_screen_time_avg['Screen On Time (hours/day)']):
        fig.add_annotation(
            x=gender_screen_time_avg['Gender'][i],
            y=val + 0.001,  # Posição do valor acima da barra
            text=f"{round(val, 2)}",  # Texto com o valor arredondado
            showarrow=False,
            font=dict(size=15)
        )

    # Exibe o gráfico interativo no Streamlit
    st.plotly_chart(fig)

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

    # Criação do gráfico interativo com Plotly
    fig = go.Figure(data=[go.Bar(
        x=x,
        y=y,
        marker=dict(color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff']),
    )])

    # Adicionando título e rótulos
    fig.update_layout(
        title='Tempo de tela médio por faixa etária',
        xaxis_title='Faixa etária',
        yaxis_title='Tempo de tela médio (horas/dia)',
        yaxis=dict(range=[min(y) - 0.1, max(y) + 0.1]),  # Ajusta o intervalo do eixo y
    )

    # Adiciona os valores acima das barras
    for i, val in enumerate(y):
        fig.add_annotation(
            x=x[i],
            y=val + 0.05,  # Ajusta a posição do valor acima da barra
            text=f"{round(val, 2)}",  # Valor arredondado
            showarrow=False,
            font=dict(size=15)
        )

    # Exibe o gráfico interativo no Streamlit
    st.plotly_chart(fig)
        

def quantidade_idade(df):
    # Calcular a quantidade de pessoas por idade
    age_count = df['Age'].value_counts().sort_index()

    # Criar gráfico interativo de barras
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=age_count.index,  # Idades
            y=age_count.values,  # Quantidade de pessoas
            marker_color='#18c0c4',  # Cor personalizada
        )
    )

    # Personalizar layout
    fig.update_layout(
        title="Contagem de pessoas por Idade",
        xaxis=dict(
            title="Idade",
            range=[17, 60],  # Intervalo do eixo X
            tickmode="linear"  # Exibir valores de idade como inteiros
        ),
        yaxis=dict(
            title="Quantidade de pessoas"
        ),
        template="plotly_dark",  # Tema do gráfico
        margin=dict(t=50, b=50, l=50, r=50)
    )

    # Mostrar gráfico no Streamlit
    st.plotly_chart(fig)


def tela_genero(df):
    # Traduzir o gênero para português
    df['Gender'] = df['Gender'].replace({'Female': 'Feminino', 'Male': 'Masculino'})
    
    # Calcular a média do tempo de tela por gênero
    gender_screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()
    
    # Criar o gráfico de barras interativo
    fig = px.bar(
        gender_screen_time_avg,
        x='Gender',
        y='Screen On Time (hours/day)',
        text='Screen On Time (hours/day)',
        labels={'Gender': 'Gênero', 'Screen On Time (hours/day)': 'Tempo de Tela (Horas/Dia)'},
        title="Tempo de Tela Médio por Gênero",
        color='Gender',  # Cor para destacar cada gênero
        color_discrete_map={'Feminino': '#f62196', 'Masculino': '#18c0c4'}  # Mapeamento de cores
    )
    
    # Ajustar layout
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        yaxis=dict(range=[5.22, 5.32]),  # Intervalo eixo Y
        xaxis_title="Gênero",
        yaxis_title="Tempo de Tela (Horas/Dia)",
        showlegend=False,
        title_x=0.5,  # Centralizar título
    )
    
    st.plotly_chart(fig)

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

    fig = go.Figure(data=[go.Bar(
        x=labels_faixa_etaria,
        y=medias,
        text=[round(val, 2) for val in medias],  # Adiciona texto com os valores arredondados
        textposition='outside',  # Posiciona o texto acima das barras
        marker=dict(color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b'])
    )])

    # Personalizar o layout
    fig.update_layout(
        title='Tempo de tela médio por faixa etária',
        xaxis_title='Faixa etária',
        yaxis_title='Tempo de tela médio (horas/dia)',
        yaxis=dict(range=[min(medias) - 0.1, max(medias) + 0.1]),  # Ajusta o intervalo do eixo Y
        font=dict(size=15),
        plot_bgcolor='rgba(0,0,0,0)',  # Remove fundo do gráfico
        paper_bgcolor='rgba(0,0,0,0)',  # Remove fundo do layout
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)

def usuarios_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Contagem de usuários por faixa etária
    contagem = [len(filtro) for filtro in filtros]
    contagem = [0 if isna(val) else val for val in contagem]  # Substitui NaN por 0

    fig = px.pie(
        names=labels_faixa_etaria,
        values=contagem,
        title="Distribuição de usuários por faixa etária",
        color_discrete_sequence=["#ffb3b3", "#80b3ff", "#b3ffb3", "#ffb366", "#c2b3ff"]
    )

    # Personalizar o layout
    fig.update_traces(textinfo='percent+label')  # Mostra rótulos e porcentagens
    fig.update_layout(
        legend_title="Faixas Etárias",
        legend=dict(
            orientation="v",  # Exibe verticalmente
            yanchor="top",
            y=0.9,
            xanchor="left",
            x=1.05  # Move a legenda para fora do gráfico
        ),
        width=600,  # Largura do gráfico
        height=600   # Altura do gráfico
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig,use_container_width=False)

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

     # Criação do gráfico de pizza com Plotly Express
    fig = px.pie(
        names=labels_genero,
        values=contagem,
        title="Distribuição de usuários por gênero",
        color_discrete_map={"Male": "#66b3ff", "Female": "#ffcbdb"},
        width=600,  # Largura do gráfico
        height=600   # Altura do gráfico
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)

def aplicativos_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Calcular a média do tempo de tela para cada filtro de idade
    medias = [filtro['Number of Apps Installed'].mean() for filtro in filtros]
    medias = [0 if isna(val) else val for val in medias]  # Substitui NaN por 0

    # Criação do gráfico interativo com Plotly
    fig = go.Figure(data=[go.Bar(
        x=labels_faixa_etaria,
        y=medias,
        marker=dict(color=["#ffb3b3", "#80b3ff", "#b3ffb3", "#ffb366", "#c2b3ff"]),
    )])

    # Personalizar o gráfico
    fig.update_layout(
        title='Média de aplicativos instalados por faixa etária',
        xaxis_title='Faixa etária',
        yaxis_title='Aplicativos instalados',
        yaxis=dict(range=[min(medias) - 1, max(medias) + 1]),
        font=dict(size=15),
        width=600,  # Largura do gráfico
        height=600   # Altura do gráfico
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)
