import requests
import json

API_KEY = 'AIzaSyD8M_arBlBANxACa4emOo5d5mVu5ngmO8E'

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyD8M_arBlBANxACa4emOo5d5mVu5ngmO8E"

image_path = "D:/TEST_Image_plat_mobil.jpeg"

with open(image_path, "rb") as image_file:
    image_data = image_file.read()

headers = {
    "Content-Type": "application/json",
}

data = {
    "key": API_KEY,
    "contents": [{
        "parts": [{
            "image": {
                "content": image_data.decode("utf-8")
            },
            "text": "Extract plate number and vehicle details from this image."
        }]
    }]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    response_json = response.json()
    plate_number = response_json.get('plate_no', 'N/A')
    vehicle_type = response_json.get('vehicle', 'N/A')
    color = response_json.get('color', 'N/A')

    result = {
        "plat_no": plate_number,
        "vehicle": vehicle_type,
        "vehicle_type": "sedan",
        "color": color,
        "gate_open": "2024-12-02 18:15:01",
        "gate_closed": "N/A"
    }

    print(json.dumps(result, indent=4))
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")
