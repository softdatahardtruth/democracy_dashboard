import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gumbel_r

st.set_page_config(page_title="Democracy 2029 – Szenarien & Simulationen", layout="wide")

st.title("🗳️ Democracy 2029")
st.markdown("Ein datenbasiertes Analyse-Tool zur Zukunft der US-Demokratie nach dem Wahlsieg von 2024.")

# --- Hilfsfunktionen ---
def normalize_count(count, max_val):
    return np.clip(count / max_val, 0, 1)

def plot_risk_distribution(data, mean_risk, high_risk_prob, title, color):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=50, color=color, edgecolor='white')
    ax.axvline(mean_risk, color='crimson', linestyle='--', label=f"Mittelwert: {mean_risk:.2f}")
    ax.axvline(0.6, color='orange', linestyle=':', label=f">60 % Risiko: {high_risk_prob:.1%}")
    ax.set_title(title)
    ax.set_xlabel("Risiko-Wert (0 = niedrig, 1 = hoch)")
    ax.set_ylabel("Häufigkeit")
    ax.legend()
    st.pyplot(fig)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["🔁 Automatisches Szenario", "🎲 Monte-Carlo", "⚠️ Hybrid-Modell"])

# --- TAB 1: Automatisiertes Szenario ---
with tab1:
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

# --- TAB 2: Klassische Monte-Carlo-Simulation ---
with tab2:
    st.subheader("Monte-Carlo-Simulation (Beta-Modell)")
    if st.button("Simulation starten (klassisch)"):
        n_sim = 10000
        nachfolger = np.random.beta(4, 2, n_sim)
        systembruch = np.random.beta(2, 8, n_sim)
        ziviler_widerstand = np.random.beta(3, 3, n_sim)
        buergerkrieg = np.random.beta(1.5, 10, n_sim)
        propaganda = np.random.beta(3, 2, n_sim)
        bundesstaaten_resistenz = np.random.beta(2, 3, n_sim)

        risiko = (
            nachfolger * (1 - systembruch) * (1 - ziviler_widerstand) *
            (1 - buergerkrieg) * propaganda * (1 - bundesstaaten_resistenz)
        )
        mean_risk = np.mean(risiko)
        high_risk_prob = np.mean(risiko > 0.6)
        plot_risk_distribution(risiko, mean_risk, high_risk_prob,
                               "Monte-Carlo-Simulation: Autoritäres Risiko 2029", "steelblue")
        st.markdown(f"**Durchschnittliches Risiko:** {mean_risk:.2%}")
        st.markdown(f"**Risiko > 60 % in:** {high_risk_prob:.1%} der Szenarien")
    else:
        st.info("Starte die Simulation, um 10.000 Szenarien zu berechnen.")

# --- TAB 3: Hybrid-Modell (Beta + Gumbel) ---
with tab3:
    st.subheader("Hybrid-Simulation mit Extremrisiken (Beta + Gumbel)")
    if st.button("Simulation starten (Hybrid-Modell)"):
        n_sim = 10000
        nachfolger = np.random.beta(4, 2, n_sim)
        ziviler_widerstand = np.random.beta(3, 3, n_sim)
        propaganda = np.random.beta(3, 2, n_sim)
        bundesstaaten_resistenz = np.random.beta(2, 3, n_sim)
        systembruch = np.clip(gumbel_r.rvs(loc=0.2, scale=0.1, size=n_sim), 0, 1)
        buergerkrieg = np.clip(gumbel_r.rvs(loc=0.1, scale=0.05, size=n_sim), 0, 1)

        risiko = (
            nachfolger * (1 - systembruch) * (1 - ziviler_widerstand) *
            (1 - buergerkrieg) * propaganda * (1 - bundesstaaten_resistenz)
        )
        mean_risk = np.mean(risiko)
        high_risk_prob = np.mean(risiko > 0.6)
        plot_risk_distribution(risiko, mean_risk, high_risk_prob,
                               "Hybrid-Simulation: Autoritäres Risiko 2029", "indigo")
        st.markdown(f"**Durchschnittliches Risiko:** {mean_risk:.2%}")
        st.markdown(f"**Risiko > 60 % in:** {high_risk_prob:.1%} der Szenarien")
    else:
        st.info("Starte die Hybrid-Simulation, um realistische Extremszenarien zu berücksichtigen.")
