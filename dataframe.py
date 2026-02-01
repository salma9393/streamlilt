import streamlit as st
import pandas as pd
table1=pd.DataFrame ({"column1":[1,2,3,4,5,6],"column2":[7,8,9,5,6,4]})
st.table(table1)
st.dataframe(table1)