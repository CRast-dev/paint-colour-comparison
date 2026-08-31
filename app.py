import streamlit as st
from src.colour import Colour

from src.comparison import calculate_rgb_euclidian_dist
from src.comparison import calculate_hsv_dist
from src.comparison import calculate_cie76_distance
from src.comparison import calculate_ciede2000_distance

st.title("Paint Colour Analyzer")

st.write(
    "Test"
)

colour1_input = st.color_picker(
    "Choose the colour",
    "#C04040"
)

colour2_input = st.color_picker(
    "Choose the colour",
    "#C11111"
)
colour1 = Colour(colour1_input)
colour2 = Colour(colour2_input)

st.subheader("Selected colours")
col1, col2 = st.columns(2)
with col1:
    st.write("Colour 1")
    st.code(colour1.hex)
with col2:
    st.write("Colour 2")
    st.code(colour2.hex)

st.subheader("Colour distances")
rgb_distance = calculate_rgb_euclidian_dist(colour1,colour2)
hsv_distance = calculate_hsv_dist(colour1,colour2)
cie76_distance = calculate_cie76_distance(colour1,colour2)
ciede2000_distance = calculate_ciede2000_distance(colour1,colour2)

result1, result2, result3, result4 = st.columns(4)
with result1:
    st.metric("RGB Euclidean",f"{rgb_distance:.4f}")

with result2:
    st.metric("HSV",f"{hsv_distance:.4f}")

with result3:
    st.metric("CIE76",f"{cie76_distance:.4f}")

with result4:
    st.metric("CIEDE2000",f"{ciede2000_distance:.4f}")