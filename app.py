import streamlit as st
from src.debate.crew import Debate

st.set_page_config(page_title="AI Debate Arena")

st.title("🧠 AI Debate Arena")
st.write("Enter a topic and let AI debate!")

topic = st.text_input("Enter Debate Topic")

if st.button("Start Debate"):
    if topic:
        with st.spinner("Running debate..."):
            result = Debate().crew().kickoff(inputs={"topic": topic})

        st.success("Debate Completed!")
        st.write(result.raw)
    else:
        st.warning("Please enter a topic")
