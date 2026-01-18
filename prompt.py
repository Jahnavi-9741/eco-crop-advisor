def generate_advice(crop, soil, weather):
    advice = ""

    # Step 1: Watering advice
    if "rain" in weather.lower():
        advice += "1️⃣ Watering: Rain is expected. Do NOT irrigate today to conserve water.\n"
    elif soil.lower() == "sandy":
        advice += "1️⃣ Watering: Sandy soil dries fast. Water lightly but frequently (morning & evening).\n"
    else:
        advice += "1️⃣ Watering: Water once a day in the early morning to reduce evaporation.\n"

    # Step 2: Soil care
    advice += "2️⃣ Soil Care: Add organic compost or mulch to improve soil moisture and health.\n"

    # Step 3: Sustainability tip
    advice += "3️⃣ Sustainability Tip: Use natural pest control methods like neem oil and avoid chemicals.\n"

    advice += "\n⚠️ Note: This is AI-generated advice. For serious crop issues, consult an agricultural expert."

    return advice
