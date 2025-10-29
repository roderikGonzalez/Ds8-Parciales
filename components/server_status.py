import streamlit as st

def server_status_page():
    st.title("🟢 Estado de Servidores")
    st.write("Monitorea y gestiona tus servidores registrados en tiempo real.")

    # 🚀 Servidores de ejemplo (luego se reemplazan por datos de Supabase)
    servidores = [
        {"Nombre": "Servidor Ubuntu 01", "IP": "192.168.1.10", "Sistema": "Ubuntu 22.04", "Estado": "🟢 Activo"},
        {"Nombre": "Windows Server AD", "IP": "192.168.1.15", "Sistema": "Windows Server 2019", "Estado": "🔴 Apagado"},
        {"Nombre": "Servidor Backup", "IP": "192.168.1.22", "Sistema": "Debian 11", "Estado": "🟡 Mantenimiento"},
    ]

    # 🔍 Barra de búsqueda
    search = st.text_input("Buscar servidor por nombre o IP:")

    if search:
        servidores = [
            srv for srv in servidores 
            if search.lower() in srv["Nombre"].lower() or search in srv["IP"]
        ]

    # 🧱 Mostrar tarjetas
    for srv in servidores:
        with st.container():
            st.markdown(
                f"""
                <div style="
                border:1px solid #444; border-radius:10px; padding:18px; margin-top:12px;
                background-color:#d3d3d3;">
                    <h3 style="margin:0;">{srv['Nombre']}</h3>
                    <p style="margin:0; opacity:0.8;">{srv['Sistema']} | {srv['IP']}</p>
                    <p style="margin-top:6px; font-size:18px;">Estado: <strong>{srv['Estado']}</strong></p>
                </div>
                """, unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)
            with col1:
                st.button("🔎 Ver detalles", key=f"det_{srv['IP']}")
            with col2:
                st.button("♻️ Reiniciar", key=f"restart_{srv['IP']}")
            with col3:
                st.button("🗑️ Eliminar", key=f"del_{srv['IP']}")

    st.write("---")
    st.button("➕ Registrar nuevo servidor", use_container_width=True)
