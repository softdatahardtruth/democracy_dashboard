import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

def render_tab():
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
