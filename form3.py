import streamlit as st
st.markdown("<h1 'style=text-align:center;'>user registration</h1>",unsafe_allow_html=True)
with st.form ("form2",clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("first_name")
    l_name=col2.text_input("last_name")
    st.text_input("email_address")
    st.text_input("confirm password")
    day,month,year=st.columns(3)
    day.text_input("day")
    month.text_input("month")
    year.text_input("year")
    state=st.form_submit_button("submit")
    if state:
        if f_name==" " and l_name==" ":
            st.warning("please fill the above fields")
        else:
            st.success("submitted successfully")