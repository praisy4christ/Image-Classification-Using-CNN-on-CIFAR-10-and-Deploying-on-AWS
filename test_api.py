import requests

url =  "http://127.0.0.1:7080/predict"


file_path = "image.jpg"  # Ensure this file exists

try:
    with open(file_path, "rb") as img:
        files = {"file": img}
        response = requests.post(url, files=files)  # Ensure this is POST
        
        print("Status Code:", response.status_code)  # Print HTTP response status
        print("Response Content:", response.text)    # Print response body
        
        response.raise_for_status()  # Raise an error if the request failed
        print(response.json())  # Print the JSON response
except Exception as e:
    print("Error:", e)
