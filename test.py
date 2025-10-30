import requests

url = "http://localhost:8000/predict"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
result = response.json()

print(f"Prediction: {result['prediction']}")
if 'probability' in result:
    print(f"Probability: {result['probability']:.4f}")