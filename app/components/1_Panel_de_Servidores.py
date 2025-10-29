import streamlit as st

st.set_page_config(page_title="Mis Servidores", page_icon="🖥️", layout="centered")

st.title("🖥️ Mis Servidores")

st.write("Aquí se mostrarán los servidores registrados del usuario.")

# Tabla de ejemplo (SIN FUNCIONALIDAD)
servidores = [
    {"Nombre": "Servidor Ubuntu 01", "Estado": "Activo"},
    {"Nombre": "Windows Server 2019", "Estado": "Apagado"},
]

for srv in servidores:
    with st.container(border=True):
        st.subheader(srv["Nombre"])
        st.write(f"Estado: **{srv['Estado']}**")

        col1, col2 = st.columns(2)
        with col1:
            st.button("🔧 Ver detalles", key=f"detalles_{srv['Nombre']}")
        with col2:
            st.button("🗑️ Eliminar servidor", key=f"eliminar_{srv['Nombre']}")

st.divider()

st.button("➕ Crear nuevo servidor", use_container_width=True)

st.button("🔄 Actualizar lista", use_container_width=True)
