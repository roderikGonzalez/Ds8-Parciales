import streamlit as st
from datetime import datetime

def logs_page():
    st.title("📜 Registro de Logs del Servidor")

    st.write("Aquí podrás visualizar eventos, cambios y acciones realizadas en el servidor.")

    st.markdown("### 🔍 Filtros de búsqueda")

    col1, col2, col3 = st.columns(3)
    with col1:
        fecha = st.date_input("Fecha", datetime.today())
    with col2:
        tipo = st.selectbox(
            "Tipo de Log",
            ["Todos", "Información", "Advertencia", "Error", "Sistema"]
        )
    with col3:
        st.text_input("Buscar palabra clave", placeholder="Ejemplo: reinicio, usuario...")

    st.button("Aplicar Filtros", use_container_width=True)

    st.markdown("---")

    st.markdown("### 📝 Agregar registro manual")
    nota = st.text_area("Descripción del evento:")
    if st.button("Guardar Log"):
        if nota.strip() == "":
            st.warning("⚠️ Escribe una descripción antes de guardar.")
        else:
            st.success("✅ Log guardado (modo simulación).")
            st.code(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] MANUAL: {nota}")

    st.markdown("---")

    st.markdown("### 📄 Historial de Logs (Simulados)")

    logs = [
        "[2025-10-27 14:12:33] INFO: Servidor iniciado correctamente.",
        "[2025-10-27 14:15:40] ADVERTENCIA: Uso de CPU al 85%.",
        "[2025-10-27 14:18:10] ERROR: Fallo en conexión SSH entrante.",
        "[2025-10-27 14:20:01] SISTEMA: Usuario admin ejecutó comando 'reboot'.",
    ]

    for entry in logs:
        if "ERROR" in entry:
            color = "#FF6B6B"
        elif "ADVERTENCIA" in entry:
            color = "#FFA600"
        elif "INFO" in entry:
            color = "#4CAF50"
        else:
            color = "#8AB4F8"

        st.markdown(
            f"""
            <div style="padding:10px;border-radius:6px;border-left:6px solid {color};
            background-color:#1e1e1e;margin-bottom:8px;">
            <span style="color:{color};font-weight:bold;">{entry}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
