import streamlit as st
st.markdown("#user registration")
with st.form("form2"):
    col1,col2=st.columns(2)
    col1.text_input("firstname")
    col2.text_input("lastname")
    st.text_input("email address")
    st.text_input("password")
    st.form_submit_button("submit")

