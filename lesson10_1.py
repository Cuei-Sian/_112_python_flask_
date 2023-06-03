import streamlit as st

def button_click():
    st.write(st.session_state)

if st.button("Say Hello!",key="myButton",on_click=button_click):
    st.write("Why hello there")
else:
    st.write("Goodbye")