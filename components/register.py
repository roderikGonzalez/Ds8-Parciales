import streamlit as st

def register_page():
    st.title("📝 Crear Cuenta")

    name = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    if st.button("Registrarme"):
        st.success("Cuenta creada (más adelante activaremos Supabase) 🎉")

    st.write("---")

    st.button("Volver a iniciar sesión", on_click=lambda: cambio("login"))

def cambio(pagina):
    st.session_state["page"] = pagina
