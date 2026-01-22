import os
import logging
import streamlit as st
from google import genai
from prompts import PROMPT_MAP


API_KEY = os.getenv("GOOGLE_API_KEY")
logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY not found")
    st.stop()

client = genai.Client(api_key=API_KEY)

# UI Config
st.set_page_config(
    page_title="AI Study Buddy",
    layout="wide"
)

st.title("AI Study Buddy")

mode = st.selectbox("Select Mode", list(PROMPT_MAP.keys()))
question = st.text_area("Ask your question", height=150)

if st.button("Generate Answer"):
    if not question.strip():
        st.warning("Enter a question")
    else:
        logging.info(f"Mode={mode} | Length={len(question)}")

        with st.spinner("Thinking..."):
            try:
                prompt = PROMPT_MAP[mode](question)

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )

                st.markdown("### AI Response")
                st.write(response.text.strip())

            except Exception as e:
                logging.error(str(e))
                st.error("Internal AI error")
