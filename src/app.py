import streamlit as st

st.title("Primeiro projeto com Streamlit")
"ola mundo"

if st.button("Clique aqui"):
    st.file_uploader("Escolha um arquivo")

st.chat_input("Digite algo aqui")
st.chat_message("Mensagem de chat")