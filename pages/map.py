import sys
sys.dont_write_bytecode = True

import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
import folium
from utils import *

st.set_page_config(layout="wide")
#st.logo("visual_assets\Logo_main.png", size="large")
def main():
    st.title("Build Your Own Map")
    st.caption("""Chose your preferred points of interest from the sidebar, then adjust the importance of each point of interest using the sliders.      
    Once you are satisfied with your selections, click the 'Submit when Finish Browsing' button to generate your personalized map.            
    You can always return to adjust your preferences and regenerate the map, just remember that making one map can take up to a few minutes.""")

    if "data" not in st.session_state:
        data = gpd.read_file("data/data1.shp")
        data.columns = ["FID_data",
                        'playground_quality', 
                        'picnic_quality', 
                        'parks_quality', 
                        'sport_equipment_quality', 
                        'sport_entities_quality',
                        'hotels_quality', 
                        'recycling_quality', 
                        'restrooms_quality', 
                        'funicular_quality', 
                        'electrocar_quality',
                        'tracks_quality', 
                        'bicicle_quality', 
                        'roads_quality', 
                        'greens_quality',
                        'dog_quality',
                        'field_quality', 
                        'metro_quality', 
                        'train_quality', 
                        'theatres_quality', 
                        'museums_quality',
                        'papelarias_quality', 
                        'monuments_quality', 
                        'malls_quality', 
                        'mercados_quality', 
                        'feiras_quality',
                        'private_school_quality', 
                        'public_school_quality', 
                        'bombeiros_quality', 
                        'private_hospital_quality', 
                        'public_hospital_quality',
                        'pharmacies_quality', 
                        'health_center_quality', 
                        'police_quality', 
                        'public_kindergarten_quality', 
                        'university_quality',
                        'professionial_school_quality', 
                        'private_kindergarten_quality', 
                        'special_school_quality', 
                        "buy_quality",
                        "rent_quality",
                        'Shape_Leng', 
                        'Shape_Area',
                        'geometry']
        st.session_state["data"] = data
    else:
        data = st.session_state["data"]

    list_names = ["parks_val", "greens_val", "museums_val", "monuments_val", "public_kindergarten_val", "private_kindergarten_val",
                  "public_school_val", "private_school_val", "university_val", "special_school_val", "professionial_school_val",
                  "sport_equipment_val", "playground_val", "dog_val", "field_val", "private_hospital_val", "public_hospital_val",
                  "health_center_val", "pharmacies_val", "bombeiros_val", "police_val", "malls_val", "mercados_val", "feiras_val",
                  "papelarias_val", "theatres_val", "picnic_val", "hotels_val", "metro_val", "train_val", "bicicle_val", "roads_val",
                  "electrocar_val", "funicular_val", "tracks_val",
                  "recycling_val", "restrooms_val", "buy_val", "rent_val"]

    for val in list_names:
        if val not in st.session_state:
            st.session_state[val] = 0

    if "mapped" not in st.session_state:
            st.session_state["mapped"] = False
    
    topics = [
              "Parks & Green Areas",
              "Cultural & Historical Landmarks",
              "Educational Institutions",
              "Sports Facilities & Recreation",
              "Healthcare Services",
              "Public Safety & Law Enforcement",
              "Retail & Grocery Stores",
              "Leisure & Entertainment Venues",
              "Housing Costs",
              "Public Transport & Mobility",
              "Other"
              ] 

    with st.sidebar:
        selectbox = st.sidebar.selectbox("Topic", topics)
        if selectbox == "Parks & Green Areas":
            st.session_state["parks_val"] = st.number_input("Proximity to Parks", value=st.session_state["parks_val"])
            st.session_state["greens_val"] = st.number_input("Proximity to Green Spaces", value=st.session_state["greens_val"])
        elif selectbox == "Cultural & Historical Landmarks":
            st.session_state["museums_val"] = st.number_input("Proximity to Museums", value=st.session_state["museums_val"])
            st.session_state["monuments_val"] = st.number_input("Proximity to National Monuments", 
                                                                value=st.session_state["monuments_val"])
        elif selectbox == "Educational Institutions":
            st.session_state["public_kindergarten_val"] = st.number_input("Proximity to Public Kindergartens", 
                                                                          value=st.session_state["public_kindergarten_val"])
            st.session_state["private_kindergarten_val"] = st.number_input("Proximity to Private Kindergartens", 
                                                                           value=st.session_state["private_kindergarten_val"])
            st.session_state["public_school_val"] = st.number_input("Proximity to Public Schools", 
                                                                    value=st.session_state["public_school_val"])
            st.session_state["private_school_val"] = st.number_input("Proximity to Private Schools", 
                                                                     value=st.session_state["private_school_val"])
            st.session_state["university_val"] = st.number_input("Proximity to Universities", 
                                                                 value=st.session_state["university_val"])
            st.session_state["special_school_val"] = st.number_input("Proximity to Special-Needs Education Schools", 
                                                                     value=st.session_state["special_school_val"])
            st.session_state["professionial_school_val"] = st.number_input("Proximity to Professional Schools", 
                                                                           value=st.session_state["professionial_school_val"])
        elif selectbox == "Sports Facilities & Recreation":
            st.session_state["sport_equipment_val"] = st.number_input("Proximity to Outdoor Gyms", 
                                                                      value=st.session_state["sport_equipment_val"])
            st.session_state["playground_val"] = st.number_input("Proximity to Playgrounds",
                                                                  value=st.session_state["playground_val"])
            st.session_state["dog_val"] = st.number_input("Proximity to Dog Playgrounds", value=st.session_state["dog_val"])
            st.session_state["field_val"] = st.number_input("Proximity to Public Farms", value=st.session_state["field_val"])
        elif selectbox == "Healthcare Services":
            st.session_state["private_hospital_val"] = st.number_input("Proximity to Private Hospitals", 
                                                                       value=st.session_state["private_hospital_val"])
            st.session_state["public_hospital_val"] = st.number_input("Proximity to Public Hospitals", 
                                                                      value=st.session_state["public_hospital_val"])
            st.session_state["health_center_val"] = st.number_input("Proximity to Health Centers", 
                                                                    value=st.session_state["health_center_val"])
            st.session_state["pharmacies_val"] = st.number_input("Proximity to Pharmacies", value=st.session_state["pharmacies_val"])
        elif selectbox == "Public Safety & Law Enforcement":
            st.session_state["bombeiros_val"] = st.number_input("Proximity to Firefighters Stations", 
                                                                value=st.session_state["bombeiros_val"])
            st.session_state["police_val"] = st.number_input("Proximity to Police Stations", value=st.session_state["police_val"])
        elif selectbox == "Retail & Grocery Stores":
            st.session_state["malls_val"] = st.number_input("Proximity to Malls", value=st.session_state["malls_val"])
            st.session_state["mercados_val"] = st.number_input("Proximity to Markets", value=st.session_state["mercados_val"])
            st.session_state["feiras_val"] = st.number_input("Proximity to Fairs", value=st.session_state["feiras_val"])
            st.session_state["papelarias_val"] = st.number_input("Proximity to Stationery Stores", 
                                                                 value=st.session_state["papelarias_val"])
        elif selectbox == "Leisure & Entertainment Venues":
            st.session_state["theatres_val"] = st.number_input("Proximity to Theatres", value=st.session_state["theatres_val"])
            st.session_state["picnic_val"] = st.number_input("Proximity to Picnic Spaces", value=st.session_state["picnic_val"])
        elif selectbox == "Housing Costs":
            st.session_state["rent_val"] = st.number_input("Rent in € per m2 per Month", value=st.session_state["rent_val"])
            st.session_state["buy_val"] = st.number_input("Price in € per m2", value=st.session_state["buy_val"])
            st.session_state["hotels_val"] = st.number_input("Proximity to Hotels", value=st.session_state["hotels_val"])
        elif selectbox == "Public Transport & Mobility": 
            st.session_state["metro_val"] = st.number_input("Proximity to Metro Stations", value=st.session_state["metro_val"])
            st.session_state["train_val"] = st.number_input("Proximity to Train Stations", value=st.session_state["train_val"])
            st.session_state["bicicle_val"] = st.number_input("Proximity to Bicicle Lanes", value=st.session_state["bicicle_val"])
            st.session_state["roads_val"] = st.number_input("Proximity to Roads", value=st.session_state["roads_val"])
            st.session_state["electrocar_val"] = st.number_input("Proximity to Electric Vehicle Charge Stations", 
                                                                 value=st.session_state["electrocar_val"])
            st.session_state["funicular_val"] = st.number_input("Proximity to Funiculars and Inclined Elevators", 
                                                                 value=st.session_state["funicular_val"])
            st.session_state["tracks_val"] = st.number_input("Remoteness from Train Tracks", value=st.session_state["tracks_val"])
        elif selectbox == "Other":
            st.session_state["recycling_val"] = st.number_input("Proximity to EcoPoints", value=st.session_state["recycling_val"])
            st.session_state["restrooms_val"] = st.number_input("Proximity to Public Restrooms", value=st.session_state["restrooms_val"])

        with st.form(key="submit_form"):
            st.session_state["submitted"] = st.form_submit_button(label="Submit when Finish Browsing")
            if st.session_state["submitted"]:
                for el in list_names:
                    st.session_state[splitter(el) + "_final"] = st.session_state[el]

    if st.session_state["submitted"]:
        st.session_state["trying"] = None
        st.session_state["map_base"] = None
        tot = []
        for val in list_names:
            tot.append((splitter(val) + "_quality", st.session_state[splitter(val) + "_final"]))
        st.session_state["trying"] = user_importance(data, tot)

        st.session_state["mapped"] = True
        st.session_state["submitted"] = False
            
        st.session_state["map_base"] = st.session_state["trying"].explore(column='result', tiles='CartoDB Positron', 
                                                                          cmap="RdYlGn", vmin=0, vmax=5,
                                                                          location=[38.71, -9.05], zoom_start=10.5, 
                                                                          scrollWheelZoom=False, #tooltip=False,
                                                                          #legend_kwds={"labels":labels}
                                                                          )
        st_map = st_folium(st.session_state["map_base"], width=900, height=500)
    elif st.session_state["mapped"]:
        st.session_state["map_base"] = st.session_state["trying"].explore(column='result', tiles='CartoDB Positron', 
                                                                          cmap="RdYlGn", vmin=0, vmax=5,
                                                                          location=[38.71, -9.05], zoom_start=10.5, 
                                                                          scrollWheelZoom=False, #tooltip=False,
                                                                          #legend_kwds={"labels":labels}
                                                                          )
        st_map = st_folium(st.session_state["map_base"], width=900, height=500)
    else:
        map_base = folium.Map(location=[38.71, -9.05], zoom_start=10.5, scrollWheelZoom=False, tiles="CartoDB Positron")
        st_map = st_folium(map_base, width=900, height=500)
    
    exit_bt = st.sidebar.button(label="Exit", icon=":material/logout:")
    if exit_bt:
        st.switch_page("app.py") 

if __name__ == "__main__":
    main()
