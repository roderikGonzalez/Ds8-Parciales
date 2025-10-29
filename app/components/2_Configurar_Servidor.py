import streamlit as st

st.set_page_config(page_title="Configurar Servidor", page_icon="⚙️", layout="centered")

st.title("⚙️ Configuración del Servidor")

# NO HAY LOGICA: El backend luego enviará estos datos
st.text_input("Nombre del servidor", "Servidor Ubuntu 01")
st.selectbox("Sistema Operativo", ["Ubuntu", "Debian", "Windows Server", "CentOS"])
st.number_input("CPU (núcleos)", min_value=1, max_value=64, value=4)
st.number_input("RAM (GB)", min_value=1, max_value=256, value=8)
st.number_input("Almacenamiento (GB)", min_value=10, max_value=2000, value=120)

st.button("💾 Guardar cambios", use_container_width=True)

st.divider()
st.subheader("📜 Eventos del servidor")

eventos_ejemplo = [
    "Servidor reiniciado",
    "Actualización de paquetes instalada",
    "Usuario root inició sesión"
]

for e in eventos_ejemplo:
    st.write(f"- {e}")

st.button("➕ Registrar evento")
