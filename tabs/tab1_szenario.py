import streamlit as st
import numpy as np

def normalize_count(count, max_val):
    return np.clip(count / max_val, 0, 1)

def render_tab():
    st.subheader("Automatische Risikoeinschätzung basierend auf Ereignisdaten")

    fake_data = {
        "media_laws_last_30_days": 5,
        "protest_events_last_30_days": 12,
        "shutdown_indicators": 2,
        "state_resistance_cases": 6,
        "violence_signals": 1
    }

    automated_inputs = {
        "propaganda": normalize_count(fake_data["media_laws_last_30_days"], 10),
        "ziviler_widerstand": normalize_count(fake_data["protest_events_last_30_days"], 20),
        "systembruch": normalize_count(fake_data["shutdown_indicators"], 5),
        "bundesstaaten_resistenz": normalize_count(fake_data["state_resistance_cases"], 10),
        "buergerkrieg": normalize_count(fake_data["violence_signals"], 5)
    }

    if st.button("Szenario automatisch analysieren"):
        st.info("🚨 Automatisierte Wahrscheinlichkeiten (simulierte Ereignisdaten):")
        for key, value in automated_inputs.items():
            st.write(f"**{key.replace('_', ' ').capitalize()}**: {value:.2f}")

        nachfolger = 0.7
        p_autoritaer = (
            nachfolger *
            (1 - automated_inputs["systembruch"]) *
            (1 - automated_inputs["ziviler_widerstand"]) *
            (1 - automated_inputs["buergerkrieg"]) *
            automated_inputs["propaganda"] *
            (1 - automated_inputs["bundesstaaten_resistenz"])
        )
        st.metric("Geschätztes Risiko eines autoritären US-Systems 2029", f"{p_autoritaer * 100:.1f}%")
    else:
        st.info("Klicke auf den Button, um das Szenario automatisch einzuschätzen.")
