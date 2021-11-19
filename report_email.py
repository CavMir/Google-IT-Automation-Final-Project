#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

## Gera uma lista de strings a partir de arquivos .txt que será passada como parâmetro para a função "reports.generate_report()"
path = "./supplier-data/descriptions/"
txt_dir = os.listdir(path)
fruits = []
for txt in txt_dir:
    with open(path+txt) as text:
        fruit = text.readlines()
        fruits.append("name: {}".format(fruit[0][:-1]))
        fruits.append("weight: {}".format(fruit[1][:-1]))
        fruits.append("<br/>")

if __name__ == "__main__":
    
## O método "<br/>".join() transforma a lista numa string separada por quebras de linha para que seja passada como parâmetro
    pdf_path = "/tmp/processed.pdf"
    today = date.today().strftime("%B %d, %Y")
    reports.generate_report(pdf_path, "Processed Update on {}".format(today), "<br/>".join(fruits[:-1]))

## Envia por e-mail para o fornecedor o arquivo pdf que foi gerado
    sender = "automation@example.com"
    recipient = "student-04-b5664336174c@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, pdf_path)
    emails.send_email(message)
