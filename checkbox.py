import streamlit as st
st.checkbox("checkbox1")
st.checkbox("checkbox2",value=True)
state=st.checkbox("checkbox3",value=True)
if state:
    st.write("hi")
else:
    st.write("hello")