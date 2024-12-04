import matplotlib.pyplot as plt
import streamlit as st
from pandas import isna

import plotly.express as px
import plotly.graph_objects as go

#Obsoleto na troca da biblioteca
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
plt.rcParams.update({'font.size': 15})


def so_distribuicao(df):


    # Contar ocorrências de cada sistema operacional
    os_counts = df["Operating System"].value_counts().reset_index()
    os_counts.columns = ["Operating System", "Count"] 

    # Criar gráfico 
    fig = px.pie(
        os_counts, 
        values="Count",  # Coluna com valores
        names="Operating System",  # Coluna com nomes
        title="Distribuição de usuários por sistema operacional",
        color_discrete_sequence=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width=600,  
        height=600   
    )
   
    st.plotly_chart(fig)

def consumo_modelo(df):
    # Calcular a média do consumo de bateria por modelo
    battery_drain_avg = df.groupby('Device Model')['Battery Drain (mAh/day)'].mean().reset_index()


    fig = go.Figure()

    
    fig.add_trace(
        go.Bar(
            x=battery_drain_avg['Device Model'],
            y=battery_drain_avg['Battery Drain (mAh/day)'],
            marker_color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
            text=battery_drain_avg['Battery Drain (mAh/day)'].round(2),  
            textposition='outside'  
        )
    )

    
    fig.update_layout(
        title="Média de consumo de bateria por dispositivo",
        xaxis_title="Dispositivos",
        yaxis_title="Média de consumo de bateria (mAh/dia)",
        yaxis=dict(range=[1400, 1600]),  
        xaxis_tickangle=30,  
        template='plotly_white',  
        margin=dict(t=50, b=50, l=50, r=50)
    )

    
    st.plotly_chart(fig)

def tela_idade(df):
    # Calcula a média de idade de pessoas por tempo de tela
    age_screen_time_avg = df.groupby('Age')['Screen On Time (hours/day)'].mean().reset_index()


    fig = go.Figure()

  
    fig.add_trace(
        go.Bar(
            x=age_screen_time_avg['Age'],
            y=age_screen_time_avg['Screen On Time (hours/day)'],
            marker_color='#18c0c4',  
        )
    )


   
    fig.update_layout(
        title="Tempo de tela médio por idade",
        xaxis=dict(
            title="Idade",
            range=[17, 60], 
            tickmode="linear"  # Garante que as idades sejam exibidas como inteiros
        ),
        yaxis=dict(
            title="Tempo de tela médio (horas/dia)",
            range=[4, 7] 
        ),
        template="plotly_dark",  # Tema do gráfico
        margin=dict(t=50, b=50, l=50, r=50)
    )


    
    st.plotly_chart(fig)

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
    # Calcula a média do tempo de tela por gênero
    df['Gender'] = df['Gender'].replace({'Female': 'Feminino', 'Male': 'Masculino'})
    gender_screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()


    
    # Criação do gráfico 
    fig = go.Figure(data=[go.Bar(
        x=gender_screen_time_avg['Gender'],
        y=gender_screen_time_avg['Screen On Time (hours/day)'],
        marker=dict(color=['#18c0c4', '#f62196']),
    )])

    # título e rótulos
    fig.update_layout(
        title="Tempo de tela médio por gênero",
        xaxis_title="Gênero",
        yaxis_title="Tela Ligada (Hora/dia)",
        yaxis=dict(range=[5.2, 5.3]),  
        font=dict(size=15),
    )

    # valores acima das barras
    for i, val in enumerate(gender_screen_time_avg['Screen On Time (hours/day)']):
        fig.add_annotation(
            x=gender_screen_time_avg['Gender'][i],
            y=val + 0.001,  
            text=f"{round(val, 2)}",  
            showarrow=False,
            font=dict(size=15)

        )

   
    st.plotly_chart(fig)


def tela_faixa_etaria(df):
    df_filtered_1 = df[df['Age'] <= 20]
    df_filtered_2 = df[(df['Age'] > 20) & (df['Age'] <= 30)]
    df_filtered_3 = df[(df['Age'] > 30) & (df['Age'] <= 40)]
    df_filtered_4 = df[(df['Age'] > 40) & (df['Age'] <= 50)]
    df_filtered_5 = df[(df['Age'] > 50)]

    mean_filtered_1 = df_filtered_1['Screen On Time (hours/day)'].mean()
    mean_filtered_2 = df_filtered_2['Screen On Time (hours/day)'].mean()
    mean_filtered_3 = df_filtered_3['Screen On Time (hours/day)'].mean()
    mean_filtered_4 = df_filtered_4['Screen On Time (hours/day)'].mean()
    mean_filtered_5 = df_filtered_5['Screen On Time (hours/day)'].mean()

    
    x = ['[0 - 20]', '[21 - 30]', '[31 - 40]', '[41 - 50]', '50+']
    y = [
        mean_filtered_1,
        mean_filtered_2,
        mean_filtered_3,
        mean_filtered_4,
        mean_filtered_5
    ]
    y = [0 if isna(val) else val for val in y]   # Substitui NaN por 0

    # Criação do gráfico
    fig = go.Figure(data=[go.Bar(
        x=x,
        y=y,
        marker=dict(color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff']),
    )])

    # título e rótulos
    fig.update_layout(
        title='Tempo de tela médio por faixa etária',
        xaxis_title='Faixa etária',
        yaxis_title='Tempo de tela médio (horas/dia)',
        yaxis=dict(range=[min(y) - 0.1, max(y) + 0.1]),  
    )

    # valores acima das barras
    for i, val in enumerate(y):
        fig.add_annotation(
            x=x[i],
            y=val + 0.05, 
            text=f"{round(val, 2)}",  
            showarrow=False,
            font=dict(size=15)
        )

    
    st.plotly_chart(fig)
        

def quantidade_idade(df):
    # conta pessoas por idade
    age_count = df['Age'].value_counts().sort_index()

    # Criar gráfico 
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=age_count.index,  
            y=age_count.values,  
            marker_color='#18c0c4',  
        )
    )

   
    fig.update_layout(
        title="Contagem de pessoas por Idade",
        xaxis=dict(
            title="Idade",
            range=[17, 60],  
            tickmode="linear"  
        ),
        yaxis=dict(
            title="Quantidade de pessoas"
        ),
        template="plotly_dark", 
        margin=dict(t=50, b=50, l=50, r=50)
    )

    
    st.plotly_chart(fig)


def tela_genero(df):
    
    df['Gender'] = df['Gender'].replace({'Female': 'Feminino', 'Male': 'Masculino'})
    
    # média do tempo de tela por gênero
    gender_screen_time_avg = df.groupby('Gender')['Screen On Time (hours/day)'].mean().reset_index()
    
    # Criar o gráfico 
    fig = px.bar(
        gender_screen_time_avg,
        x='Gender',
        y='Screen On Time (hours/day)',
        text='Screen On Time (hours/day)',
        labels={'Gender': 'Gênero', 'Screen On Time (hours/day)': 'Tempo de Tela (Horas/Dia)'},
        title="Tempo de Tela Médio por Gênero",
        color='Gender', 
        color_discrete_sequence=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'] 
    )
    
    
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        yaxis=dict(range=[5.22, 5.32]),  
        xaxis_title="Gênero",
        yaxis_title="Tempo de Tela (Horas/Dia)",
        showlegend=False,
        title_x=0.5,  
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
        text=[round(val, 2) for val in medias],  #texto com os valores arredondados
        textposition='outside',  # Posiciona acima das barras
        marker=dict(color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'])
    )])

    # Personalizar o layout
    fig.update_layout(
        title='Tempo de tela médio por faixa etária',
        xaxis_title='Faixa etária',
        yaxis_title='Tempo de tela médio (horas/dia)',
        yaxis=dict(range=[min(medias) - 0.1, max(medias) + 0.1]),  
        font=dict(size=15),
        plot_bgcolor='rgba(0,0,0,0)',  
        paper_bgcolor='rgba(0,0,0,0)',  
    )


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
        color_discrete_sequence=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff']
    )

   
    fig.update_traces(textinfo='percent+label')  # rótulos
    fig.update_layout(
        #colocando legenda
        legend_title="Faixas Etárias",
        legend=dict(
            orientation="v",  
            yanchor="top",
            y=0.9,
            xanchor="left",
            x=1.05  
        ),
        width=600,  
        height=600  
    )


    st.plotly_chart(fig,use_container_width=False)

def usuarios_genero(df):
    #filtros de gênero
    filtros = [
        df[df['Gender'] == "Male"],
        df[df['Gender'] == "Female"]
    ]
    labels_genero = ["Masculino", "Feminino"]

    # Contar de usuários por gênero
    contagem = [len(filtro) for filtro in filtros]
    contagem = [0 if isna(val) else val for val in contagem]  # Substitui NaN por 0

    fig = px.pie(
        names=labels_genero,
        values=contagem,
        title="Distribuição de usuários por gênero",
        color_discrete_sequence=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff'],
        width=600,  
        height=600   
    )

 
    st.plotly_chart(fig)

def aplicativos_faixa_etaria(df):
    #filtros de faixa etária
    filtros = filtros_faixa_etaria(df)

    #média do tempo de tela para cada filtro de idade
    medias = [filtro['Number of Apps Installed'].mean() for filtro in filtros]
    medias = [0 if isna(val) else val for val in medias]  #Substitui NaN por 0

    fig = go.Figure(data=[go.Bar(
        x=labels_faixa_etaria,
        y=medias,
        marker=dict(color=['#18c0c4', '#f62196', '#A267F5', '#f3907e', '#ffe46b', '#fefeff']),
    )])

    
    fig.update_layout(
        title='Média de aplicativos instalados por faixa etária',
        xaxis_title='Faixa etária',
        yaxis_title='Aplicativos instalados',
        yaxis=dict(range=[min(medias) - 1, max(medias) + 1]),
        font=dict(size=15),
        width=600, 
        height=600  
    )

    st.plotly_chart(fig)
