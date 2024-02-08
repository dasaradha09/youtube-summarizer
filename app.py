import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from  youtube_transcript_api import YouTubeTranscriptApi
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
def transcriptGenerator(url):
    try:
        video_id=url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=""
        for i in transcript_text:
            transcript+=" "+i["text"]
        return transcript
    except Exception as e:
        pass
def summarize(transcript,prompt):
    response=model.generate_content(prompt+transcript)
    return response.text
prompt="""you need to provide summarize the
youtube video transcript and return important poins as bullet points.here is my transcript:"""

st.title("YOUTUBE VIDEO SUMMARIZER")
youtube_link=st.text_input("enter the video link")
transcript=transcriptGenerator(youtube_link)
#summarize(transcript,propmt)
if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
a=st.button("Enter")
if a:
    transcript=transcriptGenerator(youtube_link)
    st.markdown("##detailednote")
    st.write(summarize(transcript,prompt))
    
    
    

    