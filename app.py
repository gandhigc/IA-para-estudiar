import streamlit as st
import openai

st.title("Asistente Pro Max")

# Clave secreta desde el archivo .streamlit/secrets.toml
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

pregunta = st.text_input("Escribe tu pregunta o idea aquí:")

if st.button("Responder") and pregunta:
    with st.spinner("Pensando..."):
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": pregunta}
            ]
        )
        st.write(respuesta.choices[0].message.content)
