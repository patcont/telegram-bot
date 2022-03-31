import string
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import json

import requests

url = "http://worldtimeapi.org/api/timezone/America/Santiago"

payload = ""
headers = {
    "authority": "api.axie.management",
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "dnt": "1",
    "sec-gpc": "1",
    "origin": "https://tracker.axie.management",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://tracker.axie.management/",
    "accept-language": "en-US,en;q=0.9,es-CL;q=0.8,es;q=0.7",
    "if-none-match": "W/^\^116-OID3/IlVKKekIwWnfJh0Bpklpn4^^"
}

response = requests.request("GET", url, data=payload, headers=headers).text

hora_stgo= json.loads(response)

y= (hora_stgo["datetime"])

z = y[11:18]


def hola(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hola {update.effective_user.first_name}')

def cumple(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'cumpleaños de patricio es el 19 de julio')
    
def hora(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'La hora es: ' + z)    
    

    
updater = Updater('5225045177:AAGrd04Dv1DiOzfIVAldnYh7v4OVANlQYQ8')

updater.dispatcher.add_handler(CommandHandler('hola', hola))
updater.dispatcher.add_handler(CommandHandler('cumple', cumple))
updater.dispatcher.add_handler(CommandHandler('hora', hora))



updater.start_polling()
updater.idle()