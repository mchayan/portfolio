import requests
import streamlit as st
from streamlit_lottie import st_lottie
#pip install streamlit-lottie

st.set_page_config(page_title="Manoj Roy", page_icon=":running:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_WdTEui.json")
lottie_research = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_inviljje.json")
lottie_project = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_NxzTQeH77d.json")


# ---- Header ----

with st.container():
    st.subheader("Hi, I am Manoj Roy :wave:")
    st.title("A Data Enthusiast & Researcher")
    st.write()

# ---- What I do ----
with st.container():
    st.write("____")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - A proactive Learner
            - Problem Solver
            - Explorer
                        
            """

        )
    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")


# ---- Research ----
with st.container():
    st.write("_ _ _ _")
    st.header("Research")
    st.write("##")
    image_column, text_column = st.columns((2))
    with text_column:
        st.subheader("")
        st.subheader("")
        st.write(
        
        """
        
        """
        )
        
        
        
        
        # tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
        # tab1.write("this is tab 1")
        # tab1.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
        # tab2.write("this is tab 2")
    with image_column:
        st_lottie(lottie_research, height=200, key="research")


# ---- Projects ----
with st.container():
    st.write("____")
    st.header("My Projects")
    st.write("##")
    text_column, image_column = st.columns((2))
    with image_column:
        st_lottie(lottie_project, height=200, key="project")
    with text_column:
        st.subheader("")
        st.write(
        
        """
        
        """
        )

    # with st.expander("More"):
    #     st.write("""
    #         The chart above shows some numbers I picked for you.
    #         I rolled actual dice for these, so they're *guaranteed* to
    #         be random.
    #     """)
    #     st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


