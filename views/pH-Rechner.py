import streamlit as st
import math
 
def calculate_ph(h_conc: float) -> float:
    """Berechnet den pH-Wert aus der H⁺-Konzentration.
    Erwartet einen positiven Wert, sonst wird eine Ausnahme geworfen."""
    if h_conc <= 0:
        raise ValueError("Die Konzentration muss größer als 0 sein.")
    return -math.log10(h_conc)
 
def app() -> None:
    st.title("pH‑Rechner")
    st.write("Ermitteln des pH‑Werts aus der Wasserstoffionenkonzentration [H⁺].")
 
    h_input = st.number_input(
        "Konzentration [H⁺] (mol L⁻¹)",
        min_value=0.0,
        format="%.6g"
    )
 
    if st.button("Berechnen"):
        if h_input <= 0:
            st.error("Bitte geben Sie einen Wert größer als 0 ein.")
        else:
            try:
                ph_val = calculate_ph(h_input)
                st.success(f"pH = {ph_val:.3f}")
            except Exception as exc:
                st.error(str(exc))
if __name__ == "__main__":
    app()
 