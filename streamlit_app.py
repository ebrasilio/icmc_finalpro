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
st.markdown("""---""")
st.markdown("Imagens")

# imagens
#colunas =st.columns(3)
st.write("nossas redes:")
#colunas[0].image("img/foto1.pg")
#colunas[1].image("img/foto2.pg")
#colunas[2].image("img/foto3.pg")
#st.image("img/animada.gif")


# formulario aula 5:
nome = st.text_input("Infomr seu nome:", placeholder="preencha seu nome")
idade = st.number_input("Idade:", min_value=8, max_value=80, step=1)
nasc = st.date_input("data nascimento: ", format="DD/MM/YYYY")
horaAtual = st.time_input("selecione a hora", step=60) # a cada 15 minutos
# para agendar step = tempo em segundos
corPerfil = st.color_picker("selecione a cor")

st.write("Nome: ",nome)
st.write("Idade: ", idade)
st.write("Nasc: ", nasc)
st.write("Hora ", horaAtual)

html_code = """
    <h1 style = 'color: {};'>Essa é a sua cor</h1>

""".format(corPerfil)
st.markdown(html_code, unsafe_allow_html=True)