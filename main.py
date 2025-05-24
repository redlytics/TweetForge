# pip install --upgrade langchain langchain-google-google-genai streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os
import base64

os.environ['GOOGLE_API_KEY'] = "AIzaSyApdVSUZyVKrIZQY1is3meRX6fyzd2KFFI"

# Initialize Google's Gemini Model

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

#Prompt Template

# Create Prompt Templates for generating Tweets

tweet_template = """You write amazing tweets. Give me {number} tweets on {topic}. the tweet should be in first person. the tweet should be regarding the following {context}. Generate an engaging and positive tweet highlighting the impactful work of {organisation} in the {context}. Focus on the value they bring to their community, and the nation as a whole the dedication of their team, and any recent successes or contributions. The tweet should be warm, relatable, and inspiring. Avoid controversy and aim for a tone that encourages engagement through likes, shares, and comments. Include a call to action, such as inviting followers to learn more or join the cause. Keep it concise, with a positive, forward-looking message. The tweet should also include an aggressive Call to Action. the tweets should be in {language}. 

Please follow the following instructions:
1. Dont be offensive. 
2. Do not create tweets uses explicit language. 
3. Do not create political tweets.
4. Ensure all content is respectful and appropriate to all audiences.
5. Avoid creating tweets on offensive and controversial topics.
6. Include emojis where required alongwith text.



"""
tweet_prompt = PromptTemplate(input_variables = ["number", "topic", "context", "organisation", "language"], template = tweet_template)

#tweet_template.format(number=3, topic="Technology Absorption", context="Development of Quadcopter with Civilian vendor named RK Industries", organisation="Indian Army", language = "English")

# Create LLM Chain using Prompt Template and Model
tweet_chain = tweet_prompt | gemini_model

st.set_page_config(page_title="TWEET FORGE by FEARLESS", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp2628993.jpg');
        background-size: cover;
        background-repeat: repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.header("TWEETFORGE by REDLYTICS")

st.markdown("""
    <style>
    .custom-header {
        font-size: 48px;           /* Change font size */
        color: #FF4500;            /* OrangeRed color */
        font-family: 'Impact', sans-serif;  /* Bold font */
        text-align: center;        /* Center align */
        margin-top: 5px;
        margin-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Custom styled header
st.markdown('<div class="custom-header">TWEET FORGE</div>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .custom-subheader {
        font-size: 24px;              /* Adjust font size */
        color: #FF4500;               /* Orange Red color */
        font-family: 'Verdana', sans-serif; /* Custom font */
        text-align: center;           /* Center align */
        margin-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Custom styled subheader
st.markdown('<div class="custom-subheader">by REDLYTICS</div>', unsafe_allow_html=True)
#st.subheader("by REDLYTICS")

st.markdown("""
    <style>
    .custom-subheader_1 {
        font-size: 24px;              /* Adjust font size */
        color: #FFFFFF;               /* White color */
        font-family: 'Verdana', sans-serif; /* Custom font */
        text-align: center;           /* Center align */
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-subheader_1">Generate Tweets that has HIGH User Engagement and User Retention without disclosing YOUR IDENTITY"</div>', unsafe_allow_html=True)
#st.subheader("Generate Tweets that has HIGH User Engagement and User Retention without disclosing YOUR IDENTITY")

# Streamlit input
topic = st.text_input('Enter the TOPIC of the Tweet', "Example - Tech Absorption, Make In India, Fitness")
#topic = st.text_input("Topic")

context = st.text_area('Enter CONTEXT of the TWEET',"Example - Collabaration with RK Industries development of Quadcopter as part of Make In India")
#language = st.text_input("Language")

col1, col2, col3 = st.columns(3)

with col1:
    language = st.selectbox(label = "Choose LANGUAGE of Tweet", options = ['English', 'Hindi', 'Urdu', 'Mandarin', 'Cantonese'])

with col2:
    organisation = st.text_input('Organisation', "Example - Indian Army/ Ashtashakti Command")

with col3:
    number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

left, middle, right = st.columns(3)
#if left.button("Plain button", use_container_width=True):
#    left.markdown("You clicked the plain button.")
if middle.button("Generate Tweet", icon="😃", use_container_width=True):
#    middle.markdown("You clicked the emoji button.")
#if right.button("Material button", icon=":material/mood:", use_container_width=True):
#   right.markdown("You clicked the Material button.")
#if st.button("Generate Tweets"):
    #Response
    response = tweet_chain.invoke({"number" : number, "topic" : topic, "context" : context, "organisation" : organisation, "language" : language})
    st.write(response.content)
