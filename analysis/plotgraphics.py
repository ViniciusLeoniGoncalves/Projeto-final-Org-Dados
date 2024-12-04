import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from pandas import isna

def so_distribuicao(df):
    # Contar ocorrências de cada sistema operacional
    os_counts = df["Operating System"].value_counts().reset_index()
    os_counts.columns = ["Sistema Operacional", "Usuários"] 

    # Criar gráfico
    fig = px.pie(
        os_counts,
        values = "Usuários",    # Coluna com valores
        names = "Sistema Operacional",  # Coluna com nomes
        title = "Distribuição de usuários por sistema operacional",
        color_discrete_sequence = ['#18c0c4', '#f62196'],
        template = 'plotly_dark',
        width = 600,
        height = 600
    )

    st.plotly_chart(fig)

def consumo_modelo(df):
    # Calcular a média do consumo de bateria por modelo
    media_consumo = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()

    # Cria a figura
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x = media_consumo['Device Model'],
            y = media_consumo['Battery Drain (mAh/day)'],
            marker_color = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b'],
            text = media_consumo['Battery Drain (mAh/day)'].round(2),
            textposition = 'outside'
        )
    )

    # Configura os índices do gráfico
    fig.update_layout(
        title = "Média de consumo de bateria por dispositivo",
        xaxis_title = "Dispositivos",
        yaxis_title = "Média de consumo de bateria (mAh/dia)",
        yaxis = dict(range = [1400, 1600]),
        xaxis_automargin = True,
        template = 'plotly_dark',
        margin = dict(t = 50, b = 50, l = 50, r = 50)
    )

    st.plotly_chart(fig)

def tela_idade(df):
    # Calcula a média de idade de pessoas por tempo de tela
    media_tela_idade = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()

    # Cria a figura
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x = media_tela_idade['Age'],
            y = media_tela_idade['Screen On Time (hours/day)'],
            marker_color ='#18c0c4'  
        )
    )

    # Configura os índices do gráfico
    fig.update_layout(
        title = "Tempo de tela médio por idade",
        xaxis = dict(
            title = "Idade",
            range = [17, 60],
            tickmode = "linear",    # Garante que as idades sejam exibidas como inteiros
            automargin = True
        ),
        yaxis = dict(
            title = "Tempo de tela médio (horas/dia)",
            range = [4, 7]
        ),
        template = "plotly_dark",   # Tema do gráfico
        margin = dict(t = 50, b = 50, l = 50, r = 50)
    )

    st.plotly_chart(fig)

def quantidade_idade(df):
    # Calcular a quantidade de pessoas por idade
    contagem_idade = df['Age'].value_counts().sort_index()

    # Cria a figura
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x = contagem_idade.index,
            y = contagem_idade.values,
            marker_color ='#18c0c4'  
        )
    )

    # Configura os índices do gráfico
    fig.update_layout(
        title = "Contagem de pessoas por idade",
        xaxis = dict(
            title = "Idade",
            range = [17, 60],
            tickmode = "linear",    # Garante que as idades sejam exibidas como inteiros
            automargin = True
        ),
        yaxis_title = "Quantidade de pessoas",
        template = "plotly_dark",   # Tema do gráfico
        margin = dict(t = 50, b = 50, l = 50, r = 50)
    )

    st.plotly_chart(fig)

def tela_genero(df):
    # Calcula a média do tempo de tela por gênero
    media_tela_genero = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()

    # Cria a figura
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x = media_tela_genero['Gender'],
            y = media_tela_genero['Screen On Time (hours/day)'],
            marker_color = ['#f62196', '#18c0c4'],
            text = media_tela_genero['Screen On Time (hours/day)'].round(2),
            textposition = 'outside'
        )
    )

    # Título e rótulos
    fig.update_layout(
        title = "Tempo de tela médio por gênero",
        xaxis_title = "Gênero",
        yaxis_title = "Tempo de tela (Hora/dia)",
        yaxis = dict(range = [5.2, 5.3]),
        font = dict(size = 15),
        title_x = 0,    # Alinha o título à esquerda
        title_y = 0.95, # Ajusta a posição vertical do título, se necessário
        template = "plotly_dark",   # Tema do gráfico
        margin = dict(t = 50, b = 50, l = 50, r = 50)
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

titulo_faixas = ['[0 - 20]', '[21 - 30]', '[31 - 40]', '[41 - 50]', '[ 50+ ]']

def tela_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Calcula a média de tempo de tela para cada faixa etária
    medias = [filtro['Screen On Time (hours/day)'].mean() for filtro in filtros]
    medias = [0 if isna(val) else val for val in medias]    # Substitui NaN por 0

    # Cria a figura
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x = titulo_faixas,
            y = medias,
            marker = dict(color = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b']),
            text = [f'{round(valor, 2)}' for valor in medias],
            textposition = 'outside'
        )
    )

    # Título e rótulos
    fig.update_layout(
        title = 'Tempo de tela médio por faixa etária',
        xaxis_title = 'Faixa etária',
        yaxis_title = 'Tempo de tela médio (horas/dia)',
        yaxis = dict(range = [min(medias) - 0.1, max(medias) + 0.1]),
        template = "plotly_dark",   # Tema do gráfico
        margin = dict(t = 50, b = 50, l = 50, r = 50)
    )
    
    st.plotly_chart(fig)

def usuarios_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Contagem de usuários por faixa etária
    contagem = [len(filtro) for filtro in filtros]
    contagem = [0 if isna(val) else val for val in contagem]  # Substitui NaN por 0

    # Criar gráfico
    fig = px.pie(
        names = titulo_faixas,
        values = contagem,
        title = "Distribuição de usuários por faixa etária",
        color_discrete_sequence = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b']
    )

    fig.update_traces(
        textinfo = 'percent+label',   # Exibe o percentual e a faixa etária na parcela
        hovertemplate = 'Faixa etária = %{label}<br>%{percent}'  # Exibe a faixa etária e o percentual
        )
    
    # Colocando legenda
    fig.update_layout(
        legend_title = "Faixas Etárias",
        legend = dict(
            orientation = "v",
            yanchor = "top",
            y = 0.9,
            xanchor = "left",
            x = 1.05
        ),
        template = 'plotly_dark',
        width = 600,
        height = 600
    )

    st.plotly_chart(fig,use_container_width = False)

def usuarios_genero(df):
    # Filtros de gênero
    filtros = [
        df[df['Gender'] == "Masculino"],
        df[df['Gender'] == "Feminino"]
    ]
    titulo_generos = ["Masculino", "Feminino"]

    # Contagem de usuários por gênero
    contagem = [len(filtro) for filtro in filtros]

    # Criar gráfico
    fig = px.pie(
        names = titulo_generos,
        values = contagem,
        title = "Distribuição de usuários por gênero",
        color_discrete_sequence = ['#18c0c4', '#f62196'],
        template = 'plotly_dark',
        width = 600,
        height = 600
    )

    fig.update_traces(hovertemplate='Gênero = %{label}<br>Contagem = %{value}')  # Exibe o gênero e o percentual

    st.plotly_chart(fig)

def aplicativos_faixa_etaria(df):
    # Obter os filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    # Calcula a média do tempo de tela para cada faixa etária
    medias = [filtro['Number of Apps Installed'].mean() for filtro in filtros]
    medias = [0 if isna(val) else val for val in medias]  #Substitui NaN por 0

    # Cria a figura
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
        x = titulo_faixas,
        y = medias,
        marker = dict(color = ['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b']),
        )
    )

    # Título e rótulos
    fig.update_layout(
        title = 'Média de aplicativos instalados por faixa etária',
        xaxis_title = 'Faixa etária',
        yaxis_title = 'Aplicativos instalados',
        yaxis = dict(range = [49, 53]),
        font = dict(size = 15),
        template = 'plotly_dark',
        margin = dict(t = 50, b = 50, l = 50, r = 50)
    )

    st.plotly_chart(fig)
