import streamlit as st

def options_page():
    st.title("⚙️ Opciones del Servidor")

    st.write("Desde aquí podrás administrar configuraciones generales del servidor.")

    st.markdown("### 🖥️ Configuración del Servidor")

    col1, col2 = st.columns(2)

    with col1:
        nombre_servidor = st.text_input("Nombre del servidor", "Servidor Minecraft")
        version_minecraft = st.selectbox("Versión de Minecraft", [
            "1.21.1", "1.20.4", "1.19.3", "1.18.2"
        ])
        modo_juego = st.selectbox("Modo de juego", [
            "Supervivencia", "Creativo", "Aventura", "Espectador"
        ])

    with col2:
        max_jugadores = st.slider("Máximo de jugadores", 1, 50, 10)
        pvp = st.toggle("PVP Activado", value=True)
        dificultad = st.selectbox("Dificultad", [
            "Pacífica", "Fácil", "Normal", "Difícil"
        ])

    st.markdown("---")

    st.markdown("### 🌐 Configuración de Red")

    col3, col4 = st.columns(2)
    with col3:
        puerto = st.number_input("Puerto del servidor", 1, 65535, 25565)
    with col4:
        ip_externa = st.text_input("IP Pública", placeholder="Aún no configurado")

    st.markdown("---")

    st.markdown("### 🧩 Plugins (Simulación)")

    plugins = ["EssentialsX", "WorldEdit", "Vault", "LuckPerms"]

    for plugin in plugins:
        st.checkbox(plugin, value=True)

    st.button("📦 Agregar nuevo plugin", use_container_width=True)

    st.markdown("---")

    if st.button("💾 Guardar Configuración", use_container_width=True):
        st.success("✅ Configuración guardada (modo simulación)")
