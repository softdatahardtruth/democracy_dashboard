import streamlit as st
from tabs import tab1_szenario, tab2_montecarlo, tab3_hybrid, tab4_supabase

st.set_page_config(page_title="Democracy 2029", layout="wide")
st.title("🗳️ Democracy 2029")

tabs = st.tabs([
    "🔁 Automatisches Szenario",
    "🎲 Monte-Carlo",
    "⚠️ Hybrid-Modell",
    "🌐 Supabase Live"
])

with tabs[0]:
    tab1_szenario.render_tab()

with tabs[1]:
    tab2_montecarlo.render_tab()

with tabs[2]:
    tab3_hybrid.render_tab()

with tabs[3]:
    tab4_supabase.render_tab()
