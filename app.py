import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts
import plotly.graph_objects as go

#Configuration
st.set_page_config(page_title="Manoj Roy", page_icon=":running:", layout="wide")

#Helping Function
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_education = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_30dyzzax.json"
)
lottie_coding = load_lottieurl(
    "https://assets8.lottiefiles.com/private_files/lf30_WdTEui.json"
)
lottie_research = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_inviljje.json"
)
lottie_project = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_NxzTQeH77d.json"
)

lottie_skills = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_ul35wckt.json"
)

# ---- Header ----
with st.container():
    st.subheader("Hi, I am Manoj Roy :wave:")
    st.title("Data Enthusiast & Researcher")
    st.write("##")
    st.markdown(
        """
        <div class="newspaper">
            <p class="first-letter">A</p> highly motivated and detail-oriented researcher with an Masters in Applied Statistics and
            Data Science, possessing a strong background in statistics and data analysis. Passionate about
            public health and epidemiology, with a keen interest in understanding the spread and control
            of infectious diseases, committed to improving health outcomes in communities. A natural
            collaborator with excellent communication skills, confident in the ability to work effectively
            with multidisciplinary research teams and engage with stakeholders from diverse
            backgrounds. Committed to continuous learning and professional development, excited
            about opportunities in a career as a researcher in epidemiology.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
        .newspaper {
            font-family: 'Georgia', serif;
            font-size: 16px;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 700px;
            padding: 20px;
            text-align: justify;
        }
        
        .first-letter {
            font-size: 48px;
            font-weight: bold;
            color: #333333;
            margin: 0;
            padding-right: 10px;
            float: left;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# ---- Header ----

# ---- What I Do & Skills----
with st.container():
    # st.write("____")
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.header("")
        # st.write("##")

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
    st_echarts(
        options=option, height="600px",
    )

# Create two columns layout
left_column, right_column = st.columns([2, 1])

# Display the Nightingale Rose Diagram in the first column
with left_column:
    render_nightingale_rose_diagram()

# Display the skills animation in the second column
with right_column:
    st_lottie(lottie_skills, speed=1, width=300, height=300)
    st.markdown(
        """
        <style>
            .newspaper {
                font-family: 'Georgia', serif;
                font-size: 16px;
                line-height: 1.6;
                margin: 0 auto;
                max-width: 700px;
                padding: 20px;
                text-align: justify;
                color: white; /* Set the text color to white */
            }
            
            .first-letter {
                font-size: 48px;
                font-weight: bold;
                color: #333333;
                margin: 0;
                padding-right: 10px;
                float: left;
            }
            
            .colored-span {
                color: red;
            }
        </style>
        <div class="newspaper">
            "If the statistics are boring, you’ve got the <span class="colored-span">wrong numbers</span>."<br>
            — Edward <span class="colored-span">Tufte</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---- What I Do & Skills----

# # ---- Expandable ----
# # Create an expander section
# with st.expander("My Skills"):
#     # Add content inside the expander
#     st.write("")

#     # Add a button to open the other Streamlit Python file
#     if st.button("Open"):
#         # Get the path to the other Streamlit Python file
#         file_path = "./footer.py"
#         # Launch the other Streamlit Python file using subprocess
#         subprocess.run(["streamlit", "run", file_path])
        
# # ---- Expandable ----   
        
# ---- Education ----
with st.container():
    st.write("____")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education")
        st.write("##")


def create_line_graph():
    # Data for the graph
    education_levels = ["Secondary", "Higher Secondary", "B.Sc.", "MS"]
    years = [2010, 2012, 2018, 2022]
    institutes = [
        "Dinajpur Zilla School",
        "Dinajpur Govt. College",
        "Daffodil International University",
        "Jahangirnagar University",
    ]
    degrees = [
        "SSC",
        "HSC",
        "B.Sc. in Computer Science and Engineering",
        "Masters in Applied Statistics and Data Science",
    ]

    # Creating the line graph figure
    fig = go.Figure()

    # Add the line trace
    fig.add_trace(
        go.Scatter(
            x=years,
            y=education_levels,
            mode="lines",
            line=dict(color="white", width=6, dash="dashdot"),
        )
    )

    # Add the marker symbols at the specified points
    for year, level, institute, degree in zip(
        years, education_levels, institutes, degrees
    ):
        if year in [2010, 2012, 2018, 2022]:
            fig.add_trace(
                go.Scatter(
                    x=[year],
                    y=[level],
                    mode="markers",
                    marker=dict(symbol="square-x", size=12, color="white"),
                    hovertemplate="<b>%{text}</b><extra></extra>",
                    text=[f"{institute}<br>Degree Obtained: {degree}"],
                )
            )

    # Customizing the graph
    fig.update_layout(
        title="Education Progression",
        xaxis_title="Year of Graduation",
        yaxis_title="Level of Education",
        template="plotly_dark",
        font=dict(color="white"),
        showlegend=False,
    )

    # Displaying the graph in Streamlit
    st.plotly_chart(fig, use_container_width=True)


# Layout the page with two columns
col1, col2 = st.columns([1, 2])

# Column 1 -  Animation
with col1:
    st_lottie(lottie_education, height=200, key="education")

# Column 2 - Graph
with col2:
    create_line_graph()
# ---- Education ----

# # ---- Research ----
with st.container():
    st.write("_ _ _ _")
    st.header("Research")
    st.write("##")
    text_column, image_column = st.columns((2))
    with text_column:
        tab1, tab2 = st.tabs(["1", "2"])
        with tab1:
            st.markdown(
                """
                <div class="stMarkdownContainer">
                    
                    Chapter Title : Computer Vision-Based Street Width Measurement for Urban Aesthetics Identification

                    ISBN : 9780367742515

                    Abstract : This paper presents a computer-vision-based Street-Width measurement system 
                    for Urban Aesthetics identification. In this system, the image is captured using a digital 
                    camera. In the preprocessing section, the image is scaled in high to low resolution. The 
                    method used to identify the object is contour tracing and canny edge detection algorithm. 
                    Then the object is measured by generalizing the pixel mapping. Finally, the finding output 
                    is matched with the Standard Street Measurement. The measurement findings in this 
                    proposed methodology were then analyzed and based on some criteria the street aesthetics 
                    of Dhaka city was provided.

                    Reference Link : https://www.routledge.com/.../Ari.../p/book/9780367742515?fbclid=IwAR0OG4UnZNPur9o3m-h36jUewGDhsKBLmdKBWDhcVaXmav9nJD8sKH-4j_4
                    
                </div>
                """,
                unsafe_allow_html=True
            )

        with tab2:
            st.markdown(
                """
                <div class="stMarkdownContainer">
                
                    
                    Student paper published at the 17th _International Conference on Computer and Information Technology (ICCIT) 2014_

                    Title : Online Medication

                    Abstract : Proper medication is a very common need of daily life. With the improvement of 
                    modern medical science, the maintenance cost of medication has also increased in the same 
                    way. For this, it is becoming a common problem for the citizens of undeveloped countries 
                    to maintain a balanced health care system. This paper highlights the basic need for an 
                    online medication system from the perspective of these undeveloped countries.

                    Reference Link : www.iccit.org.bd/2014/student-conference-iccit-2014
                    
                </div>
                """,
                unsafe_allow_html=True
            )
    with image_column:
        st_lottie(lottie_research, height=200, key="research")

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 2rem;
        font-family: Georgia, serif;
        text-align: justify;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)
# # ---- Research ----

# ---- Projects ----
# with st.container():
#     st.write("____")
#     st.header("Projects")
#     st.write("##")
#     text_column, image_column = st.columns((2))
#     with image_column:
#         st_lottie(lottie_project, height=200, key="project")
#     with text_column:
#         st.subheader("")
#         st.write(
#             """
        
#         """
#         )

    # with st.expander("More"):
    #     st.write("""
    #         The chart above shows some numbers I picked for you.
    #         I rolled actual dice for these, so they're *guaranteed* to
    #         be random.
    #     """)
    #     st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# ---- Projects ----

# ---- Footer ----
st.markdown("---")
st.header("Connect with Me")
st.write("##")

# Contact information
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        <a href="mailto:manoj4292@diu.edu.bd">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div class="contact-icon">
                <i class="fa fa-envelope" aria-hidden="true"></i>
                <span>manoj4292@diu.edu.bd</span>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href="https://github.com/mchayan">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div class="contact-icon">
                <i class="fab fa-github"></i>
                <span>https://github.com/mchayan</span>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

# Add spacing between col1 and col2
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            background-color: #f8f8f8;
            padding: 20px;
            border-radius: 25px;
            background-image: linear-gradient(to right, #00B4DBe , #0083B0);
        }
        
        .footer .made-by {
            font-size: 16px;
            margin-bottom: 0px;
            color: #555555;
        }
        
        .footer .flag {
            width: 25px;
            height: 25px;
            vertical-align: middle;
        }
        
        .footer .author {
            font-weight: bold;
            color: #0366d6;
            text-decoration: none;
        }
        
        .footer .coffee {
            width: 100px;
            height: auto;
            display: block;
            margin: 20px auto;
        }
        
        /* Add center alignment and margin for col1 and col2 */
        .contact-icon {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }
        
        /* Adjust font size and vertical alignment of font-awesome icons */
        .contact-icon i {
            font-size: 18px;
            margin-right: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="footer">
        <p class="made-by">Made with ❤️ in <img class="flag" src="https://avatars3.githubusercontent.com/u/45109972?s=400&v=4"> by
        <a class="author" href="https://www.tumblr.com/blog/mchayan" target="_blank">@mchayan</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
# ---- Footer ----







