import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts

st.set_page_config(page_title="Manoj Roy | Academic Portfolio", page_icon="📊", layout="wide")

# Custom CSS for styling and mobile responsiveness
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem 2rem;
    }
    .main-title {
        font-size: 3.2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .sub-title {
        font-size: 1.6rem;
        color: #555555;
        margin-bottom: 1.8rem;
    }
    .intro-text {
        font-family: 'Georgia', serif;
        font-size: 16px;
        line-height: 1.7;
        text-align: justify;
        max-width: 760px;
        margin: 0 auto 1.5rem auto;
        padding: 20px;
    }
    .first-letter {
        font-size: 48px;
        font-weight: bold;
        color: #333333;
        margin: 0;
        padding-right: 12px;
        float: left;
        line-height: 1;
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
        color: #00CED1;
        font-weight: bold;
    }
    
    /* Responsive Top Navigation Bar */
    .menu {
        list-style-type: none;
        padding: 0;
        margin: 0 0 2rem 0;
        background-color: #333333;
        border-radius: 6px;
        display: flex;
        flex-wrap: wrap;
        overflow: hidden;
    }
    .menu li {
        flex: 1 1 auto;
    }
    .menu li a {
        display: block;
        color: white !important;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none !important;
        font-size: 0.95rem;
        transition: background-color 0.3s;
    }
    .menu li a:hover {
        background-color: #111111;
    }
    .menu li a.active {
        background-color: #008B8B;
        font-weight: 600;
    }

    /* Clean Academic Cards */
    .cv-card {
        background-color: #ffffff;
        border-left: 4px solid #008B8B;
        border-radius: 4px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
    }
    .cv-card-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 0.3rem;
    }
    .cv-card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #222222;
        margin: 0;
    }
    .cv-card-date {
        font-size: 0.9rem;
        color: #666666;
        font-weight: 500;
        white-space: nowrap;
    }
    .cv-card-subtitle {
        font-size: 0.95rem;
        color: #006666;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    .cv-card-body {
        font-size: 0.95rem;
        color: #333333;
        line-height: 1.6;
        margin: 0;
    }
    .skill-badge {
        display: inline-block;
        background-color: #f0f4f8;
        color: #2c3e50;
        padding: 4px 10px;
        margin: 3px 4px 3px 0;
        border-radius: 4px;
        font-size: 0.88rem;
        border: 1px solid #dce4ec;
    }

    /* Mobile Adjustments */
    @media (max-width: 768px) {
        .stApp {
            padding: 0.5rem 1rem;
        }
        .main-title {
            font-size: 2.2rem;
        }
        .sub-title {
            font-size: 1.25rem;
        }
        .intro-text {
            padding: 10px 5px;
            font-size: 15px;
        }
        .menu li {
            flex: 1 1 50%;
        }
        .menu li a {
            padding: 10px 8px;
            font-size: 0.85rem;
        }
        .cv-card-header {
            flex-direction: column;
            gap: 0.1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None


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
                "radius": ["15%", "65%"],
                "center": ["50%", "45%"],
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


def render_card(title, subtitle, date, body, tools=None, link=None):
    title_html = f'<a href="{link}" target="_blank" style="color: #222222; text-decoration: underline;">{title}</a>' if link else title
    subtitle_html = f'<div class="cv-card-subtitle">{subtitle}</div>' if subtitle else ""
    tools_html = f'<div style="margin-top: 0.4rem; font-size: 0.88rem; color: #555;"><strong>Tools:</strong> {tools}</div>' if tools else ""
    body_html = f'<p class="cv-card-body">{body}</p>' if body else ""

    st.markdown(f"""
        <div class="cv-card">
            <div class="cv-card-header">
                <div class="cv-card-title">{title_html}</div>
                <div class="cv-card-date">{date}</div>
            </div>
            {subtitle_html}
            {body_html}
            {tools_html}
        </div>
    """, unsafe_allow_html=True)


def home_page():
    st.markdown('<h1 class="main-title">Hi, I am Manoj Roy 👋</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">Data Enthusiast & Researcher</h2>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="intro-text">
        <p><span class="first-letter">A</span> dedicated data enthusiast with a Master's in Applied Statistics and Data Science, I am passionately pursuing knowledge in statistical modeling, deep learning, and quantum machine learning. My foundation in statistics and classical ML algorithms fuels my curiosity to explore how emerging methods—from evidential uncertainty quantification to quantum computing fundamentals—can improve model reliability under challenging conditions.</p>
        
        <p>As an eager learner and collaborator, I enjoy bridging statistical thinking with practical problem solving. Whether working on multi-resolution indoor localization, 3D computer vision, or guiding students in data analysis, I am committed to learning continuously and contributing humbly to meaningful research.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    left_column, right_column = st.columns([2, 1])

    with left_column:
        st_echarts(options=render_nightingale_rose_diagram(), height="500px")

    with right_column:
        lottie_skills = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ul35wckt.json")
        if lottie_skills:
            st_lottie(lottie_skills, speed=1, height=280)

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
    st.header("Education & Skills")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🎓 Education")
        render_card(
            title="M.Sc. in Applied Statistics and Data Science",
            subtitle="Jahangirnagar University",
            date="2021 – 2022",
            body="CGPA: 3.77 / 4.00"
        )
        render_card(
            title="B.Sc. in Computer Science and Engineering",
            subtitle="Daffodil International University",
            date="2014 – 2018",
            body="CGPA: 3.58 / 4.00"
        )

        st.subheader("🛠️ Technical & Research Skills")
        skills_data = {
            "Statistical Analysis & ML": [
                "Applied Statistics", "Deep Learning", "Computer Vision",
                "Predictive Modeling", "Feature Engineering", "Quantitative Problem Solving"
            ],
            "Programming Languages": ["Python", "R", "SQL", "Java"],
            "Data Science & AI Frameworks": [
                "PyTorch", "OpenMMLab", "OpenCV", "Scikit-learn", "Pandas", "NumPy"
            ],
            "Data Visualization & BI": ["Power BI", "Tableau", "Matplotlib", "Seaborn"],
            "Research & Development Tools": [
                "LaTeX", "Git", "Docker", "Linux (Ubuntu/WSL2)",
                "Android Studio", "Unity", "Kobo Toolbox", "Survey Solutions"
            ],
        }

        for category, items in skills_data.items():
            badges = "".join([f'<span class="skill-badge">{item}</span>' for item in items])
            st.markdown(f"**{category}**<div>{badges}</div><br>", unsafe_allow_html=True)

    with col2:
        st.subheader("📜 Selected Certifications")
        certifications = [
            ("Data Analysis and Interpretation", "Wesleyan University", "2020", "https://www.coursera.org/account/accomplishments/specialization/Z2J48LBUJU4M"),
            ("Applied Data Science with Python", "University of Michigan", "2020", "https://www.coursera.org/account/accomplishments/specialization/WXFWX2AD54NL"),
            ("Data Mining", "University of Illinois Urbana-Champaign", "2020", "https://www.coursera.org/account/accomplishments/specialization/RZUALYJXPFSL"),
            ("Advanced Statistics for Data Science", "Johns Hopkins University", "2020", "https://www.coursera.org/account/accomplishments/specialization/67T7GMUPVKN2"),
            ("Project Management & Other Tools", "University of Illinois", "2020", "https://www.coursera.org/account/accomplishments/specialization/Y62UBR8DUFQD"),
            ("Advanced App Development in Android", "Imperial College London", "2020", "https://www.coursera.org/account/accomplishments/specialization/P44V2WAMEB89"),
            ("Data Science", "Johns Hopkins University", "2020", "https://www.coursera.org/account/accomplishments/specialization/P6TKC6X4H6GE"),
            ("Machine Learning", "University of Washington", "2020", "https://www.coursera.org/account/accomplishments/specialization/BV9CYHFR8APV"),
            ("Deep Learning", "DeepLearning.AI", "2020", "https://www.coursera.org/account/accomplishments/specialization/25TEG2MDQ2ZA"),
        ]
        for title, org, year, url in certifications:
            st.markdown(f"- **[{title}]({url})** | {org} *({year})*")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🔬 Training & Workshops")
        render_card(
            title="QBronze Quantum Computing",
            subtitle="QWorld (Quantum Computing & Programming using Qiskit)",
            date="Feb 2024",
            body=""
        )
        render_card(
            title="Top-Up IT Training (Android)",
            subtitle="Bangladesh Computer Council (LICT)",
            date="2017",
            body=""
        )
        render_card(
            title="National Mobile Apps Trainer",
            subtitle="ICT Division, Gov. of Bangladesh",
            date="2015",
            body=""
        )


def research():
    st.header("Academic Research")

    render_card(
        title="Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift",
        subtitle="Role: Co-Researcher | Accepted at Journal of Physics: Conference Series (ISAS 2026 Challenge — Champion, 1st of 37 Teams)",
        date="2026",
        body=(
            "Proposed a multi-resolution framework utilizing Random Forest and XGBoost to study BLE signal loss, "
            "class imbalance, and temporal shift in a care facility setting. Explored fold-local signal-pattern "
            "augmentation and probability fusion, which helped improve minority-class recovery and strict "
            "forward-protocol accuracy."
        )
    )

    render_card(
        title="Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction",
        subtitle="Role: Co-Researcher | Accepted at IEEE EAEEIE 2026 & WiML Symposium @ ICML 2026",
        date="2026",
        body=(
            "Investigated structural vulnerabilities of 2D convolutional backbones in vision-centric 3D semantic "
            "occupancy prediction under environmental anomalies (e.g., motion blur, snow). Participated in introducing "
            "an Evidential Feature Gate (EFG) grounded in Dirichlet subjective logic to help quantify epistemic "
            "uncertainty and suppress corrupted spatial inputs. The approach maintained clean-weather semantic "
            "accuracy while offering improved robustness under severe conditions."
        )
    )

    render_card(
        title="Machine Learning Based Feature Engineering for Identifying The Causes Of Divorce",
        subtitle="Role: Graduate Researcher | M.Sc. Dissertation, Statistics & Data Science, Jahangirnagar University",
        date="Jun – Dec 2022",
        body=(
            "Analyzed behavioral and communication factors related to divorce using a dataset curated by field "
            "specialists. Applied feature engineering methods, including Recursive Feature Elimination (RFE) and "
            "Shapley Additive Explanations (SHAP), to study influential variables. Used t-SNE for dimensionality "
            "reduction and evaluated the predictive models using 5-fold cross-validation."
        ),
        tools="Python (Pandas, NumPy, Scikit-learn, SHAP), t-SNE, Matplotlib"
    )

    render_card(
        title="Computer Vision-based Street-width Measurement for Urban Aesthetics Identification",
        subtitle="Role: Undergraduate Researcher | B.Sc. Dissertation, Dept. of CSE, Daffodil International University",
        date="Nov 2017 – Jul 2018",
        body=(
            "Applied a computer vision methodology to estimate physical street dimensions from digital imagery "
            "using OpenCV. Utilized grayscale filtering, Canny edge detection, and morphological operations to "
            "identify object boundaries. Mapped pixel measurements to physical dimensions to categorize road "
            "widths and evaluate urban aesthetics in Dhaka."
        ),
        link="https://www.youtube.com/watch?v=Ds8k-aPHVKk"
    )


def experience():
    st.header("Professional & Teaching Experience")

    render_card(
        title="Faculty (Data Analysis)",
        subtitle="PeoplenTech",
        date="February 2025 – Present",
        body=(
            "Assist in teaching practical data analysis courses. Support students in understanding fundamental "
            "concepts, from initial data preparation to creating visual dashboards. Help prepare study materials, "
            "offer individual guidance, and collaborate with colleagues to maintain a supportive learning environment."
        )
    )

    render_card(
        title="Deputy Manager (Software Development)",
        subtitle="Radisson Digital Technologies Ltd.",
        date="February 2022 – March 2023",
        body=(
            "Assisted in coordinating software delivery and worked alongside the development team to meet project "
            "goals. Communicated with international clients regarding timelines and requirements. Helped build data "
            "collection pipelines and conducted basic data analysis. Prepared visual dashboards to share findings "
            "with stakeholders."
        )
    )

    render_card(
        title="Asst. Manager (Software Development)",
        subtitle="Radisson Digital Technologies Ltd.",
        date="February 2021 – January 2022",
        body=(
            "Managed technical compliance for a specific import project, ensuring all technical specifications "
            "strictly aligned with overseas tender documents. Guided a cross-functional development team and "
            "assisted with task organization. Participated in drafting technical proposals and shared routine "
            "progress updates with the team and clients."
        )
    )

    render_card(
        title="Team Lead (Mobile Apps and Games)",
        subtitle="Radisson Digital Technologies Ltd.",
        date="July 2020 – January 2021",
        body=(
            "Coordinated a group of developers and designers to create mobile applications and games. Helped track "
            "project milestones, listed and prioritized development tasks, and assisted in explaining technical "
            "details to non-technical team members."
        )
    )

    render_card(
        title="Android Apps Development Coach",
        subtitle="Radisson Digital Technologies Ltd.",
        date="November 2019 – June 2020",
        body=(
            "Mentored junior developers in core mobile development practices using Java and Android Studio. Guided "
            "trainees in understanding basic application logic and code troubleshooting to support their transition "
            "into professional development."
        )
    )

    render_card(
        title="Android Developer",
        subtitle="Radisson Digital Technologies Ltd.",
        date="September 2019 – October 2019",
        body=(
            "Contributed to the development and maintenance of mobile applications, assisting with basic screen "
            "layouts and third-party integrations. Helped fix bugs and support app functionality within a "
            "collaborative team environment."
        )
    )

    st.subheader("🤝 Leadership Experience")
    col1, col2, col3 = st.columns(3)
    with col1:
        render_card(
            title="Class Prefect",
            subtitle="Daffodil Int'l Univ. (OS & Web Engineering)",
            date="2017 – 2018",
            body=""
        )
    with col2:
        render_card(
            title="Motivational Speaker",
            subtitle="BRAC Urban Innovation Challenge, Dhaka",
            date="2016",
            body=""
        )
    with col3:
        render_card(
            title="Class Representative",
            subtitle="Daffodil International University",
            date="2014 – 2016",
            body=""
        )


def projects_and_publications():
    st.header("Publications, Projects & Honors")

    st.subheader("📄 Publications")
    st.markdown("""
    <div class="cv-card">
        <p class="cv-card-body" style="margin-bottom: 0.8rem;">
            1. Chowdhury, U. R., <strong>Roy, M.</strong>, Kamal, M. A. S., & Yamada, K. (2026). 
            <em>Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift</em>. 
            In <em>Journal of Physics: Conference Series</em> (Accepted).
        </p>
        <p class="cv-card-body" style="margin-bottom: 0.8rem;">
            2. Chowdhury, U. R., <strong>Roy, M.</strong>, Bakibillah, A. S. M., Kamal, M. A. S., & Yamada, K. (2026). 
            <em>Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction</em>. 
            In <em>IEEE EAEEIE 2026</em> (Accepted).
        </p>
        <p class="cv-card-body" style="margin-bottom: 0.8rem;">
            3. Chowdhury, U. R., <strong>Roy, M.</strong>, Bakibillah, A. S. M., Kamal, M. A. S., & Yamada, K. (2026). 
            <em>Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction</em>. 
            In <em>WiML Symposium @ ICML 2026</em> (Accepted).
        </p>
        <p class="cv-card-body">
            4. Chowdhury, U. R., <strong>Roy, M.</strong>, Hasanuzzaman, M., Mahmud, S., & Ferdous, M. F. (2022). 
            <a href="https://www.taylorfrancis.com/chapters/edit/10.1201/9781003156789-5/computer-vision-based-street-width-measurement-urban-aesthetics-identification-umme-rubaiyat-chowdhury-manoj-roy-md-hasanuzzaman-shakik-mahmud-mohammad-farhan-ferdous" target="_blank">
            <em>Computer Vision-based Street-width Measurement for Urban Aesthetics Identification</em></a>. 
            In <em>Vehicular Ad Hoc Networks</em>. Taylor & Francis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("💻 Selected Projects")
        render_card(
            title="JustTune.AI | Experimental Music Generation Pipeline",
            subtitle="",
            date="October 2023",
            body=(
                "Built an experimental pipeline using MusicGen for text-to-audio synthesis. Processed the generated "
                "audio with librosa for frequency analysis and applied pitch detection to map notes into exportable "
                "MIDI sequences."
            ),
            tools="MusicGen, librosa, aubio, mido, Python",
            link="https://www.youtube.com/watch?v=Cqcx3R3xZxs"
        )
        render_card(
            title="Arannya Bengali Web Browser Prototype",
            subtitle="",
            date="Aug 2017 – Feb 2018",
            body=(
                "Developed a prototype web browser that executed basic navigation actions based on Bengali speech "
                "recognition. Wrote custom configurations using Microsoft SAPI and CMUSphinx to map detected spoken "
                "words to specific browser commands."
            ),
            tools="VB.NET, Chromium Browser Engine, Microsoft SAPI, CMUSphinx",
            link="https://www.youtube.com/watch?v=OCxz-BOBHQ8"
        )

    with col2:
        st.subheader("🏆 Honors & Awards")
        honors = [
            ("Champion (¥100k Prize)", "ISAS 2026 Challenge (1st of 37 Teams)", "Oct 2026"),
            ("Data Science Scholar", "Data Insight Career Program", "Aug 2021"),
            ("Innovation Award", "Daffodil ICT Carnival", "Dec 2018"),
            ("Top 25 Apps", "EATL-Prothom Alo Mobile Apps Contest", "Dec 2016"),
            ("Top 10", "DIU Code-A-Thon", "Aug 2016"),
            ("CodersTrust Scholar", "Web Development Bootcamp", "2015"),
            ("Top 40 Apps", "EATL-Prothom Alo Mobile Apps Contest", "Dec 2014"),
        ]
        for award, event, date in honors:
            render_card(title=award, subtitle=event, date=date, body="")


def contact():
    st.header("Contact")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="cv-card">
            <h3 style="margin-top: 0; color: #222;">Get in Touch</h3>
            <p class="cv-card-body" style="margin-bottom: 1rem;">
                I am always open to discussing academic research collaborations, statistical data analysis, 
                and teaching opportunities. Feel free to reach out via email or phone.
            </p>
            <p class="cv-card-body"><strong>📧 Email:</strong> <a href="mailto:roy.manoj.stats@gmail.com">roy.manoj.stats@gmail.com</a></p>
            <p class="cv-card-body"><strong>📞 Phone:</strong> +88-01617402136</p>
            <p class="cv-card-body"><strong>🌐 Portfolio:</strong> <a href="https://manojroy.streamlit.app/" target="_blank">manojroy.streamlit.app</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cv-card">
            <h3 style="margin-top: 0; color: #222;">Interests</h3>
            <p class="cv-card-body">
                Outside of statistical modeling and research, I enjoy spending my time on:
            </p>
            <div style="margin-top: 0.8rem;">
                <span class="skill-badge">Public Speaking</span>
                <span class="skill-badge">Bibliography</span>
                <span class="skill-badge">Music</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def get_current_nav():
    # Compatible with both modern Streamlit (st.query_params) and older versions
    if hasattr(st, "query_params"):
        return st.query_params.get("nav", "Home")
    else:
        return st.experimental_get_query_params().get("nav", ["Home"])[0]


def main():
    pages = [
        "Home",
        "Education and Skills",
        "Research",
        "Experience",
        "Projects and Publications",
        "Contact"
    ]

    current_nav = get_current_nav()
    if current_nav not in pages:
        current_nav = "Home"

    # Render responsive top navigation bar with active state
    menu_items_html = ""
    for page in pages:
        active_class = "active" if page == current_nav else ""
        menu_items_html += f'<li><a href="?nav={page}" target="_self" class="{active_class}">{page}</a></li>'

    st.markdown(f'<ul class="menu">{menu_items_html}</ul>', unsafe_allow_html=True)

    if current_nav == "Home":
        home_page()
    elif current_nav == "Education and Skills":
        education_and_skills()
    elif current_nav == "Research":
        research()
    elif current_nav == "Experience":
        experience()
    elif current_nav == "Projects and Publications":
        projects_and_publications()
    elif current_nav == "Contact":
        contact()


if __name__ == "__main__":
    main()
