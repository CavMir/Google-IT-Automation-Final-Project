#!/usr/bin/env python3

import os
import requests

## Faz o upload das imagens com o formato .jpeg para o banco de imagens do site
url = "http://localhost/upload/"
path = "./supplier-data/images/"
im_dir = os.listdir(path)
for im in im_dir:
    if im.lower().endswith(('.jpeg')):
        with open (path+im, 'rb') as upload:
            r = requests.post(url, files={'file': upload})
