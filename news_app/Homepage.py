import streamlit as st
from PIL import Image
image = Image.open('PVhub.png')
st.set_page_config(
    page_title = "Project Valuehub",
    page_icon = "🥹",
)
image = Image.open('PVhub.png')
st.title("Main Page")
st.sidebar.success("Select a page above.")
st.image(image, caption='Project Valuehub, Designed for New Generation Investors')
val = st.radio("Select Language", ("中文", "English"))

