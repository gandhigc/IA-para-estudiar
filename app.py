import streamlit as st
import openai

st.set_page_config(page_title="Asistente Pro Max", page_icon="🧠")

st.title("Asistente Pro Max") st.markdown("Tu compañero de estudio inteligente y buena onda.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

notas = st.text_area("Pega aquí tus apuntes, resumen o texto del tema que estás estudiando:", height=200) pregunta = st.text_input("¿Qué quieres saber o que te explique?")

if st.button("Responder con IA"): if notas and pregunta: prompt = f"Estos son mis apuntes: {notas}

Con esa información, responde esta pregunta de forma clara y útil: {pregunta}"

with st.spinner("Pensando como estudiante nerd..."):
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success("Listo, crack:")
        st.write(respuesta['choices'][0]['message']['content'])
else:
    st.warning("Por favor, escribe tus apuntes y una pregunta.")

