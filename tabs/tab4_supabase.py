import streamlit as st

def render_tab():
    st.subheader("Live-Risikoanalyse (Supabase deaktiviert)")

    st.warning("Diese Funktion ist aktuell deaktiviert, da `supabase-py` nicht mit Streamlit Cloud kompatibel ist.")
    st.markdown("""
    Wenn du lokal arbeitest oder später auf einen anderen Server gehst,  
    kannst du die Supabase-Funktionalität wieder aktivieren.
    """)
