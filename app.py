import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Vehículos Usados')

# Casillas de verificación
show_hist = st.checkbox('Construir histograma')
show_scatter = st.checkbox('Construir gráfico de dispersión')

if show_hist:
    st.write('Distribución de kilometraje')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig)

if show_scatter:
    st.write('Precio vs Kilometraje')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig)
