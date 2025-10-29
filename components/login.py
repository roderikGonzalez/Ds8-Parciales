import streamlit as st

def login_page():
    st.title("🔐 Iniciar Sesión")

    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        # ✅ Más adelante se validará con Supabase
        st.session_state["is_logged"] = True
        st.session_state["page"] = "dashboard"
        st.rerun()

    st.write("---")

    st.button("Crear una cuenta nueva", on_click=lambda: cambio("register"))
    st.button("Olvidé mi contraseña", on_click=lambda: cambio("forgot_password"))

def cambio(pagina):
    st.session_state["page"] = pagina
    st.rerun()
