import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

API_URL_SEMANTICS = os.getenv("IMAGE_TEXT_API_URL")
API_URL_CAPTION = os.getenv("TEXT_GENERATION_API_URL")

headers = {"Authorization": os.getenv("IMAGE_TEXT_HEADERS")}


def generate_semantics(file):
    response = requests.post(API_URL_SEMANTICS, headers=headers, data=file)
    return response.json()[0]["generated_text"]


def generate_caption(payload):
    response = requests.post(API_URL_CAPTION, headers=headers, json=payload)
    return response.json()[0]["generated_text"]


st.title("Image Captioning")
st.image("Image\MizSpaceTech.png", use_column_width=True)

file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if file:
    col1, col2 = st.columns(2)
    with col1:
        st.image(file, use_column_width=True)

    with col2:
        with st.spinner("Generating Semantics"):
            semantics = generate_semantics(file)
            # st.subheader("Semantics")
            # st.write(semantics)

        with st.spinner("Generating Captions"):
            prompt_dic = {"inputs": f"Question: Convert the following image semantics" 
                                    f"'{semantics}' to an instagram caption for my post."
                                    f" Make sure to add hashtags and emojis." 
                                    f"Answer: "}
            caption_raw = generate_caption(prompt_dic)
            st.subheader("Caption")

            caption = caption_raw.split("Answer: ")[1]
            # st.write(caption)


            # Define the dynamic text
            dynamic_text = caption

            # CSS styling for the fancy text box
            st.markdown(
                f"""
                <style>
                /* Add a rectangle around the text */
                .fancy-text {{
                    padding: 20px;
                    border-radius: 15px; /* Curved edges */
                    border: 2px solid #ccc; /* Green border */
                    box-shadow: 5px 5px 15px #aaa; /* Box shadow */
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            # Display the fancy text box with dynamic content
            st.markdown(f'<div class="fancy-text">{dynamic_text}</div>', unsafe_allow_html=True)

# output = query("Image\cat.jpg")
# print(output[0]["generated_text"])
