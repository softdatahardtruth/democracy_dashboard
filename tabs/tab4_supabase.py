import streamlit as st
import pandas as pd
from supabase import create_client, Client

def render_tab():
    url = "https://clzaciqixfdqxgxceaiz.supabase.co"  # <- Ersetze mit deiner Supabase-URL
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsemFjaXFpeGZkcXhneGNlYWl6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM2MTA1NTQsImV4cCI6MjA1OTE4NjU1NH0.obLqpoAfrgXAkPPTQ_Iv9DDw91Jk33e0FBd0zK2O9kg"  # <- Ersetze mit deinem Supabase anon key
    supabase: Client = create_client(url, key)

    st.subheader("Live-Risikoanalyse aus Supabase (Tabelle: DemoData)")

    response = supabase.table("DemoData").select("*").order("timestamp", desc=True).limit(10).execute()

    if not response.data:
        st.warning("Keine Daten gefunden.")
    else:
        df = pd.DataFrame(response.data)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        latest = df.iloc[0]

        st.metric("Autoritäres Risiko 2029", f"{latest['risiko'] * 100:.1f}%")
        st.markdown("#### Einflussfaktoren:")
        st.write(f"- **Propaganda:** {latest['propaganda']:.2f}")
        st.write(f"- **Ziviler Widerstand:** {latest['ziviler_widerstand']:.2f}")
        st.write(f"- **Systembruch:** {latest['systembruch']:.2f}")
        st.write(f"- **Bürgerkrieg:** {latest['buergerkrieg']:.2f}")
        st.write(f"- **Bundesstaaten-Resistenz:** {latest['bundesstaaten_resistenz']:.2f}")

        with st.expander("📊 Vergangene Einträge anzeigen"):
            st.dataframe(df)
