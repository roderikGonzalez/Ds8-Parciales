import streamlit as st
import random

import streamlit as st

def dashboard_page():
    st.title("📊 Dashboard")
    st.write("Bienvenido al panel principal 🚀")


def dashboard_page():
    st.markdown("""
        <style>
        .title {
            font-size: 36px;
            font-weight: 700;
            color: #2b2d42;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #6c757d;
            font-size: 18px;
            margin-bottom: 25px;
        }
        .card {
            background-color: #f8f9fa;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
            text-align: center;
            transition: 0.2s;
        }
        .card:hover {
            transform: scale(1.02);
            background-color: #f1f3f5;
        }
        .metric-title {
            font-size: 18px;
            color: #495057;
        }
        .metric-value {
            font-size: 28px;
            font-weight: bold;
            color: #212529;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            color: #2b2d42;
            margin-top: 40px;
        }
        .event {
            padding: 10px 0;
            border-bottom: 1px solid #dee2e6;
        }
        .event:last-child {
            border-bottom: none;
        }
        .event span {
            color: #007bff;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="title">🖥️ Panel Principal</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Bienvenido al panel de control de tus servidores 🚀</div>', unsafe_allow_html=True)

    # Métricas
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="card"><div class="metric-title">Servidores Activos</div><div class="metric-value">2</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><div class="metric-title">CPU Global</div><div class="metric-value">14%</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><div class="metric-title">Memoria Promedio</div><div class="metric-value">37%</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card"><div class="metric-title">Usuarios Conectados</div><div class="metric-value">5</div></div>', unsafe_allow_html=True)

    # Sección de rendimiento
    st.markdown('<div class="section-title">📊 Rendimiento del Sistema</div>', unsafe_allow_html=True)

    cpu = random.randint(10, 80)
    memoria = random.randint(30, 90)
    red = random.randint(20, 60)

    st.progress(cpu / 100)
    st.write(f"CPU en uso: {cpu}%")

    st.progress(memoria / 100)
    st.write(f"Memoria utilizada: {memoria}%")

    st.progress(red / 100)
    st.write(f"Tráfico de red: {red}%")

    # Sección de eventos
    st.markdown('<div class="section-title">🕓 Últimos eventos del sistema</div>', unsafe_allow_html=True)

    eventos = [
        ("Servidor 1", "Iniciado correctamente"),
        ("Servidor 2", "Realizando copia de seguridad"),
        ("Servidor 3", "Actualización completada"),
        ("Servidor 4", "Reinicio programado"),
        ("Servidor 2", "Apagado por inactividad")
    ]

    for nombre, evento in eventos:
        st.markdown(f'<div class="event">🟢 <span>{nombre}</span> - {evento}</div>', unsafe_allow_html=True)

