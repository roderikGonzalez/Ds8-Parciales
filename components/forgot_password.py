import streamlit as st

def forgot_password_page():
    st.title("🔄 Recuperar Contraseña")

    email = st.text_input("Ingresa tu correo")

    if st.button("Enviar enlace de recuperación"):
        st.info("Aquí enviaremos el enlace cuando conectemos Supabase 📩")

    st.write("---")

    st.button("Volver al inicio", on_click=lambda: cambio("login"))

def cambio(pagina):
    st.session_state["page"] = pagina
