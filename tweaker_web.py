"""
Roblox Tweaker - Streamlit Web Version
Run: streamlit run tweaker_web.py
"""

import streamlit as st
import json
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Roblox Tweaker",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling
st.markdown("""
    <style>
    :root {
        --bg-color: #0e0e0e;
        --card-color: #161616;
        --green: #00d97e;
        --text: #f0f0f0;
    }
    
    .main {
        background-color: #0e0e0e;
        color: #f0f0f0;
    }
    
    [data-testid="stMetricValue"] {
        color: #00d97e;
    }
    </style>
""", unsafe_allow_html=True)

# Session state for settings
if 'settings' not in st.session_state:
    st.session_state.settings = {}

# Header
st.markdown("# 🚀 Roblox Tweaker - Performance Optimizer")
st.markdown("*Optimize your Roblox gaming experience*")
st.divider()

# Category data
CATEGORIES = [
    {
        "title": "Basic Tweaks",
        "desc": "General performance settings",
        "icon": "⚙️",
        "tweaks": [
            {"label": "Disable Telemetry", "type": "toggle", "default": True},
            {"label": "Reduce Memory Usage", "type": "toggle", "default": True},
            {"label": "Auto-Close Background Apps", "type": "toggle", "default": False},
            {"label": "Render Quality", "type": "slider", "default": 70, "min": 0, "max": 100},
        ],
    },
    {
        "title": "Modifications",
        "desc": "Game modifications and patches",
        "icon": "🔧",
        "tweaks": [
            {"label": "FPS Unlocker", "type": "toggle", "default": True},
            {"label": "Hyperion Bypass", "type": "toggle", "default": False},
            {"label": "Texture Optimizer", "type": "toggle", "default": True},
            {"label": "Target FPS", "type": "slider", "default": 144, "min": 30, "max": 360},
        ],
    },
    {
        "title": "Advanced Tweaks",
        "desc": "Expert-level optimizations",
        "icon": "⚡",
        "tweaks": [
            {"label": "CPU Priority Boost", "type": "toggle", "default": False},
            {"label": "Network Buffer Tuning", "type": "toggle", "default": False},
            {"label": "Disable VSync", "type": "toggle", "default": True},
            {"label": "Thread Count", "type": "slider", "default": 4, "min": 1, "max": 16},
        ],
    },
    {
        "title": "GPU Tweaks",
        "desc": "Graphics and rendering options",
        "icon": "🖥️",
        "tweaks": [
            {"label": "Low-Latency Mode", "type": "toggle", "default": True},
            {"label": "Shader Cache", "type": "toggle", "default": True},
            {"label": "Anti-Aliasing", "type": "toggle", "default": False},
            {"label": "Render Distance", "type": "slider", "default": 60, "min": 0, "max": 100},
        ],
    },
    {
        "title": "KBM + Mouse Tweaks",
        "desc": "Input and sensitivity settings",
        "icon": "🖱️",
        "tweaks": [
            {"label": "Raw Input", "type": "toggle", "default": True},
            {"label": "Reduce Input Lag", "type": "toggle", "default": True},
            {"label": "Disable Mouse Accel", "type": "toggle", "default": True},
            {"label": "Sensitivity", "type": "slider", "default": 50, "min": 1, "max": 100},
        ],
    },
]

# Create tabs for categories
tabs = st.tabs([f"{cat['icon']} {cat['title']}" for cat in CATEGORIES])

for tab, category in zip(tabs, CATEGORIES):
    with tab:
        st.subheader(f"{category['icon']} {category['title']}")
        st.caption(category['desc'])
        st.divider()
        
        col1, col2 = st.columns(2)
        
        for idx, tweak in enumerate(category['tweaks']):
            col = col1 if idx % 2 == 0 else col2
            
            with col:
                if tweak['type'] == 'toggle':
                    value = st.checkbox(
                        tweak['label'],
                        value=st.session_state.settings.get(tweak['label'], tweak['default']),
                        key=f"toggle_{tweak['label']}"
                    )
                    st.session_state.settings[tweak['label']] = value
                    
                elif tweak['type'] == 'slider':
                    value = st.slider(
                        tweak['label'],
                        min_value=tweak['min'],
                        max_value=tweak['max'],
                        value=st.session_state.settings.get(tweak['label'], tweak['default']),
                        key=f"slider_{tweak['label']}"
                    )
                    st.session_state.settings[tweak['label']] = value

# Sidebar - Settings & Export
st.sidebar.markdown("## ⚙️ Settings")

if st.sidebar.button("💾 Save Settings to File"):
    settings_file = Path("tweaker_settings.json")
    with open(settings_file, 'w') as f:
        json.dump(st.session_state.settings, f, indent=2)
    st.sidebar.success(f"✅ Settings saved to `{settings_file}`")

if st.sidebar.button("🔄 Reset to Defaults"):
    st.session_state.settings = {}
    st.rerun()

# Display current settings
st.sidebar.markdown("### 📊 Current Settings")
if st.session_state.settings:
    st.sidebar.json(st.session_state.settings)
else:
    st.sidebar.info("No custom settings yet")

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #7a7a7a; padding: 20px;'>
        <p>🎮 <strong>Roblox Tweaker v2.0</strong> | Web Optimizer</p>
        <p style='font-size: 0.9em;'>Settings are stored in browser session. Use 'Save Settings to File' to persist.</p>
    </div>
""", unsafe_allow_html=True)
