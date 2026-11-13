import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_echarts import st_echarts

st.set_page_config(
    page_title="Manoj Roy | Academic Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for Academic Styling, High-Contrast Navbar, Dark/Light Mode Support, and Responsive Layout
st.markdown("""
    <style>
    /* Theme-aware CSS variables (Light Mode Defaults) */
    :root {
        --card-bg: #ffffff;
        --card-alt-bg: #f8fafc;
        --intro-bg: #fcfcfd;
        --border-color: #e2e8f0;
        --border-strong: #cbd5e1;
        --text-primary: #1e293b;
        --text-heading: #1a202c;
        --text-secondary: #475569;
        --text-muted: #64748b;
        --accent-teal: #008B8B;
        --accent-teal-hover: #006666;
        --accent-subtitle: #006666;
        --badge-bg: #f0f4f8;
        --badge-text: #2c3e50;
        --badge-border: #dce4ec;
        --date-bg: #f1f5f9;
        --nav-container-bg: #f1f5f9;
        --nav-item-bg: #ffffff;
        --nav-hover-bg: #e6fffa;
    }

    /* Automatic Dark Mode Overrides */
    @media (prefers-color-scheme: dark) {
        :root {
            --card-bg: #1e293b;
            --card-alt-bg: #16202e;
            --intro-bg: #1e293b;
            --border-color: #334155;
            --border-strong: #475569;
            --text-primary: #f1f5f9;
            --text-heading: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --accent-teal: #0d9488;
            --accent-teal-hover: #14b8a6;
            --accent-subtitle: #2dd4bf;
            --badge-bg: #0f172a;
            --badge-text: #e2e8f0;
            --badge-border: #334155;
            --date-bg: #0f172a;
            --nav-container-bg: #0f172a;
            --nav-item-bg: #1e293b;
            --nav-hover-bg: #134e4a;
        }
    }

    /* Also respect Streamlit's internal dark theme attribute if toggled manually in Settings */
    [data-testid="stAppViewContainer"][data-theme="dark"],
    .stApp[data-theme="dark"] {
        --card-bg: #1e293b;
        --card-alt-bg: #16202e;
        --intro-bg: #1e293b;
        --border-color: #334155;
        --border-strong: #475569;
        --text-primary: #f1f5f9;
        --text-heading: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --accent-teal: #0d9488;
        --accent-teal-hover: #14b8a6;
        --accent-subtitle: #2dd4bf;
        --badge-bg: #0f172a;
        --badge-text: #e2e8f0;
        --badge-border: #334155;
        --date-bg: #0f172a;
        --nav-container-bg: #0f172a;
        --nav-item-bg: #1e293b;
        --nav-hover-bg: #134e4a;
    }

    /* Main Container */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        padding: 1rem 2rem;
    }

    /* Clean Academic Top Navbar */
    div.row-widget.stRadio > div[role="radiogroup"] {
        background-color: var(--nav-container-bg) !important;
        border: 1.5px solid var(--border-strong) !important;
        border-radius: 10px !important;
        padding: 6px !important;
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 8px !important;
        margin-bottom: 2rem !important;
        justify-content: space-between !important;
    }

    /* Unselected Buttons */
    div.row-widget.stRadio > div[role="radiogroup"] > label {
        background-color: var(--nav-item-bg) !important;
        border: 1px solid var(--border-strong) !important;
        border-radius: 7px !important;
        padding: 9px 18px !important;
        margin: 0 !important;
        flex: 1 1 auto !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        cursor: pointer !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08) !important;
        transition: all 0.15s ease-in-out !important;
    }

    /* Hide the default radio circle button */
    div.row-widget.stRadio > div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }

    /* High-contrast unselected text */
    div.row-widget.stRadio > div[role="radiogroup"] > label * {
        color: var(--text-primary) !important;
        font-size: 0.96rem !important;
        font-weight: 600 !important;
        margin: 0 !important;
        text-align: center !important;
        opacity: 1 !important;
    }

    /* Hover State */
    div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
        background-color: var(--nav-hover-bg) !important;
        border-color: var(--accent-teal) !important;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label:hover * {
        color: var(--accent-subtitle) !important;
    }

    /* Active Selected Button */
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) {
        background-color: var(--accent-teal) !important;
        border-color: var(--accent-teal) !important;
        box-shadow: 0 2px 5px rgba(0, 139, 139, 0.35) !important;
    }
    div.row-widget.stRadio > div[role="radiogroup"] > label:has(input:checked) * {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* Homepage Typography */
    .main-title {
        font-size: 3.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: var(--text-heading);
        letter-spacing: -0.5px;
    }
    .sub-title {
        font-size: 1.65rem;
        color: var(--text-secondary);
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
        background-color: var(--intro-bg);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
        border-left: 4px solid var(--accent-teal);
        border-radius: 6px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }
    .intro-text p {
        color: var(--text-primary);
        margin: 0;
    }
    .first-letter {
        font-size: 46px;
        font-weight: bold;
        color: var(--text-heading);
        margin: 0;
        padding-right: 10px;
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
        background-color: var(--card-alt-bg);
        color: var(--text-primary);
        border-radius: 6px;
        border: 1px dashed var(--border-strong);
    }
    .highlight {
        color: var(--accent-subtitle);
        font-weight: bold;
    }

    /* Academic Summary Metric Boxes */
    .stat-ribbon {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .stat-box {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-top: 3px solid var(--accent-teal);
        border-radius: 6px;
        padding: 0.9rem 1rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .stat-value {
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--text-heading);
        font-family: 'Georgia', serif;
    }
    .stat-label {
        font-size: 0.8rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.2rem;
    }

    /* Clean Academic Cards */
    .cv-card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-left: 4px solid var(--accent-teal);
        border-radius: 6px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.06);
        transition: box-shadow 0.15s ease;
    }
    .cv-card-alt {
        background-color: var(--card-alt-bg);
        border: 1px solid var(--border-color);
        border-left: 4px solid var(--border-strong);
        border-radius: 6px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 1rem;
    }
    .cv-card:hover {
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
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
        color: var(--text-heading);
        margin: 0;
    }
    .cv-card-title a {
        color: var(--text-heading) !important;
        text-decoration: underline;
    }
    .cv-card-date {
        font-size: 0.85rem;
        color: var(--text-secondary);
        background-color: var(--date-bg);
        border: 1px solid var(--border-color);
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 500;
        white-space: nowrap;
    }
    .cv-card-subtitle {
        font-size: 0.93rem;
        color: var(--accent-subtitle);
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    .cv-card-body {
        font-size: 0.94rem;
        color: var(--text-primary);
        line-height: 1.65;
        margin: 0;
    }
    .cv-card-body a {
        color: var(--accent-subtitle) !important;
    }
    .cv-card-tools {
        margin-top: 0.5rem;
        font-size: 0.86rem;
        color: var(--text-secondary);
    }

    /* Certification List Row */
    .cert-row {
        padding: 7px 0;
        border-bottom: 1px solid var(--border-color);
        color: var(--text-primary);
    }
    .cert-row a {
        font-weight: 600;
        color: var(--text-heading) !important;
        text-decoration: none;
    }
    .cert-row a:hover {
        color: var(--accent-subtitle) !important;
        text-decoration: underline;
    }
    .cert-org {
        color: var(--text-muted);
        font-size: 0.9rem;
    }

    /* Easy-to-Read Note Box */
    .method-box {
        background-color: var(--card-alt-bg);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        padding: 1.1rem 1.25rem;
        font-size: 0.92rem;
        color: var(--text-primary);
        line-height: 1.65;
        margin-bottom: 1rem;
    }

    /* Skill & Topic Badges */
    .skill-badge {
        display: inline-block;
        background-color: var(--badge-bg);
        color: var(--badge-text);
        padding: 5px 11px;
        margin: 3px 5px 3px 0;
        border-radius: 4px;
        font-size: 0.86rem;
        font-weight: 500;
        border: 1px solid var(--badge-border);
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
        div.row-widget.stRadio > div[role="radiogroup"] > label {
            flex: 1 1 45%;
            padding: 8px 10px !important;
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
    return {
        "tooltip": {"trigger": "item", "formatter": "{b}: {c} ({d}%)"},
        "legend": {
            "top": "bottom",
            "textStyle": {"color": "#8892b0"}
        },
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
                "label": {"color": "#8892b0"},
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


def render_ble_protocol_line_chart():
    return {
        "tooltip": {"trigger": "axis"},
        "legend": {"top": "bottom", "textStyle": {"color": "#8892b0"}},
        "grid": {"left": "4%", "right": "4%", "bottom": "16%", "top": "10%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "axisLabel": {"color": "#8892b0"},
            "data": [
                "Row-Random\n(Overlapping)",
                "45s Block\n(Purged)",
                "Event-Group\n(Unseen Visits)",
                "LODO\n(Cross-Day)",
                "Strict-Forward\n(Future Day)"
            ],
        },
        "yAxis": {
            "type": "value",
            "name": "Macro-F1 Score",
            "nameTextStyle": {"color": "#8892b0"},
            "axisLabel": {"color": "#8892b0"},
            "splitLine": {"lineStyle": {"color": "rgba(148, 163, 184, 0.2)"}},
            "min": 0.15,
            "max": 0.95
        },
        "series": [
            {
                "name": "Proposed Multi-Resolution System",
                "type": "line",
                "smooth": True,
                "symbolSize": 9,
                "data": [0.901, 0.348, 0.280, 0.322, 0.316],
                "itemStyle": {"color": "#14b8a6"},
                "lineStyle": {"width": 3.5},
                "areaStyle": {"opacity": 0.15, "color": "#14b8a6"}
            },
            {
                "name": "60s Rich XGBoost (Standalone)",
                "type": "line",
                "smooth": True,
                "symbolSize": 8,
                "data": [0.910, 0.303, 0.199, 0.254, 0.255],
                "itemStyle": {"color": "#e07a5f"},
                "lineStyle": {"width": 2.5, "type": "dashed"}
            },
            {
                "name": "10s Random Forest Baseline",
                "type": "line",
                "smooth": True,
                "symbolSize": 8,
                "data": [0.628, 0.302, 0.237, 0.287, 0.256],
                "itemStyle": {"color": "#64748b"},
                "lineStyle": {"width": 2.5}
            },
            {
                "name": "10s Causal TCN",
                "type": "line",
                "smooth": True,
                "symbolSize": 7,
                "data": [0.542, 0.270, 0.235, 0.265, 0.211],
                "itemStyle": {"color": "#94a3b8"},
                "lineStyle": {"width": 2, "type": "dotted"}
            }
        ]
    }


def render_ble_ablation_combo_chart():
    return {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}},
        "legend": {"top": "bottom", "textStyle": {"color": "#8892b0"}},
        "grid": {"left": "4%", "right": "4%", "bottom": "16%", "top": "10%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "axisLabel": {"color": "#8892b0"},
            "data": [
                "10s RF\nBaseline",
                "Multi-Resolution\nFusion (Untargeted)",
                "+ Room 510\nScore Gate",
                "+ Room 518\nVote Weight"
            ]
        },
        "yAxis": [
            {
                "type": "value",
                "name": "Macro-F1",
                "nameTextStyle": {"color": "#8892b0"},
                "axisLabel": {"color": "#8892b0"},
                "splitLine": {"lineStyle": {"color": "rgba(148, 163, 184, 0.2)"}},
                "min": 0.20,
                "max": 0.35
            },
            {
                "type": "value",
                "name": "Accuracy / Weighted-F1",
                "nameTextStyle": {"color": "#8892b0"},
                "axisLabel": {"color": "#8892b0"},
                "splitLine": {"show": False},
                "min": 0.50,
                "max": 0.65
            }
        ],
        "series": [
            {
                "name": "Macro-F1 (Equal weight across 23 rooms)",
                "type": "bar",
                "barWidth": "38%",
                "yAxisIndex": 0,
                "data": [0.2561, 0.3051, 0.3077, 0.3159],
                "itemStyle": {"color": "#14b8a6", "borderRadius": [4, 4, 0, 0]}
            },
            {
                "name": "Overall Accuracy",
                "type": "line",
                "yAxisIndex": 1,
                "symbolSize": 9,
                "data": [0.5533, 0.6048, 0.6051, 0.6054],
                "itemStyle": {"color": "#38bdf8"},
                "lineStyle": {"width": 3}
            },
            {
                "name": "Weighted-F1",
                "type": "line",
                "yAxisIndex": 1,
                "symbolSize": 8,
                "data": [0.5293, 0.5962, 0.5966, 0.5973],
                "itemStyle": {"color": "#e07a5f"},
                "lineStyle": {"width": 2.5, "type": "dashed"}
            }
        ]
    }


def render_efg_clean_radar_chart():
    return {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "bottom", "textStyle": {"color": "#8892b0"}},
        "radar": {
            "axisName": {"color": "#8892b0"},
            "splitLine": {"lineStyle": {"color": "rgba(148, 163, 184, 0.25)"}},
            "splitArea": {"areaStyle": {"color": ["rgba(148, 163, 184, 0.04)", "rgba(148, 163, 184, 0.08)"]}},
            "indicator": [
                {"name": "Overall mIoU\n(Max 35)", "max": 35},
                {"name": "Overall RayIoU\n(Max 40)", "max": 40},
                {"name": "Near Ring 0–15m\n(Max 45)", "max": 45},
                {"name": "Mid Ring 15–30m\n(Max 35)", "max": 35},
                {"name": "Far Ring >30m\n(Max 20)", "max": 20}
            ],
            "radius": "62%",
            "center": ["50%", "45%"]
        },
        "series": [
            {
                "name": "Clean-Weather Profile",
                "type": "radar",
                "data": [
                    {
                        "value": [31.10, 36.75, 41.73, 31.33, 17.93],
                        "name": "Baseline (SparseOcc v1.1)",
                        "itemStyle": {"color": "#64748b"},
                        "lineStyle": {"width": 2, "type": "dashed"}
                    },
                    {
                        "value": [30.44, 36.10, 41.07, 30.60, 17.02],
                        "name": "EFG + 2D Pretraining (Proposed)",
                        "itemStyle": {"color": "#14b8a6"},
                        "areaStyle": {"opacity": 0.2, "color": "#14b8a6"},
                        "lineStyle": {"width": 3}
                    },
                    {
                        "value": [25.11, 30.63, 35.49, 24.64, 12.69],
                        "name": "EFG without 2D Pretraining",
                        "itemStyle": {"color": "#e07a5f"},
                        "lineStyle": {"width": 2}
                    }
                ]
            }
        ]
    }


def render_efg_degradation_line_chart():
    return {
        "tooltip": {"trigger": "axis"},
        "legend": {"top": "bottom", "textStyle": {"color": "#8892b0"}},
        "grid": {"left": "4%", "right": "4%", "bottom": "16%", "top": "10%", "containLabel": True},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "axisLabel": {"color": "#8892b0"},
            "data": [
                "Motion Blur\n(Easy)",
                "Motion Blur\n(Mid)",
                "Motion Blur\n(Hard)",
                "Snow\n(Easy)",
                "Snow\n(Mid)",
                "Snow\n(Hard)"
            ]
        },
        "yAxis": {
            "type": "value",
            "name": "Relative Robustness Retained (%)",
            "nameTextStyle": {"color": "#8892b0"},
            "axisLabel": {"color": "#8892b0"},
            "splitLine": {"lineStyle": {"color": "rgba(148, 163, 184, 0.2)"}},
            "min": 0,
            "max": 100
        },
        "series": [
            {
                "name": "EFG (3D Volumetric Priors / No 2D Pretrain)",
                "type": "line",
                "smooth": True,
                "symbolSize": 9,
                "data": [93.0, 71.0, 61.2, 34.8, 16.1, 10.4],
                "itemStyle": {"color": "#14b8a6"},
                "lineStyle": {"width": 3.5},
                "areaStyle": {"opacity": 0.15, "color": "#14b8a6"}
            },
            {
                "name": "Standard Pre-Trained Baseline (SparseOcc)",
                "type": "line",
                "smooth": True,
                "symbolSize": 8,
                "data": [85.9, 28.6, 14.9, 16.2, 10.1, 9.7],
                "itemStyle": {"color": "#e07a5f"},
                "lineStyle": {"width": 2.5, "type": "dashed"}
            }
        ]
    }


def render_card(title, subtitle, date, body, tools=None, link=None):
    title_html = (
        f'<a href="{link}" target="_blank">{title} 🔗</a>'
        if link else title
    )
    subtitle_html = f'<div class="cv-card-subtitle">{subtitle}</div>' if subtitle else ""
    tools_html = (
        f'<div class="cv-card-tools"><strong>Tools:</strong> {tools}</div>'
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
    st.markdown('<h1 class="main-title">Hi, I am Manoj Roy 👋</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">Data Enthusiast & Researcher</h2>', unsafe_allow_html=True)

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

    st.markdown(
        """
        <div class="intro-text">
        <p><span class="first-letter">I</span> hold degrees in Applied Statistics (M.Sc.) and Computer Science (B.Sc.). My background combines statistical methodology with applied machine learning, focusing on evaluation protocol design and robustness under real-world data constraints. Currently, I teach data analysis and collaborate on applied machine learning research.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    left_column, right_column = st.columns([2, 1])

    with left_column:
        st_echarts(options=render_nightingale_rose_diagram(), height="500px", key="home_rose_chart")

    with right_column:
        lottie_skills = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ul35wckt.json")
        if lottie_skills:
            st_lottie(lottie_skills, speed=1, height=280, key="home_lottie_anim")

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
        cert_filter = st.selectbox(
            "Filter Certifications by Domain:",
            ["All (9)", "Statistics & Data Science", "Machine Learning & AI", "Engineering & Management"]
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
                    f'<div class="cert-row">'
                    f'🔹 <a href="{url}" target="_blank">{title}</a> '
                    f'<span class="cert-org">| {org} ({year})</span></div>',
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
    st.header("Academic Research")

    st.markdown("""
        <div class="cv-card-alt">
            <div class="cv-card-title" style="margin-bottom: 0.3rem;">🔎 Interactive Research Explorer</div>
            <p class="cv-card-body">
                Below is an interactive overview of our two recent studies. Select a study to explore how the models perform across different validation methods and real-world conditions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_sel1, col_sel2 = st.columns([1.2, 1])
    with col_sel1:
        study_choice = st.selectbox(
            "1. Choose a Study:",
            [
                "BLE Indoor Localization in Nursing Care (ISAS 2026)",
                "3D Occupancy Prediction under Bad Weather (EAEEIE / ICML WiML 2026)"
            ]
        )

    if "BLE Indoor Localization" in study_choice:
        with col_sel2:
            view_mode = st.selectbox(
                "2. Choose What to View:",
                [
                    "How Validation Splits Change Model Scores (Line Chart)",
                    "Step-by-Step Ensemble Improvement (Combo Chart)"
                ]
            )

        if "Validation Splits" in view_mode:
            col_chart, col_notes = st.columns([1.35, 1])
            with col_chart:
                st.markdown("##### Model Performance Across 5 Validation Methods")
                st_echarts(options=render_ble_protocol_line_chart(), height="380px", key="ble_line_chart")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>What This Chart Shows Simply:</strong><br><br>
                    • <strong>The Practical Problem:</strong> In a care facility, we want to recognize which of the 23 rooms a nurse is in using Bluetooth (BLE) signals from 25 beacons (47,121 labeled seconds across 4 days).<br><br>
                    • <strong>Why Random Splitting Can Be Misleading:</strong> Adjacent time windows share almost the same signal history. If we split rows randomly, a 60-second XGBoost model scores <strong>0.910 Macro-F1</strong> because similar neighboring seconds appear in both training and test sets. However, when tested on a <em>future unseen day</em> (Strict-Forward), that same model drops to <strong>0.255</strong>.<br><br>
                    • <strong>Our Approach:</strong> By combining a short 10-second Random Forest with two 60-second XGBoost models and borrowing signal patterns from geometrically similar rooms, the combined system achieves <strong>0.316 Macro-F1</strong> on future-day evaluation.
                </div>
                """, unsafe_allow_html=True)
        else:
            col_chart, col_notes = st.columns([1.35, 1])
            with col_chart:
                st.markdown("##### How Each Step Contributes (Strict-Forward Evaluation)")
                st_echarts(options=render_ble_ablation_combo_chart(), height="380px", key="ble_combo_chart")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>What We Learned from the Step-by-Step Test:</strong><br><br>
                    • <strong>Combining Short & Long Windows Helps Most:</strong> Over <strong>81%</strong> of our overall Macro-F1 improvement (rising from 0.2561 to 0.3051) and nearly <strong>99%</strong> of the accuracy gain (55.33% → 60.48%) came simply from blending the 10-second and 60-second models together.<br><br>
                    • <strong>Targeted Adjustments for Rare Rooms:</strong> Adding specific rules for two hard-to-detect rooms (Room 510 and Room 518) nudged the final Macro-F1 to <strong>0.3159</strong> (with 60.54% accuracy).<br><br>
                    • <strong>Honest Limitations:</strong> Because we used the April 11–13 chronological folds to choose our model settings, we report these numbers modestly as internal development estimates rather than untouched external test scores.
                </div>
                """, unsafe_allow_html=True)

    else:
        with col_sel2:
            view_mode = st.selectbox(
                "2. Choose What to View:",
                [
                    "Clean-Weather Performance by Distance (Radar Chart)",
                    "Model Stability Under Blur & Snow (Line Trajectory)"
                ]
            )

        if "Clean-Weather" in view_mode:
            col_chart, col_notes = st.columns([1.35, 1])
            with col_chart:
                st.markdown("##### Clean-Weather Accuracy Across Distance Rings")
                st_echarts(options=render_efg_clean_radar_chart(), height="380px", key="efg_radar_chart")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>What This Radar Chart Explains:</strong><br><br>
                    • <strong>Why 2D Pre-Training is Used:</strong> 3D occupancy models use camera images to map the 3D space around a vehicle. When objects are far away (>30 meters), they appear very small in images. Without pre-trained 2D image weights, accuracy at long distances drops noticeably (from 17.93 to 12.69 mIoU).<br><br>
                    • <strong>Keeping Clean-Weather Quality:</strong> Adding our Evidential Feature Gate (EFG) alongside pre-trained 2D weights keeps clean-weather accuracy close to the original baseline across all distances (<strong>30.44 mIoU</strong> and <strong>36.10 RayIoU</strong>).<br><br>
                    • <strong>Lightweight on Hardware:</strong> Tested on a single RTX A4500 GPU, the gate adds only <strong>+0.01M parameters</strong> and runs in real time at <strong>14.25 FPS</strong>.
                </div>
                """, unsafe_allow_html=True)
        else:
            col_chart, col_notes = st.columns([1.35, 1])
            with col_chart:
                st.markdown("##### Percentage of Clean-Weather Performance Retained Under Stress")
                st_echarts(options=render_efg_degradation_line_chart(), height="380px", key="efg_deg_line_chart")
            with col_notes:
                st.markdown("""
                <div class="method-box">
                    <strong>What Happens Under Motion Blur and Snow:</strong><br><br>
                    • <strong>The Trade-Off We Found:</strong> Pre-trained 2D backbones rely heavily on sharp edges and textures. While this helps in static fog, it struggles when motion blur smooths out edges or snow adds false textures—corrupting the model's 3D memory of previous frames.<br><br>
                    • <strong>Measuring Uncertainty:</strong> Under severe motion blur, the standard baseline retains only <strong>14.9%</strong> of its normal geometric accuracy, whereas training with 3D volumetric priors and evidential gating retains <strong>61.2%</strong>.<br><br>
                    • <strong>How the Gate Works:</strong> When input images become unfamiliar or blurry, the gate estimates uncertainty using Dirichlet logic and scales unreliable image features down toward zero so the 3D history stays clean.
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📚 Research Summaries")

    render_card(
        title="Multi-Resolution BLE Indoor Localization for Nursing Care under Signal Loss, Class Imbalance, and Temporal Shift",
        subtitle="Role: Co-Researcher | Accepted at Journal of Physics: Conference Series (ISAS 2026 Challenge — Champion, 1st of 37 Teams)",
        date="2026",
        body=(
            "Studied how to recognize staff locations across 23 rooms in a nursing-care facility using noisy Bluetooth "
            "beacon signals. Because some visits are brief and others last much longer, we combined a short 10-second "
            "Random Forest model with two 60-second XGBoost models. To handle rooms with very few recorded visits, we "
            "transferred signal patterns from geometrically similar rooms strictly within each training fold. We also "
            "compared five different validation methods to show how strongly model scores depend on temporal separation."
        ),
        tools="Python, Scikit-learn, XGBoost, LightGBM, PyTorch"
    )
    with st.expander("📖 Read Original Paper Abstract (BLE Indoor Localization)"):
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
            "0.5973, and accuracy of 0.6054, compared with 0.2561, 0.5293, and 0.5533 for the 10 s Random Forest baseline."
        )

    render_card(
        title="Spatio-Temporal Paradox of 2D Priors: Evidential Feature Gating for Robust 3D Occupancy Prediction",
        subtitle="Role: Co-Researcher | Accepted at IEEE EAEEIE 2026 & WiML Symposium @ ICML 2026 (Supported by JSPS KAKENHI 26K07547)",
        date="2026",
        body=(
            "Examined how 2D pre-trained image backbones affect 3D occupancy prediction for autonomous driving under bad "
            "weather. We found a practical trade-off: 2D pre-training helps classify distant objects (>30m) and see through "
            "static fog, but struggles under motion blur and snow, where corrupted image features overwrite the model's 3D "
            "temporal memory. To help address this, we worked on an Evidential Feature Gate (EFG) that estimates uncertainty "
            "and quiets down unreliable 2D features before they enter the 3D memory buffer, while adding minimal computing cost."
        ),
        tools="PyTorch, OpenMMLab, SparseOcc, Occ3D-nuScenes, Robo3D",
        link="https://github.com/ummerubaiyat/spatio-temporal-paradox-of-2d-priors"
    )
    with st.expander("📖 Read Original Paper Abstract (3D Occupancy Prediction)"):
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
            "To resolve this structural vulnerability without sacrificing clean-weather performance, we propose an "
            "Evidential Feature Gate (EFG) grounded in Dirichlet subjective logic."
        )

    render_card(
        title="Machine Learning Based Feature Engineering for Identifying The Causes Of Divorce",
        subtitle="Role: Graduate Researcher | M.Sc. Dissertation, Statistics & Data Science, Jahangirnagar Univ.",
        date="Jun – Dec 2022",
        body=(
            "Analyzed behavioral and communication survey data curated by field specialists to study key factors "
            "associated with marital separation. Applied Recursive Feature Elimination (RFE) and SHAP values to "
            "identify the most informative variables, used t-SNE to visualize data groupings, and evaluated the "
            "models using 5-fold cross-validation."
        ),
        tools="Python (Pandas, NumPy, Scikit-learn, SHAP), t-SNE, Matplotlib"
    )

    render_card(
        title="Computer Vision-based Street-width Measurement for Urban Aesthetics Identification",
        subtitle="Role: Undergraduate Researcher | B.Sc. Dissertation, Dept. of CSE, Daffodil Int'l Univ.",
        date="Nov 2017 – Jul 2018",
        body=(
            "Used basic computer vision techniques in OpenCV to estimate street widths from manually captured images "
            "in Dhaka. Applied grayscale filtering, Canny edge detection, and contour tracing to find road boundaries, "
            "and mapped pixel counts to physical measurements to compare streets against standard width criteria."
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
            <h3 style="margin-top: 0;">Get in Touch</h3>
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
            <h3 style="margin-top: 0;">Research Capabilities & Interests</h3>
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
    selected_page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🎓 Education & Skills",
            "🔬 Research",
            "💼 Experience",
            "📄 Publications & Honors",
            "✉️ Contact"
        ],
        horizontal=True,
        label_visibility="collapsed"
    )

    if selected_page == "🏠 Home":
        home_page()
    elif selected_page == "🎓 Education & Skills":
        education_and_skills()
    elif selected_page == "🔬 Research":
        research()
    elif selected_page == "💼 Experience":
        experience()
    elif selected_page == "📄 Publications & Honors":
        projects_and_publications()
    elif selected_page == "✉️ Contact":
        contact()


if __name__ == "__main__":
    main()
