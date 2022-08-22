import requests
import streamlit as st
from streamlit_lottie import st_lottie

#  Find emoji https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Home", page_icon=":warning:", layout="wide")

def load_lottieurl(url):
    r =requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown (f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("Css/style.css")

#Loading
lottie_coding= load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_pjagkisd.json")



with st.container():
    st.header("Hi, Im penny")
    st.title("bla")
    st.write("[Let's start >](https://www.webfx.com/tools/emoji-cheat-sheet/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What do I want to test")
        st.write("##")
        st.write(
            """"
            At here am testing what am going to learn about Python 
            Hope I can creat my own website here 
            """
        )
        st.write("[Youtube channel >](https::/www.youtube.come)")
    with right_column:
        st_lottie(lottie_coding, height="300", key="coding")
        
with st.container():
    st.write("---")