from prompt import generate_advice

def main():
    print("🌱 Welcome to Eco Crop Advisor 🌱")
    print("Please enter the following details:\n")

    crop = input("Enter crop type: ")
    soil = input("Enter soil type: ")
    weather = input("Describe today's weather: ")

    print("\n📋 AI Generated Sustainable Farming Advice:\n")
    advice = generate_advice(crop, soil, weather)
    print(advice)

if __name__ == "__main__":
    main()
