#!/usr/bin/env python3

import psutil
import shutil
import emails
import socket

## Checa a saúde da máquina e envia um e-mail para o usuário caso haja algum problema
sender = "automation@example.com"
recipient = "student-04-b5664336174c@example.com"
body = "Please check your system and resolve the issue as soon as possible."

## Retorna True se o uso de CPU estiver acima de 80%
def check_cpu():
    return psutil.cpu_percent(1) > 80

## Retorna True se o disco estiver com menos de 20% de espaço livre
def check_disk(disk):
    usage = shutil.disk_usage(disk)
    free = usage.free / usage.total * 100
    return free < 20

## Retorna True se menos de 500MB de RAM estiver disponível para uso
def check_ram():
    mem = psutil.virtual_memory()
    limit = 100 * 1024 * 1024
    return mem.available < limit

## Retorna True se o localhost não for condizente com o IP esperado
def check_localhost():
    return socket.gethostbyname('localhost') != "127.0.0.1"

if check_cpu():
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(message)

if check_disk("/"):
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(message)

if check_ram():
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(message)

if check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(message)

## O script é usado a cada minuto através de um cron
