import streamlit as st
import re
st.markdown("<h1 style:'text-align:center;'>Density Checker</h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
text=st.text_area("paragraph")
col1,col2,col3=st.columns(3)
words_dict=dict()
if text:
    col1.markdown (f"<h3 style='text-align:center;'>keywords</h3>",unsafe_allow_html=True)
    col2.markdown (f"<h3 style ='text-align:center;'>occurances</h3>",unsafe_allow_html=True)
    col3.markdown (f"<h3 style ='text-align:center;'>percentages</h3>",unsafe_allow_html=True)
sim_text=re.sub("[.,?!@$&*#:]","",text)
words=sim_text.lower().split()
t_len=len(words)
for word in words:
    if word:
        words_dict[word] = words_dict.get(word, 0) + 1
    else:
        words_dict[word]=1
key=list(words_dict.keys())
values=list(words_dict.values())
for i in range(len(key)):
    col1.markdown(f"<h5>{key[i]}</h5>",unsafe_allow_html=True)
    col2.markdown (f"<h5>{values[i]}</h5>",unsafe_allow_html=True)
    col3.markdown(f"<h5>{round((values[i]/t_len)*100,2)}%</h5>",unsafe_allow_html=True)