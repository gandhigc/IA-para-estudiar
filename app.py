import streamlit as st
import openai

# Configuración de la página
st.set_page_config(page_title="Asistente Pro Max", page_icon="🤖")

# Título de la app
st.title("Asistente Pro Max")

# API Key desde los secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Área de texto para ingresar la pregunta
prompt = st.text_area("Escribe tu pregunta o idea aquí:")

# Botón para generar respuesta
if st.button("Responder"):
    if prompt.strip() != "":
        with st.spinner("Pensando..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("**Respuesta:**")
            st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Por favor escribe algo antes de presionar el botón.")
