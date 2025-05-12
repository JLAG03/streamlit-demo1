import streamlit as st
import pandas as pd
import plotly.express as px

st.title("DEMO 12 de mayo")
file = st.file_uploader("Sube una imagen (JPG o PNG)", type=["jpg","png"])

# if st.button("Confirmar input") and file is not None:
#     st.image(file, caption="Imagen subida", use_column_width=True)

ticker     = st.text_input("Ingrese un ticker (E): AAPL")
period     = st.selectbox("Periodo", ["America","Lakers","Clippers"])
slider_val = st.slider("Deslizador de 0 a 10", 0,10)
show_chart = st.checkbox("Mostrar gráfica")

if show_chart:
    df = pd.DataFrame({
        "x": range(10),
        "y": [i**2 for i in range(10)]
    })
    fig = px.line(df, x="x", y="y", title="Grafica ejemplo")
    st.plotly_chart(fig)

col1, col2 = st.columns(2)
with col1:
    st.subheader("RESUMEN")
    st.write("COLUMNA 1")
with col2:
    st.subheader("RESUMEN")
    st.write("COLUMNA 2")

# Que el usuario descargue el CSV
df2 = pd.DataFrame({
    "Columna 1": [1,2,3],
    "Columna 2": ["A","B","C"]
})
st.dataframe(df2)
csv = df2.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Descarga como csv",
    data=csv,
    file_name="data.csv",
    mime="text/csv"
)
st.table(df2)
