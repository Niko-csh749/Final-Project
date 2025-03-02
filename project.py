import streamlit as st
import requests
import os


def get_weather_data(location):
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "b589bf07fdcccfb9d127da7fdb95de49")  
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def extract_weather_details(weather_data):
    temp = weather_data["main"].get("temp", "N/A")
    wind = weather_data["wind"].get("speed", 0)
    rain = weather_data.get("rain", {}).get("1h", 0)  

    rain_chance = 100 if rain > 0 else 0  
    weather_desc = weather_data["weather"][0].get("description", "N/A")

    return temp, wind, rain_chance, weather_desc

def recommend_outfit(temperature, wind_speed, rain_chance):
    """
    Suggests an outfit based on weather conditions.
    Prioritizes wind speed and rain before temperature.
    """
    if rain_chance > 50:
        return "Wear a raincoat, waterproof shoes, and carry an umbrella."
    elif wind_speed > 20:  
        return "Wear a windbreaker."
    elif temperature < 5:
        return "Wear a heavy winter coat, gloves, a scarf, and a hat."
    elif temperature < 15:
        return "Wear a warm jacket and layer up."
    elif temperature < 25:
        return "A light jacket or sweater should be fine."
    elif temperature > 30:
        return "Wear breathable fabrics, sunglasses, and stay hydrated."
    else:
        return "T-shirt and jeans should be fine."

def suggest_alternative_clothing(weather_trends):
    weather_trends = weather_trends.lower()
    
    if "snow" in weather_trends:
        return "Wear thermal clothing, waterproof boots, and gloves."
    elif "rain" in weather_trends:
        return "Carry an umbrella and wear waterproof shoes."
    elif "clear" in weather_trends:
        return "Wear sunglasses and a hat if it's sunny."
    elif "hot" in weather_trends or "heat" in weather_trends:
        return "Wear light, breathable clothing and drink plenty of water."
    else:
        return "Dressing normally should be fine."

st.set_page_config(page_title="Weather Outfit Recommender", page_icon="⛅", layout="centered")

st.title("🌦️ Weather-Based Outfit Recommender")
st.write("Enter your location to get outfit recommendations based on the weather.")


location = st.text_input("Enter your city:", "New York")

if st.button("Get Weather"):
    weather_data = get_weather_data(location)

    if weather_data:
        temp, wind, rain_chance, weather_desc = extract_weather_details(weather_data)

        st.subheader(f"📍 Weather in {location}")
        st.write(f"🌡️ Temperature: **{temp}°C**")
        st.write(f"💨 Wind Speed: **{wind} m/s**")
        st.write(f"🌧️ Rain Chance: **{rain_chance}%**")
        st.write(f"☁️ Weather Condition: **{weather_desc.capitalize()}**")

        outfit_recommendation = recommend_outfit(temp, wind, rain_chance)
        alternative_clothing = suggest_alternative_clothing(weather_desc)

        st.subheader("👕 Outfit Recommendation")
        st.success(outfit_recommendation)

        st.subheader("🛍️ Alternative Clothing Suggestion")
        st.info(alternative_clothing)

    else:
        st.error("Could not retrieve weather data. Please try again.")
