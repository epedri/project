import folium.map
import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
import folium
from utils import *

st.set_page_config(layout="wide")
#st.logo("visual_assets\Logo_main.png", size="large")
def main():
    #st.set_page_config("WTF") # NICE TO SET
    st.title("Titles")
    st.caption("Subtitle")
    


    data = gpd.read_file("data/metro_train.shp")
    # columns will be named properly at final
    data.columns = ["FID_Metro_",
                    "Id",
                    "metro_quality",
                    "FID_Train_",
                    "Id_1",
                    "train_quality",
                    "Shape_Leng",
                    "Shape_Area",
                    "geometry"]

    for val in ["metro_val", "train_val", "whatever_val"]:
        if val not in st.session_state:
            st.session_state[val] = 0

    if "mapped" not in st.session_state:
            st.session_state["mapped"] = False
    
    topics = ["Transportation", "Something Else"] 
    selectbox = st.sidebar.selectbox("Topic", topics)

    with st.sidebar:
        if selectbox == "Transportation":
                st.session_state["metro_val"] = st.number_input("Metro Importance", value=st.session_state["metro_val"])
                st.session_state["train_val"] = st.number_input("Train Importance", value=st.session_state["train_val"])
        else:
            st.session_state["whatever_val"] = st.number_input("Something Importance", value=st.session_state["whatever_val"])

        with st.form(key="submit_form"):
            st.session_state["submitted"] = st.form_submit_button(label="Submit when Finish Browsing")
            if st.session_state["submitted"]:
                st.session_state["metro_final"] = st.session_state["metro_val"]
                st.session_state["train_final"] = st.session_state["train_val"]
                st.session_state["whatever_final"] = st.session_state["whatever_val"]


    if st.session_state["submitted"] or st.session_state["mapped"]:
        st.session_state["mapped"] = True
        st.session_state["submitted"] = False
        tring = user_importance(data, 
                                [("metro_quality", st.session_state["metro_final"]),
                                 ("train_quality", st.session_state["train_final"])
                                ]
                                )
        st.session_state["map_base"] = tring.explore(column='result', tiles='CartoDB dark_matter', cmap="RdYlGn", vmin=0, vmax=5,
                                 location=[38.71, -9.05], zoom_start=10.5, scrollWheelZoom=False)
        st_map = st_folium(st.session_state["map_base"], width=900, height=500)
    else:
        map_base = folium.Map(location=[38.71, -9.05], zoom_start=10.5, scrollWheelZoom=False, tiles="CartoDB dark_matter")
        st_map = st_folium(map_base, width=900, height=500)
        
    exit_bt = st.sidebar.button("Exit")
    if exit_bt:
        st.switch_page("app.py") 

if __name__ == "__main__":
    main()



