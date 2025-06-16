import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

st.sidebar.page_link("app.py", label="Home", icon=":material/home:")
st.sidebar.page_link("pages/map.py", label="Build Your Map", icon=":material/public:")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_animation = load_lottiefile(r"visual_assets\ani1.json")


st.title("Mapping Your Ideal Place")

with st.container():
    col1, col2, col6 = st.columns((4,1, 2))
    with col1: 

        st.subheader("A Tool for Finding Your Best Location in Lisbon")
        st.markdown("""Choosing where to live, visit, or rent has always been a complex decision. 
                        
Typically we seek locations that meet our personal preferences, such as proximity to amenities, access to public transport, green spaces, schools, and more. 
                        
Here you can define your most preferred points of interest and visualize the best locations in Lisbon based on these. 
                        
This tool identifies and ranks areas according to how well they satisfy the your criteria. 
                        
Locations with a higher concentration of your dersired Points of interest within a 5-minute walking radius are given the highest scores, while those farther away score lower.
                    """)
    with col6:
        st_lottie(lottie_animation, speed=1, loop=True, quality="low", height=270, width=270)

with st.container():
    col3, col4, col5 = st.columns((1, 1, 1))
    with col4:
        Build_map= st.button("**Want to build your own map?! Build it here!**")
        if Build_map:
            st.switch_page("pages/map.py")



