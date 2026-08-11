import streamlit as st
import requests

st.title("GTZAN Music Genre Classifier")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Predict Genre"):
        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://127.0.0.1:8000/predict/",
                files={"file": uploaded_file.getvalue()}
            )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Model thinks it's: {result['Class']} (Index: {result['Index']})")
        else:
            st.error(f"Error: {response.json()['detail']}")