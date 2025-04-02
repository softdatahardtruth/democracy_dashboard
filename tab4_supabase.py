import streamlit as st
import pandas as pd
from supabase import create_client, Client

def render_tab():
    url = "https://DEIN_PROJECT_URL.supabase.co"  # <- Ersetze mit deiner Supabase-URL
    key = "DEIN_ANON_KEY"  # <- Ersetze mit deinem Supabase anon key
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
