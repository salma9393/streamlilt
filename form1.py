import streamlit as st
st.markdown("#user registration")
form=st.form("form")
form.text_input("firstname")
form.form_submit_button("submit")