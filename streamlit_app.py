import streamlit as st
import openai
import os

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title
st.set_page_config(page_title="AI Student Assistant", page_icon="🎓")
st.title("🎓 AI Study Assistant for Pakistani Students")

# Intro
st.markdown("""
Welcome! Ask any question from your **O/A Levels, Matric, or FSC syllabus** and I'll explain it in simple words.  
This assistant is trained to help you understand key concepts easily.  
""")

# Input
user_question = st.text_input("❓ Ask a question related to your studies:")

# Process input
if user_question:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to "gpt-4" if your API key supports it
            messages=[
                {"role": "system", "content": "You are a helpful study assistant for Pakistani students doing O/A Levels or Matric/FSC. Explain topics clearly, briefly, and in easy English or light Urdu-English mix."},
                {"role": "user", "content": user_question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        st.success("🧠 Here's the explanation:")
        st.write(answer)

# Footer
st.markdown("---")
st.markdown("Made by **Roman Faisal** | Arfa Karim Incubator")
