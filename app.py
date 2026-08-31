from src.similarity import get_similarity_level
from src.similarity import RGB_THRESHOLDS
from src.similarity import HSV_THRESHOLDS
from src.similarity import CIE76_THRESHOLDS
from src.similarity import CIEDE2000_THRESHOLDS

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

rgb_level, rgb_color = get_similarity_level(rgb_distance, RGB_THRESHOLDS)
hsv_level, hsv_color = get_similarity_level(hsv_distance, HSV_THRESHOLDS)
cie76_level, cie76_color = get_similarity_level(cie76_distance, CIE76_THRESHOLDS)
ciede2000_level, ciede2000_color = get_similarity_level(ciede2000_distance, CIEDE2000_THRESHOLDS)


st.markdown(
    f"""
    <div style="
        text-align: center;
        color: {rgb_color};
    ">
        <span style="
            font-size: 24px;
            font-weight: bold;
        ">
            {rgb_distance:.4f}
        </span>
        <br>
        <span style="
            font-size: 16px;
            color: inherit;
        ">
            {rgb_level}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div style="
        text-align: center;
        color: {hsv_color};
    ">
        <span style="
            font-size: 24px;
            font-weight: bold;
        ">
            {hsv_distance:.4f}
        </span>
        <br>
        <span style="
            font-size: 16px;
            color: inherit;
        ">
            {hsv_level}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="
        text-align: center;
        color: {cie76_color};
    ">
        <span style="
            font-size: 24px;
            font-weight: bold;
        ">
            {cie76_distance:.4f}
        </span>
        <br>
        <span style="
            font-size: 16px;
            color: inherit;
        ">
            {cie76_level}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div style="
        text-align: center;
        color: {ciede2000_color};
    ">
        <span style="
            font-size: 24px;
            font-weight: bold;
        ">
            {ciede2000_distance:.4f}
        </span>
        <br>
        <span style="
            font-size: 16px;
            color: inherit;
        ">
            {ciede2000_level}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)