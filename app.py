import streamlit as st
import streamlit as st
import json
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")
#st.logo("visual_assets\Logo_main.png", size="large")
st.title("MIAU MIAU")
Build_map= st.button("Build Your Map")
if Build_map:
    st.switch_page("pages/map.py")


