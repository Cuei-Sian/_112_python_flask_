import streamlit as st

if st.button("Say Hello!",key="myButton"):
    st.write("Why hello there")
else:
    st.write("Goodbye")