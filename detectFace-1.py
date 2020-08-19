# DevPSU Project 2
# Face Detection
# detectFace.py

# Import libraries here
from io import BytesIO
import cognitive_face, requests
from PIL import Image, ImageDraw

# FaceAPI details
subscription_key = "cd9c588e48ff4a8986733232e5b42cfc"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': True,
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    # headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blue,exposure,noise'
}

# Input image
image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Steve_Jobs_Headshot_2010-CROP2.jpg/220px-Steve_Jobs_Headshot_2010-CROP2.jpg'

# FaceAPI initiallization
data = {'url': image_url}
face_api_url='https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'
response = requests.post(face_api_url, params=params, headers=headers, json=data)
facesResponse = response.json()
print(facesResponse)

# Rectangle coordinates
def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']   
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

# Download the image from the url
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

#For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)
for face in facesResponse:
    draw.rectangle(getRectangle(face), outline='red')

#Display the image in the users default image browser.
img.show()