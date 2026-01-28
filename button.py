import streamlit as st
def btn_click():
    print("button clicked")
btn=st.button("click me!",on_click=btn_click)