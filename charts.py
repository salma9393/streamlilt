import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
table=pd.DataFrame({"column1":[1,2,3,4,5,6,7],"column2":[11,2,4,6,7,8,9]})
x=np.linespace(0,10,100)
st.sidebar.write("hello this is my sidebar")
fig=plt.figure()
plt=plt(x,np.sin(x))
st.write(fig)