import streamlit as st

st.title("Titulo")
nome = st.text_input("Informe seu nome: ")
st.write(f"Seu nome é: {nome}")
st.button(label="Oi")
st.html("<p>Oi<p/>")
st.checkbox("Concordo!")
st.balloons()
st.success("Sucesso!!!")
st.tabs(["Cat", "Dog", "Owl"])
st.date_input("Seu aniversário: ")
st.snow()
st.time_input("Horário: ")