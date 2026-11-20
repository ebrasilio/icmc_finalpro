import streamlit as st

#título
st.title("ICMC - 3a Escola web para meninas 2026/2027")

# título de sessão, cabeçalho e subcabeçalho
st.header("Cabeçalho", divider=True)
st.subheader("seção 1")
st.text("paragrafo da seçaão 1")# --> semelhante ao paragrafo do html

st.subheader("seção 2")
st.text("paragrafo da seção 2")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
