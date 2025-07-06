import streamlit as st
import matplotlib.pyplot as plt
from weather_data import get_weather_data

st.set_page_config(page_title="Dashboard Pogodowy", layout="centered")

st.title("🌤️ Dashboard Pogodowy")
st.markdown("Pobieranie i analiza danych pogodowych z Open-Meteo")

# Formularz użytkownika
lat = st.number_input("Szerokość geograficzna (np. Warszawa = 52.23)", value=52.23)
lon = st.number_input("Długość geograficzna (np. Warszawa = 21.01)", value=21.01)
start = st.date_input("Data początkowa")
end = st.date_input("Data końcowa")

if st.button("Pobierz dane"):
    try:
        df = get_weather_data(lat, lon, str(start), str(end))
        st.success("✅ Dane pobrane!")
        st.dataframe(df)

        # Wykres
        fig, ax = plt.subplots()
        ax.plot(df["date"], df["temp_max"], label="Max Temp")
        ax.plot(df["date"], df["temp_min"], label="Min Temp")
        ax.set_xlabel("Data")
        ax.set_ylabel("Temperatura (°C)")
        ax.legend()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Błąd: {e}")
