import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")



# Crea una función para analizar el texto con GPT-3
def analyze_text(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Analizar el siguiente texto desde el punto de vista retórico y brindar consejos para mejorar: {text}",
        max_tokens=2048,
    )
    return response["choices"][0]["text"]

# Crea una función para extraer los consejos para mejorar del resultado
def extract_tips(result):
    tips = []
    for line in result.split("\n"):
        if "para mejorar" in line or "sugiere" in line:
            tips.append(line)
    return tips

# Crea una función que ejecuta la lógica de tu aplicación
def app():
    st.title("Analizador retórico de textos")
    text = st.text_area("Ingresa el texto a analizar:")
    if st.button("Analizar"):
        result = analyze_text(text)
        tips = extract_tips(result)
        if tips:
            st.success("Consejos para mejorar:")
            for tip in tips:
                st.info(tip)
        else:
            st.success("El texto es efectivo y no se requiere mejoras")

# Ejecuta la aplicación
if __name__ == "__main__":
    app()
