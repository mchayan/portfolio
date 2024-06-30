import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts

def streamlit_js_eval(js_expressions, key=None, **kwargs):
    import json
    import random
    import string

    def random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    if key is None:
        key = random_string(10)

    if not isinstance(js_expressions, list):
        js_expressions = [js_expressions]

    js_expressions_str = json.dumps(js_expressions)
    st.components.v1.html(
        f"""
        <script>
        const js_expressions = {js_expressions_str};
        const results = js_expressions.map(js_expression => eval(js_expression));
        const key = '{key}';
        window.parent.postMessage({{
            type: 'streamlit:setComponentValue',
            value: results,
            key: key
        }}, '*');
        </script>
        """,
        height=0,
        width=0
    )

    return st.empty()

st.set_page_config(page_title="Manoj Roy", page_icon=":running:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.8rem;
        margin-bottom: 2rem;
    }
    .intro-text {
        font-family: 'Georgia', serif;
        font-size: 16px;
        line-height: 1.6;
        text-align: justify;
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
    }
    .first-letter {
        font-size: 48px;
        font-weight: bold;
        color: #333333;
        margin: 0;
        padding-right: 10px;
        float: left;
    }
    .quote {
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 16px;
        line-height: 1.6;
        text-align: center;
        margin-top: 1rem;
    }
    .highlight {
        color: #00CED1; /* Dark Turquoise */
        font-weight: bold;
    }
    .menu {
        list-style-type: none;
        padding: 0;
        overflow: hidden;
        background-color: #333;
        margin-bottom: 2rem;
    }
    .menu li {
        float: left;
    }
    .menu li a {
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
        transition: background-color 0.3s;
    }
    .menu li a:hover {
        background-color: #111;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_nightingale_rose_diagram():
    option = {
        "legend": {"top": "bottom"},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": False},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "series": [
            {
                "name": "My Skills",
                "type": "pie",
                "radius": [50, 200],
                "center": ["50%", "50%"],
                "roseType": "area",
                "itemStyle": {"borderRadius": 8},
                "data": [
                    {"value": 335, "name": "Statistical"},
                    {"value": 310, "name": "Technical"},
                    {"value": 274, "name": "Proactive Learning"},
                    {"value": 235, "name": "Problem Solving"},
                    {"value": 400, "name": "Exploring"},
                ],
            }
        ],
    }
    return option

def home_page():
    # Header Section
    st.markdown('<h1 class="main-title">Hi, I am Manoj Roy 👋</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">Data Enthusiast & Researcher</h2>', unsafe_allow_html=True)

    # Introduction
    st.markdown(
        """
        <div class="intro-text">
        <p><span class="first-letter">A</span> dedicated data enthusiast with a Master's in Applied Statistics and Data Science, I am passionately pursuing knowledge in quantum machine learning. My strong foundation in statistics and classical ML algorithms fuels my curiosity to explore how quantum computing can revolutionize model performance. I'm actively learning to develop hybrid quantum-classical algorithms and optimize quantum feature maps, aiming to contribute to breakthroughs in ML efficiency and accuracy.</p>
        
        <p>As an eager learner and collaborator, I'm excited to bridge my statistical expertise with emerging quantum technologies. I'm committed to growing in this cutting-edge field, aspiring to participate in innovative research and real-world applications that harness quantum advantages in machine learning.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Skills Section
    left_column, right_column = st.columns([2, 1])

    with left_column:
        st_echarts(options=render_nightingale_rose_diagram(), height="600px")

    with right_column:
        lottie_skills = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ul35wckt.json")
        if lottie_skills:
            st_lottie(lottie_skills, speed=1, width=300, height=300)
        
        st.markdown(
            """
            <div class="quote">
                "If the statistics are boring, you've got the <span class="highlight">wrong numbers</span>."<br>
                — Edward <span class="highlight">Tufte</span>
            </div>
            """,
            unsafe_allow_html=True
        )

def education_and_skills():
    st.header("Education and Skills")
    # Add content for education and skills

def research():
    st.header("Research")
    # Add content for research

def experience():
    st.header("Experience")
    # Add content for experience

def projects_and_publications():
    st.header("Projects and Publications")
    # Add content for projects and publications

def contact():
    st.header("Contact")
    # Add content for contact

def main():
    # Header Menu
    st.markdown("""
    <ul class="menu">
        <li><a href="#" onclick="handle_click('Home'); return false;">Home</a></li>
        <li><a href="#" onclick="handle_click('Education and Skills'); return false;">Education and Skills</a></li>
        <li><a href="#" onclick="handle_click('Research'); return false;">Research</a></li>
        <li><a href="#" onclick="handle_click('Experience'); return false;">Experience</a></li>
        <li><a href="#" onclick="handle_click('Projects and Publications'); return false;">Projects and Publications</a></li>
        <li><a href="#" onclick="handle_click('Contact'); return false;">Contact</a></li>
    </ul>
    """, unsafe_allow_html=True)

    # JavaScript to handle menu clicks
    st.markdown("""
    <script>
    function handle_click(page) {
        window.parent.postMessage({type: 'streamlit:setComponentValue', value: page}, '*');
    }
    </script>
    """, unsafe_allow_html=True)

    # Navigation state
    if 'nav' not in st.session_state:
        st.session_state.nav = 'Home'

    # Handle navigation
    nav = st.session_state.nav

    if nav == "Home":
        home_page()
    elif nav == "Education and Skills":
        education_and_skills()
    elif nav == "Research":
        research()
    elif nav == "Experience":
        experience()
    elif nav == "Projects and Publications":
        projects_and_publications()
    elif nav == "Contact":
        contact()

    # Update navigation state based on component value
    nav = st.experimental_get_query_params().get('nav', ['Home'])[0]
    st.session_state.nav = nav

if __name__ == "__main__":
    main()
