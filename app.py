import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts

st.set_page_config(
    page_title="Manoj Roy | Academic Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for Academic Styling, Instant Client-Side Tabs, and Responsive Layout
st.markdown("""
    <style>
    /* Main Container */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem 2rem;
    }

    /* Homepage Typography */
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
        max-width: 820px;
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
    div[data-baseweb="tab-highlight"], div[data-baseweb="tab-border"] {
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
        font-size: 1.4rem;
        font-weight: 700;
        color: #1a202c;
        font-family: 'Georgia', serif;
    }
    .stat-label {
        font-size: 0.8rem;
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
        transition: box-shadow 0.15s ease;
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
        font-size: 0.85rem;
        color: #475569;
        background-color: #f1f5f9;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 500;
        white-space: nowrap;
    }
    .cv-card-subtitle {
        font-size: 0.93rem;
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

    /* Methodological Note Box */
    .method-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 1rem 1.2rem;
        font-size: 0.9rem;
        color: #334155;
        line-height: 1.6;
        margin-bottom: 1rem;
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


def render_ble_protocol_chart():
    option = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {"top": "bottom"},
        "grid": {"left": "3%", "right": "4%", "bottom": "15%", "top": "8%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "data": [
                "Row-Random\n(Diagnostic)",
                "45s Block\n(±59s Purge)",
                "Event-Group\n(±59s Purge)",
                "LODO\n(Cross-Day)",
                "Strict-Forward\n(Chronological)"
            ],
        },
        "yAxis": {
            "type": "value",
            "name": "Fixed-23 Macro-F1",
            "max": 1.0
        },
        "series": [
            {
                "name": "Proposed Multi-Resolution System",
                "type": "bar",
                "data": [0.901, 0.348, 0.280, 0.322, 0.316],
                "itemStyle": {"color": "#008B8B", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "60s Rich XGBoost (KL-Full + SMOTE)",
                "type": "bar",
                "data": [0.910, 0.303, 0.199, 0.254, 0.255],
                "itemStyle": {"color": "#e07a5f", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "10s RF Summary Baseline",
                "type": "bar",
                "data": [0.628, 0.302, 0.237, 0.287, 0.256],
                "itemStyle": {"color": "#64748b", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "10s Causal TCN",
                "type": "bar",
                "data": [0.542, 0.270, 0.235, 0.265, 0.211],
                "itemStyle": {"color": "#94a3b8", "borderRadius": [4, 4, 0, 0]}
            }
        ]
    }
    return option


def render_ble_ablation_chart():
    option = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {"top": "bottom"},
        "grid": {"left": "3%", "right": "4%", "bottom": "15%", "top": "8%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "data": [
                "10s RF\nBaseline",
                "Untargeted Multi-Res\nFusion (T=1.25)",
                "+ Class-510\nScore Gate",
                "+ Class-518\nTemporal Vote"
            ]
        },
        "yAxis": {"type": "value", "name": "Score", "max": 0.70},
        "series": [
            {
                "name": "Fixed-23 Macro-F1",
                "type": "bar",
                "data": [0.2561, 0.3051, 0.3077, 0.3159],
                "itemStyle": {"color": "#008B8B", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "Weighted-F1",
                "type": "bar",
                "data": [0.5293, 0.5962, 0.5966, 0.5973],
                "itemStyle": {"color": "#3b82f6", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "Accuracy",
                "type": "line",
                "data": [0.5533, 0.6048, 0.6051, 0.6054],
                "itemStyle": {"color": "#0f172a"},
                "lineStyle": {"width": 3}
            }
        ]
    }
    return option


def render_efg_distance_chart():
    option = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {"top": "bottom"},
        "grid": {"left": "3%", "right": "4%", "bottom": "15%", "top": "8%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "data": [
                "Overall\nmIoU",
                "Overall\nRayIoU",
                "Near Ring\n(0–15m mIoU)",
                "Mid Ring\n(15–30m mIoU)",
                "Far Ring\n(>30m mIoU)"
            ]
        },
        "yAxis": {"type": "value", "name": "Metric (%)", "max": 45},
        "series": [
            {
                "name": "Baseline (SparseOcc v1.1)",
                "type": "bar",
                "data": [31.10, 36.75, 41.73, 31.33, 17.93],
                "itemStyle": {"color": "#64748b", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "Phase 1 EFG (No Pretrain)",
                "type": "bar",
                "data": [25.11, 30.63, 35.49, 24.64, 12.69],
                "itemStyle": {"color": "#e07a5f", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "Phase 1 EFG (With Pretrain - Proposed)",
                "type": "bar",
                "data": [30.44, 36.10, 41.07, 30.60, 17.02],
                "itemStyle": {"color": "#008B8B", "borderRadius": [4, 4, 0, 0]}
            }
        ]
    }
    return option


def render_efg_corruption_chart():
    option = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {"top": "bottom"},
        "grid": {"left": "3%", "right": "4%", "bottom": "15%", "top": "8%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "data": [
                "Motion Blur\n(Easy RR%)",
                "Motion Blur\n(Mid RR%)",
                "Motion Blur\n(Hard RR%)",
                "Snow\n(Easy RR%)",
                "Fog Hard\n(Driveable RayIoU%)"
            ]
        },
        "yAxis": {"type": "value", "name": "Retention / Score (%)", "max": 100},
        "series": [
            {
                "name": "Deterministic Baseline (Pretrained)",
                "type": "bar",
                "data": [85.9, 28.6, 14.9, 16.2, 51.9],
                "itemStyle": {"color": "#64748b", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "EFG (Un-Pretrained 3D Priors)",
                "type": "bar",
                "data": [93.0, 71.0, 61.2, 34.8, 37.9],
                "itemStyle": {"color": "#008B8B", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "EFG (With 2D Pretrain)",
                "type": "bar",
                "data": [82.0, 26.0, 14.2, 8.9, 49.4],
                "itemStyle": {"color": "#3b82f6", "borderRadius": [4, 4, 0, 0]}
            }
        ]
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


def home_page():
    # Header Section
    st.markdown('<h1 class="main-title">Hi, I am Manoj Roy 👋</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">Data Enthusiast & Researcher</h2>', unsafe_allow_html=True)

    # Academic At-a-Glance Ribbon
    st.markdown("""
        <div class="stat-ribbon">
            <div class="stat-box">
                <div class="stat-value">M.Sc. & B.Sc.</div>
                <div class="stat-label">Applied Statistics & CSE</div>
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

    # General, Humble Academic Introduction (No narrow topic lock-in)
    st.markdown(
        """
        <div class="intro-text">
        <p><span class="first-letter">A</span> dedicated data enthusiast with a Master's in Applied Statistics and Data Science and a Bachelor's in Computer Science and Engineering, I approach research through a foundation of statistical reasoning, careful problem formulation, and empirical validation. Rather than confining my curiosity to a single narrow domain, I enjoy studying how data behaves under practical real-world constraints—such as measurement noise, class imbalance, temporal shift, and distributional anomalies—and building transparent, reproducible pipelines to investigate these problems.</p>
        
        <p>As an eager learner and collaborative researcher, I value methodological honesty, clean experimental design, and clear analytical communication. Whether working with time-dependent sensor streams, computer vision architectures, behavioral datasets, or guiding students through foundational data concepts, I strive to contribute thoughtfully and learn continuously within any research team.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Skills Diagram & Lottie Animation Section
    left_column, right_column = st.columns([2, 1])

    with left_column:
        st_echarts(options=render_nightingale_rose_diagram(), height="520px", key="home_rose_chart")

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

    st.markdown("""
        <div class="cv-card" style="background-color: #f8fafc; border-left-color: #2d3748;">
            <div class="cv-card-title" style="margin-bottom: 0.4rem;">📐 Interactive Empirical Explorer: Protocol Design & Structural Robustness</div>
            <p class="cv-card-body">
                Select a study below to explore the experimental design, validation protocols, and ablation outcomes from our recent manuscripts. Both studies emphasize careful control of information boundaries, transparent reporting of trade-offs, and resistance to distributional shifts.
            </p>
        </div>
    """, unsafe_allow_html=True)

    study_choice = st.radio(
        "Select Research Study to Inspect:",
        [
            "Study 1: Multi-Resolution BLE Indoor Localization under Signal Loss, Class Imbalance & Temporal Shift (ISAS 2026)",
            "Study 2: Spatio-Temporal Paradox of 2D Priors & Evidential Feature Gating in 3D Occupancy (EAEEIE / ICML WiML 2026)"
        ]
    )

    if "Study 1" in study_choice:
        view_mode = st.radio(
            "Select Empirical View:",
            [
                "Cross-Protocol Sensitivity (5 Validation Regimes)",
                "Strict-Forward Ablation & Multi-Resolution Ensemble Design"
            ],
            horizontal=True
        )

        if "Cross-Protocol" in view_mode:
            col_chart, col_notes = st.columns([1.45, 1])
            with col_chart:
                st.markdown("##### Fixed-23 Macro-F1 Across Validation Protocols")
                st_echarts(options=render_ble_protocol_chart(), height="380px", key="ble_protocol_echarts")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>Why Validation Protocol Changes Apparent Difficulty:</strong><br><br>
                    • <strong>Dataset Scope:</strong> 47,121 labeled seconds across Apr 10–13 (25 BLE beacons, 23 official semantic locations: 18 patient rooms and 5 common areas).<br>
                    • <strong>Window Overlap & Leakage Control:</strong> Adjacent 10s and 60s windows share most underlying seconds. Under naive 70/30 row-random splitting, a 60s rich XGBoost reaches <strong>0.910 Macro-F1</strong> (0.9102 unrounded) due to overlapping temporal neighbors, but drops to <strong>0.255</strong> under strict-forward chronological evaluation.<br>
                    • <strong>Known-Label Emergence:</strong> 11 of the 18 official patient rooms have zero real labeled observations on Apr 10 and emerge only on later days. Using fold-local topology-constrained KL/symmetric donor transfer and SMOTE, the proposed ensemble maintains <strong>0.316 Macro-F1</strong> (0.3159) under strict-forward evaluation and <strong>0.322</strong> under LODO.
                </div>
                """, unsafe_allow_html=True)
        else:
            col_chart, col_notes = st.columns([1.45, 1])
            with col_chart:
                st.markdown("##### Strict-Forward Ablation (Pooled Apr 11–13, N = 36,265s)")
                st_echarts(options=render_ble_ablation_chart(), height="380px", key="ble_ablation_echarts")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>Ensemble Constituents & Honest Methodological Disclosure:</strong><br><br>
                    • <strong>Three Parallel Branches:</strong> Combines a 10s Random Forest summary view (100-dim, weight 0.70), a 60s rich XGBoost view (153-dim, weight 0.15, temperature <em>T = 1.25</em>), and a 60s full-statistics XGBoost view (253-dim, weight 0.15, KL-partial transfer, <em>T = 1.0</em>).<br>
                    • <strong>Where the Gain Comes From:</strong> <strong>81.9%</strong> of the total Macro-F1 improvement (+0.0490 of +0.0598, reaching 0.3051) and ~99% of the accuracy gain (0.5533 → 0.6048) occur at the untargeted multi-resolution fusion stage prior to class-specific rules (class-510 score gate ×1.5 and class-518 vote weight ×3.5).<br>
                    • <strong>Scope & Limitations:</strong> Because the Apr 11–13 chronological folds informed hyperparameter screening, these figures are reported transparently as internal development estimates rather than untouched external validation. In addition, the 11s centered majority vote ([t−5s, t+5s]) is an offline batch operation requiring 5s look-ahead.
                </div>
                """, unsafe_allow_html=True)

    else:
        view_mode = st.radio(
            "Select Empirical View:",
            [
                "Clean-Weather Semantics & Radial Depth Rings (Occ3D-nuScenes)",
                "Dynamic vs. Static Anomalies & Dirichlet Firewall (Robo3D)"
            ],
            horizontal=True
        )

        if "Clean-Weather" in view_mode:
            col_chart, col_notes = st.columns([1.45, 1])
            with col_chart:
                st.markdown("##### Clean-Weather Accuracy & Distance-Bounded Evaluation")
                st_echarts(options=render_efg_distance_chart(), height="380px", key="efg_dist_echarts")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>Why 2D Pre-Training Remains Necessary at Long Range:</strong><br><br>
                    • <strong>The Distance Bottleneck:</strong> As objects recede beyond 30 meters from the ego-vehicle, their projected 2D pixel volume diminishes rapidly. Training from scratch without ImageNet/nuImages 2D priors causes severe degradation in the Far (>30m) ring (dropping from 17.93 to 12.69 mIoU).<br>
                    • <strong>Restoring Clean-Weather Semantics:</strong> Pairing our Evidential Feature Gate (EFG) with 2D pre-trained weights preserves long-range acuity (<strong>17.02 mIoU</strong> at >30m) and achieves <strong>30.44 overall mIoU</strong> and <strong>36.10 RayIoU</strong> on Occ3D-nuScenes.<br>
                    • <strong>Real-Time Hardware Viability:</strong> Evaluated on a single NVIDIA RTX A4500 GPU, integrating EFG into SparseOcc adds only <strong>+0.01M parameters</strong> (80.12M → 80.13M) and maintains real-time inference at <strong>14.25 FPS</strong> (vs. 15.68 FPS baseline).
                </div>
                """, unsafe_allow_html=True)
        else:
            col_chart, col_notes = st.columns([1.45, 1])
            with col_chart:
                st.markdown("##### Relative Robustness (RR%) & Static Fog Penetration")
                st_echarts(options=render_efg_corruption_chart(), height="380px", key="efg_corr_echarts")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>The Spatio-Temporal Paradox & Dirichlet Feature Suppression:</strong><br><br>
                    • <strong>Static vs. Dynamic Anomalies:</strong> 2D texture priors help pierce static noise like <em>Fog (Hard)</em> (0.494 Driveable RayIoU with EFG + Pretrain vs. 0.379 un-pretrained). However, under dynamic <em>Motion Blur</em> (edge loss) and <em>Snow</em> (geometric hallucination), pre-trained 2D features corrupt the 8-frame temporal history buffer ("Temporal Poisoning").<br>
                    • <strong>Structural Retention:</strong> Under severe Motion Blur (Hard), the deterministic baseline retains only <strong>14.9%</strong> of its clean-weather performance, whereas our un-pretrained 3D evidential model retains <strong>61.2%</strong> Relative Robustness.<br>
                    • <strong>Dirichlet Firewall Audit:</strong> Framing spatial extraction via Subjective Logic (<em>u<sub>t</sub> = K / S<sub>t</sub></em>, gate <em>G<sub>t</sub> = 1 − u<sub>t</sub></em>), an audit of 50,000 internal activations under severe blur shows EFG reduces mean activation magnitude by <strong>70.8%</strong> and squashes <strong>55.65%</strong> of corrupted spatial features to zero.
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📚 Detailed Research Timeline")

    render_card(
        title="Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift",
        subtitle="Role: Co-Researcher | Accepted at Journal of Physics: Conference Series (ISAS 2026 Challenge — Champion, 1st of 37 Teams)",
        date="2026",
        body=(
            "Treated semantic room localization across 23 care-facility locations (47,121 labeled seconds, 25 BLE beacons) "
            "as a temporally dependent measurement problem. Combined 1-second state reconstruction (≤3s carry-forward fill "
            "and span-3 EWMA), parallel 10s Random Forest (100-dim) and 60s XGBoost (153-dim and 253-dim) representations, "
            "fold-local topology/KL signal transfer, temperature-softened probability fusion (T = 1.25), and 11s centered "
            "decoding. Conducted a five-protocol leakage-aware audit demonstrating how model rankings shift from naive "
            "row-random splitting to strict chronological forward evaluation (improving Macro-F1 from 0.2561 to 0.3159)."
        ),
        tools="Python, Scikit-learn, XGBoost, LightGBM, PyTorch (Causal TCN audit), Statistical Signal Processing"
    )
    with st.expander("📖 Read Full Abstract (BLE Indoor Localization)"):
        st.write(
            "Indoor localization of nursing staff can support analysis of care routines using unobtrusive radio sensing. "
            "This paper is submitted as part of the ISAS 2026 Challenge and addresses its Bluetooth Low Energy (BLE) "
            "nursing-care location-recognition task. In an operating care facility, BLE Received Signal Strength Indicator "
            "(RSSI) observations are intermittent and environmentally variable, while the labeled data are additionally "
            "shaped by heterogeneous visit durations and unequal room visitation. We therefore treat semantic room "
            "localization as a temporally dependent measurement problem rather than only an imbalanced classification task. "
            "We propose a multi-resolution framework combining a short-horizon 10 s Random Forest representation with two "
            "complementary 60 s XGBoost representations, fold-local signal-pattern augmentation, synthetic minority "
            "balancing, probability normalization and fusion, and conservative minority-class recovery. Evaluation spans "
            "naive row-random, 45 s block-group, event-group, leave-one-day-out (LODO), and strict-forward chronological "
            "protocols. A standalone 60 s XGBoost configuration exceeds 0.91 Macro-F1 under row-random splitting (0.9102 "
            "unrounded) but reaches about 0.25 under strict-forward evaluation, demonstrating strong protocol sensitivity. "
            "In the internal strict-forward evaluation, the proposed system obtains Macro-F1 of 0.3159, Weighted-F1 of "
            "0.5973, and accuracy of 0.6054, compared with 0.2561, 0.5293, and 0.5533 for the 10 s Random Forest baseline. "
            "The results demonstrate strong protocol sensitivity and persistent minority-room difficulty in a deployment "
            "documented to contain signal loss and unstable RSSI. The chronological folds also informed model and decoder "
            "selection; therefore, these scores are internal development estimates rather than an untouched external "
            "validation result."
        )

    render_card(
        title="Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction",
        subtitle="Role: Co-Researcher | Accepted at IEEE EAEEIE 2026 & WiML Symposium @ ICML 2026 (Supported by JSPS KAKENHI 26K07547)",
        date="2026",
        body=(
            "Investigated structural vulnerabilities of 2D pre-trained convolutional backbones in vision-centric 3D "
            "semantic occupancy prediction (SparseOcc on Occ3D-nuScenes and Robo3D). Demonstrated that while 2D priors "
            "support long-range (>30m) semantic classification and static fog penetration, their texture bias collapses "
            "under dynamic anomalies (motion blur and snow) and overwrites the 3D temporal history buffer ('Temporal "
            "Poisoning'). Co-developed an Evidential Feature Gate (EFG) grounded in Dirichlet subjective logic to "
            "quantify pixel-wise epistemic uncertainty and attenuate corrupted spatial features with +0.01M parameter "
            "overhead at 14.25 FPS on an RTX A4500."
        ),
        tools="PyTorch, OpenMMLab, SparseOcc, Occ3D-nuScenes, Robo3D, Evidential Deep Learning",
        link="https://github.com/ummerubaiyat/spatio-temporal-paradox-of-2d-priors"
    )
    with st.expander("📖 Read Full Abstract (3D Semantic Occupancy Prediction)"):
        st.write(
            "Vision-centric 3D semantic occupancy prediction has emerged as a highly scalable alternative to LiDAR for "
            "autonomous driving. Due to severe optimization challenges inherent in training complex 3D spatio-temporal "
            "transformers from scratch, existing architectures typically rely on 2D convolutional backbones pre-trained on "
            "massive image datasets. This initialization undeniably accelerates convergence. It also improves clean-weather "
            "semantic classification at long ranges. However, our research exposes a critical, inherent structural "
            "vulnerability: the Spatio-Temporal Paradox. Through a rigorous empirical analysis using the NuScenes-C "
            "robustness benchmark, we evaluate deterministic 2D spatial priors. We demonstrate that these priors excel at "
            "static noise penetration (e.g., Fog). Conversely, they exhibit severe structural collapse under environmental "
            "anomalies (e.g., Motion Blur and Snow). We show that this spatial failure induces 'Temporal Poisoning.' "
            "During this cascade, corrupted instantaneous features overwrite and fundamentally blind downstream 3D temporal "
            "routing mechanisms. To resolve this structural vulnerability without sacrificing clean-weather performance, we "
            "propose an Evidential Feature Gate (EFG). Grounded in Dirichlet subjective logic, the EFG dynamically "
            "quantifies out-of-distribution epistemic uncertainty at the feature level. It then mathematically suppresses "
            "corrupted spatial inputs toward zero. This forms a protective firewall around the temporal history buffer."
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
                "In <em>Journal of Physics: Conference Series</em> (Accepted, ISAS 2026 Challenge Winner)."
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
            <h3 style="margin-top: 0; color: #1e293b;">Research Capabilities & Interests</h3>
            <p class="cv-card-body" style="margin-bottom: 0.6rem;">
                <strong>Methodological Areas:</strong>
            </p>
            <div style="margin-bottom: 1rem;">
                <span class="skill-badge">Applied Statistical Modeling</span>
                <span class="skill-badge">Empirical Protocol Design</span>
                <span class="skill-badge">Uncertainty Quantification</span>
                <span class="skill-badge">Computer Vision & Sensor ML</span>
                <span class="skill-badge">Feature Engineering</span>
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
