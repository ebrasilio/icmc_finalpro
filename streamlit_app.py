import streamlit as st

#título
st.title("ICMC - 3a Escola web para meninas 2026/2027")

# título de sessão, cabeçalho e subcabeçalho
st.header("Cabeçalho", divider=True)
st.subheader("seção 1")
st.text("paragrafo da seçaão 1")# --> semelhante ao paragrafo do html

st.subheader("seção 2")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.markdown(":wizard: :books:")
st.markdown("""---""")
st.markdown("HTML")
html_code = """ 
<h1 style='color: purple;'> Esse é um cabeçalho rosa</h1> 
<p style='color: yellow;'> Esse é um paragrafo amarelo</p>
"""
st.markdown(html_code, unsafe_allow_html=True)
