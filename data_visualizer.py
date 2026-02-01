import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
figure=plt.figure()
def date_converter(date_col):
    result=list()
    values=date_col.values
    for value in values:
        result.append(str(value).split("T")[0])
    return result
st.markdown("<h1 style ='text-align: center;'>Data visualizer</h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
files_names=list()
files=st.file_uploader("upload multiple Files",type=["xlsx"],accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)
    selected_files=st.multiselect("select files",option=files_names)
    if selected_files:
        option=st.radio("select an entity against date",options=["None","cpu"])