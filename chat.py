from tools import tokenize,bag_of_words,stem,puncremover_lower
from model import NeuralNet
import torch
import torch.nn as nn
import json
import random
import os
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("dataset.json",'r') as json_file:
    json_dataset=json.load(json_file)

file='saved_data.pth'
data=torch.load("data.pth")

input_size=data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name="colddsam"
print("start chatting")

def get_response(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item()>0.25:
        for elements in json_dataset['items']:
            if elements['keys']==tag:
                return random.choice(elements['answers'])
    else:
        return "I can't understand master.........."
    

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)