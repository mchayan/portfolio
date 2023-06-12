import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts
import plotly.graph_objects as go
from folium.plugins import AntPath
from math import radians, sin, cos, sqrt, atan2
import folium
from streamlit_folium import folium_static
from math import radians, sin, cos, sqrt, atan2


st.set_page_config(page_title="Manoj Roy", page_icon=":running:", layout="wide")

def home_page():
    # Home page content
    # st.title("Home Page")
    # st.write("Welcome to the Home Page!")

    # Helping Function
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

    # ---- Research ----
    with st.container():
        st.write("____")
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
                    
                        Reference Link : [Book Link](https://www.routledge.com/.../Ari.../p/book/9780367742515?fbclid=IwAR0OG4UnZNPur9o3m-h36jUewGDhsKBLmdKBWDhcVaXmav9nJD8sKH-4j_4)
                    
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    
            with tab2:
                st.markdown(
                    """
                    <div class="stMarkdownContainer">
                        Student paper published at the 17th International Conference on Computer and Information Technology (ICCIT) 2014
                    
                        Title : Online Medication
                    
                        Abstract : Proper medication is a very common need of daily life. With the improvement of 
                        modern medical science, the maintenance cost of medication has also increased in the same 
                        way. For this, it is becoming a common problem for the citizens of undeveloped countries 
                        to maintain a balanced health care system. This paper highlights the basic need for an 
                        online medication system from the perspective of these undeveloped countries.
                    
                        Reference Link : [Conference Link](www.iccit.org.bd/2014/student-conference-iccit-2014)
                    
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

    # ---- Research ----

    # ---- Footer ----
    st.markdown(
        """
        <div class="footer" style="text-align: center; padding-top: 30px;">
            <p class="made-by">Made with ❤️ in <img class="flag" src="https://avatars3.githubusercontent.com/u/45109972?s=400&v=4" style="width: 18px; height: 18px; vertical-align: middle;"> by
            <a class="author" href="https://www.tumblr.com/blog/mchayan" target="_blank">@mchayan</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    # ---- Footer ----


def contact_page():
    def get_weather(lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=2055637430b846240fc64490fab81407&units=metric"
        response = requests.get(url)
        data = response.json()
        return data

    def get_country_name(lat, lon):
        url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}"
        response = requests.get(url)
        data = response.json()
        try:
            country = data["address"]["country"]
        except KeyError:
            country = "Unknown"
        return country

    # Function to calculate the distance between two sets of coordinates using the Haversine formula
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers

        # Convert latitude and longitude to radians
        lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance
    
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            color: #336699;
            padding: 20px 0;
            text-align: center;
            font-weight: bold;
        }
        .header {
            font-size: 24px;
            color: #336699;
            padding: 10px 0;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Streamlit app code
    st.title("Let's Get Introduced!")
    st.markdown("## Please let me know Your Location !")

    # Check if geolocation is supported
    if "geolocation" in st.session_state:
        lat = st.session_state.geolocation["latitude"]
        lon = st.session_state.geolocation["longitude"]
        geolocation_supported = True
    else:
        # Geolocation is not supported, provide manual input
        st.warning("Geolocation is not supported by your browser. To Continue Please provide the Latitude & Longitude manually.")
        lat = st.number_input("Latitude:", format="%.6f")
        lon = st.number_input("Longitude:", format="%.6f")
        geolocation_supported = False

    if st.button("Continue >"):
        # Get weather information based on location
        weather_data = get_weather(lat, lon)
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]

        # Display location information
        st.subheader("🌍 Location Information")
        st.markdown('<div class="header">Your Location</div>', unsafe_allow_html=True)
        country = get_country_name(lat, lon)
        st.write(f"🏴 Country: {country}")
        st.write(f"📍 Latitude: {lat}")
        st.write(f"📍 Longitude: {lon}")

        # Display weather information
        st.subheader("🌤️ Weather Information")
        st.markdown('<div class="header">Weather Near You!</div>', unsafe_allow_html=True)
        st.write(f"⊸ Description: {weather_description}")
        st.write(f"🌡️Temperature: {temperature}°C")

        # Calculate distance based on location (sample calculation using coordinates)
        if geolocation_supported:
            distance = calculate_distance(lat, lon, 23.7276, 90.3718)
            st.markdown("Distance")
            st.write(f"The probable distance between You and Me is {distance} km")
        else:
            st.warning("Distance calculation requires geolocation support.")
            distance_manual = calculate_distance(lat, lon, 23.7276, 90.3718)
            st.write(f"The probable distance between You and Me is is {distance_manual} km")

        # Create map with markers
        m = folium.Map(location=[lat, lon], zoom_start=14)

        # Add marker for visitor's location
        folium.Marker(
            location=[lat, lon],
            popup="Probably You are Here!",
            icon=folium.Icon(color="blue", icon="cloud")
        ).add_to(m)

        # Add marker for My Location with custom icon
        folium.Marker(
            location=[23.7276, 90.3718],
            popup="Hey! Here I am!",
            icon=folium.Icon(color="green", icon="university")
        ).add_to(m)

        # Add ant path line between the two locations
        locations = [[lat, lon], [23.7276, 90.3718]]
        ant_path = AntPath(
            locations=locations,
            color="green",
            weight=8,
            delay=1000,
            dash_array=[15, 20]
        ).add_to(m)

        # Display the map
        folium_static(m)

    # ---- Expandable ----
    # Create an expander section
    with st.expander("Wanna Get Connected??"):
        # Add content inside the expander
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


            
    # ---- Expandable ----
    # ---- Footer ----
    st.markdown(
        """
        <div class="footer" style="text-align: center; padding-top: 30px;">
            <p class="made-by">Made with ❤️ in <img class="flag" src="https://avatars3.githubusercontent.com/u/45109972?s=400&v=4" style="width: 18px; height: 18px; vertical-align: middle;"> by
            <a class="author" href="https://www.tumblr.com/blog/mchayan" target="_blank">@mchayan</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    # ---- Footer ----


def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Contact"])

    if page == "Home":
        home_page()
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
