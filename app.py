import streamlit as st
import requests

st.title("GROQ API Fetcher")

# Input from user
api_url = st.text_input("Enter your GROQ API Endpoint (without query params)")
api_key = st.text_input("Enter your GROQ API Key", type="password")
query = st.text_area("Enter your GROQ Query", value="*[_type == 'post']{title, _id}")

if st.button("Fetch Data"):
    if not api_url or not api_key or not query:
        st.error("Please fill all fields!")
    else:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {"query": query}

        try:
            response = requests.post(f"{api_url}/v1/data/query/production", json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            st.success("Data fetched successfully!")
            st.json(data)  # Display data in JSON format
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching data: {e}")
