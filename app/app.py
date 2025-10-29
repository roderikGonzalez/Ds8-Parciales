import streamlit as st
from pathlib import Path

# Importar páginas
from components.login import login_page
from components.register import register_page
from components.forgot_password import forgot_password_page
from components.dashboard import dashboard_page
from components.server_status import server_status_page
from components.console import console_page
from components.options import options_page
from components.logs import logs_page

def load_css():
    css_path = Path("styles.css")
    if css_path.exists():
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.set_page_config(page_title="Panel de Servidores", page_icon="🖥️", layout="wide")

# Estado de sesión
if "is_logged" not in st.session_state:
    st.session_state["is_logged"] = False

if "page" not in st.session_state:
    st.session_state["page"] = "login"

# Si NO está logueado -> forzar login/registro/recuperación
if not st.session_state["is_logged"]:
    if st.session_state["page"] == "login":
        login_page()
    elif st.session_state["page"] == "register":
        register_page()
    elif st.session_state["page"] == "forgot_password":
        forgot_password_page()
    else:
        st.session_state["page"] = "login"
        st.rerun()
    st.stop()

# -------------------------------
# Si ya está logueado → Mostrar Menú
# -------------------------------

with st.sidebar:
    st.title("📌 Panel de Control")
    selected = st.radio("Navegación", [
        "Dashboard",
        "Estado del Servidor",
        "Consola",
        "Opciones",
        "Logs",
        "Cerrar Sesión"
    ])

# Render según selección
if selected == "Dashboard":
    dashboard_page()
elif selected == "Estado del Servidor":
    server_status_page()
elif selected == "Consola":
    console_page()
elif selected == "Opciones":
    options_page()
elif selected == "Logs":
    logs_page()
elif selected == "Cerrar Sesión":
    st.session_state["is_logged"] = False
    st.session_state["page"] = "login"
    st.rerun()
