import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts
import plotly.graph_objects as go
import folium
from folium.plugins import AntPath
from geopy.distance import geodesic
import datetime
import pytz
from timezonefinder import TimezoneFinder

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
    def fetch_user_location():
        try:
            response = requests.get("https://geolocation-db.com/json/")
            data = response.json()
            user_lat = data["latitude"]
            user_lon = data["longitude"]
            return (user_lat, user_lon)
        except:
            return None

    def calculate_distance(user_location):
        # Coordinates of Dhaka, Bangladesh
        dhaka_coords = (23.8790605, 90.26904660000002)
        
        # Calculate the distance between Dhaka and the user location
        distance = geodesic(dhaka_coords, user_location).kilometers
        
        return distance

    def get_weather_info(user_location):
        api_key = "2055637430b846240fc64490fab81407"  # Replace with your OpenWeatherMap API key
        lat, lon = user_location
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        
        if "weather" in data:
            weather_description = data["weather"][0]["description"]
        else:
            weather_description = "N/A"
        
        if "main" in data:
            temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        else:
            temperature = None
        
        return weather_description, temperature

    def get_greeting(user_timezone):
        timezone = pytz.timezone(user_timezone)
        
        current_time = datetime.datetime.now(timezone)
        current_hour = current_time.hour
        
        if 5 <= current_hour < 12:
            return "Good Morning"
        elif 12 <= current_hour < 17:
            return "Good Afternoon"
        else:
            return "Good Evening"

    def get_user_timezone(user_location):
        tf = TimezoneFinder()
        timezone = tf.timezone_at(lng=user_location[1], lat=user_location[0])
        return timezone

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

    # st.markdown('<div class="title">Welcome!</div>', unsafe_allow_html=True)

    # Greetings Message
    user_location = fetch_user_location()
    if user_location:
        user_timezone = get_user_timezone(user_location)
        if user_timezone:
            greeting = get_greeting(user_timezone)
            st.write(f"🌞 {greeting}!")
        else:
            st.warning("Timezone information not available")
    else:
        st.warning("📍 Your location can't be detected automatically. Please enter your location.")

    st.markdown('<div class="header">Your Location</div>', unsafe_allow_html=True)
    if user_location is not None:
        user_lat, user_lon = user_location
        st.write(f"🌍 Probably you are Here 📍: (Lat: {user_lat:.6f}, Lon: {user_lon:.6f})")
    else:
        st.warning("📍 Your Location can't be detected automatically. Please enter your location.")
        user_lat = st.number_input("Latitude:")
        user_lon = st.number_input("Longitude:")

    user_location = (user_lat, user_lon)

    st.markdown('<div class="header">And the weather near you is ..</div>', unsafe_allow_html=True)
    weather_description, temperature = get_weather_info(user_location)

    if temperature is not None:
        st.write(f"🌤️ Weather Update: {weather_description}")
        st.write(f"🌡️ Temperature Update: {temperature:.2f} °C")
    else:
        st.warning("Weather information not available")

    st.markdown('<div class="header"></div>', unsafe_allow_html=True)
    map = folium.Map(location=[23.8790605, 90.26904660000002], zoom_start=10)

    # Marker for Dhaka, Bangladesh
    folium.Marker(location=[23.8790605, 90.26904660000002], popup=folium.Popup("🌍 Hey! Here I am!", max_width=250), 
                  icon=folium.Icon(icon="cloud", prefix="fa", color="red")).add_to(map)

    if user_lat != 0 and user_lon != 0:
        # Marker for user's location
        folium.Marker(location=user_location, popup=folium.Popup("📍 Probably You are Here!", max_width=250), 
                      icon=folium.Icon(icon="user", prefix="fa", color="green")).add_to(map)

        # Create a curved line between Dhaka and user's location
        line = [(23.8790605, 90.26904660000002), user_location]
        ant_path = AntPath(line, delay=1000, dash_array=[10, 20], color='blue', curvature=50)
        ant_path.add_to(map)

    st.components.v1.html(map._repr_html_(), height=800)

    st.markdown('<div class="header">Distance Calculation</div>', unsafe_allow_html=True)
    distance = calculate_distance(user_location)
    distance_text = f'<span style="font-size: 24px; color: #00FFFF;">{distance:.2f} km</span>'
    st.write(f"🛰️ The distance between Me and You is around: {distance_text}", unsafe_allow_html=True)

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
