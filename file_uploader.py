import streamlit as st
st.markdown ("---")
image=st.file_uploader("please upload an image",type=["jpg","jpej"])
if image is not None:
    st.image(image)
