import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Voltrush", page_icon="⚡", layout="wide")

with open("voltrush.html", "r", encoding="utf-8") as f:
    html = f.read()

# Full-viewport render of the Voltrush web app inside Streamlit
components.html(html, height=1000, scrolling=True)
