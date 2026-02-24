import streamlit as st
st.markdown("#user registration")
form=st.form("form2")
form.text_input("firstname")
st.form_submit_button("submit")   