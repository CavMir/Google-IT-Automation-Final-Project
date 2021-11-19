#!/usr/bin/env python3

import os
from PIL import Image

## Acessa a pasta de imagens e redimensiona e converte cada imagem
## As novas imagens são salvas na mesma pasta com o tamanho 600x400 e o formato .jpeg
path = "./supplier-data/images/"
im_dir = os.listdir(path)
for im in im_dir:
    if im.lower().endswith(('.tiff')):
        nem_im = Image.open(path+im)
        new_im.convert('RGB').resize((600,400)).save("{}{}.jpeg".format(path, im.split('.')[0]), "JPEG")
