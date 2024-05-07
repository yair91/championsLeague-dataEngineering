import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df_ataque = pd.read_csv('Kaggle/Champions_stats/attacking.csv')
df_attempts = pd.read_csv('Kaggle/Champions_stats/attempts.csv')
df_defensa = pd.read_csv('Kaggle/Champions_stats/defending.csv')
df_disciplina= pd.read_csv('Kaggle/Champions_stats/disciplinary.csv')
df_distribución = pd.read_csv('Kaggle/Champions_stats/distributon.csv')
df_portero = pd.read_csv('Kaggle/Champions_stats/goalkeeping.csv')
df_goles = pd.read_csv('Kaggle/Champions_stats/goals.csv')
df_keystats= pd.read_csv('Kaggle/Champions_stats/key_stats.csv')

# Concatenar los DataFrames
df_combined_filled = pd.concat([df_ataque, df_attempts, df_defensa, df_disciplina, df_distribución, df_portero, df_goles, df_keystats]).fillna(0)

# Cambiar nombres de columnas a español
df_combined_filled.rename(columns={'player_name': 'Nombre Jugador', 
                                   'match_played': 'Partidos Jugados',
                                   'club': 'Equipo',
                                   'position': 'Posición',
                                   'assits': 'Asistencias',
                                   'corner_taken': 'Tiros de Esquina Cobrados',
                                   'goals': 'Goles',
                                   'offsides': 'Fueras de Juego',
                                   'total_attempts': 'Intentos de Juego',
                                   'right_foot': 'Con Pie Derecho',
                                   'left_foot': 'Con Pie Izquierdo',
                                   'headers': 'Cabezasos',
                                   'others': 'Otros',
                                   'inside_area': 'Dentro del Área',
                                   'outside_areas': 'Fuera del Área',
                                   'penalties': 'Penales',
                                   'distance_covered': 'Distancia Recorrida',
                                   'punches made': 'Golpes Realizados',
                                   'minutes_played': 'Minutos Jugados',
                                   'balls_recovered': 'Balones Recuperados',
                                   'tackles': 'Barridas',
                                   't_won': 'Barridas Ganadas',
                                   't_lost': 'Barridas Perdidas',
                                   'clearance_attempted': 'Intentos de Despeje',
                                   'fouls_committed': 'Faltas Cometidas',
                                   'fouls_suffered': 'Faltas Recibidas',
                                   'red': 'Tarjetas Rojas',
                                   'yellow': 'Tarjetas Amarillas',
                                   'pass_accuracy': 'Precisión de Pases',
                                   'pass_attempted': 'Pases Intentados',
                                   'pass_completed': 'Pases Completados',
                                   'cross_accuracy': 'Precisión de Cruces',
                                   'cross_completed': 'Cruces Completados',
                                   'freekicks_taken': 'Tiros Libres Cobrados',
                                   'saved': 'Atajadas',
                                   'conceded': 'Goles Concedidos',
                                   'saved_penalties': 'Penaltis Salvados'}, 
                          inplace=True)

# Crear la interfaz gráfica con Streamlit
def main():
    
       # Crear marcadores de posición vacíos
    tabla_general_placeholder = st.empty()
    top_10_clubes_placeholder = st.empty()
    top_10_jugadores_placeholder = st.empty()
    top_10_equipos_tarjetas_rojas_placeholder = st.empty()
    estadisticas_jugador_placeholder = st.empty()
  
    st.title('Análisis Estadístico de la Champions League')
    st.sidebar.title('Menú')

    # Botón para mostrar la tabla general
    if st.sidebar.button('Tabla General'):
        top_10_clubes_placeholder.empty()
        top_10_jugadores_placeholder.empty()
        top_10_equipos_tarjetas_rojas_placeholder.empty()
        estadisticas_jugador_placeholder.empty()
        
        mostrar_tabla_general(df_combined_filled)# Limpiar todos los marcadores de posición

    st.sidebar.subheader('Opciones')
    opcion = st.sidebar.selectbox('Seleccione una opción', ['Top 10 Clubes', 'Top 10 Jugadores', 'Top 10 Equipos con Más Tarjetas Rojas'])

    if opcion == 'Top 10 Clubes':
        # Limpiar todos los marcadores de posición
        tabla_general_placeholder.empty()
        top_10_clubes_placeholder.empty()
        top_10_equipos_tarjetas_rojas_placeholder.empty()
        estadisticas_jugador_placeholder.empty()
        
        mostrar_top_10_clubes(df_combined_filled)
    elif opcion == 'Top 10 Jugadores':
        # Limpiar todos los marcadores de posición
        tabla_general_placeholder.empty()
        top_10_clubes_placeholder.empty()
        top_10_equipos_tarjetas_rojas_placeholder.empty()
        estadisticas_jugador_placeholder.empty()
        mostrar_top_10_jugadores(df_combined_filled)
        
    elif opcion == 'Top 10 Equipos con Más Tarjetas Rojas':
        # Limpiar todos los marcadores de posición
        tabla_general_placeholder.empty()
        top_10_clubes_placeholder.empty()
        top_10_equipos_tarjetas_rojas_placeholder.empty()
        estadisticas_jugador_placeholder.empty()
        mostrar_top_10_equipos_tarjetas_rojas(df_combined_filled)


    st.sidebar.subheader('Jugador')
    jugadores = df_combined_filled['Nombre Jugador'].unique()
    jugador_seleccionado = st.sidebar.selectbox('Seleccione un jugador', jugadores)

    if jugador_seleccionado:
        
        # Limpiar todos los marcadores de posición
        tabla_general_placeholder.empty()
        top_10_clubes_placeholder.empty()
        top_10_equipos_tarjetas_rojas_placeholder.empty()
        estadisticas_jugador_placeholder.empty()
        mostrar_estadisticas_jugador(df_combined_filled, jugador_seleccionado)

    
# Función para mostrar las estadísticas de un jugador
def mostrar_estadisticas_jugador(df, jugador):
    df_jugador = df[df['Nombre Jugador'] == jugador]
    print(df_jugador.columns)
    
    goles = df_jugador['Goles'].sum()  # Suma de goles anotados por el jugador

    barridas = df_jugador[['Barridas Ganadas', 'Barridas Perdidas']].sum()
    pases = df_jugador[['Pases Completados', 'Pases Intentados']].sum()
    faltas = df_jugador[['Faltas Recibidas', 'Faltas Cometidas']].sum()

    partidos_jugados = df_jugador['Partidos Jugados'].sum()
    minutos_jugados = df_jugador['Minutos Jugados'].sum()

    st.subheader(f'Estadísticas de {jugador}')
    st.text(f'Goles Anotados: {goles}')  # Mostrar goles anotados
    st.text(f'Partidos Jugados: {partidos_jugados}')
    st.text(f'Minutos Jugados: {minutos_jugados}')

    plt.figure(figsize=(6, 6))
    plt.pie(barridas, labels=barridas.index, autopct='%1.1f%%')
    plt.title('Barridas Ganadas vs Barridas Perdidas')
    fig = plt.gcf()
    st.pyplot(fig)
    
    plt.figure(figsize=(6, 6))
    plt.pie(pases, labels=pases.index, autopct='%1.1f%%')
    plt.title('Pases Completados vs Pases Incompletos')
    fig = plt.gcf()
    st.pyplot(fig)
    
    plt.figure(figsize=(6, 6))
    plt.pie(faltas, labels=faltas.index, autopct='%1.1f%%')
    plt.title('Faltas Recibidas vs Faltas Cometidas')
    fig = plt.gcf()
    st.pyplot(fig)
    
# Función para mostrar la tabla general
def mostrar_tabla_general(df):
    st.subheader('Tabla General')
    st.write(df)

# Función para mostrar el top 10 de clubes con más goles
def mostrar_top_10_clubes(df):
    top_10_clubes = df.groupby('Equipo')['Goles'].sum().nlargest(10)
    
    st.subheader('Top 10 Clubes con Más Goles')
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_clubes.index, top_10_clubes.values, color='skyblue')
    plt.xticks(rotation=45)
    plt.xlabel('Equipo')
    plt.ylabel('Goles')
    plt.title('Top 10 Clubes con Más Goles')
    # Almacenar la figura en una variable
    fig = plt.gcf()
    st.pyplot(fig)

# Función para mostrar el top 10 de jugadores con más goles
def mostrar_top_10_jugadores(df):
    top_10_jugadores = df.groupby('Nombre Jugador')['Goles'].sum().nlargest(10)
    
    st.subheader('Top 10 Jugadores con Más Goles')
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_jugadores.index, top_10_jugadores.values, color='lightgreen')
    plt.xticks(rotation=45)
    plt.xlabel('Jugador')
    plt.ylabel('Goles')
    plt.title('Top 10 Jugadores con Más Goles')
    # Almacenar la figura en una variable
    fig = plt.gcf()
    st.pyplot(fig)

# Función para mostrar el top 10 de equipos con más tarjetas rojas
def mostrar_top_10_equipos_tarjetas_rojas(df):
    top_equipos_tarjetas_rojas = df.groupby('Equipo')['Tarjetas Rojas'].sum().nlargest(10)
    
    st.subheader('Top 10 Equipos con Más Tarjetas Rojas')
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_equipos_tarjetas_rojas.index, top_equipos_tarjetas_rojas.values, color='salmon')
    plt.xticks(rotation=45)
    plt.xlabel('Equipo')
    plt.ylabel('Tarjetas Rojas')
    plt.title('Top 10 Equipos con Más Tarjetas Rojas')
    # Almacenar la figura en una variable
    fig = plt.gcf()
    st.pyplot(fig)


if __name__ == '__main__':
    main()
