import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
    layout="wide",
)

st.title("Home")
st.sidebar.success("Pilih halaman di atas.")
st.subheader("SUB HEADER :wave:")
    
st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
st.write("Lorem ipsum dolor sit amet (https://github.com/aulanjay)")

st.write("---")

st.header("HEADER")
st.write("##")
st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            """
        )
st.header("HEADER")
col1, col2, col3 = st.columns(3)

with col1:
        st.subheader("VIVIZ - MANIAC MV")
        st.video('https://www.youtube.com/watch?v=9JFi7MmjtGA')

with col2:
        st.subheader("VIVIZ - PULL UP MV")
        st.video('https://youtu.be/ROGJzLUzIIs?si=MSAiclNJebfdEuwU')

with col3:
        st.subheader("VIVIZ - BOP BOP MV")
        st.video('https://youtu.be/cM963tI7Q_k?si=9XSOvG8oADqFJx3O')
    
st.write("---")