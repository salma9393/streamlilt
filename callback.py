import streamlit as st
def change():
    print("changed")
state=st.checkbox("checkbox",value=True,on_change=change)
if state:
    print("change")