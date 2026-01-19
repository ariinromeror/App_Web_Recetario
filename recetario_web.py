import streamlit as st
import sqlite3
import os
from google import genai
from dotenv import load_dotenv

load_dotenv() 

st.set_page_config(
    page_title="Sabor Venezolano | Chef Virtual",
    page_icon="🇻🇪",
    layout="wide"
)

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("Configuración de seguridad faltante: GEMINI_API_KEY")
        st.stop()
    return genai.Client(api_key=api_key)

def fetch_recipes():
    try:
        with sqlite3.connect('recetas_venezuela.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM platos")
            return cursor.fetchall()
    except sqlite3.Error:
        return []

def main():
    client = get_gemini_client()
    recipes = fetch_recipes()

    st.sidebar.header("👨‍🍳 Chef Virtual")
    user_query = st.sidebar.text_input("¿Qué deseas cocinar hoy?", placeholder="Ej: ¿Cómo hago la masa?")

    if user_query and recipes:
        knowledge = " ".join([f"Plato: {r[1]}. Ingredientes: {r[3]}." for r in recipes])
        
        prompt = (
            f"Actúa como un Chef venezolano experto y amable. "
            f"Basándote en este recetario: {knowledge}, responde brevemente a: {user_query}"
        )

        with st.sidebar:
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                st.info(response.text)
            except Exception as e:
                if "429" in str(e):
                    st.warning("⏳ Google está procesando muchas solicitudes. Reintenta en 30 segundos.")
                else:
                    st.error("El Chef no puede responder en este momento.")

    st.title("🇻🇪 Mi Recetario Maestro")
    st.divider()

    if not recipes:
        st.warning("No hay recetas en la base de datos. Ejecuta crear_base.py primero.")
        return

    for recipe in recipes:
        col_img, col_info = st.columns([1, 2])
        with col_img:
            st.image(recipe[5], width="stretch")
        with col_info:
            st.subheader(recipe[1])
            st.markdown(f"**Ingredientes:**\n{recipe[3]}")
            st.markdown(f"**Preparación:**\n{recipe[4]}")
        st.divider()

if __name__ == "__main__":
    main()