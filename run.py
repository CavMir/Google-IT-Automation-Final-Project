#! /usr/bin/env python3

import os
import requests

## Faz o upload da informação de cada fruta para o site como um arquivo .json
## O arquivo detalha para cada fruta o nome, peso, descrição e o caminho da imagem no banco de imagens do site.
url = "http://localhost/fruits/"
path = "./supplier-data/descriptions/"
txt_dir = os.listdir(path)
for txt in txt_dir:
    with open(path+txt) as text:
        name, weight, desc = text.readlines()[:3]
        fruit = {"name" : name[:-1],
                 "weight" : int(weight.split()[0]),
                 "description": desc[:-1],
                 "image_name": "{}.jpeg".format(txt.split('.')[0])}
    response = requests.post(url, json=fruit)
