import streamlit as st
def change():
    print(st.session_state . checker)
state=st.checkbox("checkbox",value=True,on_change=change,key="checker")