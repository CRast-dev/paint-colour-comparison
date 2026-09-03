from src.similarity import get_similarity_level
from src.similarity import RGB_THRESHOLDS
from src.similarity import HSV_THRESHOLDS
from src.similarity import CIE76_THRESHOLDS
from src.similarity import CIEDE2000_THRESHOLDS
from src.image_coordinates import get_original_pixel

import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

from src.colour import Colour
from src.comparison import calculate_rgb_euclidian_dist
from src.comparison import calculate_hsv_dist
from src.comparison import calculate_cie76_distance
from src.comparison import calculate_ciede2000_distance


def display_similarity(algo_type, distance, level, colour):
    html = f"""
<div style="text-align: center;">
    <div style="font-size: 18px; font-weight: bold;">
        {algo_type}
    </div>
    <div style="font-size: 24px; font-weight: bold; color: {colour};">
        {distance:.4f}
    </div>
    <div style="font-size: 16px; color: {colour};">
        {level}
    </div>
</div>
"""
    st.markdown(html, unsafe_allow_html=True)


st.title("Paint Colour Analyzer")


st.subheader("Colour to compare against")
colour1_input = st.color_picker(
    "Choose Colour that is compared against","#C04040")
colour1 = Colour(colour1_input)

colour2 = None
st.subheader("Your chosen colour")
colour2_source = st.radio(
    "How do you want to select your colour?",
    ["Manual Hexvalue", "Pixelcolour from an uploaded image"]
)

if colour2_source == "Manual Hexvalue":
    colour2_input = st.color_picker("Choose Colour 2", "#C11111")
    colour2 = Colour(colour2_input)
else:
    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"]
    )
    if uploaded_image is not None:
        image = Image.open(uploaded_image).convert("RGB")
        display_width = 400

        coordinates = streamlit_image_coordinates(image, width= display_width)
        if coordinates is not None:
            pixel = get_original_pixel(image,coordinates,display_width)
            hex_code_pixel = Colour.getHexFromRGB(pixel[0],pixel[1],pixel[2])
            colour2 = Colour(hex_code_pixel)
            st.markdown(
            f"""
            <div style="
                display: flex;
                align-items: center;
                gap: 10px;
            ">
                <div style="
                    width: 40px;
                    height: 40px;
                    background-color: {hex_code_pixel};
                    border: 1px solid #888;
                    border-radius: 4px;
                "></div>
                <code>{hex_code_pixel}</code>
            </div>
            """,
            unsafe_allow_html=True
            )


if colour2 is not None:
    st.subheader("Selected colours")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Target Colour")
        st.code(colour1.hex)
    with col2:
        st.write("Your Colour")
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

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_similarity("RGB Euclidean", rgb_distance, rgb_level, rgb_color)
    with col2:
        display_similarity("HSV Distance", hsv_distance, hsv_level, hsv_color)
    with col3:
        display_similarity("CIE76", cie76_distance, cie76_level, cie76_color)
    with col4:
        display_similarity("CIEDE2000", ciede2000_distance, ciede2000_level, ciede2000_color)


