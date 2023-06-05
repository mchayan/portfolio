import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.graph_objects as go


st.set_page_config(page_title="Manoj Roy", page_icon=":running:", layout="wide")


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

# ---- Header ----
with st.container():
    st.subheader("Hi, I am Manoj Roy :wave:")
    st.title("A Data Enthusiast & Researcher")
    st.write("##")
    st.markdown(
        """
        <div class="newspaper">
            <p class="first-letter">A</p> highly motivated and detail-oriented researcher with an M.Sc. in Applied Statistics and
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

# ---- What I do ----
# Data for the pie chart
labels = ["Proactive Learner", "Problem Solver", "Explorer"]
values = [1, 1, 1]  # You can modify these values based on your preference

# Creating the pie chart figure
fig = go.Figure(
    data=go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        textinfo="label+percent",
        marker=dict(
            colors=["#0080ff", "#ff0080", "#00ff80"],
            line=dict(color="#000000", width=2),
        ),
        hovertemplate="<b>%{label}</b><br>%{percent}",
        sort=False,
    )
)

# Customizing the layout
fig.update_layout(
    title="What I Do",
    title_font=dict(color="white"),
    paper_bgcolor="rgba(0, 0, 0, 0)",
    plot_bgcolor="rgba(0, 0, 0, 0)",
    showlegend=True,
    legend=dict(
        title="Activities",
        title_font=dict(color="white"),
        font=dict(color="white"),
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="right",
        x=0.9,
    ),
)

# Layout the page with two columns
col1, col2 = st.columns(2)

# Column 1 - What I do content (Pie Chart)
with col1:
    st.plotly_chart(fig, use_container_width=True)

# Column 2 - Lottie Animation
with col2:
    st_lottie(lottie_coding, height=200, key="coding")
# ---- What I do ----

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

# Column 2 - GraphLottie
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
