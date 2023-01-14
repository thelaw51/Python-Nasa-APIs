import requests
from PIL import Image
import json
from io import BytesIO


url = "https://api.nasa.gov/planetary/apod?api_key=WMBG5Ug6uHBGlkAwsjaUJg1DqMRznESghooSqOW1"

result = requests.get(url)
if result.status_code == 200:
        json= result.json()
        url = json["url"]
        imageURLResponse = requests.get(url)
        image = Image.open(BytesIO(imageURLResponse.content))
        image.show()
else:
        print("error retrivng Space image")
        print(result.status_code)