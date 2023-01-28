import requests
from PIL import Image
import json
from io import BytesIO
import io

import io

with open("api_file.bin", encoding="utf-8") as binary_file:
    # Read the whole file at once
    api_key = binary_file.read()

str(api_key)

url = "https://api.nasa.gov/planetary/apod?api_key={}"


result = requests.get(url.format(api_key))
if result.status_code == 200:
        print("Test test testy test test")
        json= result.json()
        url = json["url"]
        imageURLResponse = requests.get(url)
        image = Image.open(BytesIO(imageURLResponse.content))
        image.show()
else:
        print("error retrivng Space image")
        print(result.status_code)