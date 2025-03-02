import pytest
from project import extract_weather_details, recommend_outfit, suggest_alternative_clothing

def test_extract_weather_details():
    sample_weather_data = {
        "main": {"temp": 22.5},
        "wind": {"speed": 5.2},
        "rain": {"1h": 0.3},
        "weather": [{"description": "light rain"}]
    }

    temp, wind, rain_chance, weather_desc = extract_weather_details(sample_weather_data)

    assert temp == 22.5
    assert wind == 5.2
    assert rain_chance == 100  
    assert weather_desc == "light rain"

def test_extract_weather_details_no_rain():
    sample_weather_data = {
        "main": {"temp": 18.0},
        "wind": {"speed": 3.0},
        "weather": [{"description": "clear sky"}]
    }

    temp, wind, rain_chance, weather_desc = extract_weather_details(sample_weather_data)

    assert temp == 18.0
    assert wind == 3.0
    assert rain_chance == 0  
    assert weather_desc == "clear sky"

@pytest.mark.parametrize("temperature, wind_speed, rain_chance, expected_outfit", [
    (4, 10, 0, "Wear a heavy winter coat, gloves, a scarf, and a hat."),
    (10, 5, 0, "Wear a warm jacket and layer up."),
    (20, 5, 0, "A light jacket or sweater should be fine."),
    (32, 3, 0, "Wear breathable fabrics, sunglasses, and stay hydrated."),
    (18, 25, 0, "Wear a windbreaker."),  
    (22, 5, 60, "Wear a raincoat, waterproof shoes, and carry an umbrella.")  
])
def test_recommend_outfit(temperature, wind_speed, rain_chance, expected_outfit):
    assert recommend_outfit(temperature, wind_speed, rain_chance) == expected_outfit


@pytest.mark.parametrize("weather_trends, expected_suggestion", [
    ("snow", "Wear thermal clothing, waterproof boots, and gloves."),
    ("rain", "Carry an umbrella and wear waterproof shoes."),
    ("clear", "Wear sunglasses and a hat if it's sunny."),
    ("hot", "Wear light, breathable clothing and drink plenty of water."),
    ("heatwave", "Wear light, breathable clothing and drink plenty of water."),
    ("cloudy", "Dressing normally should be fine.")  
])
def test_suggest_alternative_clothing(weather_trends, expected_suggestion):
    assert suggest_alternative_clothing(weather_trends) == expected_suggestion