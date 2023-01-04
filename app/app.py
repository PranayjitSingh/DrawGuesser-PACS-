from flask import Flask, render_template
from flask_cors import CORS
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image, ImageOps
from flask import request, jsonify
import base64
import os
import sys

global model_loaded_cpu
data_transforms = {
    'test': transforms.Compose([
        transforms.ToTensor(),
        transforms.Grayscale(),
        transforms.Lambda(lambda x: x.repeat(3, 1, 1)) 
    ])}

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def main():
    return render_template('index.html')

def prediction(fileName):
    # ---------------------------------------#
    device = torch.device("cpu")
    model = torch.hub.load('facebookresearch/semi-supervised-ImageNet1K-models', 'resnext101_32x8d_ssl')
    # MODELS: https://github.com/facebookresearch/semi-supervised-ImageNet1K-models
    num_ftrs = model.fc.in_features
    fully_connected  = nn.Sequential(
        nn.Linear(num_ftrs, 7),
        nn.ReLU()
    )
    model.fc = fully_connected
    model = model.to(device)
    model_loaded = model
    model_loaded.load_state_dict(torch.load("model.pt", map_location=device))
    model.eval()
    model_loaded_cpu = model_loaded.cpu()

    img = Image.open(fileName)
    img = img.convert('RGB')
    img = ImageOps.expand(img, 75)
    img = img.resize((227,227))

    img = data_transforms["test"](img)
    img = img.cpu().float()
    img = img.unsqueeze(0)
    
    output = model_loaded_cpu(img)
    _, predicted = torch.max(output.data, 1)

    labels = {
        "0" : "Dog",
        "1" : "Elephant",
        "2" : "Giraffe",
        "3" : "Guitar",
        "4" : "Horse",
        "5" : "House",
        "6" : "Person"
    }

    guess = labels[str(predicted.numpy()[0])]
    
    return guess

    # RESEARCH: https://openreview.net/pdf?id=z-LBrGmZaNs
    # edge-detection?
    # --> pre-processing on the training data to conduct edge extraction --> generate model --> may improve because the output sketch

@app.route('/postmethod', methods=['POST'])
def postmethod():
    data = request.get_json()
    fullData = data['out']
    code = fullData.split(";",1)[1].replace("base64,", "")
    imgData = base64.b64decode(code)
    if os.path.exists("to_guess.png"):
        os.remove("to_guess.png")
    filename = 'to_guess.png'
    with open(filename, 'wb+') as f:
        f.write(imgData)
    out = prediction(filename)
    return jsonify({"guess": out})

if  __name__ == '__main__':
    host_ip = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host_ip, port=port, debug=True)
