import streamlit as st
from src.colour import colour

from src.comparison import calculate_rgb_euclidian_dist
from src.comparison import calculate_hsv_dist
from src.comparison import calculate_cie76_distance
from src.comparison import calculate_ciede2000_distance

st.title("Paint Colour Analyzer")

st.write(
    "Test"
)

colour1 = st.color_picker(
    "Choose the colour",
    "#C04040"
)

colour2 = st.color_picker(
    "Choose the colour",
    "#C11111"
)