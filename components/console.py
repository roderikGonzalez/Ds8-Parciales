import streamlit as st

def console_page():
    st.set_page_config(page_title="Consola Remota", page_icon="💻", layout="wide")

    st.title("💻 Consola Remota")
    st.write("Ejecuta comandos directamente en tus servidores desde el navegador.")

    # 🚀 Servidores de ejemplo (luego se cargan desde Supabase)
    servidores = [
        {"Nombre": "Servidor Ubuntu 01", "IP": "192.168.1.10"},
        {"Nombre": "Windows Server AD", "IP": "192.168.1.15"},
        {"Nombre": "Servidor Backup", "IP": "192.168.1.22"},
    ]

    servidor_seleccionado = st.selectbox(
        "Selecciona un servidor:",
        [srv["Nombre"] for srv in servidores]
    )

    st.write(f"Conectado a: **{servidor_seleccionado}**")

    comando = st.text_input("Ingresa un comando:")

    if st.button("Ejecutar"):
        if comando.strip() == "":
            st.warning("⚠️ Escribe un comando primero.")
        else:
            st.markdown(f"```\nEjecutando en {servidor_seleccionado}:\n$ {comando}\n```")

            st.success("✅ Comando ejecutado (modo simulación).")
            st.markdown(
                f"""
                ```
                {comando}: output simulado...
                (Aquí aparecerá el resultado real cuando conectemos SSH)
                ```
                """
            )

    st.write("---")
    st.subheader("📝 Historial de comandos recientes (simulado)")
    st.code("""$ uptime\n$ ls -la\n$ df -h\n$ systemctl status""")
