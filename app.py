import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts

st.set_page_config(
    page_title="Manoj Roy | Academic Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for Academic Styling, Styled Instant Tabs, and Mobile Responsiveness
st.markdown("""
    <style>
    /* Main Container */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem 2rem;
    }

    /* Homepage Typography (Preserved & Refined) */
    .main-title {
        font-size: 3.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #1a202c;
        letter-spacing: -0.5px;
    }
    .sub-title {
        font-size: 1.65rem;
        color: #4a5568;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    .intro-text {
        font-family: 'Georgia', serif;
        font-size: 16.5px;
        line-height: 1.75;
        text-align: justify;
        max-width: 780px;
        margin: 0 auto 1.8rem auto;
        padding: 24px 28px;
        background-color: #fcfcfd;
        border: 1px solid #edf2f7;
        border-left: 4px solid #008B8B;
        border-radius: 6px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    }
    .first-letter {
        font-size: 50px;
        font-weight: bold;
        color: #2d3748;
        margin: 0;
        padding-right: 12px;
        float: left;
        line-height: 0.95;
    }
    .quote {
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 16px;
        line-height: 1.6;
        text-align: center;
        margin-top: 1rem;
        padding: 1rem;
        background-color: #f8fafc;
        border-radius: 6px;
        border: 1px dashed #cbd5e1;
    }
    .highlight {
        color: #008B8B;
        font-weight: bold;
    }

    /* Style Streamlit Native Tabs as a Top Navigation Bar (Zero Reloads) */
    div[data-baseweb="tab-list"] {
        background-color: #262730;
        border-radius: 8px;
        padding: 6px 8px;
        gap: 6px;
        margin-bottom: 1.8rem;
        flex-wrap: wrap;
    }
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border-radius: 6px !important;
        padding: 10px 18px !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        border: none !important;
        transition: all 0.2s ease-in-out !important;
        flex: 1 1 auto;
        justify-content: center;
    }
    button[data-baseweb="tab"]:hover {
        background-color: #3b3d4a !important;
        color: #ffffff !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #008B8B !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    div[data-baseweb="tab-highlight"] {
        display: none !important;
    }
    div[data-baseweb="tab-border"] {
        display: none !important;
    }

    /* Academic Summary Metric Boxes */
    .stat-ribbon {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .stat-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 3px solid #008B8B;
        border-radius: 6px;
        padding: 0.9rem 1rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .stat-value {
        font-size: 1.45rem;
        font-weight: 700;
        color: #1a202c;
        font-family: 'Georgia', serif;
    }
    .stat-label {
        font-size: 0.82rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.2rem;
    }

    /* Clean Academic Cards */
    .cv-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #008B8B;
        border-radius: 6px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .cv-card:hover {
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.07);
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
        font-size: 1.08rem;
        font-weight: 700;
        color: #1e293b;
        margin: 0;
    }
    .cv-card-date {
        font-size: 0.86rem;
        color: #475569;
        background-color: #f1f5f9;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 500;
        white-space: nowrap;
    }
    .cv-card-subtitle {
        font-size: 0.94rem;
        color: #006666;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    .cv-card-body {
        font-size: 0.94rem;
        color: #334155;
        line-height: 1.65;
        margin: 0;
    }

    /* Skill & Topic Badges */
    .skill-badge {
        display: inline-block;
        background-color: #f0f4f8;
        color: #2c3e50;
        padding: 5px 11px;
        margin: 3px 5px 3px 0;
        border-radius: 4px;
        font-size: 0.86rem;
        font-weight: 500;
        border: 1px solid #dce4ec;
    }

    /* Statistical Metric Bar for Research Explorer */
    .metric-row {
        margin-bottom: 0.75rem;
    }
    .metric-label-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.88rem;
        font-weight: 600;
        color: #334155;
        margin-bottom: 0.25rem;
    }
    .metric-bar-bg {
        width: 100%;
        background-color: #e2e8f0;
        height: 10px;
        border-radius: 5px;
        overflow: hidden;
    }
    .metric-bar-fill {
        height: 100%;
        background-color: #008B8B;
        border-radius: 5px;
    }

    /* Responsive Adjustments for Mobile & Tablet */
    @media (max-width: 768px) {
        .stApp {
            padding: 0.5rem 0.8rem;
        }
        .main-title {
            font-size: 2.2rem;
        }
        .sub-title {
            font-size: 1.25rem;
        }
        .intro-text {
            padding: 16px;
            font-size: 15px;
        }
        .stat-ribbon {
            grid-template-columns: repeat(2, 1fr);
        }
        button[data-baseweb="tab"] {
            padding: 8px 10px !important;
            font-size: 0.82rem !important;
        }
        .cv-card-header {
            flex-direction: column;
            gap: 0.2rem;
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
        "tooltip": {
            "trigger": "item",
            "formatter": "{b}: {c} ({d}%)"
        },
        "legend": {"top": "bottom"},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": True},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "series": [
            {
                "name": "Core Attributes",
                "type": "pie",
                "radius": ["18%", "68%"],
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
    title_html = (
        f'<a href="{link}" target="_blank" style="color: #1e293b; text-decoration: underline;">{title} 🔗</a>'
        if link else title
    )
    subtitle_html = f'<div class="cv-card-subtitle">{subtitle}</div>' if subtitle else ""
    tools_html = (
        f'<div style="margin-top: 0.5rem; font-size: 0.86rem; color: #475569;">'
        f'<strong>Tools:</strong> {tools}</div>'
        if tools else ""
    )
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


def render_metric_bar(label, value_str, percentage, color="#008B8B"):
    st.markdown(f"""
        <div class="metric-row">
            <div class="metric-label-row">
                <span>{label}</span>
                <span>{value_str}</span>
            </div>
            <div class="metric-bar-bg">
                <div class="metric-bar-fill" style="width: {percentage}%; background-color: {color};"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def home_page():
    # Header Section
    st.markdown('<h1 class="main-title">Hi, I am Manoj Roy 👋</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">Data Enthusiast & Researcher</h2>', unsafe_allow_html=True)

    # Academic At-a-Glance Ribbon
    st.markdown("""
        <div class="stat-ribbon">
            <div class="stat-box">
                <div class="stat-value">M.Sc. (3.77/4)</div>
                <div class="stat-label">Applied Statistics & Data Science</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">4 Papers</div>
                <div class="stat-label">Accepted & Published Research</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">1st / 37 Teams</div>
                <div class="stat-label">ISAS 2026 Challenge Champion</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">5+ Years</div>
                <div class="stat-label">Industry & Teaching Experience</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Preserved Introduction Content
    st.markdown(
        """
        <div class="intro-text">
        <p><span class="first-letter">A</span> dedicated data enthusiast with a Master's in Applied Statistics and Data Science, I am passionately pursuing knowledge in quantum machine learning. My strong foundation in statistics and classical ML algorithms fuels my curiosity to explore how quantum computing can revolutionize model performance. I'm actively learning to develop hybrid quantum-classical algorithms and optimize quantum feature maps, aiming to contribute to breakthroughs in ML efficiency and accuracy.</p>
        
        <p>As an eager learner and collaborator, I'm excited to bridge my statistical expertise with emerging quantum technologies. I'm committed to growing in this cutting-edge field, aspiring to participate in innovative research and real-world applications that harness quantum advantages in machine learning.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Skills Diagram & Lottie Animation Section
    left_column, right_column = st.columns([2, 1])

    with left_column:
        st_echarts(options=render_nightingale_rose_diagram(), height="520px")

    with right_column:
        lottie_skills = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ul35wckt.json")
        if lottie_skills:
            st_lottie(lottie_skills, speed=1, height=280, key="home_lottie")

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
    st.header("Education & Technical Profile")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🎓 Academic Degrees")
        render_card(
            title="M.Sc. in Applied Statistics and Data Science",
            subtitle="Jahangirnagar University",
            date="2021 – 2022",
            body="CGPA: 3.77 / 4.00 | Focus: Statistical Modeling, Machine Learning & Feature Engineering."
        )
        render_card(
            title="B.Sc. in Computer Science and Engineering",
            subtitle="Daffodil International University",
            date="2014 – 2018",
            body="CGPA: 3.58 / 4.00 | Focus: Algorithms, Computer Vision & Software Development."
        )

        st.subheader("🛠️ Core Competencies")
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
            st.markdown(f"**{category}**<div>{badges}</div><div style='margin-bottom:0.6rem;'></div>", unsafe_allow_html=True)

    with col2:
        st.subheader("📜 Specializations & Certifications")
        cert_filter = st.radio(
            "Filter by Domain:",
            ["All (9)", "Statistics & Data Science", "Machine Learning & AI", "Engineering & Management"],
            horizontal=True
        )

        certifications = [
            ("Data Analysis and Interpretation", "Wesleyan University", "2020", "Statistics & Data Science", "https://www.coursera.org/account/accomplishments/specialization/Z2J48LBUJU4M"),
            ("Applied Data Science with Python", "University of Michigan", "2020", "Statistics & Data Science", "https://www.coursera.org/account/accomplishments/specialization/WXFWX2AD54NL"),
            ("Data Mining", "University of Illinois Urbana-Champaign", "2020", "Statistics & Data Science", "https://www.coursera.org/account/accomplishments/specialization/RZUALYJXPFSL"),
            ("Advanced Statistics for Data Science", "Johns Hopkins University", "2020", "Statistics & Data Science", "https://www.coursera.org/account/accomplishments/specialization/67T7GMUPVKN2"),
            ("Data Science", "Johns Hopkins University", "2020", "Statistics & Data Science", "https://www.coursera.org/account/accomplishments/specialization/P6TKC6X4H6GE"),
            ("Machine Learning", "University of Washington", "2020", "Machine Learning & AI", "https://www.coursera.org/account/accomplishments/specialization/BV9CYHFR8APV"),
            ("Deep Learning", "DeepLearning.AI", "2020", "Machine Learning & AI", "https://www.coursera.org/account/accomplishments/specialization/25TEG2MDQ2ZA"),
            ("Project Management & Other Tools", "University of Illinois", "2020", "Engineering & Management", "https://www.coursera.org/account/accomplishments/specialization/Y62UBR8DUFQD"),
            ("Advanced App Development in Android", "Imperial College London", "2020", "Engineering & Management", "https://www.coursera.org/account/accomplishments/specialization/P44V2WAMEB89"),
        ]

        for title, org, year, domain, url in certifications:
            if cert_filter == "All (9)" or cert_filter == domain:
                st.markdown(
                    f'<div style="padding: 6px 0; border-bottom: 1px solid #f1f5f9;">'
                    f'🔹 <a href="{url}" target="_blank" style="font-weight:600; color:#1e293b;">{title}</a> '
                    f'<span style="color:#64748b; font-size:0.9rem;">| {org} ({year})</span></div>',
                    unsafe_allow_html=True
                )

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🔬 Specialized Training & Workshops")
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
    st.header("Academic Research & Empirical Methodology")

    # Interactive Statistical Thinking Showcase
    st.markdown("""
        <div class="cv-card" style="background-color: #f8fafc; border-left-color: #2d3748;">
            <div class="cv-card-title" style="margin-bottom: 0.4rem;">📐 Statistical Thinking Spotlight: Evaluation Protocol & Uncertainty Analysis</div>
            <p class="cv-card-body">
                A recurring theme in my research is questioning standard evaluation assumptions—whether exposing how naive random splitting inflates accuracy in temporally dependent sensor streams, or quantifying epistemic uncertainty when visual priors encounter out-of-distribution weather anomalies.
            </p>
        </div>
    """, unsafe_allow_html=True)

    study_choice = st.radio(
        "Inspect Empirical Findings from Recent Studies:",
        [
            "1. BLE Indoor Localization: Protocol Sensitivity under Temporal Shift (ISAS 2026)",
            "2. 3D Semantic Occupancy: Evidential Feature Gating under Anomalies (EAEEIE / ICML WiML 2026)"
        ],
        horizontal=False
    )

    if "BLE Indoor Localization" in study_choice:
        col_a, col_b = st.columns([1.2, 1])
        with col_a:
            st.markdown("##### Strict Chronological Forward Protocol Comparison")
            render_metric_bar("Proposed Multi-Resolution Framework (Accuracy)", "60.54%", 60.54, "#008B8B")
            render_metric_bar("10s Random Forest Baseline (Accuracy)", "55.33%", 55.33, "#64748b")
            render_metric_bar("Proposed Framework (Weighted-F1)", "0.5973", 59.73, "#008B8B")
            render_metric_bar("10s Random Forest Baseline (Weighted-F1)", "0.5293", 52.93, "#64748b")
            render_metric_bar("Proposed Framework (Forward Macro-F1)", "0.3159", 31.59, "#008B8B")
            render_metric_bar("10s Random Forest Baseline (Forward Macro-F1)", "0.2561", 25.61, "#64748b")
        with col_b:
            st.info(
                "**Why Protocol Choice Matters:**\n\n"
                "In nursing-care BLE localization, a standalone 60s XGBoost model exceeds **0.91 Macro-F1** under naive row-random splitting due to temporal autocorrelation, "
                "but drops to **~0.25 Macro-F1** under strict chronological forward evaluation.\n\n"
                "By treating localization as a temporally dependent measurement problem and fusing 10s Random Forest and 60s XGBoost representations with fold-local augmentation, "
                "our framework improves forward Macro-F1 to **0.3159** and won **1st place (out of 37 teams)** at the ISAS 2026 Challenge."
            )
    else:
        col_a, col_b = st.columns([1.2, 1])
        with col_a:
            st.markdown("##### System Efficiency & Clean-Weather Baseline")
            render_metric_bar("Clean-Weather Semantic Accuracy (mIoU)", "30.44 mIoU", 65.0, "#008B8B")
            render_metric_bar("Real-Time Inference Speed (Single RTX A4500)", "14.2 FPS", 71.0, "#008B8B")
            render_metric_bar("Additional Parameter Overhead", "+0.01M Params", 5.0, "#2e7d32")
        with col_b:
            st.info(
                "**Addressing Temporal Poisoning via Dirichlet Logic:**\n\n"
                "While 2D pre-trained backbones accelerate 3D convergence and handle static noise (e.g., Fog), they suffer structural collapse under motion blur and snow—overwriting downstream 3D history buffers.\n\n"
                "Grounded in Dirichlet subjective logic, the **Evidential Feature Gate (EFG)** dynamically quantifies out-of-distribution epistemic uncertainty at the feature level and suppresses corrupted spatial inputs toward zero."
            )

    st.markdown("---")
    st.subheader("📚 Detailed Research Timeline")

    render_card(
        title="Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift",
        subtitle="Role: Co-Researcher | Accepted at Journal of Physics: Conference Series (ISAS 2026 Challenge)",
        date="2026",
        body=(
            "Proposed a multi-resolution framework utilizing Random Forest and XGBoost to study BLE signal loss, "
            "class imbalance, and temporal shift in a care facility setting. Explored fold-local signal-pattern "
            "augmentation and probability fusion, which helped improve minority-class recovery and strict "
            "forward-protocol accuracy."
        )
    )
    with st.expander("📖 Read Full Abstract (BLE Indoor Localization)"):
        st.write(
            "Indoor localization of nursing staff can support analysis of care routines using unobtrusive radio sensing. "
            "This paper is submitted in connection with the ISAS 2026 Challenge and addresses its BLE-based nursing-care "
            "location-recognition task. In an operating care facility, Bluetooth Low Energy (BLE) Received Signal Strength "
            "Indicator (RSSI) observations are intermittent and environmentally variable, while the labeled data are "
            "additionally shaped by heterogeneous visit duration and unequal room visitation. We therefore treat semantic "
            "room localization as a temporally dependent measurement problem rather than only an imbalanced classification "
            "task. We propose a multi-resolution framework combining a responsive 10s Random Forest representation with two "
            "complementary 60s XGBoost representations, fold-local signal-pattern augmentation, synthetic minority balancing, "
            "probability normalization and fusion, and conservative minority-class recovery."
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
    with st.expander("📖 Read Full Abstract (3D Semantic Occupancy Prediction)"):
        st.write(
            "Vision-centric 3D semantic occupancy prediction has emerged as a highly scalable alternative to LiDAR for "
            "autonomous driving. Due to severe optimization challenges inherent in training complex 3D spatio-temporal "
            "transformers from scratch, existing architectures typically rely on 2D convolutional backbones pre-trained on "
            "massive image datasets. Through an empirical analysis using the NuScenes-C robustness benchmark, we evaluate "
            "deterministic 2D spatial priors and demonstrate that while they excel at static noise penetration, they exhibit "
            "structural collapse under anomalies such as Motion Blur and Snow, inducing 'Temporal Poisoning.' To resolve this "
            "vulnerability without sacrificing clean-weather performance, we propose an Evidential Feature Gate (EFG) grounded "
            "in Dirichlet subjective logic to dynamically quantify out-of-distribution epistemic uncertainty and suppress "
            "corrupted spatial inputs."
        )

    render_card(
        title="Machine Learning Based Feature Engineering for Identifying The Causes Of Divorce",
        subtitle="Role: Graduate Researcher | M.Sc. Dissertation, Statistics & Data Science, Jahangirnagar Univ.",
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
        subtitle="Role: Undergraduate Researcher | B.Sc. Dissertation, Dept. of CSE, Daffodil Int'l Univ.",
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

    st.subheader("🤝 Academic & Community Leadership")
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

    st.subheader("📄 Peer-Reviewed Publications & Proceedings")

    publications = [
        {
            "citation": (
                "Chowdhury, U. R., <strong>Roy, M.</strong>, Kamal, M. A. S., & Yamada, K. (2026). "
                "<em>Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift</em>. "
                "In <em>Journal of Physics: Conference Series</em> (Accepted)."
            ),
            "bibtex": """@inproceedings{chowdhury2026multiresolution,
  author    = {Chowdhury, Umme Rubaiyat and Roy, Manoj and Kamal, Md Abdus Samad and Yamada, Kou},
  title     = {Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift},
  booktitle = {Journal of Physics: Conference Series},
  year      = {2026},
  note      = {Accepted, ISAS 2026 Challenge Winner}
}"""
        },
        {
            "citation": (
                "Chowdhury, U. R., <strong>Roy, M.</strong>, Bakibillah, A. S. M., Kamal, M. A. S., & Yamada, K. (2026). "
                "<em>Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction</em>. "
                "In <em>IEEE EAEEIE 2026</em> (Accepted)."
            ),
            "bibtex": """@inproceedings{chowdhury2026spatiotemporal_ieee,
  author    = {Chowdhury, Umme Rubaiyat and Roy, Manoj and Bakibillah, A. S. M. and Kamal, Md Abdus Samad and Yamada, Kou},
  title     = {Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction},
  booktitle = {Proceedings of the IEEE EAEEIE Annual Conference},
  year      = {2026},
  note      = {Accepted}
}"""
        },
        {
            "citation": (
                "Chowdhury, U. R., <strong>Roy, M.</strong>, Bakibillah, A. S. M., Kamal, M. A. S., & Yamada, K. (2026). "
                "<em>Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction</em>. "
                "In <em>WiML Symposium @ ICML 2026</em> (Accepted)."
            ),
            "bibtex": """@inproceedings{chowdhury2026spatiotemporal_icml,
  author    = {Chowdhury, Umme Rubaiyat and Roy, Manoj and Bakibillah, A. S. M. and Kamal, Md Abdus Samad and Yamada, Kou},
  title     = {Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction},
  booktitle = {Women in Machine Learning (WiML) Symposium at ICML},
  year      = {2026},
  note      = {Accepted}
}"""
        },
        {
            "citation": (
                'Chowdhury, U. R., <strong>Roy, M.</strong>, Hasanuzzaman, M., Mahmud, S., & Ferdous, M. F. (2022). '
                '<a href="https://www.taylorfrancis.com/chapters/edit/10.1201/9781003156789-5/computer-vision-based-street-width-measurement-urban-aesthetics-identification-umme-rubaiyat-chowdhury-manoj-roy-md-hasanuzzaman-shakik-mahmud-mohammad-farhan-ferdous" target="_blank">'
                '<em>Computer Vision-based Street-width Measurement for Urban Aesthetics Identification</em></a>. '
                'In <em>Vehicular Ad Hoc Networks</em>. Taylor & Francis.'
            ),
            "bibtex": """@incollection{chowdhury2022computer,
  author    = {Chowdhury, Umme Rubaiyat and Roy, Manoj and Hasanuzzaman, Md and Mahmud, Shakik and Ferdous, Mohammad Farhan},
  title     = {Computer Vision-based Street-width Measurement for Urban Aesthetics Identification},
  booktitle = {Vehicular Ad Hoc Networks},
  publisher = {Taylor \\& Francis},
  year      = {2022}
}"""
        }
    ]

    for idx, pub in enumerate(publications, 1):
        st.markdown(f"""
            <div class="cv-card" style="margin-bottom: 0.4rem;">
                <p class="cv-card-body"><strong>[{idx}]</strong> {pub["citation"]}</p>
            </div>
        """, unsafe_allow_html=True)
        with st.expander(f"📋 Copy BibTeX Citation [{idx}]"):
            st.code(pub["bibtex"], language="latex")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("💻 Selected Technical Prototypes")
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
    st.header("Contact & Academic Correspondence")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="cv-card">
            <h3 style="margin-top: 0; color: #1e293b;">Get in Touch</h3>
            <p class="cv-card-body" style="margin-bottom: 1.2rem;">
                I welcome discussions regarding academic research collaborations, statistical modeling, 
                graduate research opportunities, and data analysis instruction.
            </p>
            <p class="cv-card-body" style="margin-bottom: 0.6rem;">
                <strong>📧 Email:</strong> <a href="mailto:roy.manoj.stats@gmail.com">roy.manoj.stats@gmail.com</a>
            </p>
            <p class="cv-card-body" style="margin-bottom: 0.6rem;">
                <strong>📞 Phone:</strong> +88-01617402136
            </p>
            <p class="cv-card-body">
                <strong>🌐 Portfolio:</strong> <a href="https://manojroy.streamlit.app/" target="_blank">manojroy.streamlit.app</a>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cv-card">
            <h3 style="margin-top: 0; color: #1e293b;">Research & Personal Interests</h3>
            <p class="cv-card-body" style="margin-bottom: 0.6rem;">
                <strong>Research Areas:</strong>
            </p>
            <div style="margin-bottom: 1rem;">
                <span class="skill-badge">Applied Statistics</span>
                <span class="skill-badge">3D Occupancy & Vision</span>
                <span class="skill-badge">Evidential Uncertainty</span>
                <span class="skill-badge">Multi-Resolution Sensor ML</span>
                <span class="skill-badge">Quantum ML Exploration</span>
            </div>
            <p class="cv-card-body" style="margin-bottom: 0.6rem;">
                <strong>Personal Interests:</strong>
            </p>
            <div>
                <span class="skill-badge">Public Speaking</span>
                <span class="skill-badge">Bibliography</span>
                <span class="skill-badge">Music</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def main():
    # Client-side instant tabs (No browser page reload on click)
    tabs = st.tabs([
        "🏠 Home",
        "🎓 Education & Skills",
        "🔬 Research",
        "💼 Experience",
        "📄 Publications & Honors",
        "✉️ Contact"
    ])

    with tabs[0]:
        home_page()
    with tabs[1]:
        education_and_skills()
    with tabs[2]:
        research()
    with tabs[3]:
        experience()
    with tabs[4]:
        projects_and_publications()
    with tabs[5]:
        contact()


if __name__ == "__main__":
    main()
