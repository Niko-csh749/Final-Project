# Weather-Based Outfit Recommender


The **Weather-Based Outfit Recommender** is a web application developed with **Streamlit** that generates dressing suggestions for users based on current and predicted weather conditions. By leveraging the **OpenWeatherMap API**, the system fetches weather data and processes it to give apt dressing recommendations for the sake of comfort and preparedness for the day.

This project aims to assist users in choosing the right dressing considering temperature, wind speed, possibility of rain, and general weather patterns for a five-day forecast. The app features an easy-to-use interface where users can input their location and get immediate, AI-powered suggestions on dressing.


## Features
✅ **Real-Time Weather Data** – Fetches live weather information from OpenWeatherMap.  
✅ **5-Day Weather Trends** – Analyzes forecasted temperature and rain levels.  
✅ **Intelligent Clothing Recommendations** – Provides suggestions based on temperature, wind speed, and precipitation probability.  
✅ **User-Friendly Interface** – Built with **Streamlit**, ensuring an interactive and mobile-responsive experience.  
✅ **Error Handling & Resilience** – Manages API failures and missing data gracefully.

## Installation and Setup

### **Prerequisites**
Before running the application, ensure you have the following:
- **Python** installed.


### **1. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **2. Run the Streamlit Application**
```sh
streamlit run project.py
```

## Usage
1. **Enter your city** in the input field.
2. **Click "Get Weather & Trends"** to fetch live weather data and future predictions.
3. View:
   - **Current temperature, wind speed, and rain probability**.
   - **5-day average temperature and rainfall trends**.
   - **AI-generated outfit recommendations** based on weather conditions.
  
4. **Use the recommendations** to dress appropriately! 🌦️👕

## File Descriptions

### **1. `project.py` **
- This file contains the **Streamlit app** responsible for retrieving weather data and displaying recommendations.
- **Key Functions:**
  - `get_weather_data(location)`: Fetches current weather information.
  - `get_weather_forecast(location)`: Retrieves 5-day weather trends.
  - `analyze_weather_trends(forecast_data)`: Extracts and processes temperature and rain patterns.

### **2. `test_project.py` **
- Includes **`pytest`** test cases for:
  - `extract_weather_details()` – Ensures correct extraction of temperature, wind speed, and rain details.
  - `recommend_outfit()` – Validates outfit suggestions based on different weather conditions.
  - `suggest_alternative_clothing()` – Tests alternative clothing recommendations for varying weather trends.

### **3. `requirements.txt` **
- Lists the required Python libraries for running the application:
  - `streamlit`
  - `requests`
  - `pytest`
  - `python-dotenv` 

## Design Choices and Considerations
### **1. Why Use Streamlit?**
- Streamlit provides an **interactive UI** with minimal effort.
- It allows **real-time data updates** and is optimized for **data-driven applications**.
- **Simple deployment** and easy integration with APIs.

### **2. Why OpenWeatherMap?**
- Provides **both real-time and 5-day forecasted weather data**.
- Supports **temperature, wind speed, precipitation probability, and weather descriptions**.

### **3. Prioritizing Weather Conditions**
- **Rain > 50%** → Recommends a **raincoat & umbrella**.
- **Wind > 20 m/s** → Recommends a **windbreaker**.
- **Temperature < 5°C** → Suggests a **heavy coat, gloves, and scarf**.
- **Temperature > 30°C** → Suggests **light, breathable clothing**.

## Future Improvements
🚀 **Data Visualization** – Display **graphs** of temperature and rain trends.  
📍 **Geolocation Support** – Auto-detect user’s location for automatic weather retrieval.  
📊 **Historical Weather Analysis** – Compare past weather with future forecasts.  
🔄 **Real-Time Auto-Refresh** – Enable periodic data refresh to keep weather updates current.  


## AI Assistance and Citations
This project was developed entirely by **US**; however, **AI tools were used to enhance efficiency and productivity**:
- **ChatGPT** assisted in:
  - Debugging failed test cases in `test_project.py`.
  - Optimizing `recommend_outfit()` logic.
- **GitHub Copilot** was used for:
  - Suggesting function docstrings.
  - Providing syntax improvements for error handling.

**AI-generated suggestions were manually reviewed, modified, and verified** before inclusion. No AI-generated code was used without human intervention.

_Adhering to academic integrity, AI contributions are explicitly cited in code comments where applicable._


## Final Thoughts

The **Weather-Based Outfit Recommender** is a functional application that integrates **real-time weather data** with **AI-generated fashion suggestions**. With the help of **Streamlit** and **OpenWeatherMap**, we offer users a convenient and informative means to dress accordingly in response to altering weather patterns.

This project is a **basis for additional improvements**, such as **machine learning algorithms for improved forecasting, geolocation weather retrieval, and improved trend analysis**. 

 <img width="848" alt="Screenshot 2025-02-28 at 3 54 16 PM" src="https://github.com/user-attachments/assets/053ac565-9624-44ab-9007-1c2e7b9fcafc" />

 ##Link for youtube video explaining the code and functions##
 https://youtu.be/EnMnsAU1QYg
