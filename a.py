import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io
import base64

# Initialize the Hugging Face Inference Client
client = InferenceClient("black-forest-labs/FLUX.1-schnell", token="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")

# Streamlit app layout
st.title("Text to Image Generator")
st.write("Enter a prompt below and click 'Generate Image'.")

# User input for the prompt
prompt = st.text_input("Prompt:", "")

# Button to generate the image
if st.button("Generate Image"):
    if prompt:
        try:
            # Generate the image
            image = client.text_to_image(prompt)

            # Convert the PIL image to a base64 string
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            # Display the image
            st.image(image, caption=prompt, use_column_width=True)
        except Exception as e:
            st.error(f"Error generating image: {e}")
    else:
        st.warning("Please enter a prompt.")